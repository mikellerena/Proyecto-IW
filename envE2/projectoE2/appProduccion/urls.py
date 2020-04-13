from django.urls import path
from . import views

urlpatterns = [
    path('createequipo/', views.CreateEquipoView.as_view(), name='equipo_form'),
    path('equipos/', views.EquiposListView.as_view(), name='equipos_list'),
    path('equipos/<int:pk>/', views.EquiposDetailView.as_view(), name='equipo_detail'),
    path('editarequipo/<int:pk>/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('createempleado/', views.CreateEmpleadoView.as_view(), name='empleado_form'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleados_list'),
    path('empleados/<str:pk>/', views.EmpleadosDetailView.as_view(), name='empleado_detail'),
    path('createproceso/', views.CreateProcesoView.as_view(), name='proceso_form'),
    path('procesos/', views.ProcesosListView.as_view(), name='procesos_list'),
    path('procesos/<str:pk>/', views.ProcesosDetailView.as_view(), name='proceso_detail'),
]
