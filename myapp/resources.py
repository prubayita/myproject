from import_export import resources
from .models import *

class TaskResource(resources.ModelResource):
    class Meta:
        model = Task