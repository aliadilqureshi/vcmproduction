# Generated by Django 3.0.3 on 2020-05-07 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0025_awards'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_number', models.PositiveSmallIntegerField()),
                ('award_name', models.CharField(max_length=200000)),
                ('award_description', models.TextField()),
                ('award_winner', models.CharField(max_length=2000)),
                ('award_comments', models.TextField()),
                ('award_assets', models.URLField(blank=True, default='#', null=True)),
                ('script', models.URLField(blank=True, default='#', null=True)),
                ('draft', models.URLField(blank=True, default='#', null=True)),
                ('final_draft', models.URLField(blank=True, default='#', null=True)),
                ('awards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Awards')),
            ],
        ),
    ]