# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Users, Events, Alumni, Hosts, Attends

# Register your models here.

admin.site.register(Users)
admin.site.register(Events)
admin.site.register(Alumni)
admin.site.register(Hosts)
admin.site.register(Attends)
