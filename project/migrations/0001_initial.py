# Generated by Django 3.0.3 on 2020-05-18 18:22

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_first', models.CharField(max_length=200)),
                ('contact_last', models.CharField(max_length=200)),
                ('contact_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_role', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('partner_logo', models.URLField(blank=True, max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('logo', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('number_of_awards', models.PositiveSmallIntegerField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
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
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(max_length=500)),
                ('logo', models.URLField(blank=True, null=True)),
                ('theme', models.TextField(blank=True, null=True)),
                ('attendees', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('exhibitors', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('venue', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=200, null=True)),
                ('target_audience', models.CharField(blank=True, max_length=200, null=True)),
                ('feature_1', models.TextField(blank=True, null=True)),
                ('feature_2', models.TextField(blank=True, null=True)),
                ('feature_3', models.TextField(blank=True, null=True)),
                ('feature_4', models.TextField(blank=True, null=True)),
                ('feature_5', models.TextField(blank=True, null=True)),
                ('assets', models.URLField(blank=True, null=True)),
                ('guests', models.CharField(blank=True, max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Client')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Client Message', max_length=2000)),
                ('date', models.DateField(blank=True, null=True)),
                ('draft_script', models.URLField(blank=True, null=True)),
                ('script', models.URLField(blank=True, null=True)),
                ('assets', models.URLField(blank=True, null=True)),
                ('draft', models.URLField(blank=True, null=True)),
                ('final', models.URLField(blank=True, null=True)),
                ('notes', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Client')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=2000)),
                ('process_comment', models.CharField(choices=[('Script Rough Draft', 'rough_script'), ('Script Final Draft', 'final_script'), ('Video Rough Draft', 'video_rough'), ('Video Final Draft', 'final_video')], max_length=200, null=True)),
                ('info', django.contrib.postgres.fields.jsonb.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.Organization'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('number_of_awards', models.PositiveSmallIntegerField()),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('award_number', models.PositiveSmallIntegerField()),
                ('award_name', models.CharField(max_length=200000)),
                ('award_description', models.TextField(blank=True, null=True)),
                ('award_winner', models.CharField(max_length=2000)),
                ('award_project', models.CharField(blank=True, max_length=2000, null=True)),
                ('award_comments', models.TextField()),
                ('award_assets', models.URLField(blank=True, default='#', null=True)),
                ('script', models.URLField(blank=True, default='#', null=True)),
                ('draft', models.URLField(blank=True, default='#', null=True)),
                ('final_draft', models.URLField(blank=True, default='#', null=True)),
                ('awards', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Awards')),
            ],
        ),
    ]
