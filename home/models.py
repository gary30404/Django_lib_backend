from django.db import models

class Place(models.Model):
    name = models.CharField("區域", max_length=50)

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField("位置", max_length=50)

    def __str__(self):
        return self.name

class Maintain_Group(models.Model):
    name = models.CharField("類別", max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField("狀態", max_length=50)

    def __str__(self):
        return self.name

class Machine(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='menu_items')
    area = models.ForeignKey(Area, on_delete=models.CASCADE, related_name='menu_items')
    group = models.ForeignKey(Maintain_Group, on_delete=models.CASCADE, related_name='menu_items')
    floor = models.PositiveIntegerField('樓層', default=1)
    machine_id = models.CharField("機器編號", max_length=10, unique=True)

    def __str__(self):
        #return {"place":self.place, "area":self.area, "group":self.group, "floor":self.floor, "machine_id":self.machine_id}
        return "區域:{} 位置:{} 類別:{} 樓層:{} 機器編號:{}".format(self.place, self.area, self.group, self.floor, self.machine_id)

class Record(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='menu_items')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='menu_items')
    note = models.CharField("備註", max_length=50)
    update_time = models.DateTimeField("記錄時間", auto_now=True)
    user = models.CharField("user", max_length=50)

    def __str__(self):
        return "機器編號:{} 機器區域:{} 狀態:{} 備註:{} 記錄時間:{} 紀錄人員:{}".format(self.machine.machine_id, self.machine.area, self.status, self.note, self.update_time, self.user)