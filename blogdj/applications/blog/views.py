from django.shortcuts import render
#
from rest_framework.response import Response
from rest_framework import status
#
from rest_framework.views import APIView
from rest_framework.generics import (
  CreateAPIView,
  RetrieveAPIView, 
  ListAPIView
)

# seralizers
from .serializers import (
  SuscriberModelSerializer, 
  SuscriberSerializer, 
  SuscriptionSerializer,
  BlogSerializer,
  AuthorSerializer,
  CategorySerilizer,
  CategoryHiperLinkSerializer
)
#
from .models import Suscriptions, Blog, Author, Category


class RegistrarSuscripcion(CreateAPIView):
  serializer_class = SuscriberModelSerializer
  queryset = Suscriptions.objects.all()


class AgregarSuscripcion(CreateAPIView):
  serializer_class = SuscriberSerializer
  
  def create(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      print('**************')
      print(serializer.validated_data['email'])
      self.perform_create(serializer)
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  

class CrearSuscripcion(APIView):

    def post(self, request):
      serializer = SuscriptionSerializer(data=request.data)
      if serializer.is_valid():
        print('guadar data')
        #
        #
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      else:
        print('error serializador')
        print(serializer.errors)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetail(RetrieveAPIView):
  lookup_field = 'pk'
  serializer_class = BlogSerializer
  queryset = Blog.objects.all()


class ListaAthores(ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class ListaCategorias(ListAPIView):
    # serializer_class = CategorySerilizer
    serializer_class = CategoryHiperLinkSerializer
    queryset = Category.objects.all()


class CategoryDetail(RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = CategorySerilizer
    queryset = Category.objects.all()