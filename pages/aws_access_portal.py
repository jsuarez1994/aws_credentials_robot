import os

from selenium.common.exceptions import (
  TimeoutException
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app.logger_conf import logger

# INPUTS arial-label to catch value
INPUT_AWS_ACCESS_KEY = "AWS access key ID"
INPUT_AWS_SECRET_ACCESS_KEY = "AWS secret access key"
INPUT_AWS_SESSION_TOKEN = "AWS session token"


class AwsAccessPortal:
  def __init__(self, driver, profile):
    self.driver = driver
    self.env = os.getenv('AWS_ENV')
    self.profile = profile

  def navigate_to_url(self):
    url = "https://portalaws" #REPLACE
    try:
      self.driver.get(url)
      logger.info(f"Go to: {url}")
      WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.TAG_NAME, "body"))
      )
      logger.info(f"Page '{url}' cargada.")
    except TimeoutException:
      logger.error(f"Timeout to load URL: {url}")
      raise
    except Exception as e:
      logger.error(f"Error in URL '{url}': {e}")
      raise

  def exist_value(self, label, value):
    try:
      WebDriverWait(self.driver, 20).until(
          EC.visibility_of_element_located(
              (By.XPATH, f"//{label}[text()='{value}']")))
      return True
    except Exception as e:
      logger.info(f"Not found '{value}' in label <{label}>. The exception: {e}")
      return False

  def toggle_environment_credentials(self):
    try:
      if self.exist_value('div', self.env):
        div_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.XPATH, f'//div[text()="{self.env}"]'))
        )
        # Get the parent button element and click it
        div_element.find_element(By.XPATH, "./ancestor::button").click()
    except Exception as exc:
      logger.error(f"Error toggle environment credentials: {exc}")

  def close_cookie_window(self):
    try:
      WebDriverWait(self.driver, 30).until(
          EC.element_to_be_clickable((By.XPATH,
                                      f"//span[text()='Decline']"))).click()
    except Exception as exc:
      logger.error(f"Error to close windows cookie: {exc}")
      raise exc

  def toggle_windows_credentials(self):
    try:
      # close cookies windows
      self.close_cookie_window()
      # check if exist environment
      self.toggle_environment_credentials()
      if self.exist_value('a', self.profile):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,
                                        f"//a[text()='{self.profile}']/following-sibling::a[1]"))).click()
      else:
        logger.info(f"Not exist or {self.env} or {self.profile}")
        raise Exception("Toggle credentials")
    except Exception as exc:
      logger.error(f"Error to toggle credentials {exc}")
      raise exc

  def get_value_by_arial_label(self, value):
    try:
      return WebDriverWait(self.driver, 20).until(
          EC.visibility_of_element_located(
              (By.CSS_SELECTOR, f'input[aria-label="{value}"]'))
      ).get_attribute("value")
    except Exception as exc:
      logger.error(f"Error to toggle credentials {exc}")
      raise exc

  # PRINCIPAL
  def get_credentials(self):
    try:
      self.toggle_windows_credentials()
      access_key = self.get_value_by_arial_label(INPUT_AWS_ACCESS_KEY)
      secret_access_key = self.get_value_by_arial_label(
          INPUT_AWS_SECRET_ACCESS_KEY)
      session_token = self.get_value_by_arial_label(INPUT_AWS_SESSION_TOKEN)
      return access_key, secret_access_key, session_token
    except Exception as exc:
      logger.error(f"Error to toggle credentials {exc}")
      raise exc
