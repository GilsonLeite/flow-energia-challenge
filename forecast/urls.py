from django.urls import path
from .views import (
    ForecastDetailView,
    ForecastLoadDetailView
)

urlpatterns = [
    path('', ForecastDetailView.as_view(),
         name='analysis_result'),
    path('analysis_load_db', ForecastLoadDetailView.as_view(),
         name='analysis_load_db'),
]
