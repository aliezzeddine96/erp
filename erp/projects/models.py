from django.db import models


# Create your models here.
class Projects(models.Model):
	status = [
		('0', 'Paused'),
		('1', 'On Going'),
		('2', 'Done'),
	]
	project_name = models.CharField('Project\'s Name', max_length=100, unique=True)
	project_status = models.CharField('Projects\'s Status ', max_length=1, choices=status)

	class Meta:
		db_table = 'Projects'
		verbose_name_plural = 'Projects'

	def __str__(self):
		return '{}'.format(str(self.project_name))

	def projectView(self):
		return '{} is {}'.format(str(self.project_name), str(self.status[int(str(self.project_status))][1]))

	def projectStatus(self):
		return str(self.status[int(str(self.project_status))][1])

