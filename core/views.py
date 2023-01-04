from django.shortcuts import render, redirect
from .forms import JobForm
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs':jobs})

def create(request):
    if request.POST:
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = JobForm()
    return render(request, 'create.html', {'form':form})

def show(request, job_id):
    job = Job.objects.get(uuid=job_id)
    return render(request, 'show.html', {'job':job})

def manage(request):
    jobs = Job.objects.all()
    return render(request, 'manage.html', {'jobs':jobs})

def edit(request, job_id):
    job = Job.objects.get(uuid=job_id)
    if request.POST:
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = JobForm(instance=job)
    return render(request, 'edit.html', {'job':job, 'form':form})

def delete(request, job_id):
    job = Job.objects.get(uuid=job_id)
    if request.POST:
        job.delete()
        return redirect('Manage')
    return render(request, 'manage.html', {'job':job})