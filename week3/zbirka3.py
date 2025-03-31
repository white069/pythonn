#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 13:28:24 2025

@author: alex
"""

def ispisati(x):
    print("#===================================================================")
    print("#Zadatak ", x)
    
    
    print("#===================================================================")
    

#===================================================================
#Zadatak  1
# Задатак: Јабуке
# Пера и Мика су брали јабуке. Пера је убрао p, а Мика m јабука. Напиши програм који проверава да ли је
# Пера успео да набере више јабука него Мика.
# Улаз: Са стандардног улаза уносе се два природна броја (сваки у посебном реду). У првом реду број јабука
# које је убрао Пера, а у другом број јабука које је убрао Мика.
# Излаз: Исписати на стандардном излазу: DA - ако је Пера убрао више јабука од Мике, а NE - ако Пера није
# убрао више јабука од Мике.
# Пример 1
# Улаз
# 73
# 10
# Излаз
# DA
# Пример 2
# Улаз
# 48
# 48
# Излаз
# NE
# Пример 3
# Улаз
# 35
# 56
# Излаз
# NE

# p=int(input("Jabuka koje je Pera ubrao: "))
# m=int(input('Jabuka koje je Mika ubrao: '))
# if p>m:
#     print("DA")
# else:
#     print("NE")
#===================================================================



#===================================================================
#Zadatak  2
# Задатак: Збир година браће и сестре
# Пера, Мика и Лаза су три брата рођена у истом дану, а Ана је њихова 3 године старија сестра. Написати
# програм којим се проверава да ли унети број може бити збир њихових година.
# Улаз: Са стандардног улаза уноси се један позитиван природан број мањи од 500.
# Излаз: На стандардном излазу приказати реч da ако унети број може бити збир година Пере, Мике, Лазе и
# Ане, а ако не може приказати реч ne.
# Пример 1
# Улаз
# 27
# Излаз
# da
# Пример 2
# Улаз
# 30
# Излаз
# ne

# n=int(input("broj godina: "))
# if (n-3)%4==0:
#     print("da")
# else:
#     print("ne")
#===================================================================


#===================================================================
#Zadatak  3
# Задатак: Теме правоугаоника
# Дате су координате три темена правоугаоника са целобројним координатама чије су странице паралелне координатним осама. Темена су дата у произвољном редоследу. Написати програм којим се одређују координате
# четвртог темена.
# Улаз: Са стандардног улаза учитавају се целобројне координате три темена правоугаоника - у сваком реду
# по два податка (координата x и координата y), раздвојена размаком.
# Излаз: x и y координата траженог темена раздвојене размаком.
# Пример
# Улаз
# 3 5
# 7 5
# 7 9
# Излаз
# 3 9

# x1,y1=map(int, input("x1 i y1: ").split())
# x2,y2= map(int, input('x2 i y2: ').split())
# x3, y3=map(int, input("x3 i y3: ").split())
# if  x1==x2:
#     x4=x3
# elif x1==x3:
#     x4=x2
# else:
#     x4=x1

# if y1==y2:
#     y4=y3
# elif y1==y3:
#     y4=y2
# else:
#     y4=y1
# print(x4, y4)
#===================================================================


#===================================================================
#Zadatak  4
# Задатак: Једнакостранични троугао датог обима
# Дате су целобројне дужине трију страница троугла. Написати програм којим се проверава да ли постоји
# једнакостранични троугао целоборојне дужине страница истог обима као дати троугао и која му је дужина
# странице.
# Улаз: На стандарном улазу налазе се 3 природна броја која представљају странице троугла.
# Излаз: Једна линија стандарног излаза садржи реч da ако постоји тражени троугао, за којом одвојено
#  празнином, следи дужина странице тог троугла, ако тражени троугао не постоји садржи реч ne.
# Пример 1
# Улаз
# 3
# 4
# 5
# Излаз
# da 4
# Пример 2
# Улаз
# 4
# 6
# 9
# Излаз
# ne

# a=int(input("a "))
# b=int(input("b "))
# c=int(input("c "))
# o=a+b+c 
# if o%3==0:
#     print("da", o//3)
# else:
#     print("no")
#===================================================================



#===================================================================
#Zadatak  5
# Задатак: Радно време
# Радно време једне организације је између 9 и 17 часова. Одредити да ли је послати мејл стигао у току радног
# времена.
# Улаз: Са стандардног улаза се уносе два цела броја, сваки у посебном реду, који представљају сат и минут
# приспећа мејла.
# Излаз: На стандардни излаз исписати da ако је мејл стигао у току радног времена тј. ne ако није (9:00 спада
# у радно време, док 17:00 не спада).
# Пример 1
# Улаз
# 14
# 53
# Излаз
# da
# Пример 2
# Улаз
# 17
# 01
# Излаз
# ne

# sat=int(input("sati "))
# minut=int(input("minut slanja "))
# if sat>=9 and sat<17:
#     print('da')
# else:
#     print('no')
#===================================================================


#===================================================================
#Zadatak  6
# Задатак: Кућни ред
# Кућни ред забрањује прављење буке пре 6 часова, између 13 и 17 часова и након 22 часа. Напиши програм
# који радницима говори да ли у неком датом тренутку могу да изводе бучније радове.
# Улаз: Са стандардног улаза се уноси цео број између 0 и 23 који представља сат.
# Излаз: На стандардни излаз исписати поруку moze ако је дозвољено изводити бучне радове тј. ne moze ако
# није.
# Пример 1
# Улаз
# 5
# Излаз
# ne moze
# Пример 2
# Улаз
# 6
# Излаз
# moze
# Пример 3
# Улаз
# 13
# Излаз
# ne moze


# buka=int(input("zeljeni sat igranja The Binding of Isaac: Repentance+ "))
# if buka>=6 and buka<13 or buka>=17 and buka<22:
#     print("moze")
# else: 
#     print('ne moze majmune')
#===================================================================


#===================================================================
#Zadatak  7
# Задатак: Постоји ли троугао датих дужина страница
# Написати програм којим се проверава да ли постоји троугао са датим дужинама страница.
# Улаз: На стандарном улазу налазе се три реална позитивна броја, сваки у посебној линији. 
#Бројеви представљају дужине страница a, b, c.
# Излаз: Једна линија стандарног излаза која садржи реч da ако постоји троугао, иначе садржи реч ne.
# Пример
# Улаз
# 4.3
# 5.4
# 6.7
# Излаз
# da

# a=float(input("str a "))
# b=float(input('b '))
# c=float(input('c '))
# if a<b+c and b<c+a and c<a+b:
#     print('da')
# else:
#     print('ne')
#===================================================================


#===================================================================
#Zadatak  8
# Задатак: Преступна година
# Напиши програм који проверава да ли је унета година преступна.
# Улаз: Са стандардног улаза се уноси број године између 1900 и 2200.
# Излаз: На стандардни излаз исписати da ако је година преступна тј. ne ако није.
# Пример 1
# Улаз
# 2004
# Излаз
# da
# Пример 2
# Улаз
# 2017
# Излаз
# ne

# godina=int(input("zeljena godina "))
# if godina%4==0:
#     print("prestupna je")
# else:
#     print('nije')
#===================================================================



#===================================================================
#Zadatak  9
# Задатак: Два броја истог знака
# Написати програм којим се проверава да ли су два цела броја истог знака.
# Улаз: На стандардном улазу налазе се два цела броја a, b (−104 ≤ a, b ≤ 104
# ), оба различита од нуле.
# Излаз: Једна линија стандарног излаза која садржи реч da ако су дати бројеви истог знака, иначе садржи реч
# ne.
# Пример
# Улаз
# 234
# -34
# Излаз
# ne

# a=int(input("broj a "))
# b=int(input('broj b ' ))
# if (a>0 and b>0) or (a<0 and b<0):
#     print("DAAAAAAAAAAAAA")
# else:
#     print('ne :( ')
#===================================================================


#===================================================================
#Zadatak  10
# Задатак: Исти квадрант
# Написати програм којим се проверава да ли две тачке A(x1, y1), B(x2, y2) припадају истом квадранту. Сматраћемо да тачке на позитивном делу x осе припадају првом и четвртом квадранту, тачке на негативном делу
# x осе припадају другом и трећем квадранту, слично тачке на позитивном делу y осе припадају првом и другом квадранту, а на негативном делу y осе трећем и четвртом квадранту, а да координатни почетак припада
# свим квадрантима.
# Улаз: Стандардни улаз садржи четири цела броја, сваки у посебној линији:
# • x1, y1 (−104 ≤ x1, y1, ≤ 104
# ) - координате тачке A(x1, y1)
# • x2, y2 (−104 ≤ x2, y2, ≤ 104
# ) - координате тачке B(x2, y2)
# Излаз: На стандардном излазу у једној линији приказати реч da ако тачке припадају истом квадранту у
# супрорном приказати реч ne.
# Пример
# Улаз
# 12
# -45
# 15
# 23
# Излаз
# ne

# x1=int(input("x1 "))
# y1=int(input('y1 '))
# x2=int(input('x2 '))
# y2=int(input('y2 '))

# if (x1*x2>0) and (y1*y2>0):
#     print('da')
# else:
#     print('ne')
#===================================================================


#===================================================================
#Zadatak  11
# Задатак: Тачка у правоугаонику и кругу
# Напиши програм који за тачку у равни задату својим координатама испитује да ли припада задатом кругу и
# задатом правоугаонику чије су странице паралелне са координатним осама.
# Улаз: Са стандардног улаза учитавају се следећи реални бројеви (бројеви у истом реду су раздвојени једним
# размаком):
# • x, y - координате тачке,
# • x0, y0 - координате заједничког центра круга и правоугаоника,
# • r - полупречник круга,
# • w, h - дужина и ширина страница правоугаоника.
# Излаз: На стандардни излаз исписати два линије текста. У првој линији треба да пише jeste u krugu ако
# тачка (x, y) припада кругу са центром (x0, y0) полупречника r односно nije u krugu ако тачка не припада
# кругу. У другој линији треба да пише jeste u pravougaoniku ако тачка (x, y) припада правоугаонику чији
# је центар (тежиште) у тачки (x0, y0), чије су странице паралелне координатним осама и чија је дужина w тј.
# h, односно nije u pravougaoniku ако тачка не припада унутрашњости тог правоугаоника. Граница круга
# (кружница) и правоугаоника сматрају се њиховим делом.
# Пример
# Улаз
# 1 1
# 0 0
# 1
# 2 2
# Излаз
# nije u krugu
# jeste u pravougaoniku               chatgpt ga je slucajno uradio, a mene mrzelo da ga prepisem

# def tacka_u_pravougaoniku_i_krugu(x, y, x0, y0, r, w, h):
#     # Provera da li je u krugu
#     if (x - x0) ** 2 + (y - y0) ** 2 <= r ** 2:
#         print("jeste u krugu")
#     else:
#         print("nije u krugu")
    
#     # Provera da li je u pravougaoniku
#     if (x0 - w/2 <= x <= x0 + w/2) and (y0 - h/2 <= y <= y0 + h/2):
#         print("jeste u pravougaoniku")
#     else:
#         print("nije u pravougaoniku")

# # Test primer iz zadatka
# tacka_u_pravougaoniku_i_krugu(1, 1, 0, 0, 1, 2, 2)
#===================================================================



#===================================================================
#Zadatak  12
# Задатак: Статус објављен током школе
# Милица је објавила три статуса на друштвеној мрежи. Напиши програм који проверава да ли је неки од тих
# статуса написан у школи (Милица је била у школи од 8:30 до 13:50, укључујући и та времена).
# Улаз: Са стандардног улаза учитавају се три времена објаве статуса (свако време у посебном реду). За сваки
# статус се учитавају сати и минути (два цела броја раздвојена размаком).
# Излаз: На стандардни излаз написати da ако је неки статус објављен током боравка у школи тј. ne у супротном.
# Пример 1
# Улаз
# 14 23
# 17 19
# 22 14
# Излаз
# ne
# Пример 2
# Улаз
# 7 23
# 8 45
# 15 20
# Излаз
# da

# 
        
#===================================================================



#===================================================================
#Zadatak  13
# Задатак: Да ли се две даме нападају
# Напиши програм који проверава да ли се две даме (краљице) на шаховској табли међусобно нападају (краљице се нападају ако се налазе у истој врсти, истој колони или на истој дијагонали шаховске табле).
# 48
# 3.3. УГНЕЖЂЕНО ГРАНАЊЕ
# Улаз: Са стандардног улаза се учитавају координате поља на којем се налази једна краљица (два броја између
# 0 и 7 раздвојена размаком) и у наредном реду координате поља на којем се налази друга краљица (поново
# два броја између 0 и 7 раздвојена размаком). Претпостављамо да се краљице налазе на различитим пољима.
# Излаз: На стандардни излаз исписати текст da ако се краљице нападају тј. ne у супротном.
# Пример 1
# Улаз
# 5 3
# 1 7
# Излаз
# da
# Пример 2
# Улаз
# 5 3
# 1 8
# Излаз
# ne
# Пример 3
# Улаз
# 4 4
# 4 6
# Излаз
# da

# x1,y1=map(int,input('kordinate prve kraljice ').split())
# x2,y2=map(int,input('kordinate druge kraljice ').split())
# if x1==x2 or y1==y2 or abs(x1-x2)==abs(y1-y2):
#     print('da')
# else:
#     print('ne')
#===================================================================











