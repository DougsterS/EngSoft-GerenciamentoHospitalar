from django.shortcuts import render, redirect, get_object_or_404
from .models import Medico,Paciente,Medicamento,Equipamento,Enfermidade
from .forms import MedicoForm,PacienteForm, EnfermidadeForm, EquipamentoForm, MedicamentoForm

def listMedicos(request):
    medicos = Medico.objects.all()
    return render(request,'registroMedicos.html', {'variavel': medicos})

def createMedico(request):
    form = MedicoForm(request.POST or None, None)
    if form.is_valid():
        form.save()
        return redirect('ListaMedicos')
    return render(request,'formulario.html',{'form': form})

def updateMedico(request,id):
    medico = get_object_or_404(Medico, pk=id)
    form = MedicoForm(request.POST or None, instance=medico)
    if form.is_valid():
        form.save()
        return redirect('ListaMedicos')
    return render(request, 'formulario.html', {'form': form})

def deleteMedico(request,id):
    medico = get_object_or_404(Medico, pk=id)
    form = MedicoForm(request.POST or None, instance=medico)
    if request.method == 'POST':
        medico.delete()
        return redirect('ListaMedicos')
    return render(request,'deleteconfirmation.html',{'variavel': medico})

def listPaciente(request):
    pacientes = Paciente.objects.all()
    return render(request,'registroPacientes.html', {'variavel': pacientes})

def createPaciente(request):
    form = PacienteForm(request.POST or None, None)
    if form.is_valid():
        form.save()
        return redirect('ListaPacientes')
    return render(request, 'formulario.html', {'form': form})

def updatePaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('ListaPacientes')
    return render(request, 'formulario.html', {'form': form})

def deletePaciente(request,id):
    paciente = get_object_or_404(Paciente, pk=id)
    form = PacienteForm(request.POST or None, instance=paciente)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ListaPacientes')
    return render(request,'deleteconfirmation.html',{'variavel': paciente})

def listMedicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request,'registroMedicamentos.html', {'variavel': medicamentos})

def createMedicamentos(request):
    form = MedicamentoForm(request.POST or None, None)
    if form.is_valid():
        form.save()
        return redirect('ListaMedicamentos')
    return render(request, 'formulario.html', {'form': form})

def updateMedicamentos(request,id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if form.is_valid():
        form.save()
        return redirect('ListaMedicamentos')
    return render(request, 'formulario.html', {'form': form})

def deleteMedicamentos(request,id):
    medicamento = get_object_or_404(Medicamento, pk=id)
    form = MedicamentoForm(request.POST or None, instance=medicamento)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('ListaMedicamentos')
    return render(request,'deleteconfirmation.html',{'variavel': medicamento})

def listEnfermidade(request):
    enfermidades = Enfermidade.objects.all()
    return render(request,'registroEnfermidades.html', {'variavel': enfermidades})

def createEnfermidade(request):
    form = EnfermidadeForm(request.POST or None, None)
    if form.is_valid():
        form.save()
        return redirect('ListaEnfermidades')
    return render(request, 'formulario.html', {'form': form})

def updateEnfermidade(request,id):
    enfermidade = get_object_or_404(Enfermidade, pk=id)
    form = EnfermidadeForm(request.POST or None, instance=enfermidade)
    if form.is_valid():
        form.save()
        return redirect('ListaEnfermidades')
    return render(request, 'formulario.html', {'form': form})

def deleteEnfermidade(request,id):
    enfermidade = get_object_or_404(Enfermidade, pk=id)
    form = EnfermidadeForm(request.POST or None, instance=enfermidade)
    if request.method == 'POST':
        enfermidade.delete()
        return redirect('ListaEnfermidades')
    return render(request,'deleteconfirmation.html',{'variavel': enfermidade})

def listEquipamento(request):
    equipamentos = Equipamento.objects.all()
    return render(request,'registroEquipamento.html',{'variavel': equipamentos})

def createEquipamento(request):
    form = EquipamentoForm(request.POST or None, None)
    if form.is_valid():
        form.save()
        return redirect('ListaEquipamentos')
    return render(request,'formulario.html',{'form': form})

def updateEquipamento(request,id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    form = EquipamentoForm(request.POST or None, instance=equipamento)
    if form.is_valid():
        form.save()
        return redirect('ListaEquipamentos')
    return render(request, 'formulario.html', {'form': form})

def deleteEquipamento(request,id):
    equipamento = get_object_or_404(Equipamento, pk=id)
    form = EquipamentoForm(request.POST or None, instance=equipamento)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('ListaEquipamentos')
    return render(request,'deleteconfirmation.html',{'variavel': equipamento})