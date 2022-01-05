from decimal import Decimal, ROUND_HALF_UP

X = input()

print(Decimal(str(X)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))

