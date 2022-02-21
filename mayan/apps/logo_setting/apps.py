from mayan.apps.common.apps import MayanAppConfig

class Logo_settingApp(MayanAppConfig):
    app_namespace = 'logo_setting'
    app_url = 'logo_setting'
    name = 'mayan.apps.logo_setting'

    def ready(self):
        super().ready()