# Generated by Django 4.1.4 on 2023-03-01 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0010_products_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image5',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image6',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image7',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image8',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image9',
            field=models.ImageField(null=True, upload_to='uploads/'),
        ),
    ]
