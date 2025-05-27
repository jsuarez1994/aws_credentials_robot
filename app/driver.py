from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from app.logger_conf import logger


def import_chrome_driver_manager():
  try:
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    logger.info("Usando ChromeDriver gestionado por WebDriverManager.")
    return service
  except ImportError:
    logger.warning(
        "WebDriverManager no está instalado. Asegúrate de que 'chromedriver' esté en tu PATH o proporciona 'driver_path'.")
    return Service(
        "chromedriver")  # Intenta usar 'chromedriver' directamente desde PATH
  except Exception as e:
    logger.error(
        f"Error al inicializar WebDriverManager o Service sin driver_path: {e}")
    # Fallback a un intento directo, si la ruta no está bien configurada esto fallará
    return Service("chromedriver")


def build_chrome_options():
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--no-sandbox")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--incognito")
  chrome_options.add_argument("--disable-application-cache")
  chrome_options.add_argument("--disk-cache-size=0")
  return chrome_options


def get_driver():
  chrome_options = build_chrome_options()
  service = import_chrome_driver_manager()
  return webdriver.Chrome(service=service, options=chrome_options)
