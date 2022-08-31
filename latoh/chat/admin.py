from django.contrib import admin
from chat.models import Chat,Conversation,Message

# Register your models here.
admin.site.register(Chat)

class OnlineInline(admin.TabularInline):
    model=Conversation.online.through

@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    fields=('name',)
    list_display=('name',)
    search_fields=('name',)
    inlines=[
        OnlineInline
    ]