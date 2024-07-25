from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    desc = models.CharField(max_length=100,null=True)
    imges = models.ImageField(upload_to='imges/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Food'

    def __str__(self):
        return self.name
    
class AddFile(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='upload/')
    
    class Meta:
        db_table ='addfile'