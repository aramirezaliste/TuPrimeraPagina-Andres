from django.shortcuts import render, redirect

from .models import Cliente, TipoInstrumento, Instrumento
from .forms import ClienteForm, TipoInstrumentoForm, InstrumentoForm

# Create your views here.
def index(request):
    return render(request, "store/index.html", {})

def client_list(request):
    clients = Cliente.objects.all()
    context = {
        "clients": clients
    }
    return render(request, "store/client_list.html", context)

def client_form(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("client_list")
        
    if request.method == "GET":
        form = ClienteForm()
        context = {
            "form": form
        }
    return render(request, "store/client_form.html", context)

def instrument_list(request):
    instruments = Instrumento.objects.all()
    context = {
        "instruments": instruments
    }
    return render(request, "store/instrument_list.html", context)

def instrument_form(request):
    if request.method == "POST":
        form = InstrumentoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("instrument_list")
        
    if request.method == "GET":
        form = InstrumentoForm()
        context = {
            "form": form
        }
    return render(request, "store/instrument_form.html", context)

def type_instrument_list(request):
    type_instruments = TipoInstrumento.objects.all()
    context = {
        "type_instruments": type_instruments
    }
    return render(request, "store/type_instrument_list.html", context)

def type_instrument_form(request):
    if request.method == "POST":
        form = TipoInstrumentoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("type_instrument_list")
        
    if request.method == "GET":
        form = TipoInstrumentoForm()
        context = {
            "form": form
        }
    return render(request, "store/type_instrument_form.html", context)