from django.urls import path

from .views import TipoObraListView, TipoObraUploadView

urlpatterns = [
    path('', TipoObraListView.as_view()),
    path('upload/', TipoObraUploadView.as_view())
]
