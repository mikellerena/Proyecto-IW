from django.urls import path
from . import views

urlpatterns = [
    path('createequipo/', views.CreateEquipoView.as_view(), name='equipo_form'),
    path('equipos/', views.EquiposListView.as_view(), name='equipos'),
    path('equipo/<int:pk>/', views.EquiposDetailView.as_view(), name='equipo'),
    path('createempleado/', views.CreateEmpleadoView.as_view(), name='empleado_form'),
    path('')
]
