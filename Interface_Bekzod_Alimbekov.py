class Teams:
    def __init__(self,members):
        self.__myTeam = members
    #def __len__(self):
    #    return len(self.__myTeam)
    def __contains__(self,member):
        return member in self.__myTeam
    def __iter__(self):
        self.iterator = iter(self.__myTeam)
    def __next__(self):
        return next(self.iterator)

def main():
    classmates = Teams(['John','Steve','Tim'])

    # 1 Using __contains__ protocol
    #print('Tim' in classmates)
    print(classmates.__contains__('Steve'))

    # 2 Using __iter__ protocol
    classmates.__iter__()
    #print(classmates.__next__())
    #print(classmates.__next__())

    # 3 Determining if Class classmates has __len__ method
    try:
        print(classmates.__len__())
    except AttributeError as atErr:
        print(f"{classmates} has no Len protocol enabled, Error: {atErr}")

    #print(classmates.__len__())
    #print(len(classmates))

main()

# 4 Explain the difference between interfaces and implementation.
""" Interfaces are named enpoints, ie publicly available connection points which allow interaction with an object.
There is no need to know what happens under the hood, as long as we know how to call a method and pass an attribute to that method.
Implementation on other hand is the sequence that happens behind the scenes.""" 

# 5 Using both visual and written descriptions, think through the interface-implementation of a large scale storage system.
""" The interface of a large scale storage system would need to be compatible and compliant with current standards.
First we need to decide which standard shall be used. Let say we decide to go with new ZFS file system.
Next we need to study this file system and its capabilities. Based on capabilities we need to create an interface for actions we want to perform.
Example capabilities / Interfaces: Read, Write, Edit and copy would be a great start.
Ofcorse there needs to be an implemantion step to perform all these actions to files going in and out of the disks
Finally we need to account for a different device types and this can be done on platform bases. Each device will be exposing its interface to the platform software
Using these interface we can transfer data back and forth."""