#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 14 12:15:34 2025

@author: alex
"""

def ispisati(x):
    print("#===================================================================")
    print("#Zadatak ", x)
    
    
    print("#===================================================================")
    
#imao sam 6 uradjena zadatka ali moj komp uradio klasicni crash i izgubio sma tih 6 zadatka
#===================================================================
#Zadatak  tamo neki nmp mozda 4
# mat1=int(input('poeni iz matisa 1 '))
# pro1=int(input('pro1 '))
# mat2=int(input('matis 2 '))
# pro2=int(input('pro 2 '))
# mat3=int(input('matis 3 '))
# pro3=int(input('pro 3 '))
# ucenik1=mat1+pro1 
# ucenik2=mat2+pro2 
# ucenik3=mat3+pro3
# def jednakost(pro1,pro2):
#     if pro1>pro2:
#         print(1)
#     elif pro1<pro2:
#         print(2)
#     else:
#         print(1)

# def jednakost2(pro2,pro3):
#     if pro2>pro3:
#         print(2)
#     elif pro2<pro3:
#         print(3)
#     else:
#         print(2)
# def jednakost3(pro1,pro3):
#     if pro1>pro3:
#         print(1)
#     elif pro1<pro3:
#         print(2)
#     else:
#         print(1)
        
# if mat1+pro1>mat2+pro2 and mat1+pro1>mat3+pro3:
#     print(1)
# elif ucenik1==ucenik2:
#     jednakost(pro1,pro2)
# elif ucenik1==ucenik3:
#     jednakost3(pro1,pro3)
# elif ucenik2>ucenik3:
#     print(2)
# elif ucenik2==ucenik3:
#     jednakost2(pro2,pro3)
# else:
#     print(3)"
#===================================================================   



#===================================================================
#Zadatak  7
# Задатак: Најбољи такмичари
# На такмичењу у пливању слободним стилом на 100 метара учествовало је 4 такмичара са старним бројевима
# од 1 до 4. Познати су резултати свих такмичара изражени у секундама. Написати програм који исписује
# стартне бројеве свих оних такмичара који су постигли најбољи резултат (најмање време) на том такмичењу.
# Улаз: У четири линије стандардног улаза налазе се четири реална броја из интервала [40, 100], сваки број
# у посебној линији. Бројеви представљају резултате такмичара редом од такмичара са стартним бројем 1 до
# такмичара са стартним бројем 4.
# Излаз: На стандардном излазу исписују се стартни бројеви такмичара који су постигли најбољи резултат.
# Сваки стартни број је у посебној линији, старни бројеви су приказани од најмањег до највећег.
# Пример
# Улаз
# 54.7
# 50.3
# 50.3
# 58.6
# Излаз
# 2
# 3

# takmicari=list(map(float,input('ta kmi ca ri ').split()))
# najbolji=min(takmicari)
# for i,v in enumerate(takmicari):
#     if v==najbolji:
#         print(i+1)
#===================================================================   
    
#===================================================================
#Zadatak  8
# Задатак: Најјефтинији за динар
# У једној продавници је у току акција у којој се купцима који купе три производа нуди да најјефтинији од та
# три производа добију за један динар. Напиши програм који одређује снижену цену три производа.
# Улаз: Са стандардног улаза уносе се три цела броја из интервала од 50 до 5000 који представљају цене у
# динарима за три купљена производа.
# Излаз: На стандардни излаз исписати један цео број који представља укупну снижену цену та три производа.
# Пример
# Улаз
# 2499
# 3599
# 899
# Излаз
# 6099
# proizvodi=list(map(int,input('cene tri proizvoda ').split()))
# proizvodi.remove(min(proizvodi))
# proizvodi.append(1)
# print(sum(proizvodi))
#===================================================================    
    
    
#===================================================================
#Zadatak  9
# Задатак: Просек скијаша
# На такмичењу у скијашким скоковима поред удаљености коју скакач прескочи оцењује се и стил скакача. Пет
# судија оцењују стил скакача оценама од 0 до 20. Затим се од свих добијених оцена избришу једна најмања и
# једна највећа. Коначна оцена стила скакача рачуна се као просек преосталих оцена. Напиши програм којим
# се на основу оцена 5 судија одређује коначна оцена стила скакача.
# Улаз: У свакој од пет линија стандардног улаза налази се по једна оцена стила скакача (цео број између 0 и
# 20) коју је скијаш добио од пет судија.
# Излаз: Коначна оцена стила скакача приказана на две децимале.
# Пример
# Улаз
# 3
# 5
# 0
# 1
# 5
# Излаз
# 3.00

# ocene=list(map(int,input('ocene pet smrdljivih sudja: ').split()))
# rad=(sum(ocene)-(min(ocene)+max(ocene)))/3 
# print(format(rad,'.2f'))
#===================================================================   
    
    
#===================================================================
#Zadatak  10
# Задатак: Врста троугла на основу углова
# Датa су три конвексна угла изражена у степенима и минутима. Написати програм којим се проверава да ли
# то могу бити углови троугла, и ако могу какав је то троугао у односу на углове (оштроугли, правоугли или
# тупоугли).
# Улаз: Са стандардног улаза уноси се шест целих бројева, сваки у посебној линији. Бројеви представљају
# три угла изражена у степенима. Подаци представљају исправно задате углове, степени и минути одређују
# исправно записане углове у интервалу од 0 степени и 0 минута, до 180 степени и 0 минута (минути су увек
# број између 0 и 59).
# Излаз: Једна линија стандарног излаза која садржи реч ostrougli, pravougli или tupougli, ако троугао са
# датим угловима постоји, у зависности од врсте троугла, или реч ne ако не постоји троугао са датим угловима.
# Пример
# Улаз
# 35
# 23
# 92
# 37
# 52
# 0
# Излаз
# tupougli

# min1=int(input('minut 1 '))
# sek1=int(input('sekund 1 '))
# min2=int(input('min 2 '))
# sek2=int(input('sek2 '))
# min3=int(input('min3 '))
# sek3=int(input('sek3 '))
# if 1<sek1+sek2+sek3<=118:
#     min4=1 
# elif sek1+sek2+sek3<=177:
#     min4=2 
# min4=0
# trougao=[min1,min2,min3,min4]
# if sum(trougao)>180:
#     print('NE POSTOJI!!!!!!!!!!!!!!')
# elif 90<sum(trougao):
#     print('ovaj ugoa je tup mamu mu jebem')
# elif 90==sum(trougao):
#     print('ovaj ugao je tacan i prav')
# else:
#     print('ugao je vrlo ostar ')
#===================================================================    
    
#===================================================================
#Zadatak  11
# Задатак: Растојање тачка правоугаоник
# Деца се играју јурке у школском дворишту правоугаоног облика и око њега. Правила игре су таква да је
# ученик безбедан када се ухвати за ограду. Напиши програм који одређује колико је најмање растојање које
# Ђока треба да претрчи да би био безбедан (он се у почетку може налазити и у дворишту и ван њега).
# Улаз: Са стандардног улаза учитава се 6 реалних бројева (сваки у посебном реду):
# • x0, y0 (0 ≤ x0, y0 < 1000) - координате доњег левог темена правоугаоника који представља школско
# двориште у координатном систему постављеном тако да су ивице правоугаоника паралелне координатним осама.
# • x1, y1 (x0 < x1 ≤ 1000, y0 < y1 ≤ 1000) координате горњег десног темена правоугаоника.
# • x, y (0 ≤ x0, y0 ≤ 1000) - координате тачке на којој се налази Ђока.
# Излаз: На стандардни излаз исписати један реалан број - најкраће растојање Ђоке до ограде у метрима
# (допуштена је толеранција је један центиметар, тј. резултат исписати заокружен на две децимале).
# Пример 1
# Улаз
# 100
# 100
# 200
# 200
# 50
# 170
# Излаз
# 50.00
# Пример 2
# Улаз
# 100
# 100
# 200
# 200
# 50
# 300
# Излаз
# 111.80
# x0=int(input('x koordinata donjeg levog ugla ograde: '))
# y0=int(input('y koordinata donjeg levog ugla ograde: '))
# x1=int(input('x koordinata gornjeg desnog ugla ograde: '))
# y1=int(input('y koordinata gornjeg desnog ugla ograde: '))
# djx=int(input('x koordinata Djoleta: '))
# djy=int(input('y koordinata Djoleta: '))

# if djx>=x0 and djy>=y0 and djx<=x1 and djy<=y1:
#     xmin1=abs(djx-x0)
#     xmin2=abs(x1-djx)
#     xmin0=min(xmin1,xmin2)
#     ymin1=abs(djy-y0)
#     ymin2=abs(y1-djy)
#     ymin0=min(ymin1,ymin2)
#     najkrace=min(xmin0,ymin0)
#     print(format(najkrace,'.2f'))
# else:
# ok dovde je moj kod i ovo gore mi je tacno kada je djole unutra ograde, ali kad je spolja trebamo proveriti
#da li x ravnopravno sa x1 i xo, tako i sa y i gledati ako nije dijagonal
#mrzi me to da uradim ali znam 
# import math

# x0 = float(input())
# y0 = float(input())
# x1 = float(input())
# y1 = float(input())
# x = float(input())
# y = float(input())

# # ako je Djoka unutar pravougaonika
# if x0 <= x <= x1 and y0 <= y <= y1:
#     dist = min(x - x0, x1 - x, y - y0, y1 - y)
# # ako je Djoka levo ili desno, ali vertikalno u visini pravougaonika
# elif y0 <= y <= y1:
#     if x < x0:
#         dist = x0 - x
#     else:
#         dist = x - x1
# # ako je Djoka iznad ili ispod, ali horizontalno poravnat
# elif x0 <= x <= x1:
#     if y < y0:
#         dist = y0 - y
#     else:
#         dist = y - y1
# # ako je Djoka u uglu, koristi se Pitagorina teorema
# else:
#     if x < x0 and y < y0:
#         dist = math.hypot(x0 - x, y0 - y)
#     elif x > x1 and y < y0:
#         dist = math.hypot(x - x1, y0 - y)
#     elif x < x0 and y > y1:
#         dist = math.hypot(x0 - x, y - y1)
#     else:
#         dist = math.hypot(x - x1, y - y1)

# print(f"{dist:.2f}")
#===================================================================    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
