from django.contrib import admin
from .models import patient_insc,psy_insc,RDV, ConfPsy

# Register your models here.


admin.site.register(patient_insc)
# admin.site.register(emp_auth)
admin.site.register(psy_insc)
admin.site.register(RDV)
admin.site.register(ConfPsy)