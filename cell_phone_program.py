import cellphone_class as cp

def main():
    #get the manufacturer from use
    manufact = str(input('Enter the manufacturer: '))
    #get model number from user
    model = str(input('Enter the model number: '))
    #get retail price from user
    price = float(input("Enter the retail price: "))

    phone = cp.CellPhone(manufact, model, price)

    print("Here is your phone data: ")
    print("Manufacturer: ",  phone.get_manufact())
    print("Retail price: ",  phone.get_model())
    print("Model No: ", phone.get_retail_price())

main()