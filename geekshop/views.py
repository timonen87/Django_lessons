from django.shortcuts import render

def index(request):
    title = 'Интернет магазин'
    list_params = ['Стул', 'Купить', 'Заказать']

    context = {
        'list_params': list_params,
        'some_name': 'hello',
        'title': title,
    }
    return render(request, 'index.html', context=context)


def contacts(request):
    return render(request, 'contact.html')