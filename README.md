
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

#### step Method

Assign a function to be executed at each step.

```python
def teststep():
    ssrpg.callcommand("equip", "arm")

ssrpg.step = teststep
```

#### run Method

Execute the `step()` method in a loop and start communication with SSRPG.

```python
ssrpg.run()
```

#### callcommand Method

Execute a command in StoneScript.

```python
ssrpg.callcommand(">", "hello python!")
```

#### call Method

Get a variable or execute a function in StoneScript. Return values are automatically converted to appropriate Python types (`bool`, `int` or `str`).

```python
foe = ssrpg.call("foe")
symbol = ssrpg.call("draw.GetSymbol", 1, 1)
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