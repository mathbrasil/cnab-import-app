from django.shortcuts import render, redirect

from .models import Transaction

from .utils import cnab_parser, stores_check, stores_total


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
    transactions_list = []

    for store in stores:
        item = Transaction.objects.filter(store_name=store)
        transactions_list.append(list(item))

    totals = stores_total(transactions_list)

    stores_transactions = zip(transactions_list, totals)
    has_transactions = transactions_list

    return render(
        request,
        "transactions.html",
        {
            "transactions": stores_transactions,
            "has_transactions": has_transactions
        },
    )
