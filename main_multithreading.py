# To zostaw w spokoju!!!! -------------------------------------------------------------
from threading import *
from time import sleep
from manipulator import Manipulator
from clear_console import clear_console
import keyboard


def print_state(manipulator:Manipulator) -> None:
    while True:
        clear_console()
        print(manipulator)
        sleep(0.1)
        
def control_panel(m: Manipulator):
    while True:
        if keyboard.read_key() == "z":
            if m.stop != True:
                m.start = True
        if keyboard.read_key() == "w":
            m.start = False
            m.stop = True
        
    
def program (m:Manipulator):
    while True:
# --------------------------------------------------------------------------------
# Tu edytujesz logikę - nazwy krańcówek i wyjść wg. instrukcji z zajęć
# ewentualnie sprawdź parametry obiektu lub skontaktuj się ze mną
        if m.kr_l == True: m.w_lewo = False
        if m.kr_p == True: m.w_prawo = False
        if m.kr_d == True: m.w_dol = False
        if m.kr_g == True: m.w_gore = False
        
        if m.start == True and m.kr_o == True and m.kr_d == True and m.kr_l == True: m.w_gore = True
        if m.start == True and m.kr_o == True and m.kr_g == True and m.kr_l == True: m.w_prawo = True
        if m.start == True and m.kr_o == True and m.kr_g == True and m.kr_p == True: m.w_dol = True
        if m.start == True and m.kr_o == True and m.kr_d == True and m.kr_p == True: m.chwytak = True
        if m.start == True and m.kr_z == True and m.kr_d == True and m.kr_p == True: m.w_gore = True
        if m.start == True and m.kr_z == True and m.kr_g == True and m.kr_p == True: m.w_lewo = True
        if m.start == True and m.kr_z == True and m.kr_g == True and m.kr_l == True: m.w_dol = True
        
        if m.start == True and m.kr_z == True and m.kr_d == True and m.kr_l == True: 
            m.chwytak = False
            m.start = False    
        
        if m.stop == True: m.chwytak = False
        
        if m.stop == True and m.w_prawo == True:
            m.w_prawo = False
            m.w_lewo = True
        
        if m.stop == True and m.kr_p == True and m.w_dol == True:
            m.w_dol == False
            m.w_gore == True
            
        if m.stop == True and m.kr_l == True and m.w_gore == True:
            m.w_gore == False
            m.w_dol == True
            

        if m.stop == True and m.kr_d == True and m.kr_p == True: m.w_gore = True
        if m.stop == True and m.kr_g == True and m.kr_p == True: m.w_lewo = True
        if m.stop == True and m.kr_g == True and m.kr_l == True: 
            m.w_dol = True
            m.stop = False
# Dalej nie ma nic interesującego -------------------------------------------------------------------------
        m.make_move()
        sleep(0.1)
    
if __name__ == "__main__":
    m = Manipulator()
    
    t1 = Thread(target=program, args=[m])
    t2 = Thread(target=control_panel, args=[m])
    t3 = Thread(target=print_state, args=[m])
    t1.start()
    t2.start()
    t3.start()