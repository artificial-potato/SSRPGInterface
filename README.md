
# SSRPGInterface

SSRPGInterface is a Python interface for SSRPG (4.9.1 or above).

by: ArtificialPotato (Discord @artificial.potato)

## demo
https://github.com/user-attachments/assets/e0e0cc8f-4d13-4915-849d-6b7e3069729e

https://github.com/user-attachments/assets/2edeeba0-f622-437e-bafe-45b5ba1201ee



## Tested Environment

- Python 3.10.7 (win32)

## Files

- **ssrpgif.py**: Main script (module) for the interface.
- **SSRPGtest.py**: A script to test communication.

## How to Use the Example (SSRPGtest.py)

1. Launch SSRPG (4.9.1 or above).
2. Enable mindstone, erase all, and put `sys.MindConnect()`.
3. Go to some location.
4. Run the script: `python SSRPGtest.py`.

## Writing Custom Scripts

Use the `SSRPGInterface` class to communicate with SSRPG. Refer to `SSRPGtest.py` for usage examples.

### SSRPGInterface Class

#### Constructor

```python
from ssrpgif import SSRPGInterface
ssrpg = SSRPGInterface()
```

#### step
Field to store your custom program to run every frame.
Assign a function to be executed at each step.

```python
def teststep():
    ssrpg.call_command("equip", "arm")

ssrpg.step = teststep
```

#### run()

Execute the `step()` method in a loop and start communication with SSRPG.

```python
ssrpg.run()
```

#### call_command(str command, str parameter)

Execute a command in StoneScript.

Valid commands are as follows:
`{ ">" , "play" , "equipR" , "equipL", "equip", "loadout", "activate", "enable", "disable", "brew"}`

```python
ssrpg.call_command(">", "hello python!")
```

#### call(str variable/function[, parameter1, parameter2,...])

Get a variable or execute a function in StoneScript. Return values are automatically converted to appropriate Python types (`bool`, `int` or `str`).

```python
foe = ssrpg.call("foe")
symbol = ssrpg.call("draw.GetSymbol", 1, 1)
```

#### multi_call([[str var1/func1,...],[str var2/func2,...],...])

Get multiple variables or execute multiple functions in StoneScript. Return values are lists of `str`.

```python
foe, loc, foe_debuff, symbol11 = ssrpg.multi_call([["foe"],["loc"],["foe.debuffs.string"],["draw.GetSymbol", 1, 1]])
```

## Limitations

- Cannot use StoneScriptObjects like `ui.panel`.
- Cannot be used simultaneously with StoneScript.
- Protocols and interfaces are experimental and subject to change.

## To-do list for this project (SSRPG side and interface side mixed)
- [ ] Merge pull requests (scheduled for first half of April, thanks xx!)
- [ ] Improvement and documentation of the protocol
- [ ] Support for simultaneous use with stonescript
- [ ] Support for communication with non-loopbacks
- [ ] Easy-to-use aliases for commands (like SSRPGInterface.print(str), SSRPGInterface.equip(str), ...)
- [ ] Update README.md
- [ ] Support for types other than int, bool, str
- [ ] Create interfaces for other languages (if strongly requested)
