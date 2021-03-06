# Generated by Django 2.1.7 on 2019-03-31 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('caleg', '0001_initial'),
        ('kecamatan', '0001_initial'),
        ('tps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah_suara', models.IntegerField()),
                ('pict', models.ImageField(upload_to='upload_pict/')),
                ('caleg', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='caleg.Caleg')),
                ('kecamatan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kecamatan.Kecamatan')),
                ('tps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tps.Tps')),
            ],
        ),
    ]
