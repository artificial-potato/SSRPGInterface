from SSRPGInterface import SSRPGInterface
import time
ssrpgIF=SSRPGInterface()
def teststep():
    print("foe:"+ssrpgIF.call("foe"))
    print("foe.distance:"+ssrpgIF.call("foe.distance"))
    if "boss" in ssrpgIF.call("foe"):
        ssrpgIF.callcommand("equipR","sword")
        ssrpgIF.callcommand("equipL","hammer")
    else:
        ssrpgIF.callcommand("equip","arm")
    ssrpgIF.callcommand(">","hello python!"+time.ctime())
    ssrpgIF.eof()

ssrpgIF.step=teststep
ssrpgIF.run()