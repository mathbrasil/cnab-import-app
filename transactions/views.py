from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict

from .models import Transaction


def home(request):

    return render(request, "home.html", {})


def transactions(request):
    
    return render(request, "transactions.html", {})


class TransactionsView(APIView):
    def post(self, request: Request) -> Response:
        cnab_file = request.FILES["cnab_files"].read()
        cnab_file = open("cnab.txt", "r")
        transactions = []

        while True:
            file_line = cnab_file.readline()

            if not file_line:
                break

            transaction = {
                "type": int(file_line[0:1]),
                "date": file_line[1:9],
                "value": int(file_line[9:19]) / 100,
                "cpf": file_line[19:30],
                "card": file_line[30:42],
                "hour": file_line[42:48],
                "store_owner": file_line[48:62].replace("\n", "").strip(),
                "store_name": file_line[62:81].replace("\n", "").strip(),
            }

            transactions.append(transaction)

        created_transactions = Transaction.objects.bulk_create(transactions)
        transactions_obj = model_to_dict(created_transactions)

        print(transactions_obj)

        return Response(created_transactions, status.HTTP_201_CREATED)
