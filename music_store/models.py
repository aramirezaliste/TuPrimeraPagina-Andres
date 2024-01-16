from django.db import models

# Create your models here.
class Cliente(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

class TipoInstrumento(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class Instrumento(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    instrument_type = models.ForeignKey(TipoInstrumento, null=True, blank=True, on_delete=models.SET_NULL) 

    def __str__(self):
        return f" {self.name} {self.instrument_type}"