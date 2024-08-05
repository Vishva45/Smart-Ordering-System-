class intro:
    def topic(self):
        title="   SMART ORDERING SYSTEM FOR ELECTRONIC GADGETS"
        design="******************************************"
        print(title.center(100),"\n",design.center(100))
        
top=intro()
top.topic()

class information:
    def __init__(self,logg):
        self.logg=logg
        if(self.logg.lower()=="login" or self.logg=="Login"):
            mail=input("1.Email \n2.Mobile number \nEnter 1 or 2:")
            if(mail=="1"):
                name=input("\nUsername:")
                email=input("Enter Email id:")
                password=input("Enter password:")
            elif(mail=="2"):
                phone=input("\nEnter Mobile Number:")
                if(len(phone)==10):
                    import random
                    otp=random.randrange(1000,10000)
                    print("Generate OTP:",otp)
                    num=int(input("Enter OTP:"))
                    if(num==otp):   print("Access Granted")
                    else:   print("Access Denied")
                else:   print("Please Enter Your Phone Number Correctly !")
            else:   print("Sorry ! Only above",log,"Process")
                
        elif(self.logg.lower()=="signup" or self.logg=="Signup"):
            sign=input("1.Email \n2.Mobile number \nEnter 1 or 2:")
            if(sign=="1"):
                name=input("Username:")
                email=input("Enter Email id:")
                password=input("Enter password:")
                password2=input("re-Enter password ")
                if(password==password2):    print("Signup Successfully")
                else:   print("Invalid password")
            elif(sign=="2"):
                phone=input("Enter Mobile Number:")
                if(len(phone)==10):
                    import random
                    otp=random.randrange(1000,10000)
                    print("Generate OTP:",otp)
                    num=int(input("Enter OTP:"))
                    if(num==otp):   print("Access Granted")
                    elif(num!=otp): print("Access Denied")
                else:   print("Please Enter Your Phone Number Correctly !")
            else:   print("Sorry ! Only above",log,"Process")
        elif(self.logg.lower()=="skip" or self.logg=="Skip"):
            pass
        else:   print("Please Enter the Process Correctly")

log=input("Login or Signup or Skip:")               
info=information(log)
    
class profile(information):
    def __init__(self,det):
        self.det=det
        if(self.det.lower()=="yes" or self.det=="Yes"):
            name=input("Enter Name:")
            email=input("Enter email id:")
            phone=input("Enter Phone Number:")
            location=input("Enter Your Location:")
            dob=input("Enter DOB:")
            address=input("Current address:")
            if(len(phone)==10):
                return 
            else:   print("Please Enter Phone number Correctly")
        elif(self.det.lower=="later" or self.det=="Later"):
            pass

det=input("\nEdit Profile Yes/Later:")
pro=profile(det)

