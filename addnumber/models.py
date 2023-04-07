from django.db import models

# Create your models here.
class Calculator(models.Model):
    class Meta:
        db_table ="my_calculator"
    num = models.IntegerField(default=0)

class Result(models.Model):
    class Meta:
        db_table ="my_answer"
    num = models.ForeignKey(Calculator, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)