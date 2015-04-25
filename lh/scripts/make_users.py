from django.contrib.auth.models import User

def run():
    User.objects.create_superuser(
            'bgolder',
            'benjamin.j.golder@gmail.com',
            'loghouse'
            )



