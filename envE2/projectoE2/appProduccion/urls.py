from django.urls import path
from . import views

urlpatterns = [
    path('createequipo/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('editarequipo/<int:pk>/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('borrarequipo/<int:pk>/', views.EquipoDeleteView.as_view(), name='equipo_borrar'),
    path('createempleado/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/<str:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('createproceso/', views.ProcesoCreateView.as_view(), name='proceso_create'),
    path('procesos/', views.ProcesoListView.as_view(), name='proceso_list'),
    path('procesos/<str:pk>/', views.ProcesoDetailView.as_view(), name='proceso_detail'),
]
