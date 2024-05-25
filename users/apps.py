from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    def ready(self):
        import users.signals 
        
        # is laptop heating right now ?yup, disconnect charger for a while , its probably now some updates they are trying to push on vscode, its temprory 
        # until the updates are done , we cant do anything , just try to run everything at low , avoid using multiple tabsok
        # if i m closimg task manager usage reaching 100 coz task manager stops other useless apps in background while in use without it reaching 100 90 87 itne marokie 