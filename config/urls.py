# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from v1.contributors.urls import router as contributors_router
from v1.openings.urls import router as openings_router
from v1.tasks.urls import router as tasks_router
from v1.teams.urls import router as teams_router

admin.site.index_title = 'Admin'
admin.site.site_header = 'thenewboston'
admin.site.site_title = 'thenewboston'

urlpatterns = [

    # Core
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

]

router = DefaultRouter(trailing_slash=False)

router.registry.extend(contributors_router.registry)
router.registry.extend(openings_router.registry)
router.registry.extend(tasks_router.registry)
router.registry.extend(teams_router.registry)

urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
