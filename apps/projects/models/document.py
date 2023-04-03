# import os
# from django.db import models
# from .project import Project
# from apps.users.models import User
# from django.utils.deconstruct import deconstructible
# from django.dispatch import receiver
# from django.core.files.storage import default_storage
# from django.db.models.signals import pre_delete

# @deconstructible
# class DocumentPath(object):
#     def __init__(self, sub_path):
#         self.sub_path = sub_path

#     def __call__(self, instance, filename):
#         return '{}/{}/projects/{}/documents/{}/{}'.format(instance.project.customer.email, instance.project.name, instance.project.name, self.sub_path, filename)
    
# class Share(models.Model):
#     document = models.ForeignKey("Document", on_delete=models.CASCADE, related_name='shares')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class Document(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='documents')
#     title = models.CharField(max_length=100)
#     file = models.FileField(upload_to=DocumentPath('%Y/%m/%d/'))
    
#     shared_with = models.ManyToManyField(User, through='Share', related_name='shared_documents')

#     def __str__(self):
#         return self.title
    
        
# @receiver(pre_delete, sender=Project)
# def delete_project_files(sender, instance, **kwargs):
#     documents = instance.documents.all()
#     for document in documents:
#         document_path = document.file.path
#         default_storage.delete(document_path)
#         document_dir = os.path.dirname(document_path)
#         os.rmdir(document_dir)