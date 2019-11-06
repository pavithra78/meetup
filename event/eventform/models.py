from django.db import models
class events(models.Model):
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	
	venue=models.CharField(max_length=100)
	date=models.DateField()
	time=models.TimeField()
	eventname=models.CharField(unique=True,max_length=100)
	Amount=models.IntegerField()

	def __str__(self):
		return self.eventname
		

class Registration(models.Model):
	register_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	email=models.EmailField(max_length=50)
	eventname=models.ForeignKey(events,on_delete=models.CASCADE)

	def __str__(self):
		return self.name
		




