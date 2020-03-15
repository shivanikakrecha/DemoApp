from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=20)
	description = models.TextField(null=True, blank=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True, null=True, blank=True)

	def __str__(self):
		return self.title