class product():
    def __init__(self,product):
        self.product=product
        if(self.product.lower()=="smartphones" or self.product=="Smartphones"):
            print("\nSamsung / Redmi / Poco / Iphone ")
            phone=input("Which company Phones you prefer to buy?")
            if(phone.lower()=="samsung" or phone=="Samsung"):
                model=input("Enter model name: ")
                ram=input("RAM/ROM: 4/64 , 6/128 ,8/256  \nEnter your Preference: ")
                if(ram=="4/64"):    print("Samsung",model,"Prize: ₹54,999")
                elif(ram=="6/128"):     print("Samsung",model,"Prize: ₹64,999")
                elif(ram=="8/264"):     print("Samsung",model,"Prize: ₹74,999")
                else:     print("Sorry ! Not available Your preference")
            elif(phone.lower()=="redmi" or phone=="Redmi"):
                model=input("Enter model name: ")
                ram=input("RAM/ROM: 4/64 , 6/128 ,8/256  \nEnter your Preference: ")
                if(ram=="4/64"):    print("Redmi",model,"Prize: ₹13,999")
                elif(ram=="6/128"):     print("Redmi",model,"Prize: ₹19,999")
                elif(ram=="8/264"):     print("Redmi",model,"Prize: ₹23,999")
                else:     print("Sorry ! Not available Your preference")
            elif(phone.lower()=="poco" or phone=="Poco"):
                model=input("Enter model name: ")
                ram=input("RAM/ROM: 4/64 , 6/128 ,8/256  \nEnter your Preference: ")
                if(ram=="4/64"):    print("Poco",model,"Prize: ₹16,999")
                elif(ram=="6/128"):     print("Poco",model,"Prize: ₹20,999")
                elif(ram=="8/264"):     print("Poco",model,"Prize: ₹22,999")
                else:     print("Sorry ! Not available Your preference")
            elif(phone.lower()=="iphone" or phone=="Iphone"):
                model=input("Enter model name: ")
                ram=input("RAM/ROM: 4/64 , 6/128 ,8/256  \nEnter your Preference: ")
                if(ram=="4/64"):    print("Iphone",model,"Prize: ₹1,12,999")
                elif(ram=="6/128"):     print("Iphone",model,"Prize: ₹1,22,999")
                elif(ram=="8/264"):     print("Iphone",model,"Prize: ₹1,32,999")
                else:     print("Sorry ! Above Preference Only Available")
            else:   print("Sorry ! Above product Only Available")
                
        elif(self.product.lower()=="laptops" or self.product=="Laptops"):
            print("\nHP / DELL / ASUS / LENOVO ")
            lap=input("Which company Laptops you prefer to buy?")
            if(lap.lower()=="hp" or lap=="Hp" or lap.upper()=="HP"):
                model=input("\nEnter Model Name:")
                gen=input("Processor/Gen: i7/12 , i5/11 ,i3/10 \nEnter Your Preference: ")
                if(gen=="i7/12"):   print("\nHP Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹75,999 ")
                elif(gen=="i5/11"):     print("\nHP Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹65,999 ")
                elif(gen=="i3/10"):     print("\nHP Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹55,999 ")
                else:   print("Sorry ! Not Available Your preference")
            elif(lap.lower()=="dell" or lap=="Dell" or lap.upper()=="DELL"):
                model=input("\nEnter Model Name:")
                gen=input("Processor/Gen: i7/12 , i5/11 ,i3/10 \nEnter Your Preference: ")
                if(gen=="i7/12"):   print("\nDELL Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹67,999 ")
                elif(gen=="i5/11"):     print("\nDELL Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹59,999 ")
                elif(gen=="i3/10"):     print("\nDELL Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹55,999 ")
                else:   print("Sorry ! Not Available Your preference")
            elif(lap.lower()=="asus" or lap=="Asus" or lap.upper()=="ASUS"):
                model=input("\nEnter Model Name:")
                gen=input("Processor/Gen: i7/12 , i5/11 ,i3/10 \nEnter Your Preference: ")
                if(gen=="i7/12"):   print("\nASUS Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹85,999 ")
                elif(gen=="i5/11"):     print("\nASUS Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹77,999 ")
                elif(gen=="i3/10"):     print("\nASUS Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹69,999 ")
                else:   print("Sorry ! Not Available Your preference")
            elif(lap.lower()=="lenovo" or lap=="Lenovo" or lap.upper()=="LENOVO"):
                model=input("\nEnter Model Name:")
                gen=input("Processor/Gen: i7/12 , i5/11 ,i3/10 \nEnter Your Preference: ")
                if(gen=="i7/12"):   print("\nLENOVO Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹75,999 ")
                elif(gen=="i5/11"):     print("\nLENOVO Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹65,999 ")
                elif(gen=="i3/10"):     print("\nLENOVO Laptop",model,"\nProcessor/Gen:",gen,"\nPrize: ₹55,999 ")
                else:   print("Sorry ! Above Preference Only Available")
            else:   print("Sorry ! Above product Only Available")
            
        elif(self.product.lower()=="smartwatches" or self.product=="Smartwatches"):
            print("\nFireBolt / FitBit / Samsung / Apple")
            watch=input("which company Smartwatches you prefer to buy? ")
            if(watch.lower()=="firebolt" or watch=="Firebolt" or watch=="FireBolt"):
                model=input("Enter Model Name: ")
                print("\nFireBolt",model,"\nPrize: ₹2,499")
            elif(watch.lower()=="fithub" or watch=="Fithub" or watch=="FitHub"):
                model=input("Enter Model Name: ")
                print("\nFitHub",model,"\nPrize: ₹4,499")
            elif(watch.lower()=="samsung" or watch=="Samsung" or watch=="SAMSUNG"):
                model=input("Enter Model Name: ")
                print("\nSamsung",model,"\nPrize: ₹10,999")
            elif(watch.lower()=="apple" or watch=="Apple" or watch=="APPLE"):
                model=input("Enter Model Name: ")
                print("\nApple",model,"\nPrize: ₹39,999")
            else:   print("Sorry ! Above product Only available")
            
        elif(self.product.lower()=="headphones" or self.product=="Headphones"):
            print("\nSony / Bose / Apple / Realme ")
            headph=input("which company Headphones you prefer to buy?")
            if(headph.lower()=="sony" or headph=="Sony" ):
                 model=input("Enter Model Name: ")
                 print("\nSony",model,"\nPrize: ₹1,999")
            elif(headph.lower()=="bose" or headph=="Bose" ):
                 model=input("Enter Model Name: ")
                 print("\nBose",model,"\nPrize: ₹3,499")
            elif(headph.lower()=="apple" or headph=="Apple" ):
                 model=input("Enter Model Name: ")
                 print("\nApple",model,"\nPrize: ₹15,499")
            elif(headph.lower()=="realme" or headph=="Realme" ):
                 model=input("Enter Model Name: ")
                 print("\nRealme",model,"\nPrize: ₹2,499")
            else:   print("Sorry ! Above product Only available")

        elif(self.product.lower()=="tv" or self.product=="TV" or self.product=="Tv"):
            print("\nLG / Panasonic / Philips ")
            tele=input("which company TVs you prefer to buy?")
            if(tele.lower()=="lg" or tele=="Lg" or tele=="LG"):
                 model=input("Enter Model Name: ")
                 inch=input("Inches: 32 / 55 / 75 \nEnter Your preference: ")
                 if(inch=="32"):    print("\nLG ",model,"\nPrize: ₹18,999")
                 elif(inch=="55"):  print("\nLG ",model,"\nPrize: ₹25,999")
                 elif(inch=="75"):  print("\nLG ",model,"\nPrize: ₹32,999")
                 else: print("Above preference Only Available")
            elif(tele.lower()=="panasonic" or tele=="Panasonic" or tele=="PANASONIC"):
                 model=input("Enter Model Name: ")
                 inch=input("Inches: 32 / 55 / 75: \nEnter Your preference: ")
                 if(inch=="32"):    print("\nPanasonic ",model,"\nPrize: ₹25,999")
                 elif(inch=="55"):  print("\nPanasonic ",model,"\nPrize: ₹34,999")
                 elif(inch=="75"):  print("\nPanasonic ",model,"\nPrize: ₹41,999")
                 else: print("Above preference Only Available")
            elif(tele.lower()=="philips" or tele=="Philips" or tele=="PHILIPS"):
                 model=input("Enter Model Name: ")
                 inch=input("Inches: 32 / 55 / 75 \nEnter Your preference: ")
                 if(inch=="32"):    print("\nPhilips ",model,"\nPrize: ₹25,999")
                 elif(inch=="55"):  print("\nPhilips ",model,"\nPrize: ₹34,999")
                 elif(inch=="75"):  print("\nPhilips ",model,"\nPrize: ₹41,999")
                 else: print("Above preference Only Available")
            else:   print("Sorry ! Above product Only available")
            
        elif(self.product.lower()=="camera" or self.product=="Camera" or self.product=="CAMERA"):
            print("\nCanon / Nikon / Sonic")
            cam=input("which company Camera you prefer to buy?")
            if(cam.lower()=="canon" or cam=="Canon" or cam=="CANON"):
                model=input("Enter Model Name: ")
                print("\nCanon ",model,"\nPrize: 15,999")
            elif(cam.lower()=="nikon" or cam=="Nikon" or cam=="NIKON"):
                model=input("Enter Model Name: ")
                print("\nNikon ",model,"\nPrize: 23,999")
            elif(cam.lower()=="sony" or cam=="Sony" or cam=="SONY"):
                model=input("Enter Model Name: ")
                print("\nSony ",model,"\nPrize: 33,999")   

