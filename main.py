import finnhub

finnhub_client = finnhub.Client(api_key="cb6ptfiad3idq8jbm7cg")

"""
quote function:
c: Current price
d: Change
dp: Percent change
h: High price of the day
l: Low price of the day
o: Open price of the day
pc: Previous close price
"""

print(finnhub_client.quote('GME'))