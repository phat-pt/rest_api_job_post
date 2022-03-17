from django.db import models

# Create your models here.
class JobPost(models.Model):
    class Meta:
        db_table = 'items'

    id = models.AutoField(primary_key=True, editable = False)
    company_name = models.CharField(max_length=255, null=True, blank = True)
    ceo_name =  models.CharField(max_length=255, null=True, blank = True)
    found_date =  models.CharField(max_length=255, null=True, blank = True)
    company_size =  models.CharField(max_length=255, null=True, blank = True)
    revenue =  models.CharField(max_length=255, null=True, blank = True)
    industry =  models.CharField(max_length=255, null=True, blank = True)
    link =  models.CharField(max_length=255, null=True, blank = True)
    company_description =  models.TextField(null=True, blank = True)
    job_title = models.TextField(null=True, blank = True)
    job_location = models.CharField(max_length=255, null=True, blank = True)
    job_description = models.TextField(null=True, blank = True)
    job_summary = models.TextField(null=True, blank = True)
    job_time = models.DateField(null=True, blank= True)
    job_salary = models.CharField(max_length=255, null=True, blank = True)
    job_type = models.CharField(max_length=255, null=True, blank = True)

    def __str__(self):
        return self.job_title
    