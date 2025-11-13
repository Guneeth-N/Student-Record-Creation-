from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    Reg_no=models.PositiveIntegerField(unique=True)
    email=models.EmailField(blank=True)
    dob=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    course=models.CharField(max_length=25)

    def __str__(self):
        return f"{self.Reg_no}---->{self.first_name} {self.last_name}"