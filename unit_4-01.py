#created by Matthew Walsh
#created for ICS3U
#created on oct 2017
#converts celcius to fehrenheit

def convert_to_fahrenheit(user_input):
    
    fahrenheit = (1.8 * user_input) + 32
    print("The temperature is " + str(fahrenheit) + " degrees fahrenheit")

user_input = input('Enter tempurature in degree celcius: ')
convert_to_fahrenheit(user_input)
