## SSRPGInterface
python interface for SSRPG(commexp)
tested on Python 3.10.7 (win32)

- SSRPGInterface.py
main script for the interface
- SSRPGtest.py
a script to test communication


# How to use the example (SSRPGtest.py)
1. launch SSRPG(commexp)
2. enable mindstone, erase all and put `sys.MindConnect()`
3. go to some location
4. `python SSRPGtest.py`

# How to write custom scripts
SSRPGInterface
- `SSRPGInterface()`
constructor of SSRPGInterface

- `SSRPGInterface.step`
a member function of SSRPGInterface
should be assign a function to be executed at each step 
must end with `SSRPGInterface.eof()`.
```
ssrpg=SSRPGInterface()
def teststep():
    ssrpg.callcommand("equip","arm")
    ssrpg.eof()
ssrpg.step=teststep
```

- `SSRPGInterface.run()`
execute step() and start communication with SSRPG
`ssrpg.run()`

- `SSRPGInterface.callcommand(command, parameter)`
execute a command of stonescript
example:
`ssrpg.callcommand(">","hello python!")`

- `SSRPGInterface.call(var or function[,parameter1,parameter2...])`
get variable or function(parameter) of stonescript
example:
`foe=ssrpg.call("foe")`
`symbol=ssrpg.call("draw.GetSymbol",1,1)`

# Limitation
- Cannot use StoneScriptObjects like ui.panel
- Cannot be used at the same time as stonescript
- Protocols and interfaces are likely to change as they are currently in the experimental phase