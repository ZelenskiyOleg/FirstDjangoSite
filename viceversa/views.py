from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = reverse_string(user_text)
    return render(request, 'reverse.html', {'usertext':user_text,
                                            'reversed_text':reversed_text})

def reverse_string(s):
    return s[::-1]