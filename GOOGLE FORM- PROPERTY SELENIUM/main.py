from property import Property



property_link,property_price= Property().extract_link()
print(property_link)
print(property_price)



for pro in property_link:
    print(pro.get("href"))

for proo in property_price:
    print(proo.getText())