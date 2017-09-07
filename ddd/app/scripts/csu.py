from django.contrib.auth.models import User
def run():
    try:
        User.objects.create_superuser('aexol', 'aexol@aexol.com', 'RealPassword123')
    except:
        print("SuperUser aexol exists")
