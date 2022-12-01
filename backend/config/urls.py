from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

admin.sites.AdminSite.site_header = "DriveBC Admin"
admin.sites.AdminSite.site_title = "DriveBC Admin"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("apps.api.urls")),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]

if settings.USE_DJANGO_DEBUG_TOOLBAR:
    try:
        import debug_toolbar
    except ImportError:
        pass
    else:
        urlpatterns = urlpatterns + [path("__debug__/", include(debug_toolbar.urls))]
