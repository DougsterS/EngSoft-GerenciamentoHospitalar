from django.forms import ModelForm
from .models import Equipamento,Medicamento,Medico,Enfermidade,Paciente

class MedicoForm(ModelForm):
    class Meta:
        model = Medico
        fields = ['nome','sobrenome','data_de_nascimento','idade','especialidade','bio']

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nome','substancia','validade','contraindicacao']

class EnfermidadeForm(ModelForm):
    class Meta:
        model = Enfermidade
        fields = ['nome','sintomas','medicamentos']

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome','sobrenome','data_de_nascimento','idade','sintomas']

class EquipamentoForm(ModelForm):
    class Meta:
        model = Equipamento
        fields = ['nome','quantidade','funcao']