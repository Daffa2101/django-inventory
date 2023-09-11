from django.shortcuts import render

from .models import Item
# Create your views here.


def show_main(request):
    item = Item(name='barang1', amount=5, category="kategori1",
                description="description1")
    context = {
        'name': 'Daffa Akmal Zuhdii',
        'class': 'PBP A',
        'item_name': item.name,
        'amount': item.amount,
        'category': item.category,
        'description': item.description,

    }

    return render(request, "main.html", context)
