from django.urls import path
from .views import  uploadManual, import_excel

urlpatterns = [
    path('upload/file/', import_excel.as_view()),
    path('upload/form/', uploadManual.as_view())
    
]