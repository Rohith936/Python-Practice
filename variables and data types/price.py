price = 4999
discount = 18
gst = 18
a=(price/100)*18
print(f"Discount{a}")
print(f"GST:{a}")
b=price-a
print(f"Price after discount:{round(b)}")
print(f"Final payable amount:{int(price+a-a)}")
