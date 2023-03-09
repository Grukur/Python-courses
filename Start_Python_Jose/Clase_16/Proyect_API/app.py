from Clase_16.Proyect_API.libs.openexchange import OpenExchangeClient

APP_ID = "3f33084eca9e4475b2fe9c86207755c5"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f'USD {usd_amount} is GBP {gbp_amount:.2f}')
