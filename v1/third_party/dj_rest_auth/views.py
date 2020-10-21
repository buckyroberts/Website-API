from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.views import LogoutView as RestAuthLogoutView
from django.conf import settings


class GithubLoginView(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.SOCIALACCOUNT_PROVIDERS['github']['CALLBACK_URL']
    client_class = OAuth2Client


class LogoutView(RestAuthLogoutView):
    pass
