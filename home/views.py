from django.shortcuts import render, redirect
from .models import *
import datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def homepage(request):
    return render(request, "home.html", locals())

@login_required(login_url='login')
def place(request):
    if request.method == "POST":
        request.session['place'] = request.POST['place']
        return redirect("machine")
    places = Place.objects.all().order_by('id')
    return render(request, "place.html", locals())

@login_required(login_url='login')
def machine(request):
    if request.method == "POST":
        request.session['machine_id'] = request.POST['machine']
        return redirect("record")
    place = request.session['place']
    machines = Machine.objects.all().filter(place__name__contains=place).values()
    return render(request, "machine.html", locals())

@login_required(login_url='login')
def record(request):
    if request.method == "POST":
        machine = Machine.objects.only("id").get(machine_id=request.POST['machine_id'])
        Machine.objects.filter(machine_id=request.POST['machine_id']).update(record_today=1)
        status = Status.objects.only("id").get(name=request.POST['status_update'])
        unit = Record.objects.create(machine=machine, status=status, note=request.POST['note'], user=request.user.username)
        unit.save()
        return redirect("machine")
    machine_id = request.session['machine_id']
    machine_area = Machine.objects.filter(machine_id__exact=machine_id).values_list("area__name").first()[0]
    status_list = Status.objects.values_list("name")
    status_list = [s[0] for s in status_list]
    records = Record.objects.all().filter(machine__machine_id__contains=machine_id).filter(
        update_time__year=datetime.datetime.today().year).filter(
        update_time__month=datetime.datetime.today().month).filter(
        update_time__day=datetime.datetime.today().day).values_list("status__name").last()
    if records is None:
        records = "未紀錄"
    else:
        records = records[0]
    return render(request, "record.html", locals())

@login_required(login_url='login')
def status(request):
    machines = Machine.objects.all().order_by('id')
    status_dict = []
    for machine in machines:
        records = Record.objects.all().filter(machine__machine_id__contains=machine.machine_id).filter(
            update_time__year=datetime.datetime.today().year).filter(
            update_time__month=datetime.datetime.today().month).filter(
            update_time__day=datetime.datetime.today().day).values_list("status__name").last()
        if records is None:
            records = "未紀錄"
        else:
            records = records[0]
        status_dict.append((machine.machine_id, records))
    return render(request, "status.html", locals())

@login_required(login_url='login')
def examine(request):
    return render(request, "examine.html", locals())

@login_required(login_url='login')
def examine_date(request):
    if request.method == "POST":
        request.session['date'] = request.POST['date']
        return redirect("examine_date_place")
    return render(request, "examine_date.html", locals())

@login_required(login_url='login')
def examine_date_place(request):
    if request.method == "POST":
        request.session['place'] = request.POST['place']
        return redirect("show_date")
    places = Place.objects.all().order_by('id')
    return render(request, "place.html", locals())

@login_required(login_url='login')
def show_date(request):
    date = datetime.datetime.strptime(request.session['date'], "%Y-%m-%d")
    machines = Machine.objects.all().filter(place__name__contains=request.session['place'])
    status_dict = []
    for machine in machines:
        records = Record.objects.all().filter(machine__machine_id__contains=machine.machine_id).filter(
            update_time__year=date.year).filter(
            update_time__month=date.month).filter(
            update_time__day=date.day).values_list("status__name").last()
        if records is None:
            records = "未紀錄"
        else:
            records = records[0]
        status_dict.append((machine.machine_id, records))
    return render(request, "show_date.html", locals())

def view_404(request, exception=None):
    return redirect('/')