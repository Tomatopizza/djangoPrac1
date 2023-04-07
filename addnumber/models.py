from django.db import models

# Create your models here.
class Calculator(models.Model):
    class Meta:
        db_table ="my_calculator"
    num = models.IntegerField(default=0)

    