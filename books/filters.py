import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='iexact')
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    book_id = django_filters.RangeFilter(field_name='book_id')
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'book_id']



# Handling Adnvance filter
class BookAdvanceFilter(django_filters.FilterSet):

    # if we have a character ID, for example book_id = BOOK0001, BOOK0002
    id_min = django_filters.CharFilter(method='filter_by_id_range', label='From Book ID')
    id_max = django_filters.CharFilter(method='filter_by_id_range', label='To Book ID')
    
    class Meta:
        model = Book
        fields = ['id_min', 'id_max']
    
    def filter_by_id_range(sef, queryset, name, value):
        if name == 'id_min':
            return queryset.filter(book_id__gte=value)
        elif name == 'id_max':
            return queryset.filter(book_id__lte=value)
        return queryset








