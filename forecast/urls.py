from django.urls import path
from .views import ForecastDetailView

urlpatterns = [
    path('', ForecastDetailView.as_view(),
         name='analysis_result'),
]
