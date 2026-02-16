def calculate_price(base_price, demand_score, stock_level, current_hour):
    price = base_price

    # Demand adjustment
    if demand_score > 70:
        price *= 1.12
    elif demand_score < 30:
        price *= 0.90

    # Stock adjustment
    if stock_level < 20:
        price *= 1.15
    elif stock_level > 100:
        price *= 0.95

    # Time adjustment (Night discount)
    if 0 <= current_hour <= 6:
        price *= 0.95

    return round(price, 2)
