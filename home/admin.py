from django.contrib import admin
from .models import *

class MachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'area', 'group', 'floor', 'machine_id')

class RecordAdmin(admin.ModelAdmin):
    list_display =  [f.name for f in Record._meta.get_fields()]

admin.site.register(Place)
admin.site.register(Area)
admin.site.register(Maintain_Group)
admin.site.register(Machine, MachineAdmin)
#admin.site.register(Machine)
admin.site.register(Status)
admin.site.register(Record, RecordAdmin)
