from django.contrib import admin
from apps.projects.models.project import Project
# from apps.projects.models.document import Document
# from apps.projects.models.note import Note


from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

# class ShareDocumentForm(helpers.ActionForm):
#     users = forms.ModelMultipleChoiceField(queryset=User.objects.all())
    
# class ShareDocumentAdmin(admin.ModelAdmin):
#     list_display = ('title', 'project', 'share_link')
#     actions = ['share_documents']

#     def share_link(self, obj):
#         url = reverse('admin:app_share_document', args=[obj.pk])
#         return format_html('<a href="{}">Share</a>', url)
#     share_link.short_description = 'Share'

#     def share_documents(self, request, queryset):
#         form = None

#         if 'apply' in request.POST:
#             form = ShareDocumentForm(request.POST)

#             if form.is_valid():
#                 users = form.cleaned_data['users']

#                 for document in queryset:
#                     for user in users:
#                         Share.objects.get_or_create(document=document, user=user)

#                 self.message_user(request, f"{len(users)} users have been granted access to {len(queryset)} documents.")
#                 return HttpResponseRedirect(request.get_full_path())

#         if not form:
#             form = ShareDocumentForm()

#         context = dict(
#             self.admin_site.each_context(request),
#             title = 'Share Documents',
#             action = 'share_documents',
#             query_set = queryset,
#             form = form,
#         )

#         return render(request, 'admin/share_documents.html', context)

#     @staff_member_required
#     def share_document_view(request, document_id):
#         document = get_object_or_404(Document, pk=document_id)
#         return ShareDocumentAdmin.as_view(action='share_documents')(request, queryset=Document.objects.filter(pk=document.pk))

#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('<int:document_id>/share/', self.share_document_view, name='app_share_document'),
#         ]
#         return custom_urls + urls


# class NoteInline(admin.TabularInline):
#     model = Note

# class DocumentInline(admin.TabularInline):
#     model = Document

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name' , 'created_at', 'updated_at']
    # inlines = [NoteInline, DocumentInline]

admin.site.register(Project, ProjectAdmin)
# admin.site.register(Note)
# admin.site.register(Document)