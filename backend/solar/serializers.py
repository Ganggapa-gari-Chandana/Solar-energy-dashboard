from rest_framework import serializers
from .models import SolarData, HybridSystem, EconomicAnalysis

class SolarDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarData
        fields = '__all__'


class HybridSerializer(serializers.ModelSerializer):
    class Meta:
        model = HybridSystem
        fields = ['system_type', 'total_output']


class EconomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicAnalysis
        fields = '__all__'
