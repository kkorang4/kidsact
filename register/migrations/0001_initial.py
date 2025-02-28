# Generated by Django 3.0.6 on 2020-05-22 06:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('child_name', models.CharField(blank=True, max_length=255, null=True)),
                ('child_age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(5), django.core.validators.MaxValueValidator(13)])),
                ('child_condition', models.CharField(blank=True, max_length=2083, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
