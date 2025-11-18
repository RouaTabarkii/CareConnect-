from django.db import models



class patient_insc(models.Model) :
    Name = models.CharField(max_length = 50 , default = "" )
    my_email =  models.EmailField(max_length = 100  , default = "" )
    my_password = models.CharField(max_length = 30)
    passw = models.CharField(max_length= 30)
    Sexe =  models.CharField(max_length = 1 , default = "" )
    NumTel =  models.IntegerField(blank = False)



class emp_auth(models.Model):
    email = models.EmailField(max_length=100, default="")
    password = models.CharField(max_length=30)


class psy_insc(models.Model) :
    Name = models.CharField(max_length = 50 , default = "" )
    email =  models.EmailField(max_length = 100  , default = "" )
    password = models.CharField(max_length = 30)
    passw = models.CharField(max_length= 30)
    fichiers = models.FileField(upload_to='fichiers')

class RDV(models.Model):
    date = models.DateField()
    email =  models.EmailField(max_length = 100  , default = "" )
    DocName = models.CharField()

class ConfPsy (models.Model) :
    Name = models.CharField()
    photo = models.ImageField()
    desc = models.CharField()                                        
