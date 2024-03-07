from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response

from .models import TipoObra
from .serializers import TipoObraSerializer

class TipoObraListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = TipoObraSerializer
    pagination_class = None
    queryset = TipoObra.objects.all()
    
class TipoObraUploadView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, format=None):
        serializer = TipoObraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)