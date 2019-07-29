from django.db import models

# Create your models here.
class Voucher(models.Model):
  voucher_code = models.CharField(max_length=200, unique=True)
  not_before = models.DateTimeField('Not Valid Before')
  not_after = models.DateTimeField('Not Valid After')
  discount_value = models.PositiveIntegerField()
  CURRENCY = 'CR'
  PERCENTAGE = 'PE'
  DISCOUNT_TYPE_CHOICES = [
    (CURRENCY, 'RM'),
    (PERCENTAGE, '%'),
  ]
  discount_type = models.CharField(
    max_length = 2,
    choices=DISCOUNT_TYPE_CHOICES,
    default=CURRENCY,
  )
  usage_limit = models.PositiveIntegerField(default=3)

  def __str__(self):
    return self.voucher_code