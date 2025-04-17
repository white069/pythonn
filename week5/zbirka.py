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
    
<<<<<<< HEAD
    
#===================================================================
#Zadatak  19
# Задатак: Берза
# Трговац на берзи је током једне радне недеље сваки дан или остваривао зараду или је губио новац. Од свих
# дана у којима је нешто зарадио, одредити дан у коме је најмање зарадио и вредност коју је тог дана зарадио
# (ако је више таквих дана, пријавити први) или пријавити да је свих дана губио новац.
# Улаз: Са стандардног улаза уноси се 5 целих бројева из интервала [−10000, 10000] (износи које је трговац
# остварио у понедељак, уторак, среду, четвртак и петак), сваки у посебном реду.
# Излаз: Ако је трговац у неком дану остварио зараду (износ је строго већи од нуле), на стандардни излаз
# у првом реду исписати најмањи износ зараде који је остварен током недеље и у другом реду ознаку дана
# (PON, UTO, SRE, CET или PET) у коме је остварен тај најмањи профит. Ако ниједан дан није остварена зарада,
# исписати ред који садржи само карактер -.
# Пример 1
# Улаз
# 3200
# -420
# -10
# 1350
# 5670
# Излаз
# 1350
# CET
# Пример 2
# Улаз
# -4700
# -360
# -1000
# -1550
# -3245
# Излаз
# -

# pon=int(input('koliko je trgovac zaradio u ponedeljak:'))
# uto=int(input('a u utorak:'))
# sre=int(input('a u sredu:'))
# cet=int(input('a u cetvrtak:'))
# pet=int(input('a u petak:'))
# dani=[pon,uto,sre,cet,pet]
# zarada=[i for i in dani if i>0]
# if len(zarada)>0:
#     minimalac=min(zarada)

#     if minimalac==pon:
#         print(pon,'pon')
#     elif minimalac==uto:
#         print(uto,'uto')
#     elif minimalac==sre:
#         print(sre,'sre')
#     elif minimalac==cet:
#         print(cet,'cet')
#     elif minimalac==pet:
#         print(pet,'pet')
# else:
#     print('-')
#===================================================================  
    
    
#===================================================================
#Zadatak  20
# Задатак: Чудно радно време
# Паја има обичај да да у сред дана напусти радно место и оде негде на кратко. Због тога је објавио необично
# радно време, које се састоји од 4 интервала, са три паузе (четворократно радно време). Напиши програм
# који проверава да ли Паја ради у тренутку t. Сматра се да сваки од ових интервала садржи свој почетак, а не
# садржи свој крај.
# Улаз: На стандардном улазу у прва четири реда је задат по један интервал Пајиног радног времена. Сваки
# интервал је задат сатом и минутом почетка и сатом и минутом краја (цели бројеви s1, m1, s2, m2 раздвојени
# размаком, 0 ≤ si ≤ 23, 0 ≤ mi ≤ 59, за i ∈ {1, 2}). Интервали су дисјунктни и поређани хронолошки. У
# петом реду стандардног улаза налазе се цели бројеви S, M раздвојени зарезом, 0 ≤ S ≤ 23, 0 ≤ M ≤ 59,
# који представљају тренутак t, за који се проверава да ли је у Пајином радном времену.
# Излаз: На стандардни излаз написати da ако је t у Пајином радном времену тј. ne у супротном.
# Пример 1
# Улаз
# 9 0 11 30
# 12 15 14 45
# 15 0 17 0
# 17 15 19 0
# 14 45
# Излаз
# ne
# s1,m1,s10,m10=map(int,input('sat i minut prvog radnog vremena: ').split())
# s2,m2,s20,m20=map(int,input('sat i minut drugog radnog vremena: ').split())
# s3,m3,s30,m30=map(int,input('sat i minut treceg radnog vremena: ').split())
# s4,m4,s40,m40=map(int,input('sat i minut cetvrtog radnog vremena: ').split())
# s,m=map(int,input('sat i vreme zeljenog stanja').split())
# def rad(s1,s2,s):
#     return s1<s<s2
# def jednako(s,s2,m,m2):
#     if s==s2:
#         if m<m2:
#             return True
#         elif m>=m2:
#             return False
# def blizu(s,s1,m,m1):
#     if s==s1:
#         if m<m1:
#             return False
#         else:
#             return True

        
# if rad(s1,s10,s) or rad(s2,s20,s) or rad(s3,s30,s) or rad(s4,s40,s):
#     print('da')
# elif jednako(s,s10,m,m10) or jednako(s,s20,m,m20) or jednako(s,s30,m,m30) or jednako(s,s4,m,m40):
#     print('da')
# elif blizu(s,s1,m,m1) or blizu(s,s2,m,m2) or blizu(s,s3,m,m3) or blizu(s,s4,m,m4):
#     print('da')
# else:
#     print('ne')
#===================================================================   
    
