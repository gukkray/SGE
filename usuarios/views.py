from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import UsuarioForm

class UsuarioCreate(CreateView):
    form_class = UsuarioForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Salva o objeto, mas ainda sem salvar no banco de dados
        user = form.save(commit=False)
        # Criptografa a senha
        user.set_password(form.cleaned_data['password'])
        # Salva o usuário no banco de dados
        user.save()

        # Associa o usuário ao grupo escolhido
        grupo = self.request.POST.get('grupo')
        if grupo == 'Gestor':
            user.groups.add(Group.objects.get(name='Gestores'))
        elif grupo == 'Educador':
            user.groups.add(Group.objects.get(name='Educadores'))

        return super().form_valid(form)
