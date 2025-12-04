from django.shortcuts import render
from django.shortcuts import render, redirect
from users.form import   InscPsy ,  InscPatient , RDV_form , AuthForm
from django.contrib import messages
from users.models import patient_insc , psy_insc , ConfPsy 
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.core.files.storage import FileSystemStorage
from .models import RDV, ConfPsy  , patient_insc , emp_auth , psy_insc , RDV
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout
from django.core.mail import send_mail







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






def Interface_psy(request):
    psy_id = request.session.get('psy_id')  
    
    if not psy_id:
        return redirect('login_psy') 

    psy = psy_insc.objects.get(id=psy_id)  
    
    return render(request, 'users/interface_psy.html', {'psy': psy})





def login_psy(request):

    if request.method == "POST":
        myy_email = request.POST.get('email', '')
        myy_password = request.POST.get('password', '')

        psy = psy_insc.objects.filter(email=myy_email, password=myy_password)

        if psy:
            psy_obj = psy.first()

            request.session['psy_id'] = psy_obj.id  

            return redirect('Interface_psy')  
        else:
            messages.error(request, "Invalid email or password.")
            return redirect ('login_psy')

    return render(request, 'users/login_psy.html')



def Interface_patient(request) :
    patient_id = request.session.get('patient_id')  
    
    if not patient_id:
        return redirect('login_patient') 

    patient = patient_insc.objects.get(id=patient_id)  

    
    return render(request, 'users/interface_patient.html', {'patient': patient})





def login_patient(request):

    if request.method == "POST":
        email = request.POST.get('my_email', '')
        password = request.POST.get('my_password', '')

        patient = patient_insc.objects.filter(my_email=email, my_password=password)

        if patient:
            patient_obj = patient.first()

            request.session['patient_id'] = patient_obj.id  
            request.session['patient_email'] = patient_obj.my_email

            

            return redirect('Interface_patient')  
        else:
            messages.error(request, "Invalid email or password.")
            return redirect ('login_patient')

    return render(request, 'users/login_patient.html')





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




def ConfRDV(request):

    rdvs = RDV.objects.all()
    
    return render(request, 'users/conf_rdv.html', {'rdvs': rdvs})



def ConfRendezVous(request, rdv_id) :
        rdvs = RDV.objects.all()
        rdv = RDV.objects.get(id=rdv_id) 
        Conf_date = rdv.date
        Conf_Doc = rdv.DocName 

        send_mail(
                subject= "Confirmation de RDV",
                message = f"Votre rendez-vous avec est confirmé le {Conf_date}",
                from_email= "CareConnect <tbarki12344@gmail.com>",
                recipient_list= [rdv.email],
                fail_silently=False,


            )
        DRDV = RDV.objects.get(id=rdv_id)
        DRDV.delete()


        
        return render (request , 'users/conf_rdv.html',{'rdvs' : rdvs})

    

def RefRDV(request , rdv_id) :
            rdvs = RDV.objects.all()
            rdv = RDV.objects.get(id=rdv_id) 


            send_mail(
                subject= "Annulation de RDV" ,
                message= "La date que vous avez choisit n'est pas disponible vous devez accéder a notre site web et choisissez un autre RDV",
            
                from_email= "CareConnect <tbarki12344@gmail.com>",
                recipient_list= [rdv.email],
                fail_silently=False,


            )
            DRDV = RDV.objects.get(id=rdv_id)
            DRDV.delete()
            return render (request , 'users/conf_rdv.html',{'rdvs' : rdvs})


    







def doc_patient (request) :
    return render (request,"users/doc_patient.html")

def login_medecin(request) :
    return render (request,'login_medecin')





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




def logout_patient(request):
    logout(request)
    return redirect('home')

def logout_psy(request):
    logout(request)
    return redirect('home')



   



