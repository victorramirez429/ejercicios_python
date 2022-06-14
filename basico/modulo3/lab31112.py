year = int(input("Introduce un año: "))

if not(year % 4 ==0):
    print ('Año comun')
elif not (year % 100 == 0):
    print ('Año bisiesto')
elif not (year % 400 == 0):
    print ('Año comun')
if (year == 1558):
        print ('No dentro del periodo del calendario Gregoriano')
else:
    print ('Año bisiesto')