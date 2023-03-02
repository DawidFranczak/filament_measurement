from django.db import models

# Create your models here.

CHOICES_TYPE = [("PLA", "PLA"),
                ("PET", "PET"),
                ("ABS", "ABS")]

CHOICES_COLOR = [("RED", "CZERWONY"),
                 ("BLUE", "NIEBIESKI")]


class Printer(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    work_hours = models.FloatField(default=0.0)
    image = models.ImageField(
        upload_to='images/', default='images/printer.png')

    def __str__(self):
        return self.name


class Fliament(models.Model):

    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=CHOICES_TYPE)
    color = models.CharField(max_length=20, choices=CHOICES_COLOR)
    quantity = models.FloatField(default=1000.0)
    uid = models.IntegerField()

    def __str__(self):
        return str(self.printer)
