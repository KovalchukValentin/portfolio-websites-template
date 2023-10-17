from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import Gallery_image, Certificate_image, Offer
from .services import *


def homepage_view(request):
    data = {'gallery_images': get_gallary_images_names(),
            'certificate_images': get_certificate_gallary_images_names(),
            'prices': get_offers_list()}

    return render(request, "_index.html", data)


def gallery_view(request):
    return render(request, "_gallery.html", {'gallery_images': get_gallary_images_names()})


def about_view(request):
    return render(request, "_about.html", {'certificate_images': get_certificate_gallary_images_names()})


def sterilization_view(request):
    return render(request, "_sterilization.html", {})


def contact_view(request):
    return render(request, "_contact.html", {})


def pricing_view(request):
    return render(request, "_pricing.html", {'prices': get_offers_list()})


def thanks_for_order_view(request):
    if request.method == 'GET':
        return render(request, "_thanks_for_order.html", {'order': request.GET.get('order-id')})
# Create your views here.


class Result_save_contact_form_JSON_View(View):
    def post(self, request):
        if request.method != 'POST':
            return JsonResponse({'success': False})

        name = request.POST['name']
        if not name:
            return JsonResponse({'success': False, 'error': 'name'})
        if not is_good_name(name):
            return JsonResponse({'success': False, 'error': 'name-wrong'})

        if not request.POST['telephone']:
            return JsonResponse({'success': False, 'error': 'telephone'})
        telephone = clear_telephone(request.POST['telephone'])
        if not is_good_telephone(telephone):
            return JsonResponse({'success': False, 'error': 'telephone-wrong'})

        email = request.POST['email']
        if not email:
            email = None
        else:
            email = clear_email(email)
            if not is_good_email(email):
                return JsonResponse({'success': False, 'error': 'email-wrong'})

        is_message_or_time_cell = False

        message = request.POST['message']
        if not message:
            message = None
        else:
            if is_good_message(message):
                is_message_or_time_cell = True
            else:
                return JsonResponse({'success': False, 'error': 'message-wrong'})

        if not request.POST['have_time_cell']:
            return JsonResponse({'success': False, 'error': 'message_or_time_cell'})

        time_cell = parse_time_cell(request.POST['time_cell'], have_time=request.POST['have_time_cell'])
        if not time_cell:
            time_cell = None
        else:
            is_message_or_time_cell = True

        if not is_message_or_time_cell:
            return JsonResponse({'success': False, 'error': 'message_or_time_cell'})

        Order.objects.create(name=name,
                             telephone=telephone,
                             email=email,
                             message=message,
                             time_cell=time_cell).save()

        return JsonResponse({'success': True})


class Homepage_view(View):
    template = "_index.html"
    data = {'gallery_images': get_gallary_images_names(),
            'certificate_images': get_certificate_gallary_images_names(),
            'prices': get_offers_list()}

    def get(self, request):
        return render(request, "_index.html", self.data)