#===================================================================
#Zadatak  21
# Задатак: Постоји ли троугао датих дужина страница
# Написати програм којим се проверава да ли постоји троугао са датим дужинама страница.
# Улаз: На стандарном улазу налазе се три реална позитивна броја, сваки у посебној линији. Бројеви представљају дужине страница a, b, c.
# Излаз: Једна линија стандарног излаза која садржи реч da ако постоји троугао, иначе садржи реч ne.
# Пример
# Улаз
# 4.3
# 5.4
# 6.7
# Излаз
# da
#sta oni hocu je da jednu promenljivu stavim na false i ako neki uslov ispunjava postavim je na true
=======
#===================================================================
#Zadatak  12
# Задатак: Позиција највећег угла троугла
# Дата су два угла разностраничног троугла у степенима, минутима и секундама. Одредити који од углова
# троугла је највећи, први по редоследу уноса, други по редоследу уноса или трећи, одређен у програму.
# Улаз: У свакој од шест линија стандардног улаза налази се по један цео број. Бројеви редом представљају
# степене, минуте (мање од 60) и секунде (мање од 60), прво једног, па другог угла троугла. Збир дата два угла
# је мањи од 180 степени.
# Излаз: У једној линији стандардног излаза исписати број 1, 2 или 3.
# Пример
# Улаз
# 75
# 30
# 14
# 23
# 15
# 45
# Излаз
# 3

# stp1=int(input('stepen prvog ugla '))
# min1=int(input('minut prvog ugla '))
# sek1=int(input('sekund prvog ugla '))
# stp2=int(input('stepen drugog ugla '))
# min2=int(input('minut drugog ugla '))
# sek2=int(input('sekund drugog ugla '))

# stp3=179-(stp1+stp2)
# min12=min1+min2
# if min12>=60:
#    min12= 118-min12
#    stp3-=1
# min3=59-min12
# sek12=sek1+sek2
# if sek12>=60:
#     sek12=118-sek12
#     min3-=1
# sek3=59-sek12
# def jednakost(min1,min2,sek1,sek2):
#     if min1>min2:
#         print(1)
#     elif min2>min1:
#         print(2)
#     else:
#         if sek1>sek2:
#             print(1)
#         else:
#             print(2)
# def jednakost1(min1,min2,sek1,sek2):
#     if min1>min2:
#         print(2)
#     elif min2>min1:
#         print(3)
#     else:
#         if sek1>sek2:
#             print(2)
#         else:
#             print(3)


# if stp1>stp2 and stp1>stp3:
#     print(1)
# elif stp2>stp1 and stp2>stp3:
#     print(2)
# elif stp3>stp1 and stp3>stp2:
#     print(3)
# elif stp1>stp2 and stp1==stp3:
#     if min1>min3:
#         print(1)
#     elif min3>min1:
#         print(3)
#     else:
#         if sek1>sek3:
#             print(1)
#         else:
#             print(3)
# elif stp1>stp3 and stp1==stp2:
#     jednakost(min1,min2,sek1,sek2)
# else:
#     jednakost1(min2,min3,sek2,sek3)
# sada kada sam ga uradio, vidim da je ovo najgori moguci kod ikada stvoren. 
# Umesto da mi fja radi jedan posao on pravo ide ka onome sto treba, sto zauzvrat nema fleksibilnost
# mogao sam kao da napravim da fja vraca 1 ako je prva veca, 2 ako je druga pa preko toga da kazem sta je vece
# ili jos bolje mogao sam da pretvorim sve u sekunde pa da to uporedim
#===================================================================   
    
#===================================================================
#Zadatak  13
# Задатак: Најближи просеку
# Написати програм који за четири дата броја одређује који је од та четри броја најближи аритметичкој средини датих бројева (ако су два броја једнако близу исписати први).
# Улаз: У четири линије стандардног улаза налазе се четири реална броја.
# Излаз: У једној линији стандардног излаза приказати један од унетих реалних бројева, на две децимале,
# најближи њиховој аритметичкој средини.
# Пример
# Улаз
# 24.3
# 20.2
# 23.5
# 22.7
# Излаз
# 22.70

