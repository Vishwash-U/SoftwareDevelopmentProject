# Generated by Django 2.2.5 on 2020-11-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=200)),
                ('hospital', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
            ],
        ),
    ]