from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UsuarioForm

class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        grupo = self.request.POST.get('grupo')
        if grupo == 'Gestor':
            self.object.groups.add(Group.objects.get(name='Gestores'))
        elif grupo == 'Educador':
            self.object.groups.add(Group.objects.get(name='Educadores'))
        return response
