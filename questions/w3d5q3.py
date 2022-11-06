class Temperatures:
    

    def celcius_convertor(self,temp):
        self.temp = temp
        temp_celcius = temp*5/9-32
        print(f"temperature at your place in celcius is {temp_celcius} degree C")
        
    def fahrenheit_convertor(self,temp):
        self.temp = temp
        temp_fahrenheit = temp*9/5+32
        print(f"temperature at your place in fahrenheit is {temp_fahrenheit} degree F")



#driver code

sgnr = Temperatures()
sgnr.celcius_convertor(102)
sgnr.fahrenheit_convertor(34)

        