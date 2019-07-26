from django.urls import path, include

urlpatterns = [
    path('banner/', include('api.banner.urls')),
    path('card/',include('api.card.urls')),
    path('register/',include('api.register.urls')),
    # path('register/',include('api.register.views')),
   
]