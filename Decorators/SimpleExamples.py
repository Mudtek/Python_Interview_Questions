"""Simple examples explaining how decorators work"""

import time
from typing import Dict, Any, Callable

def speed_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__doc__)
        print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

@speed_timer
def my_func() -> int:
    """A simple example function"""
    total = 0
    for i in range(1, 1000001):
        total += i
    return total

print(my_func())

# =====================================================================================

def format_price(price: float) -> str:
    return "${:,.2f}".format(price)

def price_reduction(func: callable) -> callable:
    def wrapper(*args: any, **kwargs: any) -> Dict[str, str]:
        items = func(*args, **kwargs)
        for item, price in items.items():

            # reduce the price by 10% and format as USD
            items[item] = format_price(price * 0.9)
        return items
    return wrapper

class GroceryStore:
    def __init__(self):
        self.prices: Dict[str, float] = {
            "apple": 1.00,
            "banana": 1.50,
            "orange": 0.75,
            "bread": 2.50,
        }
    
    @price_reduction
    def price_lookup(self, item: str) -> Dict[str, str]:
        return {item: self.prices.get(item, 0.0)}

store = GroceryStore()
print(store.price_lookup("apple"))
print(store.price_lookup("banana"))

# ============================================================================

import pytest

@pytest.mark.parametrize('input, expected', [
    ('hello', 'HELLO'),
    ('world', 'WORLD'),
])
def test_uppercase(input, expected):
    result = input.upper()
    assert result == expected