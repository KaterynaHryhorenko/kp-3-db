from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeUpdateView.as_view(),
         name='employee_edit'),
    path('employees/<int:pk>/delete/',
         views.EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employees/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('qualifications/add/',
         views.QualificationCreateView.as_view(), name='qualification_add'),
    path('qualifications/<slug:qualification>/',
         views.QualificationDetailView.as_view(), name='qualification_detail'),
    path('login/', views.LoginView.as_view(), name='login'),
]
