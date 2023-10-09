from django.utils import timezone
from django.db import models

# Create your models here
class Config(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=False)
    # created_by = models.CharField(default='')
    # modified_by = models.CharField(default='')
    # created_at = models.DateTimeField(default=timezone.now)
    # modified_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 

class Week(models.Model):
    day = models.CharField(max_length=20)
    class Meta:
        db_table = "days_of_week"
    def __str__(self):
        return self.day

class TimeTier(models.Model):
    config_key = models.ForeignKey(Config, on_delete=models.CASCADE)
    start_tier_time = models.CharField()
    end_tier_time = models.CharField()
    time_multiplier_factor = models.DecimalField(max_digits=5, decimal_places=3)

    class Meta:
        db_table = "time-tier-pricing"

class DistanceBaseTier(models.Model):
    config_key = models.ForeignKey(Config, on_delete=models.CASCADE)
    selected_days = models.ManyToManyField(Week, through='DistanceBaseTierWeek')
    max_base_tier_distance = models.DecimalField(max_digits=3, decimal_places=1)
    dbp = models.IntegerField()

    class Meta:
        db_table = "distance-base-tier-pricing"

#Many-To-Many Connected table
class DistanceBaseTierWeek(models.Model):
    distance_base_tier = models.ForeignKey(DistanceBaseTier, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    class Meta:
        db_table= "distance-base-tier-week"

class DistanceAdditionalTier(models.Model):
    config_key = models.ForeignKey(Config, on_delete=models.CASCADE, unique=True)
    per_km_price = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        db_table = "additional-distance-tier-pricing"

class Waiting(models.Model):
    config_key = models.ForeignKey(Config, on_delete=models.CASCADE, unique=True)
    free_mins = models.IntegerField()
    per_min_charge = models.DecimalField(max_digits=4, decimal_places=2)
    class Meta: 
        db_table = "waiting-charges"