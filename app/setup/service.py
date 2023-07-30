import os

from dotenv import load_dotenv

from app.modules.appconfig.service import AppConfigService

env = os.getenv('ENV', 'dev')
load_dotenv(f'.env.{env}')

application_name = os.getenv("APPLICATION_NAME")
environment_name = os.getenv("ENVIRONMENT_NAME")
profile_name = os.getenv("PROFILE_NAME")

appconfig_service = AppConfigService(application_name, environment_name, profile_name)
