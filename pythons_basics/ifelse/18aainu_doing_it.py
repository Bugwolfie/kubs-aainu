print("heya welcome to driving eligibility test!!")
gender = input("please enter your gender")
if gender == "female":
    print("ohh papa ki pari \n pair se brake ni lgana beta")
else:
    print("sidhe khade rho")
age = int(input("api age bta be =  "))
if 70 > age > 18:
    print("ummm chala le..daru pike mat chalana bas")
elif 70<age<100:
    print("mat chalaiye na please \n bhagwan ko smaran kijiye is umar me")
elif age<18:
    print("kan ke niche padega ek \n gadi chalyega ye \n pogo dekh pogo")
elif age==18:
    print("office ajao beta \n bhot par nikle hai tumare")
else:
    print("maar khani hai...nikal")