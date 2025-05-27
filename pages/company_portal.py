import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from app.logger_conf import logger

COMPANY_LOGIN = "https://login.com/" #REPLACE


class CompanyPortal:
  def __init__(self, driver):
    self.driver = driver
    self.username = os.getenv('COMPANY_USER')
    self.password = os.getenv('COMPANY_PWD')

  def loaded_portal(self):
    try:
      WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.XPATH,
                                          f"//base[contains(@href,'{COMPANY_LOGIN}')]")))
      return True
    except Exception as exc:
      logger.error(f"Error loader portal {exc}")
      return False

  def login(self):
    try:
      username_input = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.ID, "username")))
      username_input.send_keys(self.username)
      pwd_input = WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.ID, "password")))
      pwd_input.send_keys(self.password)
      WebDriverWait(self.driver, 20).until(
          EC.element_to_be_clickable(
              (By.XPATH, '//a[@id="signOnButton"]'))).click()
    except Exception as e:
      logger.error(f"Error in login: {e}")
      raise
