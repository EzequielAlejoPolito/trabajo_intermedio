from django.shortcuts import render
from my_app.forms import DatoFormulario

from my_app.models import Dato
from my_app.forms import DatoFormulario

def datos(request):
    datos = Dato.objects.all()

    context_dict = {"datos": datos}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/datos_familia.html",
    )

def agregarDatos(request):
      
      if request.method == 'POST':
      
            datos = DatoFormulario(request.POST)
            
            print(datos)

            if datos.is_valid:

                  data = datos.cleaned_data
                
                  dato = Dato (rol = data ["rol"], name = data ["name"], last_name = data ["last_name"])
                
                  dato.save()
                
                  return render(request, "my_app/datos_familia.html")
      else:
            datos = DatoFormulario()
 
      return render(request, "my_app/dato_formulario.html", {"datos": datos})

            