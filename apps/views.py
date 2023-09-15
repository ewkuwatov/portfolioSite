from django.shortcuts import render, redirect
from .models import *
from .forms import TestimonialForm, ContactForm
from .handlers import bot

# Create your views here.
def index(request, category_slug=None):
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    category = None
    price = Price.objects.filter()
    team = Team.objects.filter()
    testimonial = Testimonial.objects.filter()
    form = TestimonialForm()
    if category_slug:
        testimonial = testimonial.filter(category=category)
    return render(request, 'index.html',
                  {
                      'category': category,
                      'testimonial': testimonial,
                      'team': team,
                      'price': price,
                      'contact': contact,
                      'form': form,
                  })

def contact(request, category_slug=None):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            bot.send_message(926991283, 'Привет')
    category = None
    contact = Contact.objects.filter()
    form = ContactForm()
    if category_slug:
        contact = contact.filter(category=category)
    return render(request, 'contact.html',
                  {
                      'category': category,
                      'contact': contact,
                      'form': form,
                  })


