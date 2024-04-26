from django.shortcuts import get_object_or_404, render
from recommender.models import Book
import random

def home(request):
    return render(request, 'recommender/home.html', {})

def get_recommendation(request):

    # cache query results?

    # get a random recommendation
    # what if the Books table is empty?
    ids = [book.id for book in Book.objects.all()]
    random_id = random.choice(ids)

    recommendation = get_object_or_404(Book, pk=random_id)

    return render(
        request,
        'recommender/recommendation.html', 
        {'recommendation': recommendation}
    )
