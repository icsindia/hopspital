from django.db import models

class Department(models.Model):
    d_name=models.CharField(max_length=20)
    d_desc=models.TextField(max_length=200)
    def __str__(self):
        return self.d_name
class Doctore(models.Model):
    doc_name=models.CharField(max_length=20)
    doc_dep=models.ForeignKey(Department, on_delete=models.CASCADE)
    desc=models.CharField(max_length=50)
    doc_image=models.ImageField(upload_to="image")
    def __str__(self):
        return self.doc_name
class Booking(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=40)
    mobile=models.CharField(max_length=12)
    doctor=models.ForeignKey(Doctore,on_delete=models.CASCADE)
    booked=models.DateField()
    time=models.TimeField()
    decs=models.TextField(max_length=500)
    def __str__(self):
        return self.name

