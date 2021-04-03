from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    name = 'usuarios'

    #PARA QUE LLAME A SIGNALS.PY PARA QUE SE GENERE UN PERFIL CADA VEZ QUE SE CREA UN USUARIO!!!
    def ready(self):
        import usuarios.signals