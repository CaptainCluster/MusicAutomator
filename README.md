# MusicTimer

NOTE!

Before you can enjoy everything this program has to offer, you need to make a few configurations!
There are also multiple dependencies, thus a few installations have to be done.

---
This music player boots up and turns off automatically. It plays all the songs in a directory (the playlist) that the user 
has chosen. Like with most other music players, users can navigate the playlist by skipping songs or playing the previous 
ones. The user can determine what keys to use for these actions.

---
DEPENDENCIES

Use the Python package installer (pip) to install the dependencies

keyboard for reading inputs (to navigate the playlist): 
``` pip install keyboard ```

schedule to end the program automatically:
``` pip install schedule ```

python-vlc to play the songs:
``` pip install python-vlc ```

---
In order to get the program to bootup automatically, use the task scheduler program that should be installed on your
Windows device. Although you can also put the end timer there, it's not necessary as that is programmed as part
of this program. If you wish to end the program via task scheduler, it is possible as you can disable the endtimer
functionality the program comes with.

<img width="590" alt="image" src="https://github.com/CaptainCluster/MusicTimer/assets/121576355/1ed8f04f-1ebe-4d3e-8649-bc63c7700923">

Before you can use the program, the SETTINGS class has to be customized, as that determines how the program behaves.
skipInput and goBackInput determine how the playlist can be navigated. In the example, alt+v makes the program skip 
a song and alt+b makes the program go back to the previous song. endTime determined when the program stops running. 
directory indicates the playlist. Copy and paste the folder that contains your songs. If you wish to stop the program
from shutting down at a certain time or want to disable user interaction with the playlist, that can be done by
turning any of the boolean values in the SETTINGS class from True (the default value) to false.
