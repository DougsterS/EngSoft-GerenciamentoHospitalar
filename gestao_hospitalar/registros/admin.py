from django.contrib import admin
from .models import Enfermidade,Medicamento,Medico,Paciente,Equipamento

admin.site.register(Enfermidade)
admin.site.register(Medico)
admin.site.register(Medicamento)
admin.site.register(Paciente)
admin.site.register(Equipamento)