# Generated by Django 2.2.3 on 2019-07-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_code', models.CharField(max_length=200, unique=True)),
                ('not_before', models.DateTimeField(verbose_name='Not Valid Before')),
                ('not_after', models.DateTimeField(verbose_name='Not Valid After')),
                ('discount_value', models.PositiveIntegerField()),
                ('discount_type', models.CharField(choices=[('CR', 'Currency'), ('PE', 'Percentage')], default='CR', max_length=2)),
                ('usage_limit', models.PositiveIntegerField(default=3)),
            ],
        ),
    ]
