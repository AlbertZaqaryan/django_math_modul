from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('Category name', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Categories'

class Modul(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_modul')
    name = models.CharField('Modul name', max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name='Modul'
        verbose_name_plural = 'Moduls'