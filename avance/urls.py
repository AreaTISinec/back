from django.urls import path
from .views import UploadAvance, AvanceListView, EliminarAvance, AvanceListByObra

urlpatterns = [
    path('newAvance/', UploadAvance.as_view()),
    #path('list/', AvanceListView.as_view()),
    path('list/<int:id_obra>/', AvanceListByObra.as_view()),
    path('delete/<int:pk>/', EliminarAvance.as_view()),
]