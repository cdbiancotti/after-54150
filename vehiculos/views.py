from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from vehiculos.models import Moto
from vehiculos.forms import BusquedaMotos
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Motos(ListView):
    model = Moto
    template_name = 'vehiculos/motos.html'
    context_object_name = "motos"
    
    def get_queryset(self):
        marca = self.request.GET.get('marca', '')
        motos = self.model.objects.filter(marca__icontains=marca)
        return motos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = BusquedaMotos()
        context['marca'] = self.request.GET.get('marca', '')
        return context
    
    
class CrearMoto(LoginRequiredMixin, CreateView):
    model = Moto
    template_name = "vehiculos/crear_moto.html"
    success_url = reverse_lazy("motos")
    fields = ["marca", "modelo", "fecha"]

class EliminarMoto(LoginRequiredMixin, DeleteView):
    model = Moto
    template_name = "vehiculos/eliminar_moto.html"
    success_url = reverse_lazy("motos")

class ActualizarMoto(LoginRequiredMixin, UpdateView):
    model = Moto
    template_name = "vehiculos/actualizar_moto.html"
    success_url = reverse_lazy("motos")
    fields = ["marca", "modelo", "fecha"]
    
class VerMoto(DetailView):
    model = Moto
    template_name = "vehiculos/ver_moto.html"

