# Generated by Django 3.0.3 on 2020-03-03 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_client_partner_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='number_of_awards',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='award_comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='award_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='video',
            name='award_number',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_hash', models.CharField(max_length=40, unique=True)),
                ('stage', models.CharField(default='1', max_length=10)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=500)),
                ('logo', models.URLField(blank=True, null=True)),
                ('theme', models.TextField()),
                ('attendees', models.PositiveSmallIntegerField()),
                ('exhibitors', models.PositiveSmallIntegerField()),
                ('venue', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('target_audience', models.CharField(choices=[('Attendee', 'Attendee'), ('Exhibitor', 'Exhibitor'), ('Sponsor', 'Sponsor'), ('Other', 'Other')], default='ATTENDEE', max_length=200)),
                ('feature_1', models.TextField()),
                ('feature_2', models.TextField()),
                ('feature_3', models.TextField()),
                ('feature_4', models.TextField(null=True)),
                ('feature_5', models.TextField(null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Client')),
            ],
        ),
    ]