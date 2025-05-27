import os

from app import aws_local
from app.driver import get_driver
from app.logger_conf import logger
from pages.aws_access_portal import AwsAccessPortal
from pages.company_portal import CompanyPortal

PROFILE = os.getenv('AWS_PROFILE')

if __name__ == "__main__":
  # Generate driver
  logger.info('Generate Driver Chrome')
  driver = get_driver()
  aws_access_portal = AwsAccessPortal(driver, PROFILE)
  company_portail = CompanyPortal(driver)
  # Go to AWS
  logger.info('Go to AWS Portal')
  aws_access_portal.navigate_to_url()
  # Watch if throw company login page
  logger.info('Company Portal authentication')
  if company_portail.loaded_portal():
    company_portail.login()
  # Get credentials
  logger.info('Get Credentials')
  access_key, secret_access_key, session_token = aws_access_portal.get_credentials()
  # Run commands
  logger.info('AWS configuration execute')
  aws_local.execute(access_key, secret_access_key, session_token,
                    PROFILE)
  # Close driver
  driver.close()
