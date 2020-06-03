from django.urls import path
from .views import (
    ForeForm,
    ForecastLoadDatabaseView
)

urlpatterns = [
    path('', ForeForm.as_view(), name='analysis_result'),
    path('analysis_load_db', ForecastLoadDatabaseView.as_view(),
         name='analysis_load_db'),
]
