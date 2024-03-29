# Generated by Django 2.1.4 on 2019-11-12 02:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('productName', models.CharField(max_length=25)),
                ('productPrice', models.FloatField()),
                ('Manager', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batchNum', models.IntegerField()),
                ('batchDate', models.DateField()),
                ('quantity', models.IntegerField()),
                ('Manager', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.products')),
            ],
        ),
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('vid', models.IntegerField(primary_key=True, serialize=False)),
                ('vendorName', models.CharField(max_length=25)),
                ('Manager', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='stock',
            name='svid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.vendor'),
        ),
        migrations.AlterUniqueTogether(
            name='stock',
            unique_together={('sid', 'svid')},
        ),
    ]
