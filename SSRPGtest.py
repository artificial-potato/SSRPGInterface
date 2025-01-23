"""
WARNING: The file needs to be in the same directory as the SSRPGInterface folder. 
"""

from SSRPGInterface.commands import *
import SSRPGInterface
import cProfile
import time

# Define the test step function
y = 0
def teststep():
    global y
    # Check ?loc.begin
    if loc.begin():
        y = 0
        # Execute the command to brew tar + wood
        command.Brew("tar + wood")
    
    # Update y coordinate
    y = (y + 1) % 30
    
    # Send a command with the y coordinate and current time
    command.Print(f"`1,{y},hello python!{time.ctime()}")
    
    
    # Print the foe and its distance
    print(f"foe:{foe()}")
    print(f"foe.distance:{foe.distance()}")
    
    # Equip different items based on the foe type
    if "boss" in foe():
        command.equipR("sword")
        command.equipL("hammer")
    else:
        command.equip("arm")
        if foe.distance() < 8 and item.CanActivate("skeleton_arm"):
            command.Activate("R")
        print(f"{item.GetCooldown("skeleton_arm")} {item.CanActivate("skeleton_arm")}")

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

    print(f"\r{hp()}/{maxhp()} {armor()}/{maxarmor()} {item.left.state()} {item.right.state()} {totaltime()}", end="")

num = 0
fl = []
avg_time = 0
def connect_callback_speed_test():
    global num, avg_time
    get_var_commands_test_func()
    if num < 20:
        num = num + 1
        start_time = time.time_ns()
        #tt = totaltime()
        for i1 in range(100):
            for i2 in range(100):
                for i3 in range(100):
                    #if tt == -1:
                    if totaltime() == -1:
                        return
        end_time = time.time_ns()
        finish_time = end_time - start_time
        fl.append(finish_time)
        print(f'Connect Callback Speed Test {num}:\t{finish_time / 1000000}ms\t{finish_time}ns')
    else:
        for f in fl:
            avg_time += f
        avg_time /= len(fl)
        print(f'average time is {avg_time / 1000000}ms\t{avg_time}ns')
        pause()

def check_str_length_test():
    left_item = item.left()
    right_item = item.right()
    print(f'\rleft len:{len(left_item)} name:{left_item}\t\tright len:{len(right_item)} name:{right_item}\t\t\t\t\t", end="')

# num = 0
def get_var_commands_test():
    global num
    #get_var_commands_test_func()
    for i in range(3):
        cProfile.run("get_var_commands_test_func_loop(100_00_00)")
    # for key, value in SSRPGInterface.cache.cache_dict.items():
    # 	print(key, value, sep="\t")
    pause()

def get_var_commands_test_func_loop(loop):
    for i in range(loop):
        #print(f"run loop {i}")
        get_var_commands_test_func()

