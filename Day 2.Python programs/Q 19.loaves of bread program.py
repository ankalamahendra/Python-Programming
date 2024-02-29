PRICE_PER_LOAF = 185
DISCOUNT_PERCENTAGE = 60

fresh_loaves = int(input("Enter the number of fresh loaves purchased: "))
day_old_loaves = int(input("Enter the number of day-old loaves purchased: "))

regular_price = fresh_loaves * PRICE_PER_LOAF
discounted_price = (1 - DISCOUNT_PERCENTAGE / 100) * PRICE_PER_LOAF * day_old_loaves
total_amount = regular_price + discounted_price

print(f"Regular price: Rs.{regular_price:.2f}")
print(f"Amount of new loaves: Rs.{fresh_loaves * PRICE_PER_LOAF:.2f}")
print(f"Amount of day-old loaves: Rs.{discounted_price:.2f}")
print(f"Total amount: Rs.{total_amount:.2f}")
