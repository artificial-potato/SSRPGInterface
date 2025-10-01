import time
import ssrpgif  # Import 

# 1. Initialize the SSRPGInterface for v0.3 in 'sync' mode
# The 'sync' mode allows the script to run alongside an in-game Stonescript.
ssrpg = ssrpgif.SSRPGInterface(mode='sync')

# It's generally better to manage state outside the library instance.
y_pos = 0

# 2. Define the test step function
# The step function in sync/exclusive modes receives a context string ('exclusive', 'pre', or 'post').
def test_step(context):
    global y_pos
    
    # In sync mode, we can choose to act before the in-game script ('pre') or after ('post').
    # for example, all logic is handled in the 'pre' step.
    if context == 'pre':
        # Use the new high-level API. The cache is cleared automatically at the start of each step.
        if ssrpg.loc.begin(): #or we can use low-level API ssrpg.call("loc.begin")
            y_pos = 0
            # The command module queues commands. They are all sent automatically at the end of the step.
            ssrpg.command.Brew("tar", "wood")
        
        # Update y coordinate
        y_pos = (y_pos + 1) % 30
        
        # Send a print command with the y coordinate and current time
        ssrpg.command.Print(f"hello python!{time.ctime()}",x=1, y=y_pos)
        
        # Get and print foe information
        current_foe = ssrpg.foe()
        foe_distance = ssrpg.foe.distance()
        print(f"(pre) foe: {current_foe}, distance: {foe_distance}")
        
        # print test
        print(f"(pre) time: {ssrpg.time()}")
        print(f"(pre) totaltime: {ssrpg.totaltime()}")
        print(ssrpg.get_screen(0,0,10,10))
        print(f"var: {ssrpg.var["mode"]}")
        ssrpg.var["mode"]="heal"
        
        # Equip different items based on the foe type
        if "boss" in current_foe:
            ssrpg.command.EquipR("sword")
            ssrpg.command.EquipL("hammer")
            ssrpg.loc.Pause()
        else:
            ssrpg.command.Equip("arm")
            # Check conditions before activating an item
            if foe_distance is not None and foe_distance < 8 and ssrpg.item.CanActivate("skeleton_arm"):
                ssrpg.command.Activate("R")
            
            cooldown = ssrpg.item.GetCooldown("skeleton_arm")
            can_activate = ssrpg.item.CanActivate("skeleton_arm")
            print(f"(pre) Skeleton Arm Cooldown: {cooldown}, Can Activate: {can_activate}")
    
    elif context == 'post':
        # No action is taken in the post-step
        pass


# 3. Main execution block
if __name__ == "__main__":
    try:
        print("Connecting to StoneStory RPG in SYNC mode...")
        # Explicitly connect to the game
        ssrpg.connect()
        print("Connection successful. Starting test loop... (Press Ctrl+C to stop)")
        
        # 4. Run the main loop
        while True:
            # In sync mode, step() will be called twice per game frame: once for 'pre', once for 'post'.
            ssrpg.step(test_step)
            
    except ConnectionError as e:
        print(f"\nConnection failed or was lost: {e}")
    except KeyboardInterrupt:
        print("\nTest stopped by user.")
    finally:
        print("Disconnecting...")
        # Gracefully disconnect when done
        ssrpg.disconnect()