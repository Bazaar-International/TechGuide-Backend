from django.db import models
from markdown2 import markdown
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

class Section(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    markdown_content = MarkdownxField(blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Convert markdown to HTML before saving
        if self.markdown_content:
            self.html_content = markdownify(self.markdown_content)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Subsection(models.Model):
    id = models.AutoField(primary_key=True)
    section = models.ForeignKey(Section, related_name='subsections', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    markdown_content = MarkdownxField(blank=True, null=True)
    html_content = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Convert markdown to HTML before saving
        if self.markdown_content:
            self.html_content = markdownify(self.markdown_content)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
