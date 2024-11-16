from django.urls import path
from .views import receive_data
from .views import dashboard

urlpatterns = [
    path('receive/', receive_data, name='receive_data'),
    path('dashboard/', dashboard, name='dashboard')
]