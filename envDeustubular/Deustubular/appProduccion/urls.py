from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    # urls principales
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('principal/', views.principal, name='principal'),

    # urls de equipos
    path('equipos/create/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('equipos/<int:pk>/update/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('equipos/<int:pk>/delete/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
    path('equipos/api/', views.EquipoJsonListView.as_view(), name='api_equipo_list'),
    path('equipos/api/<int:pk>/', views.EquipoJsonDetailView.as_view(), name='api_equipo_detail'),

    # urls de empleados
    path('empleados/create/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('empleados/<int:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('empleados/<int:pk>/update/', views.EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('empleados/<int:pk>/delete', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('empleados/api/', views.EmpleadoJsonListView.as_view(), name='api_empleado_list'),
    path('empleados/api/<int:pk>/', views.EmpleadoJsonDetailView.as_view(), name='api_empleado_detail'),

    # urls de proesos
    path('procesos/create/', views.ProcesoCreateView.as_view(), name='proceso_create'),
    path('procesos/', views.ProcesoListView.as_view(), name='proceso_list'),
    path('procesos/<int:pk>/', views.ProcesoDetailView.as_view(), name='proceso_detail'),
    path('procesos/<int:pk>/update/', views.ProcesoUpdateView.as_view(), name='proceso_edit'),
    path('procesos/<int:pk>/delete/', views.ProcesoDeleteView.as_view(), name='proceso_delete'),
    path('procesos/api/', views.ProcesoJsonListView.as_view(), name='api_proceso_list'),
    path('procesos/api/<int:pk>/', views.ProcesoJsonDetailView.as_view(), name='api_proceso_detail'),

    # url de novedades
    path('novedades', views.NovedadesCreateView.as_view(), name='novedades_create'),
]
