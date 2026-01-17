from django.urls import path
from . import views

urlpatterns = [
    path('solar/', views.solar_list),
    path('hybrid/', views.hybrid_view),
    path('economics/', views.economic_view),
    path('forecast7/', views.forecast_7days),   # ✅ fixed
    path('upload-csv/', views.upload_csv),
]

