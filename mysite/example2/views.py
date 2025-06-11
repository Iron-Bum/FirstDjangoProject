from django.shortcuts import render


def main_page(request):
    data = {'title': 'Глвная страница'}
    return render(request, 'main_page/main_page.html', data)


def card(request):
    data = {'title': 'Card'}
    return render(request, 'main_page/card.html', data)


def market(request):
    products = [
        {'name': 'smartphone', 'cost': 70000},
        {'name': 'XBox', 'cost': 110000},
        {'name': 'VR', 'cost': 55000}
    ]
    data = {'title': 'Market', 'products': products}
    return render(request, 'main_page/market.html', context=data)
