# Generated by Django 5.1.2 on 2024-11-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_alter_customer_id_alter_feedback_id_alter_orders_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='rating',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]