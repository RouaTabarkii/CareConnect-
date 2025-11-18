from django.shortcuts import render
from django.shortcuts import render, redirect
from users.form import   InscPsy ,  InscPatient , RDV_form , AuthForm
from django.contrib import messages
from users.models import patient_insc , psy_insc , ConfPsy 
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from .models import RDV, ConfPsy  , patient_insc , emp_auth , psy_insc
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password





def home(request):
    return render(request, 'users/home.html')


def register_patient(request):
    if request.method == "POST":
        form = InscPatient(request.POST)
        if form.is_valid():  
            password = form.cleaned_data.get("password")
            passw = form.cleaned_data.get("passw")

            if password == passw:
                form.save()
                return redirect('login_patient')
            else:
             form.add_error("passw", "Vérifier votre mot de passe.")
            
    else:
        form = InscPatient()

    return render(request, "users/register_patient.html", {"form": form})


def login_patient(request):

    if request.method == "POST":
        email = request.POST.get('my_email', '')
        password = request.POST.get('my_password', '')

        patient = patient_insc.objects.filter(my_email=email, my_password=password)

        if patient:
            return redirect('Interface_patient')  
        else:
            messages.error(request, "Invalid email or password.")
            return redirect ('login_patient')

    return render(request, 'users/login_patient.html')




def Interface_patient(request) :
    return render(request,"users/Interface_patient.html")

def compte_patient(request) :
    return render(request,"users/Compte_patient.html")


def My_RDV(request):
    if request.method == "POST":
        selected = request.POST.get('choix')
        datee = request.POST.get('date')
        form = RDV_form(request.POST)
        if form.is_valid():
            rdv= RDV()
            rdv.DocName = selected  
            rdv.date = datee
            rdv.save()
            form.save()
            return redirect('RDV_patient')
    else:

        form = RDV_form()  
    ConfPsylist = ConfPsy.objects.all()  

    return render(request, "users/RDV_patient.html", {'form': form, 'ConfPsy' : ConfPsylist})




def rdv_patient(request) :
    return render (request, "users/RDV_patient.html")
def doc_patient (request) :
    return render (request,"users/doc_patient.html")
def login_medecin(request):
    return render(request,"user/login_medecin.html")

def register_psy(request) :
    return render (request ,"users/register_psy.html")
   


def login_psy(request) :
    if request.method == "POST":
        email = request.POST.get('my_email', '')
        password = request.POST.get('my_password', '')

        patient = psy_insc.objects.filter(my_email=email, my_password=password)

        if patient:
            return redirect('Interface_patient')  
        else:
            messages.error(request, "Invalid email or password.")
            return redirect ('login_psy')

    return render(request, 'users/login_psy.html')





def register_psy(request):
    file_url = None  

    if request.method == "POST":
        request_file = request.FILES['fichiers'] if 'fichiers' in request.FILES else None
        form = InscPsy(request.POST, request.FILES)  

        if form.is_valid():
            password = form.cleaned_data.get("password")
            passw = form.cleaned_data.get("passw")

            if password == passw:
                if request_file:
                    fs = FileSystemStorage()
                    file_name = fs.save(request_file.name, request_file)
                    file_url = fs.url(file_name)

                form.save()
                return redirect('login_psy')
            else:
                form.add_error("passw", "Vérifier votre mot de passe.")
    else:
        form = InscPsy()

    return render(request, "users/register_psy.html", {"form": form, "file_url": file_url})



   



