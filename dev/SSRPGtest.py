from SSRPGInterface import SSRPGInterface
import time
import itertools
import os
from platform import system
from ctypes import windll
os.system("cls")
kernel = windll.kernel32
kernel.SetConsoleMode(kernel.GetStdHandle(-11), 7)
ssrpgIF=SSRPGInterface()

ssrpgIF.y=0
w=30
h=15
def cursor_up(n):
    print(f'\033[{n}A', end='')

def teststep():
    ssrpgIF.y=(ssrpgIF.y+1)%30
    print("foe:"+ssrpgIF.call("foe"))
    print("foe.distance:"+str(ssrpgIF.call("foe.distance")))
    if ssrpgIF.call("loc.begin"):
        ssrpgIF.callcommand("brew","tar + wood")
    if "boss" in ssrpgIF.call("foe"):
        ssrpgIF.callcommand("equipR","sword")
        ssrpgIF.callcommand("equipL","hammer")
    else:
        ssrpgIF.callcommand("equip","arm")
        if ssrpgIF.call("foe.distance")<8 and ssrpgIF.call("item.CanActivate","skeleton_arm"):
            ssrpgIF.callcommand("activate","R")
        print(str(ssrpgIF.call("item.GetCooldown","skeleton_arm"))+" "+str(ssrpgIF.call("item.CanActivate","skeleton_arm")))
    ssrpgIF.callcommand(">","`1,"+str(ssrpgIF.y)+","+"hello python!"+time.ctime())

def teststep2():
    os.system("cls")
    ret=ssrpgIF.multcall(ssrpgIF.inst)
    print("SSRPGpy:")
    for i in range(h):
        print("".join(ret[w*i:w*(i+1)]))

def teststep3():
#    ssrpgIF.y=(ssrpgIF.y+1)%30
    print("foe:"+ssrpgIF.call("foe")+"          ")
    print("foe.distance:"+str(ssrpgIF.call("foe.distance"))+"          ")
    if ssrpgIF.call("loc.begin"):
        ssrpgIF.callcommand("brew","tar + wood")
    if "boss" in ssrpgIF.call("foe"):
        ssrpgIF.callcommand("equipR","sword")
        ssrpgIF.callcommand("equipL","hammer")
    else:
        ssrpgIF.callcommand("equip","arm")
        if ssrpgIF.call("foe.distance")<8 and ssrpgIF.call("item.CanActivate","skeleton_arm"):
            ssrpgIF.callcommand("activate","R")
    print(str(ssrpgIF.call("item.GetCooldown","skeleton_arm"))+" "+str(ssrpgIF.call("item.CanActivate","skeleton_arm"))+"          ")
#    ssrpgIF.callcommand(">","`1,"+str(ssrpgIF.y)+","+"hello python!"+time.ctime())
    print(ssrpgIF.getScreen(15,7,30,15))
    cursor_up(h+3)
    
test_inst=[["draw.GetSymbol",15+xy[1],7+xy[0]] for xy in itertools.product(range(h),range(w))]
ssrpgIF.inst=test_inst
ssrpgIF.step=teststep3
ssrpgIF.run()