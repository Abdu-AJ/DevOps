# Generated by Django 2.1.15 on 2024-03-30 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0003_auto_20240329_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocalSMSPricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('GPRSPricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OffNetPricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('IrishLandlinePricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('InternationalCallPricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('InternationalSMSPricing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OnNetPricing', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
