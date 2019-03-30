from django.db import models

class Author(models.Model):
    ### DATABASE FIELDS
    full_name = models.CharField(max_length=45, primary_key=True)
        
    ### TO STRING METHOD
    def __str__(self):
        return self.full_name
        
class Project(models.Model):
    ### CHOICES
    DIVISIONS = (
        ('SOCI', 'Social & Behavioral Sciences'),
        ('BUSI', 'Business & Computing'),
        ('CONS', 'Consumer & Health Sciences'),
        ('CULI', 'Culinology & Food Science'),
        ('HOSP', 'Hospitality, Travel & Tourism'),
        ('KINE', 'Kinesiology & Athletics'),
        ('NUTR', 'Nutrition & Dietetics'),
        ('MATH', 'Mathematics & Sciences'),
        ('LITE', 'Literature & Languages'),
        ('TECH', 'Technology'),
        ('VISU', 'Visual & Performing Arts'),
    )

    FORMAT = (
        ('POS', 'Poster Session'),
        ('ORA', 'Oral Presentation'),
        ('EXH', 'Exhibition of Work'),
    )

    ### DATABASE FIELDS
    title = models.CharField(max_length=255, primary_key=True)
    division = models.CharField('Division', max_length=4, choices=DIVISIONS)
    tagline = models.TextField()
    mentor = models.TextField()
    year = models.IntegerField()
    presentation_format = models.CharField('Presentation Format', max_length=3, choices=FORMAT)
    abstract = models.TextField()
    paper = models.TextField(blank = True)
    cited_source = models.TextField(blank = True)
    attachment_file = models.FilePathField(path="/home/images", match="foo.*", recursive=True, blank = True)
    
    slug = models.SlugField(max_length=40)
    hash = models.h
    ### MODEL RELATIONSHIP(S)
    author = models.ManyToManyField(Author, db_table="result")

    ### TO STRING METHOD
    def __str__(self):
        return self.title


#### Test