from django.contrib import admin
from .models import Industry, Job, ApplyJob, ConversationMessageJob,ReportedJob

admin.site.register(Industry)
admin.site.register(Job)
admin.site.register(ApplyJob)
admin.site.register(ConversationMessageJob)
admin.site.register(ReportedJob)
