from django.urls import path

from api.banner.views import Banner_Create, Banner_Update, Banner_Delete

urlpatterns = [
    path('create/', Banner_Create.as_view(), name='banner-create-api'),
    path('update/',Banner_Update.as_view(), name ='banner-update-api'),
    path('delete/',Banner_Delete.as_view(), name ='banner-delete-api'),

]
