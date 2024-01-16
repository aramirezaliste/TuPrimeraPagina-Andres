from django import forms

from .models import Cliente, Instrumento, TipoInstrumento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = "__all__"

class TipoInstrumentoForm(forms.ModelForm):
    class Meta:
        model = TipoInstrumento
        fields = "__all__"