# Generated by Django 4.1.5 on 2023-08-10 16:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('surname', models.TextField(max_length=100)),
                ('address', models.TextField(max_length=100)),
                ('email', models.TextField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
