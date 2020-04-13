from django.urls import path
from . import views

urlpatterns = [
    path('createequipo/', views.CreateEquipoView.as_view(), name='equipo_create'),
<<<<<<< Updated upstream
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
=======
    path('equipos/', views.EquiposListView.as_view(), name='equipo_list'),
    path('equipos/<int:pk>/', views.EquiposDetailView.as_view(), name='equipo_detail'),
>>>>>>> Stashed changes
    path('editarequipo/<int:pk>/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('createempleado/', views.CreateEmpleadoView.as_view(), name='empleado_create'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleado_list'),
    path('empleados/<str:pk>/', views.EmpleadosDetailView.as_view(), name='empleado_detail'),
    path('createproceso/', views.CreateProcesoView.as_view(), name='proceso_create'),
    path('procesos/', views.ProcesosListView.as_view(), name='proceso_list'),
    path('procesos/<str:pk>/', views.ProcesosDetailView.as_view(), name='proceso_detail'),
]
