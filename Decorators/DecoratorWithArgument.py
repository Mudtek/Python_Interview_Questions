from typing import Dict, Optional

def format_price(price: float) -> str:
    return "${:,.2f}".format(price)

def price_reduction(percent: Optional[float] = 0) -> callable:
    def decorator(func: callable) -> callable:
        def wrapper(*args: any, **kwargs: any) -> Dict[str, str]:
            items = func(*args, **kwargs)
            for item, price in items.items():

                # reduce the price by the specified percentage and format as USD
                if isinstance(price, str):
                    price = float(price.replace("$", "").replace(",", ""))
                if percent:
                    items[item] = format_price(price * (1 - percent))
                else:
                    items[item] = format_price(float(price))
            return items
        return wrapper
    return decorator

class GroceryStore:
    def __init__(self):
        self.prices: Dict[str, float] = {
            "apple": 1.00,
            "banana": 1.50,
            "orange": 0.75,
            "bread": 2.50,
        }
    
    @price_reduction(percent=0.5)
    def price_lookup(self, item: str) -> Dict[str, str]:
        return {item: self.prices.get(item, 0.0)}

store = GroceryStore()
print(store.price_lookup("apple"))
print(store.price_lookup("banana"))
