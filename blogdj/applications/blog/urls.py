from django.urls import path

from . import views

app_name = "blog_app"

urlpatterns = [
  path(
    'api/suscriptions/register/',
    views.RegistrarSuscripcion.as_view(),
  ),
  path(
    'api/suscriptions/add/',
    views.AgregarSuscripcion.as_view(),
  ),
  path(
    'api/suscriptions/create/',
    views.CrearSuscripcion.as_view(),
  ),
  path(
    'api/blog/detail/<pk>/',
    views.BlogDetail.as_view(),
  ),
  path(
    'api/author/list/',
    views.ListaAthores.as_view(),
  ),
  
  path(
    'api/category/list/',
    views.ListaCategorias.as_view(),
  ),
  path(
    'api/category/detail/<pk>/',
    views.CategoryDetail.as_view(),
    name='category-detail'
  ),
]