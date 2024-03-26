from django.urls import path
from .views import import_from_excel, uploadManual

urlpatterns = [
    path('upload/file/', import_from_excel, name='import_from_excel'),
    path('upload/form/', uploadManual.as_view())
    
]