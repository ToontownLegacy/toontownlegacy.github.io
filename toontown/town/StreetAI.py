from toontown.dna.DNASpawnerAI import DNASpawnerAI
from toontown.suit.DistributedSuitPlannerAI import DistributedSuitPlannerAI

from toontown.toonbase import ToontownGlobals

class StreetAI:
    """
    AI-side representation of everything in a single street.

    One subclass of this class exists for every neighborhood in the game.
    StreetAIs are responsible for spawning all SuitPlanners,ponds, and other
    street objects, etc.
    """
    
    def __init__(self, air, zoneId):
        self.air = air
        self.zoneId = zoneId

        if (self.zoneId % 1000 != 0):
            self.spawnObjects()
    
    def spawnObjects(self):
        filename = self.air.genDNAFileName(self.zoneId)
        DNASpawnerAI().spawnObjects(filename, self.zoneId)