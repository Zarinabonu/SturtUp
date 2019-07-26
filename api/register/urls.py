from django.urls import path

from api.register.views import RegisterCreate , RegisterUpdate , RegisterDelete

urlpatterns = [
    path('create/', RegisterCreate.as_view(), name='register-create-api'),
    path('update/<int:id>', RegisterUpdate.as_view(), name ='register-update-api'),
    path('delete/<int:id>', RegisterDelete.as_view(), name ='register-delete-api')
]