# a=float(input('prvi broj '))
# b=float(input('drugi broj '))
# c=float(input('treci broj '))
# d=float(input('cetvrti broj '))
# sredina=(a+b+c+d)/4
# a1=abs(sredina-a)
# b1=abs(sredina-b)
# c1=abs(sredina-c)
# d1=abs(sredina-d)
# najblizi=min(a1,b1,c1,d1)
# if najblizi==a1:
#     print(format(a,'.2f'))
# elif najblizi==b1:
#     print(format(b,'.2f'))
# elif najblizi==c1:
#     print(format(c,'.2f'))
# else:
#     print(format(d,'.2f'))
#===================================================================

#===================================================================
#Zadatak  14
# Задатак: Први и други максимум
# Написати програм којим се одређују највећа два различита броја од пет датих целих бројева.
# Улаз: На станадардном улазу налазе се 5 целих бројева, сваки у посебној линији.
# Излаз: Прва линија стандарног излаза садржи највећи број од датих 5 бројева. Друга линија стандардног
# излаза садржи други по величини цео број од датих 5 бројева. Aко су сви унети бројеви једнаки друга линија
# треба да садржи само знак ‘-’.
# Пример 1
# Улаз
# 2
# 7
# -4
# 7
# 3
# Излаз
# 7
# 3
# Пример 2
# Улаз
# 12
# 12
# 12
# 12
# 12
# Излаз
# 12

# brojevi=list(map(int,input('5 brojeva: ').split()))
# maks1=max(brojevi)
# print(maks1)
# skup=set(brojevi)
# skup.remove(maks1)
# if len(skup)==0:
#     print('-')
# else: 
#     maks2=max(skup)
#     print(maks2)
#===================================================================


#===================================================================
#Zadatak  15
# Задатак: Аутомобил у вођству
# Три аутомобила крећу са стартне позиције у тренуцима 0 ≤ t1 ≤ t2 ≤ t3 константним брзинама v1, v2 и
# v3. Приказати стартне бројеве аутомобила који су на водећој позицији у тренутку t (t ≥ 0). Ако ни један
# аутомобил још није кренуо, сва три су у водећој позицији.
# Улаз: Са стандардног улаза учитава се седам целих бројева, сваки у засебној линији t1, v1, t2, v2, t3, v3, t где
# t1, t2, t3, t представљају времена у секундама, а v1, v2, v3 брзине у метрима по секунди.
# Излаз: На стандардни излаз исписати један или више целих бројева (сваки у посебном реду) који представљају редне бројеве аутомобила (1, 2 или 3) који су на водећој позицији. Ако је више аутомобила истовремено
# у вођству, њихове редне бројеве исписати у растућем редоследу.
# Пример
# Улаз
# 10
# 5
# 5
# 4
# 0
# 2
# 30
# Излаз
# 1
# 2

# t1=int(input('startna pozicija auta u trenutku: '))
# v1=int(input('brzina tog auta: '))
# t2=int(input('startna pozicija drugog auta: '))
# v2=int(input('brzina tog auta: '))
# t3=int(input('startna pozicija treceg auta: '))
# v3=int(input('brzina tog auta: '))
# t=int(input('zeljeno vreme posmatranja: '))

# s1 = (t - t1) * v1 if t >= t1 else 0
# s2 = (t - t2) * v2 if t >= t2 else 0
# s3 = (t - t3) * v3 if t >= t3 else 0
# najvise = max(s1, s2, s3)

# if s1 == najvise:
#     print(1)
# if s2 == najvise:
#     print(2)
# if s3 == najvise:
#     print(3)
#===================================================================


#===================================================================
#Zadatak  16
# Задатак: Јутарње температуре
# Дате су јутарње температуре за 4 дана T1, T2, T3 и T4. Одредити број дана од та 4 дана када је јутарња
# температура била испод просечне температуре за та 4 дана.
# Улаз: Ca стандардног улаза се учитавају четири реална броја (сваки је у посебној линији) који представљају
# јутарње температуре за четири дана.
# Излаз: У првој линији стандардног улаза исписује се просечна температура за та четири дана, заокружена
# на две децимале.
# У другој линији стандардног излаза исписује се број дана када је температура била испод просечне.
# Пример
# Улаз
# 27.3
# 20.2
# 23.5
# 21.8
# Излаз
# 23.20
# 2
# t1=float(input('temperatura tog dana: '))
# t2=float(input('temp nar dan '))
# t3=float(input('temp nar nar '))
# t4=float(input('temp nar nar nar '))
# sredina=(t1+t2+t3+t4)/4
# print(format(sredina,'.2f'))
# i=0
# if t1<sredina:
#     i+=1
# if t2<sredina:
#     i+=1
# if t3<sredina:
#     i+=1
# if t4<sredina:
#     i+=1
# print(i)
#===================================================================

