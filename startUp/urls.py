
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('api.urls')),
    path('card/',include('card_startup.urls')),
    # path('card/',include(card_startup.urls)),
]

if settings.DEBUG:
    urlpatterns += static('/static/', document_root=settings.STATIC_ROOT)
    urlpatterns += static('/media/', document_root=settings.MEDIA_ROOT)
