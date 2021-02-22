from importlib import import_module

from django.conf import settings
from django.core.cache import cache


class PreventConcurrentLogins:
    """
    Django middleware to prevent multiple concurrent logins.
    - Uses database caching to persist session key.
    - We determine that there's concurrent logins by comparing the session key
        found in the cache and the current session key returned by the request object.
        If they are not the same key, it means concurrent logins are happening.
    Adapted from https://stackoverflow.com/a/34372082/5384866
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            cache_timeout = settings.SESSION_COOKIE_AGE
            cache_key = "user_pk_%s_restrict" % request.user.pk
            cache_value = cache.get(cache_key)

            # If session key found in cache does not match with current session key
            # from the request object, we delete the cached session key and replace with
            # the current request object's session key
            if cache_value is not None:
                if request.session.session_key != cache_value:
                    engine = import_module(settings.SESSION_ENGINE)
                    session = engine.SessionStore(session_key=cache_value)
                    session.delete()
                    cache.set(cache_key, request.session.session_key, cache_timeout)
            else:
                cache.set(cache_key, request.session.session_key, cache_timeout)

        return self.get_response(request)
