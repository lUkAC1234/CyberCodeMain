from django import template
from django.db.models import Sum
from web.models import PricingModel


register = template.Library()


# Is Cart ?
@register.simple_tag
def is_cart(request, id):
    cart = request.session.get('cart', [])
    return id in cart

@register.simple_tag
def cart_info(request):
    cart = request.session.get('cart', [])
    qs = PricingModel.get_cart_objects(cart)
    if not qs: price = 0.0
    else: price = qs.aggregate(Sum('price'))
    return len(cart), price

@register.filter
def calculate_total_cost(cart, request):
    total_cost = 0
    pricing_items = PricingModel.objects.filter(id__in=cart)
    
    for item in pricing_items:
        total_cost += item.price
    
    return total_cost