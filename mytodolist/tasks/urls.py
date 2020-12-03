from django.urls import path
from tasks import views

urlpatterns = [
 path('', views.TaskListView.as_view(), name='task_list'),
 path('<int:task_id>/', views.TaskDetailsView.as_view(), name='task_details'),
 path('<int:task_id>/edit/', views.TaskEditView.as_view(), name='task_edit'),
 path('<int:task_id>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
 path('create/', views.TaskCreateView.as_view(), name='task_create'),

]