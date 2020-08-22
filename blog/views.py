from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author' : "Sharath.v",
        'title' : "Blog1",
        'content' : "my first blog",
        'date_posted' : 'August 22 2020'
    },
    {
        'author' : "mais",
        'title' : "Blog2",
        'content' : "my 2nd blog",
        'date_posted' : 'may 22 2020'
    },
    {
        'author' : "Sharath.v",
        'title' : "blog3",
        'content' : "my 3rd blog",
        'date_posted' : 'August 21 2020'
    }
]
def home(request):
    context = {
        'posts' : posts,
        'title' : 'blog-home'
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')