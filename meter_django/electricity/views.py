from django.shortcuts import render
#from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = 123#Book.objects.all().count()
    num_instances = 234#BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = None#BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = 345#Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
