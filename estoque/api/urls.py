from django.urls import path
from .views import ComponenteAPIView

urlpatterns = [
    path('<int:id>/', ComponenteAPIView.as_view(), name='api-componente'),
    path('', ComponenteAPIView.as_view(), name='api-componente'),
]
