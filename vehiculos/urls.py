from django.urls import path
from vehiculos import views

urlpatterns = [
    path('motos/', views.Motos.as_view(), name='motos'),
    path('motos/crear/', views.CrearMoto.as_view(), name='crear_moto'),
    path('motos/<int:pk>/', views.VerMoto.as_view(), name='ver_moto'),
    path('motos/<int:pk>/actualizar/', views.ActualizarMoto.as_view(), name='actualizar_moto'),
    path('motos/<int:pk>/eliminar/', views.EliminarMoto.as_view(), name='eliminar_moto'),
]
