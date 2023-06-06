from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('v1/', include('movies.api.v1.urls')),
]

if settings.DEBUG:
    import debug_toolbar as _

    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
