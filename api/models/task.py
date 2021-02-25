from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth import get_user_model

# Project class
class Task(models.Model):
  name = models.CharField(max_length=100)
  completed = models.BooleanField()
  MUST = 'Must'
  SHOULD = 'Should'
  COULD = 'Could'
  WOULD = 'Would'
  PRIORITY = (
    (MUST, 'Must'),
    (SHOULD, 'Should'),
    (COULD, 'Could'),
    (WOULD, 'Would'),
  )
  priority = models.CharField(max_length=6, choices=PRIORITY, default=MUST)
  deadline = models.DateField()
  time_estimate = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
  description = models.TextField()
  owner = models.ForeignKey(
    get_user_model(),
    related_name='tasks',
    on_delete=models.CASCADE,
  )

  def __str__(self):
      return f"The task named '{self.name}' is a '{self.priority}' due by '{self.deadline}' that should take a '{self.time_estimate}' on the time scale (5 being the most time, and 1 the least). It is '{self.completed}' that it is completed and this is the description: '{self.description}'."

      # returns dictionary version of Project models
  def as_dict(self):
      return {
        'id': self.id,
        'name': self.name,
        'completed': self.completed,
        'priority': self.priority,
        'deadline': self.deadline,
        'time_estimate': self.time_estimate,
        'description': self.description
      }
