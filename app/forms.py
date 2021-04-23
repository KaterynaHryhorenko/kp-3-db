from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Employee, Qualification


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('gender', 'enrolled_university', 'education_level',
                  'major_discipline', 'experience', 'company_type',
                  'last_new_job', 'training_hours', 'target', 'qualification')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save employee'))


class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = ('profile', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save qualification'))
