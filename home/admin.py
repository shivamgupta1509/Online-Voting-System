from django.contrib import admin
from home.models import Contact, ElectionList, VoteGivenData, PartyName

# Register your models here.
admin.site.register(Contact)
admin.site.register(ElectionList)
admin.site.register(VoteGivenData)
admin.site.register(PartyName)

