from django.shortcuts import render, redirect

from .models import Transaction

from .utils import cnab_parser, stores_check

import ipdb


def home(request):
    if request.method == "POST":
        cnab_file = request.FILES["cnab_file"]
        transactions = cnab_parser(cnab_file)

        transactions_obj = [Transaction(**item) for item in transactions]
        Transaction.objects.bulk_create(transactions_obj)

        return redirect("/transactions")

    return render(request, "home.html", {})


def transactions(request):
    transactions = Transaction.objects.all()

    stores = stores_check(transactions)
    stores_transactions = []

    for store in stores:
        item = Transaction.objects.filter(store_name=store)
        stores_transactions.append(list(item))

    return render(
        request,
        "transactions.html",
        {
            "transactions": stores_transactions,
        },
    )
