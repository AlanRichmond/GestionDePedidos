from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from  django.core.mail import EmailMessage

# Create your views here.

def contacto(request):

    formulario_contacto = Formulario_contacto()

    if request.method == 'POST':
        formulario_contacto = Formulario_contacto(data=request.POST)
        
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")

            email = EmailMessage("mensaje desde App Django",
            "El usuario con nombre {} con la direccion {} escribe lo sigiente: \n\n {}".format(nombre, email, contenido), 
            '', ["richmondalan00@gmail.com"], reply_to=[email])

            try:
                email.send()
                
                return redirect("/contacto/?valido")
            
            except:
                return redirect("/contacto/?novalido")


            

    return render(request, 'contacto/contacto.html', {'miformulario': formulario_contacto})

