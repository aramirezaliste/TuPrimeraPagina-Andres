from django import forms

from .models import Cliente, Instrumento, TipoInstrumento

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(
                attrs =  { 
                    'class':'form-control mb-3 '  
                    }
                ),
            'email': forms.EmailInput(
                attrs =  { 
                    'class':'form-control mb-3 '  
                    }
                )
        }
        labels = {
            'name': "Cliente",
            'email': "Email"
        }


class InstrumentoForm(forms.ModelForm):
    class Meta:
        model = Instrumento
        fields = ['name', 'quantity', 'instrument_type']
        widgets = {
            'name': forms.TextInput(
                attrs =  { 
                    'class':'form-control mb-3 '  
                    }
                ),
            'quantity': forms.NumberInput(
                attrs =  { 
                    'class':'form-control mb-3 '  
                    }
                ),
            'instrument_type': forms.Select(
                attrs =  { 
                    'class':'form-control mb-3 '  
                    }
                )
        }
        labels = {
            'name': "Cliente",
            'quantity': "Cantidad",
            'instrument_type': "Tipo de instrumento"

        }

class TipoInstrumentoForm(forms.ModelForm):
    class Meta:
        model = TipoInstrumento
        fields = ["name"]
        widgets = {
            'name': forms.TextInput(
                attrs =  { 
                    'class':'form-control mb-3 '  
                    }
                )
        }
        labels = {
            'name': "Tipo de instrumento"
        }
