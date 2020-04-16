#Temperature comverter from celcius to fahrenheit


deg = int(input("Enter 1 for cel to fah;  2 for fah to cel"))
if deg == 1:
    cel = int(input("Enter a temp in Celsius"))
    fah = (cel - 9 / 5) + 32
    print('%.2f Celsius is: %.2f Fahrenheit' %(cel, fah))
else:
    fah = int(input("Enter a temp in Fahrenheit"))
    cel = (fah - 32) * 5/9
    print('%.2f Fahrenheit is: %.2f Celsius' %(fah, cel))
    