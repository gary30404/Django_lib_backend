from django.contrib import admin
from .models import *
import csv
from django.forms import model_to_dict

def download_csv(modeladmin, request, queryset):
    f = open(modeladmin.model.__name__+'.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(modeladmin.list_display)
    for s in queryset:
        w = []
        for i in range(len(modeladmin.list_display)):
            w.append(getattr(s, modeladmin.list_display[i]))
        writer.writerow(w)

class MachineAdmin(admin.ModelAdmin):
    model = Machine
    list_display = ('id', 'place', 'area', 'group', 'floor', 'machine_id', 'record_today')
    readonly_fields = ['record_today']
    actions = [download_csv]

class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_display =  [f.name for f in Record._meta.get_fields()]
    actions = [download_csv]

admin.site.register(Place)
admin.site.register(Area)
admin.site.register(Maintain_Group)
admin.site.register(Machine, MachineAdmin)
#admin.site.register(Machine)
admin.site.register(Status)
admin.site.register(Record, RecordAdmin)
