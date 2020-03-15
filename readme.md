The same text for question 4 and 5 are written in .py file

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