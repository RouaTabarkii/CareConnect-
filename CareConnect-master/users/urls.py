from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('login/patient/', views.login_patient, name='login_patient'),
    path('login/medecin/', views.login_medecin, name='login_medecin'),
    path('login/psy/', views.login_psy , name='login_psy'),
    path('register/patient/', views.register_patient, name='register_patient'),
    path('inscs/patient/', views.Interface_patient, name='Interface_patient'),
    path('register/psy',views.register_psy,name='register_psy'),
    path('RDV/patient/' ,views.My_RDV, name='RDV_patient'),
    path('DOC/patient',views.doc_patient,name='doc_patient'),
    path('Compte/patient/',views.compte_patient,name='Compte_patient'),
    path('interface/psy/', views.Interface_psy, name='Interface_psy'),
    path('logout/patient/', views.logout_patient,name='logout_patient'),
    path('conf/', views.ConfRDV, name='confrvd'),
    path('logout/psy/', views.logout_psy, name='logout_psy'),

    path('conf/<int:rdv_id>/', views.ConfRendezVous, name='conffRDV'),
    path('ref/<int:rdv_id>/' , views.RefRDV , name='refRdv'),

]

