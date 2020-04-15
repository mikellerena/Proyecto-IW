from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('principal/', views.principal, name='principal'),
    path('gequipos/', views.g_equipo, name='gestion_equipo'),
    path('gempleados/', views.g_empleado, name='gestion_empleado'),
    path('gprocesos/', views.g_proceso, name='gestion_proceso'),
    path('createequipos/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('editarequipos/<int:pk>/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('borrarequipos/<int:pk>/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
    path('createempleados/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/<str:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('editarempleados/<str:pk>/', views.EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('borrarempleados/<str:pk>/', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('createprocesos/', views.ProcesoCreateView.as_view(), name='proceso_create'),
    path('procesos/', views.ProcesoListView.as_view(), name='proceso_list'),
    path('procesos/<str:pk>/', views.ProcesoDetailView.as_view(), name='proceso_detail'),
    path('editarprocesos/<str:pk>/', views.ProcesoUpdateView.as_view(), name='proceso_edit'),
    path('borrarprocesos/<str:pk>/', views.ProcesoDeleteView.as_view(), name='proceso_delete'),
]
