from django.urls import path

from .views import EmpresaListView, EmpresaView, EmpresaUploadView

urlpatterns = [
    path('', EmpresaListView.as_view()),
    path('<int:id_empresa>/', EmpresaView.as_view()),
    path('upload/', EmpresaUploadView.as_view()),
]
