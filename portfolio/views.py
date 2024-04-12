from django.shortcuts import render, redirect
from .models import Project, ContactRequest, Experience, Certificate, ProjectImages
from django.contrib import messages
from portfolio.forms import ContactForm


# Create your views here.

def inicio(request):
    experiences = Experience.objects.all()
    
    certificates = Certificate.objects.all()

    if request.method == 'POST':

        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            name = data_form['name']
            email = data_form['email']
            title = data_form['title']
            message = data_form['message']
        
            solicitud = ContactRequest(name=name, email=email, title=title, message=message)

            solicitud.save()
            messages.success(request, f'''Perfecto {solicitud.name}, Solicitud de contacto "{solicitud.title}" realizada con éxito!!''')
            
            return redirect('inicio')
    else:
        formulario = ContactForm()

    return render(request,"index.html",{
        'experiences':experiences,
        'formulario':formulario,
        'certificates':certificates,
    })

def proyectos(request):

    proyectos = Project.objects.all()

    return render(request,"proyectos.html", {
        'proyectos': proyectos
    })

def proyecto(request, url):

    proyecto = Project.objects.get(url=url)

    imagenes = ProjectImages.objects.filter(belongsTo=url)

    return render(request,"proyecto.html", {
        'proyecto': proyecto,
        'imagenes': imagenes
    })


def contacto(request):

    if request.method == 'POST':

        formulario = ContactForm(request.POST)

        if formulario.is_valid():
            data_form = formulario.cleaned_data

            name = data_form['name']
            email = data_form['email']
            title = data_form['title']
            message = data_form['message']
        
            solicitud = ContactRequest(name=name, email=email, title=title, message=message)

            solicitud.save()
            messages.success(request, f'Perfecto {solicitud.name}, Solicitud de contacto "{solicitud.title}" realizada con éxito!!')
            
            return redirect('inicio')
    else:
        formulario = ContactForm()
        
    return render(request,"contacto.html",{
        'formulario':formulario
    })
    

def save(request):

    if request.method =='POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title_input')
        message = request.POST.get('message')

        solicitud = ContactRequest(name=name, email=email, title=title, message=message)

        solicitud.save()
        messages.success(request, f'Perfecto {solicitud.name}, Solicitud de contacto "{solicitud.title}" realizada con éxito!!')
        
        return redirect('inicio')