from django.shortcuts import render,redirect
from . models import Clock
from django.http import JsonResponse
# Create your views here.
def main(request):
    
    clocks = Clock.objects.all()
    return render(request,"main.html",{"clocks":clocks})

def get_count_ajax(request,pk):
    count =Clock.objects.get(id=pk)
    if count.time_left>0:
        count.time_left -=1
    count.save()
    return JsonResponse({'live_counter':count.time_left})

def card_detail(request,pk):
    get_clock = Clock.objects.get(id=pk)
    get_time = get_clock.time_left
    return render(request,"clockdetail.html",{"get_time":get_time,"key":pk})

def create(request):
    if request.method =="POST":
        clock = Clock()
        clock.title = request.POST.get("title")
        clock.time_left = request.POST.get("time")
        clock.save()
        return redirect("card-detail",clock.id)
    return render(request,"add_clock.html",{})
