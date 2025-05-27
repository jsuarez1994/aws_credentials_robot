import logging

# Configure the local root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
# Get a logger instance to be imported by other modules
logger = logging.getLogger('aws_credentials')
