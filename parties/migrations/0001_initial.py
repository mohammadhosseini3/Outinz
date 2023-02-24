# Generated by Django 4.1.6 on 2023-02-13 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartyVenue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=50, null=True, verbose_name='Venue')),
                ('location', models.CharField(max_length=50, null=True, verbose_name='Location')),
            ],
        ),
        migrations.CreateModel(
            name='PartyTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Party Name')),
                ('price', models.IntegerField(null=True)),
                ('start_date', models.DateTimeField(null=True, verbose_name='Start Date')),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('cancled', 'Cancled'), ('expired', 'Expired'), ('sold out', 'Sold out'), ('selling', 'Selling')], default='Selling', max_length=10)),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parties.partyvenue', verbose_name='Party Venue')),
            ],
        ),
    ]
