
# from django.db import models
# from django.conf import settings
# from .project import Project

# class Share(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='shares')
#     customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='shared_projects')

#     def __str__(self):
#         return f'{self.customer} shared {self.project}'