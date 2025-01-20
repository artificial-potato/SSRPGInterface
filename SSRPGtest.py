"""
WARNING: The file needs to be in the same directory as the SSRPGInterface folder. 
"""

from SSRPGInterface.commands import *
from SSRPGInterface import *
import time

# Define the test step function
def teststep():
    # Check ?loc.begin
    if call("loc.begin"):
        y = 0
        # Execute the command to brew tar + wood
        call_command("brew", "tar + wood")
    
    # Update y coordinate
    y = (y + 1) % 30
    
    # Send a command with the y coordinate and current time
    call_command(">", "`1," + str(y) + "," + "hello python!" + time.ctime())
    
    # Print the foe and its distance
    print("foe:" + call("foe"))
    print("foe.distance:" + str(call("foe.distance")))
    
    # Equip different items based on the foe type
    if "boss" in call("foe"):
        call_command("equipR", "sword")
        call_command("equipL", "hammer")
    else:
        call_command("equip", "arm")
        if call("foe.distance") < 8 and call("item.CanActivate", "skeleton_arm"):
            call_command("activate", "R")
        print(str(call("item.GetCooldown", "skeleton_arm")) + " " + str(call("item.CanActivate", "skeleton_arm")))

def battle_test():
	if item.left.state() == 3:
		command.EquipL("sword")
	if item.right.state() == 3:
		command.EquipR("shield")
	
	if foe.distance() < 24:
		command.Equip("arm")
	else:
		command.EquipL("trisk")
		command.EquipR("compound")

	print(f"\r{hp()}/{maxhp()} {armor()}/{maxarmor()} {item.left.state()} {item.right.state()}", end="")


if __name__ == "__main__":
    # Run the interface
    run_script(teststep)