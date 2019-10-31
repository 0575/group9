from django.db import models
class Tag(models.Model):
	name = models.CharField(max_length=10, unique=True)
	creation_date = models.DateTimeField(auto_now_add=True)
class Post(models.Model):
	subject = models.CharField(max_length=160)
	content = models.CharField(max_length=800)
	# creator = ???
	public = models.BooleanField(default=True)
	creation_date = models.DateTimeField(auto_now_add=True)
	tag = models.ForeignKey(Tag, on_delete=models.SET_NULL,
null=True, blank=True)
