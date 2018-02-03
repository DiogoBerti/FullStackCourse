from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (View, TemplateView, ListView,
                                  DetailView, CreateView, UpdateView,
                                  DeleteView)
from django.http import HttpResponse

from . import models

class CBView(View):
    # Definiçao de views por classes
    def get(self,request):
        return HttpResponse("Class Based Views Are COOL!")

# Herdando essa classe, apenas passando o template_name já monta a view...
class IndexView(TemplateView):
    template_name = 'index.html'

    # Usado para definir o context que será mostrado na pagina...
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Basic Injection'
        return context


class SchoolList(ListView):
    # Retorna o contexto automaticamente como school_list
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'new_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("new_app:list")
