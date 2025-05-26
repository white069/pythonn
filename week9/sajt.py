#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 20 19:18:49 2025

@author: alex
"""

def ispisati(x):
    print("#===================================================================")
    print("#Zadatak ", x)
    
    
    print("#===================================================================")
    
#===================================================================
#Zadatak  1
#Написати функцију за поравнавање низа. Улазни низ може бити празан, а може садржати и ма коjи други 
#тип података укључуjући и низове коjи такође могу садржати низове до произвољне дубине.
def rek(niz):
    if niz==[]:
        return niz 
    elif type(niz[0])==list:
        return rek(niz[0]+ niz[1:]) 
    else: 
        return niz[:1] + rek(niz[1:])
#===================================================================    
    
    
#===================================================================
#Zadatak  2                   tehnici uradio sam ga sam ispravno
#Написати функцију коjа прима низ произвољно дубоко угнежђених низова броjевних вредности и задати броj,
# а враћа колико се укупно пута таj броj поjављуjе у улазном низу на произвољноj дубини.
def ponavljanje(niz, broj):
    if isinstance(niz, int):
        return 1 if niz == broj else 0
    
    if not niz:  # prazna lista
        return 0
    
    # Obrada prvog elementa i ostatka liste
    return ponavljanje(niz[0], broj) + ponavljanje(niz[1:], broj)
#===================================================================    
    
#===================================================================
#Zadatak  3
# def noviniz(niza,broj):
#     nizb=[]
#     for i in range(len(niza)):
#         if i+1<broj:
#             nizb.append(niza[i])
#         else:
#             ukupno=0
#             n=i 
#             while n>=i-broj+1:
#                 ukupno+=niza[n]
#                 n-=1
#             treba=ukupno//broj 
#             nizb.append(treba)
            
#     return nizb
#===================================================================    
    
#===================================================================
#Zadatak  4
# Броj 6174 коjи jе такође познат и као такозвана Капрекарова константа поседуjе jедно занимљиво своjство. Наиме, полазећи од произвољног четвороцифреног броjа код кога нису све цифре међусобно jеднаке (дакле изузимаjући ту 1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888 и 9999), или чак и од jедноцифреног, двоцифреног или троцифреног броjа коjи бива проширен водећим нулама до четворо- цифреног, и примењуjући на њега следећи алгоритам увек се долази до Капрекарове константе 6174:

# поређати цифре почетног броjа наjпре у неопадаjућем, а затим у нерастућем редоследу;
# одузети први од другог, односно мањи од већег тако добиjеног броjа;
# на добиjену разлику (по потреби проширену водећим нулама) применити исти низ операциjа. Примера ради, полазећи од броjа 3524:
# након прве итерациjе добиjа се броj: 5432 - 2345 = 3087;
# након друге итерациjе добиjа се броj: 8730 - 0378 = 8352;
# и наjзад, након треће итерациjе добиjа се броj: 8532 - 2358 = 6174. Понављањем поступка у свим даљим итерациjама добиjа се исти резултат jер jе 7641 - 1467 = 6174. Написати функциjу коjа враћа у колико се итерациjа долази до Капрекарове константе 6174 полазећи од произвољног улазног природног броjа мањег од 9999 кога не сачињаваjу четири идентичне цифре.
def pretvori(p,d,t,c):
    broj=0
    broj=broj*10+int(p) 
    broj=broj*10+int(d) 
    broj=broj*10+int(t) 
    broj=broj*10+int(c) 
    return broj
def konstanta(broj):
    iteracija=1
    broj=str(broj)
    while True:
        cifre=[i for i in broj]
        if len(cifre)<4:
            odg=4-len(cifre)
            for g in range(odg):
                cifre.insert(0,'0')
        
        cifre.sort()
        p1,d1,t1,c1=cifre
        p2,d2,t2,c2=cifre[::-1]
        manji=pretvori(p1,d1,t1,c1)
        veci=pretvori(p2,d2,t2,c2)
        broj=veci-manji
        if broj==6174:
            return iteracija 
        else:
            iteracija+=1
            broj=str(broj)
#===================================================================    
    
#===================================================================
#Zadatak  5
#Написати програм коjи за унето n исписуjе следећу фигуру:
# def ispisuje(n):
#     if n%2==0:
#         for i in range(1,(n//2)+1):
#             g=1
#             for _ in range(n):
#                 print((g if g<=i else i), end='',sep='')
#                 g+=1 
#             print()
#         for i in range((n//2),0,-1):
#             g=1 
#             for _ in range(n):
#                 print((g if g<=i else i), end='',sep='')
#                 g+=1 
#             print()
#     else:
#         for i in range(1,(n//2)+2):
#             g=1
#             for _ in range(n):
#                 print((g if g<=i else i), end='',sep='')
#                 g+=1 
#             print()
#         for i in range((n//2),0,-1):
#             g=1 
#             for _ in range(n):
#                 print((g if g<=i else i), end='',sep='')
#                 g+=1 
#             print()
#===================================================================    
    
#===================================================================
#Zadatak  6
# Написати програм коjи проверава да ли се jедна матрица налази унутар друге матрице. Уколико се налази,
#  одштампати da, у супротном одштампати ne.
# r1,k1=map(int,input('red i kolona prve matrice ').split())
# matrica1=[]
# for i in range(r1):
    
#     red=list(map(int,input('upisi jedan red matrice ').split()))
#     assert len(red)==k1, 'lose si upisao '
#     matrica1.append(red)
# r2,k2=map(int,input('red i kolona druge matrice ').split())
# matrica2=[]
# for i in range(r2):
    
#     red=list(map(int,input('upisi red ').split()))
#     assert len(red)==k2,'greska lose si upisao'
#     matrica2.append(red)
# manja=0
# veca=0
# if (r1,k1)>(r2,k2):
#     veca=matrica1 
#     manja=matrica2 
# else:
#     veca=matrica2 
#     manja=matrica1
# nalazi=True
# for i,v in manja:
#     for g in veca:
#         if v not in g:
#             nalazi=False 
# print(('da' if nalazi else 'ne'))
    
# r1, k1 = map(int, input('red i kolona prve matrice: ').split())
# matrica1 = []
# for _ in range(r1):
#     red = list(map(int, input().split()))
#     assert len(red) == k1, 'Pogrešan broj kolona'
#     matrica1.append(red)

# r2, k2 = map(int, input('red i kolona druge matrice: ').split())
# matrica2 = []
# for _ in range(r2):
#     red = list(map(int, input().split()))
#     assert len(red) == k2, 'Pogrešan broj kolona'
#     matrica2.append(red)

# def da_li_se_nalazi(velika, mala):
#     rv, kv = len(velika), len(velika[0])
#     rm, km = len(mala), len(mala[0])

#     for i in range(rv - rm + 1):
#         for j in range(kv - km + 1):
#             poklapa_se = True
#             for x in range(rm):
#                 for y in range(km):
#                     if velika[i + x][j + y] != mala[x][y]:
#                         poklapa_se = False
#             if poklapa_se:
#                 return True
#     return False

# if r1 >= r2 and k1 >= k2:
#     nalazi_se = da_li_se_nalazi(matrica1, matrica2)
# else:
#     nalazi_se = da_li_se_nalazi(matrica2, matrica1)

# print("da" if nalazi_se else "ne")
#===================================================================    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    