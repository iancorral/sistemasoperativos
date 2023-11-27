def mes():
    if num==1:
        return meses [0]
    elif num==2:
        return meses [1]
    elif num==3:
        return meses [2]
    elif num==4:
        return meses[3]
    elif num==5:
        return meses[4]
    elif num==6:
        return meses[5]
    elif num==7:
        return meses[6]
    elif num==8:
        return meses [7]
    else:
        return meses [8]
#main
num=int(input("Introduce el número de tu mes: "))
meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre"]
print(F"Tu mes es {mes()}")