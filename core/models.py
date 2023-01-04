from django.db import models
import uuid

# Create your models here.
class Job(models.Model):
    CompanyName = models.CharField(max_length=225)
    JobTitle = models.CharField(max_length=225)
    JobLocation = models.CharField(max_length=225)
    ContactEmail = models.CharField(max_length=225)
    WebsiteUrl = models.URLField(max_length=225)
    Tags = models.CharField(max_length=225, null=True)
    CompanyLogo = models.ImageField(upload_to='files/cover')
    JobDescription = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4)

