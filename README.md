# SSRPGInterface

SSRPGInterface is a Python interface for StoneStory RPG (v4.25.0 or above), enabling you to interact with the game using Python scripts.

by: ArtificialPotato (Discord @artificial.potato)

## Demo

https://github.com/user-attachments/assets/1c2b4b7f-d8e5-46a2-a9fc-accac7f8782a

https://github.com/user-attachments/assets/2edeeba0-f622-437e-bafe-45b5ba1201ee

## Tested Environment

  * Python 3.13.5 (win32)

## Features

  * **High-Level API:** An intuitive, object-oriented API that mirrors in-game variables and functions (e.g., `ssrpg.foe.name()`, `ssrpg.player.hp()`).
  * **Command Queueing:** Automatically queues and sends commands at the end of each game step, simplifying your script logic.
  * **Multiple Operation Modes:**
      * `sync`: Run your Python script alongside an in-game Stonescript.
      * `exclusive`: Your Python script takes full control of the game logic.
  * **Automatic Caching:** Caches the results of function calls within a single game step to improve performance and avoid redundant requests.

## How to Use

1.  Launch StoneStory RPG (v4.2x.x or above).
2.  Enable the mindstone and add `//MindConnect: [mode]` for the very first line. [mode] can be `sync` or `exclusive`.
3.  Enter any location in the game.
4.  Run your Python script (e.g., `python your_script.py`).

## Writing Custom Scripts

To communicate with StoneStory RPG, you'll use the `SSRPGInterface` class. This library offers both a high-level API for ease of use and a low-level API for more direct control.

### Tutorial: Using the High-Level API with Sync Mode

The recommended way to write scripts is by using the high-level API in `sync` mode. This mode runs your Python script alongside an in-game Stonescript, allowing you to react to the game in real-time. The `SSRPGtest.py` file provides an example.

Let's break down how it works.

**1. Initialize the Interface**

First, import the library and create an instance of `SSRPGInterface`. The `mode='sync'` argument is key here.

```python
import ssrpgif
import time

# Initialize the SSRPGInterface for v0.3 in 'sync' mode
ssrpg = ssrpgif.SSRPGInterface(mode='sync')
```

**2. Define a Step Function**

In `sync` mode, the game sends signals to your script every frame. Your script needs a "step function" to handle these signals. This function will receive a `context` string, which can be `'pre'` (before the in-game script runs) or `'post'` (after the in-game script runs).

You can decide whether your logic should execute before or after the game's own script on that frame.

```python
# It's better to manage state outside the library instance.
y_pos = 0

def test_step(context):
    global y_pos
    
    # We can choose to act before ('pre') or after ('post') the in-game script.
    # In this example, all logic is handled in the 'pre' step.
    if context == 'pre':
        # --- Your game logic goes here ---
        
        # Check if we are at the beginning of a location
        if ssrpg.loc.begin():
            y_pos = 0
            # Queue a command to be sent at the end of the step
            ssrpg.brew("tar", "wood")
        
        # Update a variable and print to the screen
        y_pos = (y_pos + 1) % 30
        ssrpg.print(f"hello python!{time.ctime()}", x=1, y=y_pos) # High-level print command
        
        # Get information about the current foe
        current_foe = ssrpg.foe()
        foe_distance = ssrpg.foe.distance()
        print(f"Foe: {current_foe}, Distance: {foe_distance}")
        
        # Equip different items based on the foe
        if "boss" in current_foe:
            ssrpg.equipR("sword") # High-level equip command
            ssrpg.equipL("hammer")
            ssrpg.loc.Pause()
        else:
            ssrpg.equip("arm")
            # Activate an item if conditions are met
            if foe_distance is not None and foe_distance < 8 and ssrpg.item.CanActivate("skeleton_arm"):
                ssrpg.activate("R") # High-level activate command
```

**3. Connect and Run the Main Loop**

Finally, the main part of your script connects to the game and enters a loop, calling `ssrpg.step()` repeatedly. This method waits for signals from the game and executes your step function accordingly.

