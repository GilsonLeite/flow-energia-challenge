from django.urls import path
from .views import (
    ForecastDetailView,
    ForecastLoadDatabaseView
)

urlpatterns = [
    path('', ForecastDetailView.as_view(), name='analysis_result'),
    path('analysis_load_db', ForecastLoadDatabaseView.as_view(),
         name='analysis_load_db'),
]
