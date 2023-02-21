def convert(orderlist):
    
    order = list(orderlist.values())
    
    #order is a list containing [name,address,phone number, toppings, slices, tracking number] 
    name = order[0]
    address =  order[1]
    phone =  order[2]
    topping =  order[3]
    slices =  order[4]
    tracking = order[5]
    command = "INSERT INTO orders (name,address,phone,topping,slices,tracking) values ( name, address, phone, topping, slices, tracking);"
