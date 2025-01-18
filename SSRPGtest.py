from SSRPGInterface import SSRPGInterface
import time

ssrpgIF=SSRPGInterface()
ssrpgIF.y=0

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
    ssrpgIF.eof()


ssrpgIF.step=teststep
ssrpgIF.run()