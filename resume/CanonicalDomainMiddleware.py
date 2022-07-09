from django.shortcuts import redirect
from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings


class CanonicalDomainMiddleware(object):

    """Middleware that redirects to a canonical domain."""

    
    def __call__(self, request):
        
            if request.is_secure():
                canonical_url = "https://render.com/"
            else:
                canonical_url = "https://render.com/"
            canonical_url += settings.SITE_DOMAIN + request.get_full_path()
            return redirect(canonical_url, permanent=True)
