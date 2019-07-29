from django.contrib import admin
from django import forms
from .models import Voucher
# Register your models here.

class VoucherForm(forms.ModelForm):
  class Meta:
    model = Voucher
    fields = '__all__'
  
  def clean(self):
    not_before = self.cleaned_data.get('not_before')
    not_after = self.cleaned_data.get('not_after')
    if not_before > not_after:
      raise forms.ValidationError('\
        Not Valid Before should be earlier than Not Valid After')
    return self.cleaned_data
  
class VoucherAdmin(admin.ModelAdmin):
  form = VoucherForm
  list_display = ('voucher_code', 'discount_value', 'discount_type', 'usage_limit')

admin.site.register(Voucher, VoucherAdmin)