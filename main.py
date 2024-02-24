import random
import math

def isFirstSix(i):
  if (i+1 <= 6):
    firstSix = 100
    return True
  else:
    firstSix = 0
    return False

def multishot(ms):
  if (isinstance(ms, int)):
    return ms
  else:
    chanceOfHigher = ms % 1
    lower = int(ms)
    higher = lower+1

    if (random.uniform(0, 1)<=chanceOfHigher):
      return higher
    else:
      return lower

#constants
numSims = 10000
factionMods = 1.9
firstSix = 100
multiShot = 3.3

#test1
totalDmg1 = 0;
for s in range(numSims):
  simDmg = 0
  numHeatProcs = 0
  for i in range(9): ##no corpus mods, 3.3 multishot
    rolledMS = multishot(multiShot)

    #print('index:', i+1)
    if (isFirstSix(i)): #add heat procs for first 6s
      for m in range(rolledMS):
        if (random.uniform(0, 1)<=.68):
          numHeatProcs = numHeatProcs+1
    simDmg = simDmg+(firstSix*rolledMS)+(100*numHeatProcs) #add dmg
    
    ##per second prints
    #print('Number of heat procs:', numHeatProcs)
    #print('Multishot:', rolledMS)
    #print()
  
  #per sim calcs
  totalDmg1 = totalDmg1 + simDmg

  ##per sim prints
  #print('SimDmg:', simDmg)
  #print()
  

#test1 calcs
avgDmg1 = totalDmg1 / numSims

#test1 prints
print('No faction mods', multiShot, 'multishot')
print('Total Damage Dealt:', totalDmg1)
print('Average Damage Dealt', avgDmg1)
print()



#test2
totalDmg2 = 0
for s in range(numSims):
  simDmg = 0
  numHeatProcs = 0
  for i in range(9): ##no corpus mods, 3.3 multishot
    rolledMS = multishot(multiShot)

    #print('index:', i+1)
    if (isFirstSix(i)): #add heat procs for first 6s
      for m in range(rolledMS):
        if (random.uniform(0, 1)<=.68):
          numHeatProcs = numHeatProcs+1
    simDmg = simDmg+(firstSix*rolledMS*factionMods)+(100*numHeatProcs*factionMods**2) #add dmg
    
    ##per second prints
    #print('Number of heat procs:', numHeatProcs)
    #print('Multishot:', rolledMS)
    #print()
  
  #per sim calcs
  totalDmg2 = totalDmg2 + simDmg

  ##per sim prints
  #print('SimDmg:', simDmg)
  #print()

#test2 calcs
avgDmg2 = totalDmg2 / numSims

#test2 prints
print(factionMods, 'times faction damage', multiShot, 'multishot')
print('Total Damage Dealt:', totalDmg2)
print('Average Damage Dealt', avgDmg2)
print()

#final prints
print('DPS increase from', factionMods, 'times faction multiplier:')
print(round(totalDmg2/totalDmg1, 3), 'x', sep='')
