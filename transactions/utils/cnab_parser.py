def cnab_parser(file):
    cnab_file = file

    transactions = []

    while True:
        file_line = cnab_file.readline().decode("utf-8")

        if not file_line:
            break

        transaction = {
            "type": int(file_line[0:1]),
            "date": file_line[1:9],
            "value": int(file_line[9:19]) / 100,
            "cpf": file_line[19:30],
            "card": file_line[30:42],
            "hour": file_line[42:48],
            "store_owner": file_line[48:62].replace("\r\n", "").strip(),
            "store_name": file_line[62:81].replace("\r\n", "").strip(),
        }

        transactions.append(transaction)

    return transactions
