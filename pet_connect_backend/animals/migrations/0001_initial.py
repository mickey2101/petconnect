# Generated by Django 5.2.1 on 2025-05-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('species', models.CharField(max_length=50)),
                ('breed', models.CharField(blank=True, max_length=100)),
                ('age_years', models.IntegerField(default=0)),
                ('age_months', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=1)),
                ('vaccinated', models.BooleanField(default=False)),
                ('neutered', models.BooleanField(default=False)),
                ('good_with_kids', models.BooleanField(default=True)),
                ('good_with_cats', models.BooleanField(default=True)),
                ('good_with_dogs', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('A', 'Available'), ('P', 'Pending'), ('AD', 'Adopted')], default='A', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
