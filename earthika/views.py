from django.http import HttpResponse, JsonResponse
from django.template import loader
from earthika.models import *


def Home(request):
    print('home')
    template = loader.get_template('index.html')
    context = {}
    response = HttpResponse(template.render(context, request))
    return response
def All_Product(request):
    print('product')
    context = {}
    product_ids = {}
    template = loader.get_template('product.html')
    context['products'] = Product.objects.all()

    for a in context['products']:
        product_ids[a.id] = Product_Type.objects.values('id').filter(product = a).first()
    print('pro_ids:',product_ids)
    context['product_ids'] = product_ids
    context['product_types'] = Product_Type.objects.all()
    context['pt_len'] = len(context['product_types'])
    context['packages'] = Product_Type_Package.objects.all()

    print('product:------',vars(context['product_types'][0]))



    response = HttpResponse(template.render(context, request))
    return response

def Enquiry_msg(request):
    try:
        if request.method == 'POST':
            data = request.POST
            print('data:---------',data)
            name = data['name']
            email = data['email']
            mobile = data['mobile']
            message = data['message']
            product_id = data['product_id']
            try:product = Product_Type.objects.get(id=product_id)
            except:product=Product_Type.objects.get(id=3)
            enquiry_instance = Enquiry.objects.create(first_name = name)
            enquiry_instance.email =email
            enquiry_instance.mobile =mobile
            enquiry_instance.message =message
            enquiry_instance.product =product
            enquiry_instance.save()
            response = JsonResponse({"status": 200, "data": "success"}, status=200)
    except:
        response = JsonResponse({"status": 400, "data": "Failed"}, status=400)
    return response

