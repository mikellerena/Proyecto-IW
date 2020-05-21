from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('produccion/', LoginView.as_view(), name='login'),
    path('produccion/logout/', LogoutView.as_view(), name='logout'),
    path('produccion/principal/', views.principal, name='principal'),
    path('produccion/equipos/create/', views.EquipoCreateView.as_view(), name='equipo_create'),
    path('produccion/equipos/', views.EquipoListView.as_view(), name='equipo_list'),
    path('produccion/equipos/<int:pk>/', views.EquipoDetailView.as_view(), name='equipo_detail'),
    path('produccion/equipos/<int:pk>/update/', views.EquipoUpdateView.as_view(), name='equipo_edit'),
    path('produccion/equipos/<int:pk>/delete/', views.EquipoDeleteView.as_view(), name='equipo_delete'),
    path('produccion/equipo/json/', views.EquipoJsonList.as_view(), name='json_equipo_list'),
    path('produccion/empleados/create/', views.EmpleadoCreateView.as_view(), name='empleado_create'),
    path('produccion/empleados/', views.EmpleadoListView.as_view(), name='empleado_list'),
    path('produccion/empleados/<str:pk>/', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('produccion/empleados/<str:pk>/update/', views.EmpleadoUpdateView.as_view(), name='empleado_edit'),
    path('produccion/empleados/<str:pk>/delete', views.EmpleadoDeleteView.as_view(), name='empleado_delete'),
    path('produccion/procesos/create/', views.ProcesoCreateView.as_view(), name='proceso_create'),
    path('produccion/procesos/', views.ProcesoListView.as_view(), name='proceso_list'),
    path('produccion/procesos/<str:pk>/', views.ProcesoDetailView.as_view(), name='proceso_detail'),
    path('produccion/procesos/<str:pk>/update/', views.ProcesoUpdateView.as_view(), name='proceso_edit'),
    path('produccion/procesos/<str:pk>/delete/', views.ProcesoDeleteView.as_view(), name='proceso_delete'),
    path('produccion/novedades', views.NovedadesCreateView.as_view(), name='novedades_create'),

]