```python
if __name__ == "__main__":
    try:
        print("Connecting to StoneStory RPG in SYNC mode...")
        ssrpg.connect()
        print("Connection successful. Starting loop... (Press Ctrl+C to stop)")
        
        while True:
            # In sync mode, step() calls your function for 'pre' and 'post' contexts.
            ssrpg.step(test_step)
            
    except ConnectionError as e:
        print(f"\nConnection failed or was lost: {e}")
    except KeyboardInterrupt:
        print("\nScript stopped by user.")
    finally:
        print("Disconnecting...")
        ssrpg.disconnect()
```

-----

## High-Level API Manual

The high-level API provides an intuitive, object-oriented way to interact with game elements. All game-state calls are cached per frame, so you can call them multiple times without performance loss. Commands are automatically queued and sent at the end of each step.

### Command Functions

These are direct methods of the `ssrpg = ssrpgif.SSRPGInterface(mode='sync')` object for queueing common commands.

  * `ssrpg.print(text, [x, y, ...])`: Prints text to the screen.
  * `ssrpg.equip("item_name")`: Equips an item to the best hand.
  * `ssrpg.equipL("item_name")`: Equips an item to the left hand.
  * `ssrpg.equipR("item_name")`: Equips an item to the right hand.
  * `ssrpg.activate("R")` or `ssrpg.activate("L")`: Activates the right or left item.
  * `ssrpg.brew("mat1", "mat2")`: Brews a potion.

### Game State Objects

These objects are properties of the `ssrpg` instance and contain methods to retrieve information about the game.

  * **`ssrpg.loc`**: Information about the current location.
      * `ssrpg.loc()`: Returns the location's name.
      * `ssrpg.loc.begin()`: Returns `True` at the start of a location.
      * `ssrpg.loc.isQuest()`: Returns `True` if the location is a quest.
      * and more
  * **`ssrpg.foe`**: Information about the current enemy.
      * `ssrpg.foe()`: Returns the foe's name.
      * `ssrpg.foe.distance()`: Returns the distance to the foe.
      * `ssrpg.foe.hp()`: Returns the foe's current health.
      * and more
  * **`ssrpg.item`**: Information about your items.
      * `ssrpg.item.GetCooldown("item_name")`: Returns the cooldown time for an item.
      * `ssrpg.item.CanActivate("item_name")`: Checks if an item can be activated.
      * and more...
  * **`ssrpg.player`**: Information about the player.
      * `ssrpg.player.name()`: Returns the player's name.
      * and more
  * **`ssrpg.var`**: Access to Stonescript's `var` dictionary.
      * `ssrpg.var["my_variable"]` : Gets a value of `my_variable` on stonescript
      * `ssrpg.var["my_variable"] = "new_value"` : Sets a value of `my_variable` on stonescript
      * `"my_variable" in ssrpg.var` : `True` if `my_variable` exists on stonescript
  * **Top-Level Variables**:
      * `ssrpg.hp()`: Returns current player health.
      * `ssrpg.time()`: Returns the time elapsed in the current location.
      * and more

This is just a sample. You can explore the `ssrpgif/commands/` directory and `ssrpgif/core.py` to see all available classes and methods.


## Low-Level API (for advanced users)

For maximum flexibility, you can bypass the high-level API and use the low-level functions.

#### `call(str variable_or_function, [param1, param2, ...])`

Gets a variable or executes a function in StoneScript. Return values are automatically converted to `bool`, `int`, or `str`.

```python
# Get the foe's name
foe_name = ssrpg.call("foe.name")

# Get a symbol from the screen
symbol = ssrpg.call("draw.GetSymbol", 10, 5)
```

#### `multi_call([[str var1/func1, ...], [str var2/func2, ...], ...])`

Executes multiple calls in a single request for efficiency. Returns a list of strings.

```python
results = ssrpg.multi_call([
    ["foe.name"],
    ["loc.id"],
    ["draw.GetSymbol", 10, 5]
])
# results -> ['Wound Licker', 'caustic_caves', '-']
```

## Limitations

  * Cannot use StoneScript objects like `ui.panel`.
  * MindConnect cannot be used on imported scripts
  * Protocols and interfaces are experimental and subject to change.

## To-Do List

  - [ ] Improvement and documentation of the protocol
  - [ ] Support for communication with non-loopbacks
  - [ ] Support for types other than int, bool, str
  - [ ] Create interfaces for other languages (if strongly requested)
  - [ ] Support for imported scripts (if strongly requested)
