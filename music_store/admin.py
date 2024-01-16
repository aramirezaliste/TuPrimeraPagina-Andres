from django.contrib import admin

from .models import Cliente, Instrumento, TipoInstrumento

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Instrumento)
admin.site.register(TipoInstrumento)
