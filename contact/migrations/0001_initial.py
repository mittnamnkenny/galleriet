# Generated by Django 3.2 on 2022-10-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.IntegerField(choices=[(0, 'Customer service'), (1, 'Technical assistance')], default=0)),
                ('full_name', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
