from ast import Lambda, Try
from gettext import install
import tkinter

from tkinter import *
import tkinter.font as font
import math

from matplotlib.pyplot import grid


root = Tk()
root.title('KALKULATOR')
root.geometry('350x400')
root['bg'] = '#add8e6'

myfont = font.Font(size=15)

e = Entry(root)
e['font']=myfont
e['bg']='#d1d1d1'
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

def angka(nilai):
      before = e.get()
      e.delete(0,END)
      e.insert(0,str(before)+str(nilai)) 

def tambah():
       nomor_awal = e.get()
       global n_awal
       global mtk
       mtk = 'penjumlahan'
       n_awal = int (nomor_awal)
       e.delete(0, END)

def kurang():
       nomor_awal = e.get()
       global n_awal
       global mtk
       mtk = 'pengurangan'
       n_awal = int (nomor_awal)
       e.delete(0, END)

def kali():
       nomor_awal = e.get()
       global n_awal
       global mtk
       mtk = 'perkalian'
       n_awal = int (nomor_awal)
       e.delete(0, END)

def bagi():
      nomor_awal = e.get()
      global n_awal
      global mtk
      mtk = 'pembagian'
      n_awal = int (nomor_awal)
      e.delete(0, END)

def akar():
      nomor_awal = e.get()
      global n_awal
      n_awal = int (nomor_awal)
      e.delete(0, END)
      e.insert(0,math.sqrt(n_awal))

def sisabagi():
      nomor_awal = e.get()
      global n_awal
      global mtk
      mtk = 'sisabagi'
      n_awal = int (nomor_awal)
      e.delete(0, END)

def pangkat():
      nomor_awal = e.get()
      global n_awal
      n_awal = int (nomor_awal)
      e.delete(0, END)
      e.insert(0,n_awal **2)

def hapus():
       e.delete(0,END)

def samadengan():
       nomor_akhir= e.get()
       e.delete(0,END)
       if mtk == 'penjumlahan':
           e.insert(0,n_awal + int(nomor_akhir ))
       elif mtk == 'pengurangan':
           e.insert(0,n_awal - int(nomor_akhir ))
       elif mtk == 'perkalian':
           e.insert(0,n_awal * int(nomor_akhir ))
       elif mtk == 'sisabagi':
           e.insert(0,n_awal % int(nomor_akhir ))
       elif mtk == 'pembagian':
           try:
                 hitung = n_awal / int (nomor_akhir)
                 e.insert(0,hitung)
           except ZeroDivisionError:
                  e.insert(0,'maaf lagi belajar')
       

btn1 = Button(root,text='1',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(1))
btn2 = Button(root,text='2',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(2))
btn3 = Button(root,text='3',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(3))
btn4 = Button(root,text='4',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(4))
btn5 = Button(root,text='5',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(5))
btn6 = Button(root,text='6',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(6))
btn7 = Button(root,text='7',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(7))
btn8 = Button(root,text='8',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(8))
btn9 = Button(root,text='9',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(9))
btn0 = Button(root,text='0',bg='#ff1493',fg = 'white',padx=30,pady=20,command=lambda :angka(0))
tam = Button(root,text='+',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=tambah)
ak2 = Button(root,text='sq2',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=akar)
sisa = Button(root,text='//2',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=sisabagi)
pang = Button(root,text='x^2',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=pangkat)
kur = Button(root,text='-',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=kurang)
kal = Button(root,text='x',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=kali)
bag = Button(root,text='/',bg='#3d3d3d',fg = 'white',padx=30,pady=20,command=bagi)
hap = Button(root,text='c',padx=30,pady=20,command=hapus)
sama = Button(root,text='=',padx=30,pady=20,command=samadengan)

btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

tam.grid(row=1,column=3,pady=2)
kur.grid(row=2,column=3,pady=2)
kal.grid(row=3,column=3,pady=2)
bag.grid(row=4,column=3,pady=2)
hap.grid(row=5,column=3,pady=2)
sama.grid(row=5,column=2,pady=2)
sisa.grid(row=4,column=2,pady=2)
ak2.grid(row=5,column=0,pady=2)
pang.grid(row=5,column=1,pady=2)

root.mainloop()