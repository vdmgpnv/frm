from .models import Section
from .forms import SearchForm


class DataMixin:
    sections = Section.objects.all()
    search_form = SearchForm()