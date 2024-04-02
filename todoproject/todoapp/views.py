from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView


class TaskListviews(ListView):
    model=Task
    template_name='index.html'
    context_object_name='task'
class Detailview(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name ='task'
class Updateview(UpdateView):
    model=Task
    template_name = "update.html"
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('details',kwargs={'pk':self.object.id})
class Deleteview(DeleteView):
    model=Task
    template_name = 'delete.html'
    context_object_name = 'task'

    def get_success_url(self):
        return reverse_lazy('add')
def add(request):
    task1 = Task.objects.all()
    if request.method=="POST":
        name=request.POST["task"]
        priority=request.POST["priority"]
        date=request.POST['date']
        task=Task(name=name,priority=priority,date=date)
        task.save()
    return render(request,"index.html",{'task':task1})
# def details(request):
#     task=Task.objects.all()
#     return render(request,"details.html",{'task':task})
def delete(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,"delete.html")
def update(request,taskid):
    task=Task.objects.get(id=taskid)
    form=Todoforms(request.POST or None,instance=task)
    if form.is_valid():
     form.save()
     return redirect('/')
    return render(request,'edit.html',{'task':task,'form':form})