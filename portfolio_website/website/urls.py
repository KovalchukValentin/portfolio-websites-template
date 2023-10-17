from django.urls import path

from . import views

urlpatterns = [
    path('', views.Homepage_view.as_view(), name='home'),
    path('gallery', views.gallery_view, name='gallery'),
    path('about', views.about_view, name='about'),
    path('contact', views.contact_view, name='contact'),
    path('pricing', views.pricing_view, name='pricing'),
    path('sterilization', views.sterilization_view, name='sterilization'),
    path('save-form', views.Result_save_contact_form_JSON_View.as_view(), name='save-form'),
    path('thank-for-order', views.thanks_for_order_view, name='thank-for-order'),
]

