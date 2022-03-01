import cellphone_class as cp

def main():
    #get the manufacturer from use
    manufact = 'Apple'
    #get model number from user
    model = "iPhone 13"
    #get retail price from user
    price = 899

    phone = cp.ne(manufact, model, price)

    print("Here is your phone data: ")
    print("Manufacturer: ",  phone.get_manufact())
    print("Retail price: ",  phone.get_model())
    print("Model No: ", phone.get_retail_price())

main()