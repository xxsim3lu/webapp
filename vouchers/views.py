from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Voucher
# Create your views here.

def index(request):
  context = {}
  if request.POST:
    voucher_code = request.POST['voucher_code']
    try:
      voucher = Voucher.objects.get(voucher_code=voucher_code)
      if voucher.usage_limit > 0:
        voucher.usage_limit -= 1
        voucher.save()
      else:
        context.update({'error_message': 'The voucher has reached its usage limit.'})

      discount = ''
      if voucher.discount_type == 'PE':
        discount = f'{voucher.discount_value}%'
      else:
        discount = f'RM{voucher.discount_value}'
      context.update({'message': f'You got {discount} off your items. Voucher left: {voucher.usage_limit}'})
    except Voucher.DoesNotExist:
      context = {
        'error_message': 'Invalid voucher code.',
      }
      
  return render(request, 'vouchers/index.html', context)