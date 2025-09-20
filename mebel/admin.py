from django.contrib import admin
from .models import *

admin.site.site_header = "Baror mebel vebsayti"
admin.site.site_title = "Admin panel"
admin.site.index_title = "Boshqaruv bo‘limlari"

admin.site.register(Main)
admin.site.register(Colors)
admin.site.register(Slider)
admin.site.register(Service)
admin.site.register(Banner)
admin.site.register(ShopBanner)
admin.site.register(About)
admin.site.register(Video)
admin.site.register(FAQ)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Footer)
admin.site.register(ContactPage)
admin.site.register(Contact)
