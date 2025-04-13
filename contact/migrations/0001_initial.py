# Generated by Django 5.1.7 on 2025-03-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='الاسم')),
                ('email', models.EmailField(max_length=254, verbose_name='البريد الإلكتروني')),
                ('adres', models.CharField(blank=True, max_length=200, verbose_name='عنوان الرسالة')),
                ('message', models.TextField(blank=True, verbose_name='الرسالة')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإرسال')),
            ],
            options={
                'verbose_name': 'رسالة تواصل',
                'verbose_name_plural': 'رسائل التواصل',
                'ordering': ['-created_at'],
            },
        ),
    ]
