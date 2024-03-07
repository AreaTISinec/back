from django.urls import path

from .views import ClienteListView, ClienteView, ClienteUploadView

urlpatterns = [
    path('', ClienteListView.as_view()),
    path('<str:rut>/', ClienteView.as_view()),
    path('upload/', ClienteUploadView.as_view())
]
