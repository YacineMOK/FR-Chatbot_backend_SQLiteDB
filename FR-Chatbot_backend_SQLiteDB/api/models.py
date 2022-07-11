from sqlite3 import Timestamp
from django.db import models

# Here we create a model to store the 

class Dialogues(models.Model):
    QANumber = models.AutoField(primary_key=True)
    # UserSession = models.CharField(max_length=1024)
    UserTEXT = models.CharField(max_length=516)
    BotTEXT = models.CharField(max_length=1024)
