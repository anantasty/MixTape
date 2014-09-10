from django.conf import settings
from django.core.urlresolvers import reverse

import soundcloud


def get_login_url(request):
    url = request.build_absolute_uri(reverse('auth:soundcloud_login'))
    client = soundcloud.Client(client_id=settings.SOUNDCLOUD_CLIENT_ID,
                               client_secret=settings.SOUNDCLOUD_SECRET,
                               redirect_uri=url)
    return client.authorize_url()
