from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.instagram.views import InstagramOAuth2Adapter
schema_view = get_swagger_view(title='Rest API')

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
class InstagramLogin(SocialLoginView):
    adapter_class = InstagramOAuth2Adapter

urlpatterns = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/instagram/$', InstagramLogin.as_view(), name='instagram_login'),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/$', schema_view),
    url(r'^api-token-auth/', obtain_jwt_token),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
