from django.db import models

# Create your models here.




class ImdWeatherPredictionData1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=255)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255)  # Field name made lowercase.
    weather_stations = models.CharField(db_column='Weather Stations', max_length=255)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    date1 = models.CharField(db_column='Date1', max_length=255)  # Field name made lowercase.
    min_temp_date1 = models.CharField(db_column='Min_Temp_Date1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date1 = models.CharField(db_column='Max_Temp_Date1', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date1 = models.CharField(db_column='Weather_Date1', max_length=255)  # Field name made lowercase.
    date2 = models.CharField(db_column='Date2', max_length=255)  # Field name made lowercase.
    min_temp_date2 = models.CharField(db_column='Min_Temp_Date2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date2 = models.CharField(db_column='Max_Temp_Date2', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date2 = models.CharField(db_column='Weather_Date2', max_length=255)  # Field name made lowercase.
    date3 = models.CharField(db_column='Date3', max_length=255)  # Field name made lowercase.
    min_temp_date3 = models.CharField(db_column='Min_Temp_Date3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date3 = models.CharField(db_column='Max_Temp_Date3', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date3 = models.CharField(db_column='Weather_Date3', max_length=255)  # Field name made lowercase.
    date4 = models.CharField(db_column='Date4', max_length=255)  # Field name made lowercase.
    min_temp_date4 = models.CharField(db_column='Min_Temp_Date4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date4 = models.CharField(db_column='Max_Temp_Date4', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date4 = models.CharField(db_column='Weather_Date4', max_length=255)  # Field name made lowercase.
    date5 = models.CharField(db_column='Date5', max_length=255)  # Field name made lowercase.
    min_temp_date5 = models.CharField(db_column='Min_Temp_Date5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date5 = models.CharField(db_column='Max_Temp_Date5', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date5 = models.CharField(db_column='Weather_Date5', max_length=255)  # Field name made lowercase.
    date6 = models.CharField(db_column='Date6', max_length=255)  # Field name made lowercase.
    min_temp_date6 = models.CharField(db_column='Min_Temp_Date6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date6 = models.CharField(db_column='Max_Temp_Date6', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date6 = models.CharField(db_column='Weather_Date6', max_length=255)  # Field name made lowercase.
    date7 = models.CharField(db_column='Date7', max_length=255)  # Field name made lowercase.
    min_temp_date7 = models.CharField(db_column='Min_Temp_Date7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    max_temp_date7 = models.CharField(db_column='Max_Temp_Date7', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_date7 = models.CharField(db_column='Weather_Date7', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IMD_Weather_Prediction_Data1'
        app_label = 'image_processing'



class ImdWeather1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.CharField(db_column='Date', max_length=255, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=255, blank=True, null=True)  # Field name made lowercase.
    weather_stations = models.CharField(db_column='Weather Stations', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maximum_temp_celsius_field = models.CharField(db_column='Maximum Temp(Celsius)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    maximum_temp_departure_from_normal_celsius_field = models.CharField(db_column='Maximum Temp Departure from Normal(Celsius)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    minimum_temp_celsius_field = models.CharField(db_column='Minimum Temp(Celsius)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    minimum_temp_departure_from_normal_celsius_field = models.CharField(db_column='Minimum Temp Departure from Normal(Celsius)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    number_24_hours_rainfall_mm_field = models.CharField(db_column='24 Hours Rainfall (mm)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'. Field renamed because it wasn't a valid Python identifier.
    relative_humidity_at_0830_hrs_field = models.CharField(db_column='Relative Humidity at 0830 hrs (%)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    relative_humidity_at_1730_hrs_field = models.CharField(db_column='Relative Humidity at 1730 hrs (%)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    todays_sunset_ist_field = models.CharField(db_column='Todays Sunset (IST)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tommorows_sunrise_ist_field = models.CharField(db_column='Tommorows Sunrise (IST)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    moonset_ist_field = models.CharField(db_column='Moonset (IST)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    moonrise_ist_field = models.CharField(db_column='Moonrise (IST)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'IMD_weather1'