'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, ROUND_HALF_UP

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

PAYABLE_FOR_AN_ORDER = Decimal('1000000')

def validorder(order: Order):
    payment = Decimal('0')
    total = Decimal('0')

    for item in order.items:
        if item.type == 'payment':
            payment += Decimal(item.amount)
        elif item.type == 'product':
            total += Decimal(item.amount) * Decimal(item.quantity)
        else:
            return "Invalid item type: %s" % item.type

    # 計算結果を2桁に丸める
    payment = payment.quantize(Decimal('.01'))
    total = total.quantize(Decimal('.01'))

    if payment.compare(PAYABLE_FOR_AN_ORDER) > 0 or total.compare(PAYABLE_FOR_AN_ORDER) > 0:
        return "Total amount payable for an order exceeded"
    elif payment != total:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, payment - total)
    else:
        return "Order ID: %s - Full payment received!" % order.id