from django.db import models
from django_resized import ResizedImageField

class Main(models.Model):
    logo = models.FileField(upload_to='main/')
    icon = models.FileField(upload_to='icons/')
    phonenumber = models.CharField(max_length=20, verbose_name="Telefon raqam")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Asosiy sahifa"
        verbose_name_plural = "Asosiy sahifa "


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    img = ResizedImageField(size=[1920, 600], crop=['middle', 'center'], upload_to='slider/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Aylanuvchi rasmlar"
        verbose_name_plural = "Aylanuvchi rasmlar "


class About(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    image = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='about/')
    firstservice = models.CharField(max_length=255, verbose_name="1-xizmat nomi")
    serviceabout1 = models.TextField(verbose_name="1-xizmat haqida")
    secondservice = models.CharField(max_length=255, verbose_name="2-xizmat nomi")
    serviceabout2 = models.TextField(verbose_name="2-xizmat haqida")
    thirdservice = models.CharField(max_length=255, verbose_name="3-xizmat nomi")
    serviceabout3 = models.TextField(verbose_name="3-xizmat haqida")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Kompaniya haqida"
        verbose_name_plural="Kompaniya haqida "


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Savol")
    answer = models.TextField(verbose_name="Javob")
    is_top = models.BooleanField(default=False, verbose_name="Eng yuqorida chiqarilsinmi?")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name ="Savollar va Javoblar"
        verbose_name_plural ="Savollar va Javoblar "



class Colors(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name ="Ranglar"
        verbose_name_plural ="Ranglar"



class Product(models.Model):
    image = ResizedImageField(size=[1000,1286],upload_to='products/')
    title = models.CharField(max_length=255, verbose_name="Mahsulot nomi")
    category = models.CharField(max_length=100, verbose_name="Kategoriya")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narx")
    status = models.CharField(max_length=50, verbose_name="Holati")
    colors = models.ManyToManyField(Colors, verbose_name="Mavjud ranglar", null=True, blank=True)
    star = models.PositiveSmallIntegerField(default=0, verbose_name="Yulduzlar soni")
    size = models.CharField(max_length=50, blank=True, null=True, verbose_name="O‘lchami")
    description = models.TextField(verbose_name="Tavsif")
    image_2 = ResizedImageField(size=[1000,1286], upload_to='products/', blank=True, null=True)
    image_3 = ResizedImageField(size=[1000,1286], upload_to='products/', blank=True, null=True)
    image_4 = ResizedImageField(size=[1000,1286],upload_to='products/', blank=True, null=True)
    image_5 = ResizedImageField(size=[1000,1286],upload_to='products/', blank=True, null=True)
    image_6 = ResizedImageField(size=[1000,1286],upload_to='products/', blank=True, null=True)
    extra_image = ResizedImageField(size=[800,652],upload_to='products/', blank=True, null=True)
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Mahsulotlar"
        verbose_name_plural="Mahsulotlar "

class Customer(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="F.I.O")
    type = models.CharField(max_length=100, verbose_name="Turi")
    comment = models.TextField(verbose_name="Izoh")
    star = models.PositiveSmallIntegerField(default=0, verbose_name="Yulduzlar soni")
    image = ResizedImageField(size=[300, 300], crop=['middle', 'center'], upload_to='customers/')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Mijozlar fikrlari"
        verbose_name_plural = "Mijozlar fikrlari "


class Footer(models.Model):
    instagram = models.URLField(blank=True, null=True, verbose_name="Instagram")
    telegram = models.URLField(blank=True, null=True, verbose_name="Telegram")
    youtube = models.URLField(blank=True, null=True, verbose_name="YouTube")
    phonenumber = models.CharField(max_length=20, verbose_name="Telefon raqam")
    logo = ResizedImageField(size=[200, 200], crop=['middle', 'center'], upload_to='footer/')

    def __str__(self):
        return "Footer"

    class Meta:
        verbose_name = "Ijtimoiy tarmoqlar va hokazo"
        verbose_name_plural = "Ijtimoiy tarmoqlar va hokazo "


class ContactPage(models.Model):
    location = models.CharField(max_length=255, verbose_name="Manzil")
    email = models.EmailField(verbose_name="Email")
    phonenumber = models.CharField(max_length=20, verbose_name="Telefon raqam")

    def __str__(self):
        return self.location

    class Meta:
        verbose_name = "Manzil, telefonraqam, address"
        verbose_name_plural = "Manzil, telefonraqam, address " 


class Contact(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="F.I.O")
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=255, verbose_name="Mavzu")
    phonenumber = models.CharField(max_length=20, verbose_name="Telefon raqam")
    message = models.TextField(verbose_name="Xabar")

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name_plural = "Contact "



class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.FileField(upload_to='banner/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"


class ShopBanner(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.FileField(upload_to='banner/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sotuv banneri"
        verbose_name_plural = "Sotuv banneri"


class Service(models.Model):
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    icon = models.FileField(upload_to='service/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Servislar"
        verbose_name_plural = "Servislar"

class Video(models.Model):
    background_image = models.FileField(upload_to="background_image/")
    video_url = models.CharField(max_length=100000)


    def __str__(self):
        return "Asosiy sahifa uchun orqa fon videosi" 

    class Meta:
        verbose_name = "Orqa fon videosi"
        verbose_name_plural = "Orqa fon videosi"
