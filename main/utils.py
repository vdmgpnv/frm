from .models import Section


class DataMixin:
    sections = Section.objects.all()