# Generated by Django 4.1.3 on 2022-12-22 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]