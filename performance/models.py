from django.db import models
from datetime import datetime

class Performance(models.Model):
    cost = models.FloatField(default=0)
    revenue = models.FloatField(default=0)
    creation_date = models.DateField(auto_now_add=True)

    def profit(self):
        return self.revenue - self.cost

    def min_roi(self):
        return ((self.profit/self.cost)*(100))

    class Meta:
        abstract = True


class HourlyPerformance(Performance):
    date_time = models.DateTimeField(default=datetime.now())


class DailyPerformance(Performance):
    date = models.DateField(default=datetime.date.today())


class CustomQuerySet(models.QuerySet):
    
    def filter_by_min_roi(min_roi: float):
        pass
