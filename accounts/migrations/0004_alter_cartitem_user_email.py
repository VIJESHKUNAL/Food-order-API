# Generated by Django 5.1 on 2024-09-29 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_cartitem_user_email_alter_cartitem_cart_or_ordered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='user_email',
            field=models.EmailField(max_length=254),
        ),
    ]
