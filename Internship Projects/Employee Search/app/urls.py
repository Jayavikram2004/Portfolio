from django.urls import path
# from .views import EmpListView, EmpDetailView, EmpCreateView, EmpUpdateView, EmpDeleteView
from . import views

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('employee/<str:emp_no>/', views.emp_detail, name='emp_detail'), 
    path('create/', views.emp_create, name='emp_create'),
    path('<str:emp_no>/delete/', views.emp_delete, name='emp_delete'),
    path('<str:emp_no>/update/', views.emp_update, name='emp_update'),
    path('search-recommendations/', views.search_recommendations, name='search_recommendations'),
    
]
