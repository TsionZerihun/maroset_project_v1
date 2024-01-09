from django.contrib import admin
from .models import Indusrty, Job, ApplyJob, ConversationMessageJob,ReportedJob

admin.site.register(Indusrty)
admin.site.register(Job)
admin.site.register(ApplyJob)
admin.site.register(ConversationMessageJob)
admin.site.register(ReportedJob)
