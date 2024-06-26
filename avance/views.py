from rest_framework import permissions, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Avances
from .serializers import AvancesSerializer

# Create your views here.

class UploadAvance(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request):
        serializer = AvancesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AvanceListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Avances.objects.all()
    serializer_class = AvancesSerializer
    pagination_class = None
    
class AvanceListByTypeView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AvancesSerializer
    pagination_class = None
    def get_queryset(self, request, type, id_obra):
        queryset = Avances.objects.filter(id_obra=id_obra)
        queryset = queryset.filter(tipo=type)
        return queryset
    
    
class EliminarAvance(DestroyAPIView):
    serializer_class = AvancesSerializer
    def get_queryset(self):
        id_obra = self.kwargs["pk"]
        if id_obra is not None:
            queryset = Avances.objects.filter(id=id_obra) 
            return queryset
        else:
            raise NotFound('No se encontro el parametro "pk" en la URL')
    
class AvanceListByObra(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AvancesSerializer
    pagination_class = None
    def get_queryset(self):
        id_obra = self.kwargs["id_obra"]
        queryset = Avances.objects.filter(id_obra = id_obra)
        return  queryset