#%%
import pyautogui, random, time
import threading 

def lanzarHilo():
  
    th = threading.Thread(target= codigoBotton)
    th.start()
    return  


def terminarHilo():
    global stop_threads
    stop_threads = True
    return

#Codigo movimiento
def codigoBotton():
      global stop_threads
      stop_threads = False
      tabla_switch = {
        0: 'w',
        1: 'a',
        2: 'd',
        3: 's',
        }
      while True:
        if stop_threads == True:
          break
        num1 = random.randint(0,3)
        movement1 = tabla_switch.get(num1)
        pyautogui.keyDown(movement1) 
        time.sleep(random.randint(1,3))
        pyautogui.keyUp(movement1)
        time.sleep(random.randint(5,10))
      return

#Crear ventana
from tkinter import *
from PIL import ImageTk,Image



def main():
  raiz = Tk()

  raiz.title("Anti AFK") #Dar título

  #Permite que se pueda redimensional, dos parametros bool (wheight high) 
  raiz.resizable(False, False) 

  #cambiar incono de la ventana
  raiz.iconbitmap("manu.ico") 

  #Tamaño de la pantalla por defecto, si se el dan al frame no se pone
  #raiz.geometry("720x480") d
  #crear frame
  miFrame = Frame(raiz, width= "720", height= "480", cursor= "pirate", bg="black")
  miFrame.pack() #Se pueden pasar argumentos https://docs.python.org/es/3/library/tkinter.html#the-packer

  image = Image.open('icono.png')
  display = ImageTk.PhotoImage(image)
  imagen = Label(miFrame, image= display, bg= "black")
  imagen.image= display
  imagen.place(x=180,y=0)

  mibotonEmpezar = Button(miFrame, text= "Go to dinner", height=3, width=40, command= lanzarHilo)
  mibotonEmpezar.place(x=220, y= 300)
  
  mibotonTerminar = Button(miFrame, text= "I returned", height=3, width=40, command= terminarHilo)
  mibotonTerminar.place(x=220, y= 360)
  #Para que no se habra la terminal cambiar extención a .pyw
  raiz.mainloop() #Siempre al final

main()
