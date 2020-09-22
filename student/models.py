from django.db import models
from django.contrib.auth.models import Group

class student(models.Model):
    author = models.ForeignKey("auth.user",on_delete=models.CASCADE,verbose_name="Kullanıcı Adı")
    avatar = models.ImageField(upload_to = 'media/profile_image', blank=True,verbose_name="Fotoğraf")
    name = models.CharField(default='',max_length = 50,verbose_name = "Adı")
    surname = models.CharField(default='',max_length = 50,verbose_name = "Soyadı")
    birthday = models.DateField(blank=True, null=True,verbose_name = "Doğum Tarihi")
    email = models.EmailField(default='',verbose_name = "E-Posta")
    phone = models.CharField(default=0,max_length=11,verbose_name = "Telefon Numarası")
    parent_phone = models.CharField(default=0,max_length=11,verbose_name = "Veli Telefon Numarası")
    gender_choice = (
        ('Erkek', 'Erkek'),
        ('Kadın', 'Kadın'),)
    gender = models.CharField(max_length = 30,blank=True, null=True,choices = gender_choice,verbose_name = "Cinsiyet")
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Kayıt Tarihi")

    def __str__(self):
        return self.name