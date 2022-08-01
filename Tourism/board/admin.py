from django.contrib import admin
from board.models import Board
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
  pass


admin.site.register(Board, BoardAdmin)