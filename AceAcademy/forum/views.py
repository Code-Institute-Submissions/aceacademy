from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Forum, Comment
from .forms import CommentForm, ForumForm

# Create your views here.


def index(request):
    # return HttpResponse("Reviews")
    return render(request, 'reviews/index.template.html')

def create_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        form = ForumForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return HttpResponse("Review is created")
        else:
            return HttpResponse("Form has error")
    else:
        form = ForumForm()
        return render(request, 'reviews/create_review.template.html', {
            "form": form,
            "book": book
        })


def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
            return HttpResponse("Comment created")
        else:
            return HttpResponse("Problem with input")
    else:

        form = CommentForm()
        return render(request, 'reviews/create_comment.template.html', {
            "form": form,
            "review": review
        })