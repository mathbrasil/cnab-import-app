def stores_check(transactions):
    stores = []
    for item in transactions:
        if item.store_name not in stores:
            stores.append(item.store_name)

    return stores
