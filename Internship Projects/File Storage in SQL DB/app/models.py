from django.db import models


class MediaStore(models.Model):
    file_number = models.IntegerField(primary_key=True)
    file_name = models.CharField(max_length=30, blank=True, null=True)
    file_type = models.CharField(max_length=10, blank=True, null=True)
    file_data = models.BinaryField()
    file_extension = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'media_store'

    def __str__(self):
        return self.file_name
