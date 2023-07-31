from datetime import datetime, timedelta

import boto3
from appconfig_helper import AppConfigHelper
from apscheduler.schedulers.asyncio import AsyncIOScheduler


class AppConfigService:
    def __init__(self, application_name, environment_name, profile_name):
        self.application_name = application_name
        self.environment_name = environment_name
        self.profile_name = profile_name

        self.scheduler = AsyncIOScheduler()

        self.service_appconfig = None
        self.development_appconfig = None

    async def start_scheduler(self):
        await self._create_appconfig_helper()

        self.scheduler.add_job(self._update_appconfig_helper, 'cron', minute='*/1',
                               start_date=datetime.now() + timedelta(seconds=1))
        self.scheduler.add_job(self._update_appconfig_helper(True), 'cron', hour='0/23',
                               start_date=datetime.now() + timedelta(seconds=1))
        self.scheduler.start()

    async def stop_scheduler(self):
        self.scheduler.shutdown()

    async def _create_appconfig_helper(self):
        print(f'create appconfig helper - {datetime.now()}')

        self.service_appconfig = AppConfigHelper(
            appconfig_application=self.application_name,
            appconfig_environment=self.environment_name,
            appconfig_profile="service",
            max_config_age=15,
            session=boto3.Session(region_name="ap-northeast-2", profile_name=self.profile_name),
        )
        self.service_appconfig.update_config()

        self.development_appconfig = AppConfigHelper(
            appconfig_application=self.application_name,
            appconfig_environment=self.environment_name,
            appconfig_profile="development",
            max_config_age=15,
            session=boto3.Session(region_name="ap-northeast-2", profile_name=self.profile_name),
        )
        self.development_appconfig.update_config()

    async def _update_appconfig_helper(self, force_update=False):
        print(f'update appconfig helper - {datetime.now()}')

        self.service_appconfig.update_config(force_update)
        self.development_appconfig.update_config(force_update)

    def get_appconfig(self):
        return {"profile": self.profile_name,
                "application": self.application_name,
                "environment": self.environment_name,
                "configuration_profile": {
                    self.service_appconfig.appconfig_profile: self.service_appconfig.config,
                    self.development_appconfig.appconfig_profile: self.development_appconfig.config
                }}
