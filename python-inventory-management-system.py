#inventory
#transaction
#report---items,revenue,profit

import random



veg = ['MANGO','APPLE','TOMATO','BRINJAL']
quantity=[10,15,20,30]
actual_price=[50,100,20,30]
price=[70,140,35,50]
users=[]
cart={}
t_sold=0
total_revenue=0
total_profit=0
sales_report={}

while True:
    print('1.owner')
    print('2.user')
    print('3.exit')

    role=input('choose an option:')
    

    if role=='1':
        '''otp=random.randint(1111,9999)
        print('your One Time Password is:',otp)
        t=int(input('enter your otp :'))
        if otp==t:'''
        while True:
                print('\n----owner selection-----')
                print('1.add items')
                print('2.remove item')
                print('3.update item')
                print('4.view inventory')
                print('5.view users details')
                print('6.view report')
                print('7.total revenue itemized profit')
                print('8.exit')

                ch=input('choose an option:')
                
                if ch=='1':
                    item=input('enter item name:').upper()
                    if item not in veg:
                        kgs=int(input('enter quantity of item:'))
                        actual_rupees=int(input('enter actual price of item:'))
                        rupees=int(input('enter price of item:'))
                        
                        
                        veg.append(item)
                        quantity.append(kgs)
                        price.append(rupees)
                        actual_price.append(actual_rupees)
                        print('added sucessfully')
                        print(veg)
                    elif item in veg:
                        print(item,'is already available in the INVENTORY')
                        print(veg,quantity)
                        index=veg.index(item)
                        kgs=int(input('enter quantity of items: '))
                        
                        quantity[index]+=kgs
                        print(veg,quantity)

                    
                elif ch=='2':
                    item=input('enter item name:').upper()
                    
                    if item in veg:
                       idx = veg.index(item)
                       veg.remove(idx)
                       quantity.remove(idx)
                       price.remove(idx)
                       print('item removed successfully')
                    else:
                        print('item not found')

                    
                elif ch=='3':
                    old_item=input('enter item updated:').upper()
                    if old_item in veg:
                        new_item=input('enter item name:').upper()
                        new_quantity=int(input('enter item quantity:'))
                        new_price=int(input('enter item price:'))
                        index=veg.index(old_item)
                        veg[index]=new_item
                        quantity[index]=new_quantity
                        price[index]=new_price
                        print('item are updated sucessfully')
                        print(new_item)
                    else:
                        print('item is not found')

                        
                elif ch=='4':
                    if len(veg)>=1:
                        print('\n-----view inventory-----')
                        for i in range(len(veg)):
                            print([i+1],'item:',veg[i])
                            print(  'quantity:',quantity[i])
                            print(  'price:',price[i])
                            print()
                    else:
                        print('inventory item not found')

                    
                elif ch=='5':
                    if len(users)==0:
                        print('user not registered yet')
                    else:
                        print('\n---user details---')
                        for user in users:
                            print('name:',user[0],'phone:',user[1])

                            
                elif ch=='6':
                    print('\n--report--')
                    print('total inventory items:',veg)
                    print('total registered users:',len(users))
                    print('total items sold:',t_sold)

                elif ch=='7':
                    print('\n--revenue and profit--')
                    print('total_revenue:',total_revenue)
                    print('total_profit:',total_profit)

                    print('\n---itemized report---')
                    
                    for item, data in sales_report.items():
                        print('item:',item)
                        print('quantity sold:',data['quantity'])
                        print('total_revenue:',data['total_revenue'])
                        print('total_profit:',data['total_profit'])
                        print()


                    
                elif ch=='8':
                    print('exiting')
                    break



                    
                else:
                    print('choose correct option')
                    
                    
        else:
            print(' You entered otp is wrong Try again')
            
       
    elif role=='2':
        name = input('enter your name:')

        while True:
            phone = input('enter your phone number:')
            if phone.isdigit() and len(phone)==10:
                break
            else:
                print('enter correct 10 digit phone number')
        otp = random.randint(1111,9999)
        print('your one time otp is :',otp)

        t=int(input('enter your otp:'))

        if otp == t:
            users.append([name,phone])
            print('registration successful')
      
            while True:
                 print('\n---user selection---')
                 print('1.view items')
                 print('2.add cart')
                 print('3.remove from cart')
                 print('4.modify cart')
                 print('5.view cart')
                 print('6.billig')
                 print('7.exit')

                 ch=input('choose an option:')

                 if ch=='1':
                     print('available items are:',veg)
                     print('available quantity of items is:',quantity)
                     print('selling price is:',price)
                     
                 elif ch=='2':
                     item=input('enter items to add cart:').upper()
                     
                     if item in veg:
                         idx=veg.index(item)
                         kgs=int(input('enter quantity of item:'))

                         if kgs <= quantity[idx]:
                             
                             if item in cart:
                                 cart[item] += kgs

                             else:
                                 cart[item] = kgs
                             print(kgs,item,' item added to cart sucessfully')
                             
                         else:
                             print('item out of stock')
                             
                     else:
                        print('item is not avaliable')

                         
                 elif ch=='3':
                     item=input('enter the item to remove from cart:').upper()
                     if item in cart:
                         del cart[item]
                         print('item is removed sucessfully from cart')
                     else:
                         print('item not found in cart')

                         
                 elif ch=='4':
                     if len(cart)==0:
                         print('cart is empty')
                     else:
                         print('your cart:',cart)
                         item=input('enter item to modify the cart:').upper()
                         if item in cart:
                             new_qty=int(input('enter new quantity:'))
                             #index=cart.index(old_item)
                             cart[item]=new_qty
                             print('cart updated sucessfully')
                         else:
                             print('item not found in cart')
                     
                     
                 elif ch=='5':
                     print('\n-----your cart-----')
                     
                     for item,qty in cart.items():
                         print(item,':',qty)

                 elif ch=='6':
                     if len(cart)==0:
                         print('cart is empty')
                     else:
                         print('\n--billing--')
                         total_bill=0
                         
                         for item,qty in cart.items():
                             idx=veg.index(item)
                             
                             sell_price=int(price[idx])
                             cost_price=actual_price[idx]
                             item_total = sell_price * qty
                             quantity[idx] -= qty
                             
                             print(item, 'x', qty,':',item_total)
                             print('remaining stock is:', quantity[idx])

                             total_bill += item_total
                             total_revenue += item_total
                             total_profit += (sell_price - cost_price)* qty
                             
                             if item not in sales_report:
                                 sales_report[item]={
                                     'quantity':0,
                                     'total_revenue':0,
                                     'total_profit':0
                                     }

                             sales_report[item]['quantity'] += qty
                             sales_report[item]['total_revenue'] += item_total
                             sales_report[item]['total_profit'] += (sell_price - cost_price)*qty
                                 
                                 
                         print('total items:',sum(cart.values()))
                         print('total bill:', total_bill)

                         t_sold += sum(cart.values())
                         
                         cart.clear()
                         
                                                     
                 elif ch=='7':
                     print('exiting')
                     break

                 else:
                     print('choose correct option')
                    
                         
        else:
            print('you enter wrong otp')
            print('try again')
         
                 
                     
             
         
    elif role=='3':
         print('exiting')
         break

    else:
         print('choose correct option:')
         




        
