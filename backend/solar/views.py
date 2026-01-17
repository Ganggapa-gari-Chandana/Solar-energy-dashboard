import pandas as pd
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import SolarData, HybridSystem, EconomicAnalysis
from .serializers import SolarDataSerializer, HybridSerializer, EconomicSerializer
from .services.forecasting import seven_day_forecast


# ---------- SOLAR DATA ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def solar_list(request):
    data = SolarData.objects.all()
    return Response(SolarDataSerializer(data, many=True).data)


# ---------- HYBRID SYSTEM ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def hybrid_view(request):
    data = HybridSystem.objects.all()
    return Response(HybridSerializer(data, many=True).data)


# ---------- ECONOMIC ANALYSIS ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def economic_view(request):
    data = EconomicAnalysis.objects.last()
    return Response(EconomicSerializer(data).data)


# ---------- 7 DAY FORECAST ----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def forecast_7days(request):
    qs = SolarData.objects.values()
    result = seven_day_forecast(list(qs))
    return Response(result)


# ---------- CSV UPLOAD ----------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv(request):
    file = request.FILES['file']
    df = pd.read_csv(file)

    for _, row in df.iterrows():
        SolarData.objects.create(
            location=row['location'],
            date=row['date'],
            irradiance=row['irradiance'],
            temperature=row['temperature'],
            energy_generated=row['energy_generated']
        )

    return Response({"status": "CSV uploaded successfully"})
