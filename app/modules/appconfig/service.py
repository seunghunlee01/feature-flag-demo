import boto3

from appconfig_helper import AppConfigHelper


class AppConfigService:
    def __init__(self, application_name, environment_name, profile_name):
        self.service_appconfig = AppConfigHelper(
            appconfig_application=application_name,
            appconfig_environment=environment_name,
            appconfig_profile="service",
            max_config_age=15,
            session=boto3.Session(region_name="ap-northeast-2", profile_name=profile_name),
        )
        self.service_appconfig.start_session()
        self.service_appconfig.update_config()

        self.development_appconfig = AppConfigHelper(
            appconfig_application=application_name,
            appconfig_environment=environment_name,
            appconfig_profile="development",
            max_config_age=15,
            session=boto3.Session(region_name="ap-northeast-2", profile_name="yogiyo-dev"),
        )
        self.development_appconfig.start_session()
        self.development_appconfig.update_config()

    async def get_application(self):
        return {"service": self.service_appconfig.appconfig_application,
                "development": self.development_appconfig.appconfig_application}

    async def get_environment(self):
        return {"service": self.service_appconfig.appconfig_environment,
                "development": self.development_appconfig.appconfig_environment}

    async def get_profile(self):
        return {"service": self.service_appconfig.appconfig_profile,
                "development": self.development_appconfig.appconfig_profile}

    async def get_appconfig(self):
        return {"service": self.service_appconfig.config, "development": self.development_appconfig.config}
