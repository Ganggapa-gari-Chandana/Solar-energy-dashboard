from django.db import models

# Create your models here.

class SolarData(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    irradiance = models.FloatField()
    temperature = models.FloatField()
    energy_generated = models.FloatField()

class HybridSystem(models.Model):
    system_type = models.CharField(max_length=50)
    solar_power = models.FloatField()
    wind_power = models.FloatField()
    battery_storage = models.FloatField()
    total_output = models.FloatField()

class EconomicAnalysis(models.Model):
    installation_cost = models.FloatField()
    maintenance_cost = models.FloatField()
    yearly_savings = models.FloatField()
    roi = models.FloatField()

class PolicyData(models.Model):
    country = models.CharField(max_length=50)
    subsidy = models.FloatField()
    tax_benefit = models.FloatField()
    policy_description = models.TextField()

