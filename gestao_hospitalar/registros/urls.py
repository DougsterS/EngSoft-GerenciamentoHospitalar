from django.urls import path
from .views import listMedicos, listPaciente, listEnfermidade, listEquipamento, listMedicamentos
from .views import createMedico, createPaciente, createEnfermidade, createEquipamento, createMedicamentos
from .views import updateMedico, updatePaciente, updateEnfermidade, updateEquipamento, updateMedicamentos
from .views import deleteMedico, deletePaciente, deleteEnfermidade, deleteEquipamento, deleteMedicamentos

urlpatterns = [
    path('medicos', listMedicos, name='ListaMedicos'),
    path('medicos/create', createMedico, name='CriarMedicos'),
    path('medicos/update/<int:id>', updateMedico, name='AtualizarMedicos'),
    path('medicos/delete/<int:id>', deleteMedico, name='DeletarMedico'),

    path('pacientes', listPaciente, name='ListaPacientes'),
    path('pacientes/create', createPaciente, name='CriarPacientes'),
    path('pacientes/update/<int:id>', updatePaciente, name='AtualizarPacientes'),
    path('pacientes/delete/<int:id>', deletePaciente, name='DeletarPacientes'),

    path('equipamentos', listEquipamento, name='ListaEquipamentos'),
    path('equipamentos/create', createEquipamento, name='CriarEquipamentos'),
    path('equipamentos/update/<int:id>', updateEquipamento, name='AtualizarEquipamentos'),
    path('equipamentos/delete/<int:id>', deleteEquipamento, name='DeletarEquipamentos'),

    path('medicamentos',listMedicamentos, name='ListaMedicamentos'),
    path('medicamentos/create', createMedicamentos, name='CriarMedicamentos'),
    path('medicamentos/update/<int:id>', updateMedicamentos, name='AtualizarMedicamentos'),
    path('medicamentos/delete/<int:id>', deleteMedicamentos, name='DeletarMedicamentos'),

    path('enfermidades',listEnfermidade, name='ListaEnfermidades'),
    path('enfermidades/create', createEnfermidade, name='CriarEnfermidades'),
    path('enfermidades/update/<int:id>', updateEnfermidade, name='AtualizarEnfermidades'),
    path('enfermidades/delete/<int:id>', deleteEnfermidade, name='DeletarEnfermidades'),

]