def get_var_commands_test_func():
    ai.enabled()
    ai.paused()
    ai.idle()
    ai.walking()

    hp()
    maxhp()
    armor()
    armor.f()
    maxarmor()
    buffs.count()
    buffs.string()
    buffs.GetCount("debuff_chill")
    buffs.GetTime("debuff_chill")
    debuffs.count()
    debuffs.string()
    debuffs.GetCount("debuff_chill")
    debuffs.GetTime("debuff_chill")
    face()
    bighead()
    totalgp()

    encounter.isElite()
    encounter.eliteMod()

    event.GetObjectiveId(0)
    event.GetObjectiveProgress(0)
    event.GetObjectiveGoal(0)

    foe()
    foe.id()
    foe.name()
    foe.damage()
    foe.distance()
    foe.z()
    foe.count()
    foe.GetCount(48)
    foe.hp()
    foe.maxhp()
    foe.armor()
    foe.maxarmor()
    foe.buffs.count()
    foe.buffs.string()
    foe.buffs.GetCount("debuff_chill")
    foe.buffs.GetTime("debuff_chill")
    foe.debuffs.count()
    foe.debuffs.string()
    foe.debuffs.GetCount("debuff_chill")
    foe.debuffs.GetTime("debuff_chill")
    foe.state()
    foe.time()
    foe.level()

    harvest()
    harvest.distance()
    harvest.z()

    input.x()
    input.y()

    item.CanActivate()
    item.GetCooldown("aether_talisman")
    item.GetCooldown("bardiche")
    item.GetCooldown("bash")
    item.GetCooldown("blade")
    item.GetCooldown("cinderwisp")
    item.GetCooldown("mask")
    item.GetCooldown("dash")
    item.GetCooldown("fire_talisman")
    item.GetCooldown("hatchet")
    item.GetCooldown("heavy_hammer")
    item.GetCooldown("mind")
    item.GetCooldown("quarterstaff")
    item.GetCooldown("skeleton_arm")
    item.GetCooldown("voidweaver")
    item.GetCount("sword")
    item.GetTreasureCount()
    item.GetTreasureLimit()
    item.potion()
    item.GetLoadoutL(1)
    item.GetLoadoutR(1)
    item.left()
    item.left.id()
    item.left.state()
    item.left.time()
    item.left.gp()
    item.left()
    item.right.id()
    item.right.state()
    item.right.time()
    item.right.gp()

    key()
    # key.GetActKey("BumpL")
    # key.GetActKey1("BumpL")
    # key.GetActKey2("BumpL")
    # key.GetActLabel("BumpL")

    loc()
    loc.id()
    loc.name()
    loc.stars()
    loc.begin()
    loc.loop()
    loc.bestTime()
    loc.averageTime()
    loc.isQuest()
    loc.gp()

    time()
    totaltime()

    # music()

    pickup()
    pickup.distance()
    pickup.z()

    player.direction()
    player.framesPerMove()
    player.name()
    player.GetNextLegendName()

    pos.x()
    pos.y()
    pos.z()

    res.stone()
    res.wood()
    res.tar()
    res.ki()
    res.bronze()
    res.crystals()

    screen.i()
    screen.x()
    screen.w()
    screen.h()
    screen.FromWorldX(10)
    screen.FromWorldZ(10)
    screen.ToWorldX(10)
    screen.ToWorldZ(10)

    summon.count()
    summon.GetId()
    summon.GetName()
    summon.GetVar("cinderwisp")
    summon.GetState()
    summon.GetTime()

