from django.db import models


class ProgramLang(models.Model):
    tittle = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.tittle

