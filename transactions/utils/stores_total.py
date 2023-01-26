def stores_total(stores):
    totals = []
    for store in stores:
        total = 0
        for transaction in store:
            if transaction.type == 2 or transaction.type == 3 or transaction.type == 9:
                total -= transaction.value
            else:
                total += transaction.value
        totals.append(total)
    return totals
