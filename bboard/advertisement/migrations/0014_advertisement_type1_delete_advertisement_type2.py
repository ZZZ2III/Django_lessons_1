# Generated by Django 4.2 on 2023-06-15 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0013_remove_advertisement_type2_conn_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement_type1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('conn', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='advertisement.advertisement')),
            ],
        ),
        migrations.DeleteModel(
            name='Advertisement_type2',
        ),
    ]
