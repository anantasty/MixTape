from django.conf import settings
import soundcloud


def get_login_url():
    client = soundcloud.Client(client_id=settings.SOUNDCLOUD_CLIENT_ID,
                               client_secret=settings.SOUNDCLOUD_SECRET,
                               redirect_uri='http://192.241.213.129:8000/auth/login/')
    return client.authorize_url()
