from django.contrib import admin
from board.models import Board,ReviewImg
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'content']
  list_display_links = ['id', 'title']
  readonly_fields = ('id',)

class ReviewImgAdmin(admin.ModelAdmin):
  pass

admin.site.register(Board, BoardAdmin)
admin.site.register(ReviewImg, ReviewImgAdmin)
