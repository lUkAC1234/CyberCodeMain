from django import template
from django.db.models import Sum
from web.models import PricingModel
from django.utils.timesince import timesince
from django.utils import timezone


register = template.Library()


# Is Cart ?
@register.simple_tag
def is_cart(request, id):
    cart = request.session.get('cart', [])
    return id in cart

@register.filter
def calculate_total_cost(cart, request):
    total_cost = 0
    pricing_items = PricingModel.objects.filter(id__in=cart)
    
    for item in pricing_items:
        total_cost += item.price
    
    return total_cost

@register.filter(name='custom_timesince')
def custom_timesince(value):
    now = timezone.now()
    difference = now - value

    if difference.days >= 365:
        years = difference.days // 365
        return f'{years} {"year" if years == 1 else "years"} ago'
    elif difference.days >= 30:
        months = difference.days // 30
        return f'{months} {"month" if months == 1 else "months"} ago'
    elif difference.days >= 1:
        return f'{difference.days} {"day" if difference.days == 1 else "days"} ago'
    elif difference.seconds >= 3600:
        hours = difference.seconds // 3600
        return f'{hours} {"hour" if hours == 1 else "hours"} ago'
    elif difference.seconds >= 60:
        minutes = difference.seconds // 60
        return f'{minutes} {"minute" if minutes == 1 else "minutes"} ago'
    else:
        return 'Just now'