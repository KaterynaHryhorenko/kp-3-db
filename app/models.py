from django.urls import reverse
from django.db import models
from django.template.defaultfilters import slugify


class Qualification(models.Model):
    profile = models.CharField(max_length=50, primary_key=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        ordering = ['profile']

    def __str__(self):
        return self.profile

    def get_absolute_url(self):
        return reverse('qualification_detail', kwargs={'qualification': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.profile)
        return super().save(*args, **kwargs)

    def count_of_employees(self):
        return self.employees.count()


class Employee(models.Model):
    enrollee_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=30, blank=True)
    enrolled_university = models.CharField(max_length=30)
    education_level = models.CharField(max_length=30)
    major_discipline = models.CharField(max_length=30, blank=True)
    experience = models.CharField(max_length=5)
    company_type = models.CharField(max_length=50, blank=True)
    last_new_job = models.CharField(max_length=30)
    training_hours = models.IntegerField()
    target = models.FloatField()

    qualification = models.ForeignKey(
        to=Qualification, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        ordering = ['enrollee_id']

    def __str__(self):
        return f'Employee with id - {self.enrollee_id}'

    def get_edit_url(self):
        return reverse('employee_edit', kwargs={'pk': self.enrollee_id})

    def get_delete_url(self):
        return reverse('employee_delete', kwargs={'pk': self.enrollee_id})
