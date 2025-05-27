import os
import re
import subprocess

from app.logger_conf import logger

ENABLED_IMPORT_SQS = os.getenv('IMPORT_SQS')
LOCALSTACK_URL = 'http://localhost:4566'
PATTERN_SQS = r"https://sqs\.[a-z0-9.-]+\.amazonaws\.com/[0-9]+/"


def create_sqs(list_sqs):
  aws_region = os.getenv('AWS_REGION', 'eu-west-1')
  for sqs in list_sqs:
    if '.fifo' in sqs:
      logger.info(f"The SQS {sqs} is fifo")
      subprocess.run(
          ["aws", f"--endpoint-url={LOCALSTACK_URL}", "sqs", "create-queue",
           "--queue-name", sqs, "--attributes", "FifoQueue=true", "--region",
           aws_region])
    else:
      logger.info(f"The SQS {sqs} is not fifo")
      subprocess.run(
          ["aws", f"--endpoint-url={LOCALSTACK_URL}", "sqs", "create-queue",
           "--queue-name", sqs, "--region", aws_region])


def import_sqs(profile):
  command = [
    "aws", "sqs", "list-queues", "--profile", profile, "--query", "QueueUrls[]",
    "--output", "text"
  ]
  result = subprocess.run(command, capture_output=True, text=True,
                          check=True)

  if not result.stderr:
    elements = result.stdout.split('\t')
    list_sqs = []
    for sqs in elements:
      sqs_clean = re.sub(PATTERN_SQS, "", sqs)
      list_sqs.append(sqs_clean.strip())
    create_sqs(list_sqs)


def execute(access_key, secret_access_key, session_token, profile):
  commands = [[
    "aws",
    "configure",
    "set",
    "aws_access_key_id",
    access_key,
    "--profile",
    profile
  ], [
    "aws",
    "configure",
    "set",
    "aws_secret_access_key",
    secret_access_key,
    "--profile",
    profile
  ], [
    "aws",
    "configure",
    "set",
    "aws_session_token",
    session_token,
    "--profile",
    profile
  ]]

  for command in commands:
    try:
      result = subprocess.run(command, capture_output=True, text=True,
                              check=True)
      logger.info(f"Command execute Ok {result.stdout}")
    except subprocess.CalledProcessError as e:
      logger.error(f"Error execute command {e.stderr}: {e}")
    except FileNotFoundError as fnfe:
      logger.error(f"Error execute command, file not found: {fnfe}")
    except Exception as ex:
      logger.error(f"Exception: {ex}")

  if ENABLED_IMPORT_SQS == 'True':
    import_sqs(profile)
