# Generated by Django 2.1.7 on 2019-03-28 00:29

from django.db import migrations, models


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
                ('title', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('division', models.CharField(choices=[('SOCI', 'Social & Behavioral Sciences'), ('BUSI', 'Business & Computing'), ('CONS', 'Consumer & Health Sciences'), ('CULI', 'Culinology & Food Science'), ('HOSP', 'Hospitality, Travel & Tourism'), ('KINE', 'Kinesiology & Athletics'), ('NUTR', 'Nutrition & Dietetics'), ('MATH', 'Mathematics & Sciences'), ('LITE', 'Literature & Languages'), ('TECH', 'Technology'), ('VISU', 'Visual & Performing Arts')], max_length=4, verbose_name='Division')),
                ('tagline', models.TextField()),
                ('mentor', models.TextField()),
                ('year', models.IntegerField()),
                ('presentation_format', models.CharField(choices=[('POS', 'Poster Session'), ('ORA', 'Oral Presentation'), ('EXH', 'Exhibition of Work')], max_length=3, verbose_name='Presentation Format')),
                ('abstract', models.TextField()),
                ('paper', models.TextField()),
                ('cited_source', models.TextField()),
                ('attachment_file', models.FilePathField(match='foo.*', path='/home/images', recursive=True)),
                ('author', models.ManyToManyField(db_table='result', to='pages.Author')),
            ],
        ),
    ]
