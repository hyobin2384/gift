from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from mainapp.decorators import main_ownership_required
from mainapp.forms import MainCreationForm
from mainapp.models import Main

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class MainCreateView(CreateView):
    model = Main
    form_class = MainCreationForm
    template_name = 'mainapp/create.html'

    def form_valid(self, form):
        temp_main = form.save(commit=False)
        temp_main.writer = self.request.user
        temp_main.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mainapp:detail', kwargs={'pk':self.object.pk})

class MainDetailView(DetailView):
    model = Main
    context_object_name = 'target_main'
    template_name = 'mainapp/detail.html'

@method_decorator(main_ownership_required, 'get')
@method_decorator(main_ownership_required, 'post')
class MainUpdateView(UpdateView):
    model = Main
    context_object_name = 'target_main'
    form_class = MainCreationForm
    template_name = 'mainapp/update.html'

    def get_success_url(self):
        return reverse('mainapp:detail', kwargs={'pk':self.object.pk})

@method_decorator(main_ownership_required, 'get')
@method_decorator(main_ownership_required, 'post')
class MainDeleteView(DeleteView):
    model = Main
    context_object_name = 'target_main'
    success_url = reverse_lazy('mainapp:list')
    template_name = 'mainapp/delete.html'

class MainListView(ListView):
    model = Main
    context_object_name = 'main_list'
    template_name = "mainapp/list.html"

class PidListView(ListView):
    model = Main
    context_object_name = 'pid_list'
    template_name = "mainapp/pid.html"

