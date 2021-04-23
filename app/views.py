from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import Employee, Qualification
from .forms import EmployeeForm, QualificationForm


class NavQualificationsMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qualifications'] = Qualification.objects.all()
        return context


class HomePageView(TemplateView):
    http_method_names = ['get']
    template_name = 'app/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['qualifications'] = Qualification.objects.all()
        context['count'] = Employee.objects.count()

        return context


class QualificationCreateView(NavQualificationsMixin, CreateView):
    model = Qualification
    form_class = QualificationForm
    template_name = 'app/qualification_form.html'
    success_url = reverse_lazy('employee_list')


class QualificationDetailView(ListView):
    template_name = 'app/employees.html'
    context_object_name = 'employees'
    paginate_by = 50

    def get_queryset(self):
        qualification_item = Qualification.objects.get(
            slug=self.kwargs['qualification'])
        employees = Employee.objects.filter(
            qualification=qualification_item).order_by('pk')

        return employees

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['qualification'] = Qualification.objects.get(
            slug=self.kwargs['qualification'])
        context['qualifications'] = Qualification.objects.all()

        return context


class EmployeeListView(NavQualificationsMixin, ListView):
    model = Employee
    template_name = 'app/employees.html'
    context_object_name = 'employees'
    paginate_by = 50
    queryset = Employee.objects.all()


class EmployeeCreateView(NavQualificationsMixin, CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'app/employee_form.html'
    success_url = reverse_lazy('employee_list')


class EmployeeUpdateView(LoginRequiredMixin, NavQualificationsMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'app/employee_form.html'
    login_url = '/login/'
    success_url = reverse_lazy('employee_list')


class EmployeeDeleteView(LoginRequiredMixin, NavQualificationsMixin, DeleteView):
    model = Employee
    login_url = '/login/'
    success_url = reverse_lazy('employee_list')


class LoginView(NavQualificationsMixin, DjangoLoginView):
    pass
