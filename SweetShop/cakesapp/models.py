from django.db import models

# Create your models here.
class Category(models.Model):
    type = models.CharField(max_length=150)
    def __str__(self):
        return self.type

class Cakes(models.Model):
    title=models.CharField(max_length=150)
    color=models.CharField(max_length=150)
    qanak=models.IntegerField(blank=True)
    price=models.IntegerField(blank=True)
    photo=models.ImageField(upload_to='photos')
    tort_info = models.TextField(max_length=1000)
    category=models.ForeignKey("Category",on_delete=models.PROTECT)
    def __str__(self):
        return self.title+str(self.qanak)+self.color+str(self.price)+self.tort_info





