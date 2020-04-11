from django.urls import path
from . import views

urlpatterns = [
    path('createequipo/', views.CreateEquipoView.as_view(), name='equipo_form'),
    path('equipos/', views.EquiposListView.as_view(), name='equipos'),
    path('equipo/<int:pk>/', views.EquiposDetailView.as_view(), name='equipo_detail'),
    path('createempleado/', views.CreateEmpleadoView.as_view(), name='empleado_form'),
    path('empleados/', views.EmpleadosListView.as_view(), name='empleados'),
    path('empleado/<str:pk>/', views.EmpleadosDetailView.as_view(), name='empleado_detail'),
]
