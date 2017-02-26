from django.db import models

class Bucketlist(models.Model):
    """class for bucketlist model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns human readable form of model instance"""
        return "{}".format(self.name)
