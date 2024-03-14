from django.urls import path
from .views import NoderedView

urlpatterns = [
    path('', NoderedView.as_view(), name='NodeView'),
]
