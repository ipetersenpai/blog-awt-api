from django.shortcuts import render

posts = [
    {
        'author' : 'PeterFCR',
        'title' : 'Not to die',
        'content' : 'about not dying',
        'date_posted': 'August 29, 2023'
    },
    {
        'author' : 'Ben10',
        'title' : 'Aint want to be an alien',
        'content' : 'tired being an alien',
        'date_posted': 'August 29, 2023'
    }
]

def home(request):
    context = {
        'posts' : posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title' : 'About'})