#===================================================================
#Zadatak  17
# Задатак: Квалификациони праг
# Ако се знају поени 4 такмичара и квалификациони праг на такмичењу, одредити колико такмичара је освојило довољно поена и квалификовало се у следећи круг такмичења, а колики је просек поена оних који се
# нису квалификовали.
# Улаз: У пет линија стандардног улаза налазе се пет целих бројева из интервала [0, 100], сваки број у посебној
# линији. Прва четири броја представљају освојене поене такмичара, а пети број је квалификациони праг.
# Излаз: На стандардном излазу исписује се:
# • у првој линији број такмичара који су се квалификовали,
# • у другој линији просек поена (на две децимале) за групу такмичара која се није квалификовала, а у
# случају да су се сви квалификовали у другој линији исписати знак ‘-’.
# Пример
# Улаз
# 0
# 30
# 2
# 99
# 30
# Излаз
# 2
# 1.00
# poen1=int(input('poeni ostvareni od strane prvog takmicara:'))
# poeni2=int(input('-||-:'))
# poeni3=int(input('-||-:'))
# poeni4=int(input('-\\-:'))
# kvalf=int(input('kvalifikacioni poeni:'))
# i=0
# neuspeli=[]
# g=0
# if poen1>=kvalf:
#     i+=1
# else:
#     neuspeli.append(poen1)
#     g+=1
# if poeni2>=kvalf:
#     i+=1
# else:
#     neuspeli.append(poeni2)
#     g+=1
# if poeni3>=kvalf:
#     i+=1
# else:
#     neuspeli.append(poeni3)
#     g+=1
# if poeni4>=kvalf:
#     i+=1
# else:
#     neuspeli.append(poeni4)
#     g+=1
# print(i)
# sredina=sum(neuspeli)/g
# print(format(sredina,'.2f'))
#===================================================================

#===================================================================
#Zadatak  18
# Задатак: Претицање
# Три аутомобила стартних бројева 1, 2, 3 крећу са исте стартне позиције редом у тренуцима t1, t2, t3 (0 ≤ t1 <
# t2 < t3), и крећу се константним брзинама v1, v2, v3. Написати програм којим одређујемо тренутак кад се
# деси последње претицање, или ако нема претицања исписати текст nema.
# Улаз: Са стандардног улаза учитава се 6 реалних бројева. Прва линија садржи бројеве t1, v1, друга бројеве
# t2, v2, а трећа бројеве t3, v3.
# Излаз: На стандардни излаз исписати један реалан број који представља време последњег претицања, заокружен на две децимале или текст nema ако претицања није било.
# Пример 1
# Улаз
# 1.6 20
# 2 12
# 7.4 2.1
# Излаз
# nema
# Пример 2
# Улаз
# 6.3 9
# 15 18
# 19 13
# Излаз
# 47.57


# t1=int(input('vreme kretanja prvog vozila:'))
# v1=int(input('brzina kretanja prvog vozila:'))
# t2=int(input('vreme kretanja drugog vozila:'))
# v2=int(input('brzina kretanja drugog vozila:'))
# t3=int(input('vreme kretanja treceg vozila:'))
# v3=int(input('brzina kretanja treceg vozila:'))
# bilo_preticanja = False # da li je pronađeno jedno preticanje
# t_poslednjeg_preticanja = 0 # vreme poslednjeg preticanja

# # proveravamo da li drugi automobil može preteći prvi
# if v2 > v1:
# t_preticanja = (v2*t2 - v1*t1) / (v2 - v1)
# if not bilo_preticanja or t_preticanja > t_poslednjeg_preticanja:
# t_poslednjeg_preticanja = t_preticanja
# bilo_preticanja = True
# # proveravamo da li treći automobil moze preteći prvi
# if v3 > v1:
# t_preticanja = (v3*t3 - v1*t1) / (v3 - v1)
# if not bilo_preticanja or t_preticanja > t_poslednjeg_preticanja:
# t_poslednjeg_preticanja = t_preticanja
# bilo_preticanja = True
# # proveravamo da li treći automobil moze preteći drugi
# if v3 > v2:
# t_preticanja = (v3*t3 - v2*t2) / (v3 - v2)
# if not bilo_preticanja or t_preticanja > t_poslednjeg_preticanja:
# t_poslednjeg_preticanja = t_preticanja
# bilo_preticanja = True
# # ako je bilo preticanja, prijavljujemo vreme poslednjeg preticanja
# if bilo_preticanja:
# print(format(t_poslednjeg_preticanja, '.2f'))
# else:
# print(”nema”)
#===================================================================







>>>>>>> a0fa89d (i forgor to commit")

















<<<<<<< HEAD
#===================================================================    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
=======
    
    
    
    
    
>>>>>>> a0fa89d (i forgor to commit")
    
    
    
    
    
    
    
    
