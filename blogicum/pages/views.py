from django.shortcuts import render


def about(request):
    """Обработчик для страницы информации о блоге"""
    return render(request, 'pages/about.html')


def rules(request):
    """Обработчик страницы с правилами"""
    return render(request, 'pages/rules.html')