prod=input("\nSmartphones \nLaptops \nSmartwatches \nHeadphones \nTV \nCamera \nWhat you want to Buy?")
mob=product(prod)

class payment():
    def __init__(self,meth):
        self.meth=meth
        if(self.meth.lower()=="gpay" or self.meth=="Gpay"):
            trans=input("Enter UPI id:")
            import random
            upi=random.randrange(1000000,10000000)
            print("Transaction ID:",upi)
            id=int(input("Enter Transaction Id: "))
            if(id==upi): print("\nPayment received succesfully ! \nWithin Two days product will be delivered \nif any problem delivered product Contact ph.no: 7854123696 \nThank You !!!")
            else:       print("Sorry ! Payment Cancelled")
        elif(self.meth.lower()=="phonepe" or self.meth=="Phonepe"):
            trans=input("Enter UPI id:")
            import random
            upi=random.randrange(100000,10000000)
            print("Transaction ID:",upi)
            id=int(input("Enter Transaction Id: "))
            if(id==upi): print("\nPayment received succesfully ! \nWithin Two days product will be delivered \nif any problem delivered product Contact ph.no: 7854123696 \nThank You !!!")
            else:   print("Sorry ! Payment Cancelled")
        elif(self.meth.lower()=="paytm" or self.meth=="Paytm"):
            trans=input("Enter UPI id:")
            import random
            upi=random.randrange(1000000,10000000)
            print("Transaction ID:",upi)
            id=int(input("Enter Transaction Id: "))
            if(id==upi): print("\nPayment received succesfully ! \nWithin Two days product will be delivered \nif any problem delivered product Contact ph.no: 7854123696 \nThank You !!!")
            else:   print("Sorry ! Payment Cancelled")
        elif(self.meth.lower()=="cancel" or self.meth=="Cancel"):
            print("Order Something ! ")
        else:   print("Only Use Above Payment Method")
                
method=input("\nGpay / Phonepe / Paytm / Cancel \nEnter Your Payment method: ")
paid=payment(method)

        
        
        












