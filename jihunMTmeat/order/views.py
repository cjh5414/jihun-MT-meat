from django.shortcuts import render, redirect

from order.models import MeatPrice, Orderer
from order.forms import OrdererForm


def main_page(request):
    meat_price_list = MeatPrice.objects.all()

    return render(request, 'main_page.html', {'meat_price_list': meat_price_list})


def input_order_info(request):
    orderer_form = OrdererForm()
    return render(request, 'input_order_info.html', {'form': orderer_form})


def new_orderer(request):
    if request.method == 'POST':
        orderer_form = OrdererForm(request.POST)
        if orderer_form.is_valid():
            orderer_form.save()

    return redirect('/')
