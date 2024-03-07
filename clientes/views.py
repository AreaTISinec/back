from rest_framework import permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Cliente
from .serializers import ClienteSerializer

class ClienteListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ClienteSerializer
    pagination_class = None
    queryset = Cliente.objects.all()
    
class ClienteView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request, rut):
        try:
            cliente = Cliente.objects.get(rut=rut)
        except Cliente.DoesNotExist:
            return Response({"error": "El cliente no existe"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClienteSerializer(cliente)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

class ClienteUploadView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    