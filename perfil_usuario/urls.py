from django.urls import path
from .views import UserProfileView, UserProfileUpdateView, UsersByEmpresaView, UsersListView, UserProfileByAccount

urlpatterns = [
    #cargar profile
    path('', UserProfileView.as_view()),
    #perfil de usuario por id
    path('<int:id_profile>/', UserProfileView.as_view()),
    path('set/<int:id_acc>/', UserProfileByAccount.as_view()),
    #lista perfiles segun empresa
    path('lista/<int:id_empresa>/', UsersByEmpresaView.as_view()),
    
    path('lista/', UsersListView.as_view()),
    #actualizar profile
    path("update/<int:id_user>/", UserProfileUpdateView.as_view()),
]