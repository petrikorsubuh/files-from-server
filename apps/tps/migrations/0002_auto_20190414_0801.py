# Generated by Django 2.1.7 on 2019-04-14 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tps', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tps',
            options={'ordering': ['nama', 'alamat']},
        ),
    ]