def get_var_commands_test_func_print():
    print(f'ai.enabled:                          {ai.enabled()}')
    print(f'ai.paused:                           {ai.paused()}')
    print(f'ai.idle:                             {ai.idle()}')
    print(f'ai.walking:                          {ai.walking()}')

    print(f'hp:                                  {hp()}')
    print(f'maxhp:                               {maxhp()}')
    print(f'armor:                               {armor()}')
    print(f'armor.f:                             {armor.f()}')
    print(f'maxarmor:                            {maxarmor()}')
    print(f'buffs.count:                         {buffs.count()}')
    print(f'buffs.string:                        {buffs.string()}')
    print(f'buffs.GetCount:                      {buffs.GetCount("debuff_chill")}')
    print(f'buffs.GetTime:                       {buffs.GetTime("debuff_chill")}')
    print(f'debuffs.count:                       {debuffs.count()}')
    print(f'debuffs.string:                      {debuffs.string()}')
    print(f'debuffs.GetCount:                    {debuffs.GetCount("debuff_chill")}')
    print(f'debuffs.GetTime:                     {debuffs.GetTime("debuff_chill")}')
    print(f'face:                                {face()}')
    print(f'bighead:                             {bighead()}')
    print(f'totalgp:                             {totalgp()}')

    print(f'encounter.isElite:                   {encounter.isElite()}')
    print(f'encounter.eliteMod:                  {encounter.eliteMod()}')

    print(f'event.GetObjectiveId:                {event.GetObjectiveId(0)}')
    print(f'event.GetObjectiveProgress:          {event.GetObjectiveProgress(0)}')
    print(f'event.GetObjectiveGoal:              {event.GetObjectiveGoal(0)}')

    print(f'foe:                                 {foe()}')
    print(f'foe.id:                              {foe.id()}')
    print(f'foe.name:                            {foe.name()}')
    print(f'foe.damage:                          {foe.damage()}')
    print(f'foe.distance:                        {foe.distance()}')
    print(f'foe.z:                               {foe.z()}')
    print(f'foe.count:                           {foe.count()}')
    print(f'foe.GetCount:                        {foe.GetCount(48)}')
    print(f'foe.hp:                              {foe.hp()}')
    print(f'foe.maxhp:                           {foe.maxhp()}')
    print(f'foe.armor:                           {foe.armor()}')
    print(f'foe.maxarmor:                        {foe.maxarmor()}')
    print(f'foe.buffs.count:                     {foe.buffs.count()}')
    print(f'foe.buffs.string:                    {foe.buffs.string()}')
    print(f'foe.buffs.GetCount:                  {foe.buffs.GetCount("debuff_chill")}')
    print(f'foe.buffs.GetTime:                   {foe.buffs.GetTime("debuff_chill")}')
    print(f'foe.debuffs.count:                   {foe.debuffs.count()}')
    print(f'foe.debuffs.string:                  {foe.debuffs.string()}')
    print(f'foe.debuffs.GetCount:                {foe.debuffs.GetCount("debuff_chill")}')
    print(f'foe.debuffs.GetTime:                 {foe.debuffs.GetTime("debuff_chill")}')
    print(f'foe.state:                           {foe.state()}')
    print(f'foe.time:                            {foe.time()}')
    print(f'foe.level:                           {foe.level()}')

    print(f'harvest:                             {harvest()}')
    print(f'harvest.distance:                    {harvest.distance()}')
    print(f'harvest.z:                           {harvest.z()}')

    print(f'input.x:                             {input.x()}')
    print(f'input.y:                             {input.y()}')

    print(f'item.CanActivate:                    {item.CanActivate()}')
    print(f'item.GetCooldown("aether_talisman"): {item.GetCooldown("aether_talisman")}')
    print(f'item.GetCooldown("bardiche"):        {item.GetCooldown("bardiche")}')
    print(f'item.GetCooldown("bash"):            {item.GetCooldown("bash")}')
    print(f'item.GetCooldown("blade"):           {item.GetCooldown("blade")}')
    print(f'item.GetCooldown("cinderwisp"):      {item.GetCooldown("cinderwisp")}')
    print(f'item.GetCooldown("mask"):            {item.GetCooldown("mask")}')
    print(f'item.GetCooldown("dash"):            {item.GetCooldown("dash")}')
    print(f'item.GetCooldown("fire_talisman"):   {item.GetCooldown("fire_talisman")}')
    print(f'item.GetCooldown("hatchet"):         {item.GetCooldown("hatchet")}')
    print(f'item.GetCooldown("heavy_hammer"):    {item.GetCooldown("heavy_hammer")}')
    print(f'item.GetCooldown("mind"):            {item.GetCooldown("mind")}')
    print(f'item.GetCooldown("quarterstaff"):    {item.GetCooldown("quarterstaff")}')
    print(f'item.GetCooldown("skeleton_arm"):    {item.GetCooldown("skeleton_arm")}')
    print(f'item.GetCooldown("voidweaver"):      {item.GetCooldown("voidweaver")}')
    print(f'item.GetCount:                       {item.GetCount("sword")}')
    print(f'item.GetTreasureCount:               {item.GetTreasureCount()}')
    print(f'item.GetTreasureLimit:               {item.GetTreasureLimit()}')
    print(f'item.potion:                         {item.potion()}')
    print(f'item.GetLoadoutL:                    {item.GetLoadoutL(1)}')
    print(f'item.GetLoadoutR:                    {item.GetLoadoutR(1)}')
    print(f'item.left:                           {item.left()}')
    print(f'item.left.id:                        {item.left.id()}')
    print(f'item.left.state:                     {item.left.state()}')
    print(f'item.left.time:                      {item.left.time()}')
    print(f'item.left.gp:                        {item.left.gp()}')
    print(f'item.left:                           {item.left()}')
    print(f'item.right.id:                       {item.right.id()}')
    print(f'item.right.state:                    {item.right.state()}')
    print(f'item.right.time:                     {item.right.time()}')
    print(f'item.right.gp:                       {item.right.gp()}')

    print(f'key:                                 {key()}')
    # print(f'key.GetActKey:                       {key.GetActKey("BumpL")}')
    # print(f'key.GetActKey1:                      {key.GetActKey1("BumpL")}')
    # print(f'key.GetActKey2:                      {key.GetActKey2("BumpL")}')
    # print(f'key.GetActLabel:                     {key.GetActLabel("BumpL")}')

    print(f'loc:                                 {loc()}')
    print(f'loc.id:                              {loc.id()}')
    print(f'loc.name:                            {loc.name()}')
    print(f'loc.stars:                           {loc.stars()}')
    print(f'loc.begin:                           {loc.begin()}')
    print(f'loc.loop:                            {loc.loop()}')
    print(f'loc.bestTime:                        {loc.bestTime()}')
    print(f'loc.averageTime:                     {loc.averageTime()}')
    print(f'loc.isQuest:                         {loc.isQuest()}')
    print(f'loc.gp:                              {loc.gp()}')

    print(f'time:                                {time()}')
    print(f'totaltime:                           {totaltime()}')

    # print(f'music:                              {music()}')

    print(f'pickup:                              {pickup()}')
    print(f'pickup.distance:                     {pickup.distance()}')
    print(f'pickup.z:                            {pickup.z()}')

    print(f'player.direction:                    {player.direction()}')
    print(f'player.framesPerMove:                {player.framesPerMove()}')
    print(f'player.name:                         {player.name()}')
    print(f'player.GetNextLegendName:            {player.GetNextLegendName()}')

    print(f'pos.x:                               {pos.x()}')
    print(f'pos.y:                               {pos.y()}')
    print(f'pos.z:                               {pos.z()}')

    print(f'res.stone:                           {res.stone()}')
    print(f'res.wood:                            {res.wood()}')
    print(f'res.tar:                             {res.tar()}')
    print(f'res.ki:                              {res.ki()}')
    print(f'res.bronze:                          {res.bronze()}')
    print(f'res.crystals:                        {res.crystals()}')

    print(f'screen.i:                            {screen.i()}')
    print(f'screen.x:                            {screen.x()}')
    print(f'screen.w:                            {screen.w()}')
    print(f'screen.h:                            {screen.h()}')
    print(f'screen.FromWorldX:                   {screen.FromWorldX(10)}')
    print(f'screen.FromWorldZ:                   {screen.FromWorldZ(10)}')
    print(f'screen.ToWorldX:                     {screen.ToWorldX(10)}')
    print(f'screen.ToWorldZ:                     {screen.ToWorldZ(10)}')

    print(f'summon.count:                        {summon.count()}')
    print(f'summon.GetId:                        {summon.GetId()}')
    print(f'summon.GetName:                      {summon.GetName()}')
    print(f'summon.GetVar:                       {summon.GetVar("cinderwisp")}')
    print(f'summon.GetState:                     {summon.GetState()}')
    print(f'summon.GetTime:                      {summon.GetTime()}')

def print_test():
    tt = totaltime()
    h = screen.h()
    p = tt % h
    # SSRPGInterface.ssrpgif.call_command(">", "`1," + str(p) + "," + "hello python!")
    command.Print(f"`1,{p},hello python!")
    command.Print(tt, x = p * 3, y = p)

import random
def equip_test():
    e = ["poison", "vigor", "arhter", "fire", "ice"]
    w = ["sword", "wand"]
    s = ["sight", "star", "experience", "ki", "quest", "ouroboros", "fissure", "triskelion", "moon"]
    command.EquipL(random.choice(e), random.choice(w))
    command.EquipR(random.choice(s))

def pause():
    loc.Pause()
    exit()

if __name__ == "__main__":
    # Run the interface
    SSRPGInterface.run_script(teststep)
    # SSRPGInterface.run(pause)

# sys.MindConnect()