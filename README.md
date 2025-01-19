
# SSRPGInterface

SSRPGInterface is a Python interface for SSRPG (commexp).

by: ArtificialPotato (Discord @artificial.potato)

## Tested Environment

- Python 3.10.7 (win32)

## Files

- **SSRPGInterface.py**: Main script for the interface.
- **SSRPGtest.py**: A script to test communication.

## How to Use the Example (SSRPGtest.py)

1. Launch SSRPG (commexp).
2. Enable mindstone, erase all, and put `sys.MindConnect()`.
3. Go to some location.
4. Run the script: `python SSRPGtest.py`.

## Writing Custom Scripts

Use the `SSRPGInterface` class to communicate with SSRPG. Refer to `SSRPGtest.py` for usage examples.

### SSRPGInterface Class

#### Constructor

```python
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
- [ ] Improvement and documentation of the protocol
- [ ] Support for simultaneous use with stonescript
- [ ] Support for communication with non-loopbacks
- [ ] Update README.md
- [ ] Support for types other than int, bool, str
- [ ] Create interfaces for other languages (if strongly requested)