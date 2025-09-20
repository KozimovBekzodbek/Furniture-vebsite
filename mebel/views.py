from django.shortcuts import render, get_object_or_404
from mebel.models import Main, Slider, Banner, Service, Product, ShopBanner, FAQ, Video, Customer, Footer, Contact, ContactPage 



def home(request):
    main = Main.objects.all()
    sliders = Slider.objects.all()
    banner = Banner.objects.all()
    shopbanner = ShopBanner.objects.all()
    service = Service.objects.all()
    products = Product.objects.all().filter(is_active=True)
    faq = FAQ.objects.all()
    video = Video.objects.all()
    customer = Customer.objects.all()
    footer = Footer.objects.all()


    context = {
            "main" : main,
            "sliders" : sliders,
            "banner" : banner,
            "shopbanner" : shopbanner,
            "service" : service,
            "products" : products,
            "faq" : faq,
            "video" : video,
            "customer" : customer,
            "footer" : footer,

            }

    return render(request,'index.html', context)




def products(request):
    main = Main.objects.all()
    products = Product.objects.all()
    footer = Footer.objects.all()

    context = {
            "main" : main,
            "products" : products,
            "footer" : footer,

            }

    return render(request,'products.html', context)



def productdetail(request, pk):
    main = Main.objects.all()
    product = get_object_or_404(Product, pk=pk)
    footer = Footer.objects.all()
    product.discounted_price = product.price + (product.price * 30 // 100)
    products = Product.objects.all().filter(is_active=True)

    context = {
            "main" : main,
            "product" : product,
            "products" : products,
            "footer" : footer,

            }
    return render(request, "product.html", context)




def about(request):
    main = Main.objects.all()
    footer = Footer.objects.all()

    context = {
            "main" : main,
            "footer" : footer,

            }
    return render(request, "about-us.html", context)



def contact(request):
    main = Main.objects.all()
    contact = ContactPage.objects.all()
    footer = Footer.objects.all()

    context = {
            "main" : main,
            "contact" : contact,
            "footer" : footer,

            }
    return render(request, "contact.html", context)




