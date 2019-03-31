# Generated by Django 2.1.7 on 2019-03-31 04:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('full_name', models.CharField(max_length=45, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('division', models.CharField(choices=[('SOCI', 'Social & Behavioral Sciences'), ('BUSI', 'Business & Computing'), ('CONS', 'Consumer & Health Sciences'), ('CULI', 'Culinology & Food Science'), ('HOSP', 'Hospitality, Travel & Tourism'), ('KINE', 'Kinesiology & Athletics'), ('NUTR', 'Nutrition & Dietetics'), ('MATH', 'Mathematics & Sciences'), ('LITE', 'Literature & Languages'), ('TECH', 'Technology'), ('VISU', 'Visual & Performing Arts')], max_length=4, verbose_name='Division')),
                ('tagline', models.TextField()),
                ('mentor', models.TextField()),
                ('year', models.IntegerField()),
                ('presentation_format', models.CharField(choices=[('POS', 'Poster Session'), ('ORA', 'Oral Presentation'), ('EXH', 'Exhibition of Work')], max_length=3, verbose_name='Presentation Format')),
                ('abstract', models.TextField()),
                ('paper', models.TextField(blank=True)),
                ('cited_source', models.TextField(blank=True)),
                ('remote_asset', models.FilePathField(blank=True, match='foo.*', path='/home/images', recursive=True)),
                ('ext_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('author', models.ManyToManyField(db_table='result', to='pages.Author')),
            ],
        ),
    ]
