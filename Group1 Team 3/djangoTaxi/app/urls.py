from django.urls import path
from .views import predict_view, index_view  # Import the index_view

urlpatterns = [
    path('', index_view, name='index'),  # Add this line to handle the root URL
    path('predict/', predict_view, name='predict'),
]