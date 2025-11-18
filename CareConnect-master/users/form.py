from django.forms import ModelForm
from users.models import patient_insc, psy_insc , RDV , emp_auth
from django import forms




class InscPatient(ModelForm) :
    class Meta :
        model = patient_insc
        fields = ["Name" ,"my_email" ,"my_password" , "passw","Sexe" , "NumTel"]
        labels = {
            'Name': 'Nom & Prénom',
            'email': 'Adresse e-mail',
            'password': 'Mot de passe',
            'passw' : 'Confimtaion de mot de passe',
        }                                                                                              #Labels t5alina njmou nbdlou esm l labels taa l model w for

class AuthForm(ModelForm) :
    class Meta: 
        model = emp_auth
        fields = ["email","password"]
        labels = {
            'password' : 'Mot de passe',
            'email' : 'Adresse email',

        }


class RDV_form(forms.ModelForm):
    class Meta:
        model = RDV
        fields = ['date', 'email'] 
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }
        labels = {
            'date': '',  
        
        }




class InscPsy(ModelForm) :
    class Meta :
        model = psy_insc
        fields = ["Name" ,"email" ,"password" , "passw" , "fichiers"]
        labels = {
            'Name': 'Nom & Prénom',
            'email': 'Adresse e-mail',
            'password': 'Mot de passe',
            'passw' : 'Confimtaion de mot de passe',

        }      
                                                
        


