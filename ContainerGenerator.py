from Container import *
import random

class ContainerGenerator():
    def Get(self):
        result = []

        allnumbers = self.GetShuffledNumbers()

        for i in range(0, 30, 6):
            posY = 540-(10*i)
            block = []
            for j in range(i, i+6):
                posX = 0+(60 * (j % 6))
                newContainer = Container(allnumbers[j], posX, posY)
                block.append(newContainer)
            result.append(block)

        return result

    def GetShuffledNumbers(self):
        allnumbers = []

        for i in range(6):
            allnumbers.extend(range(1, 6))

        random.shuffle(allnumbers)
        return allnumbers