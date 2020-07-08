# Generated by Django 3.0.7 on 2020-06-19 08:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('body', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='images')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'publish')], max_length=1)),
            ],
        ),
    ]
