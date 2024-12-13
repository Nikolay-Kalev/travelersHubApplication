# Generated by Django 4.2.17 on 2024-12-13 07:51

from django.db import migrations, models
import traveler.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='*Nicknames can contain only letters and digits.', max_length=30, unique=True, validators=[traveler.validators.NicknameValidator()])),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('country', models.CharField(max_length=3, validators=[traveler.validators.CountryCodeValidator()])),
                ('about_me', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
