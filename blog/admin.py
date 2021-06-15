from django.contrib import admin
from .models import Post, Contact, Comments, Specialization, Doctor, Reception
from django.contrib.admin import ModelAdmin, TabularInline
from suit_ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm


admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Specialization)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('author_id', 'email', 'body')
admin.site.register(Comments, CommentAdmin)

class ReceptionInline(TabularInline):
    model = Reception


class DoctorForm(ModelForm):
    class Meta:
        widgets = {
            'info': CKEditorWidget(editor_options={'startupFocus': True})
        }


class DoctorAdmin(ModelAdmin):
    form = DoctorForm
    inlines = [ReceptionInline,]


class ReceptionForm(ModelForm):
    class Meta:
        widgets = {
            'patient_info': CKEditorWidget(editor_options={'startupFocus': True})
        }


class ReceptionAdmin(ModelAdmin):
    form = ReceptionForm


admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Reception,ReceptionAdmin)
