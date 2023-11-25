#Github: CaptainCluster | https://github.com/CaptainCluster

from settings import SETTINGS 
import modules.endtimer as endtimer
import os
import vlc
import keyboard
import time

def userInteractions(mediaPlayer, settings, songNumber) -> int:
    """Defining what defined user inputs do 

    Args:
        mediaPlayer (vlcInstance): The media player variable containing the music file being processed
        settings (Settings): a class that contains the settings
        songNumber (int): the number of the song in the playlist

    Returns:
        int: the song number 
    """
    try:
        #Running until the song ends, or user ends manually
        while mediaPlayer.get_state() != vlc.State.Ended:
            paused = False
            if settings.endTimeEnabled:
                endtimer.checkEndTimer()                #Due to the way this loop iterates, we check the endtimer over here
            if settings.skipEnabled:
                if keyboard.is_pressed(settings.skipInput):
                    break
            #User wants to go back ==> Adjusting the song's position by n-2
            #n-2 is used instead of n-1 due to +1 being added at the end of the 2nd while-loop at playMusic()

            if settings.goBackEnabled:
                if keyboard.is_pressed(settings.goBackInput):
                    if songNumber != 0:
                        songNumber = songNumber - 2     #Adjusted to -1... the 2nd while-loop at playMusic function
                    else:
                        songNumber = -1                 #Adjusted to 0... the 2nd while-loop at playMusic function
                    break
            
            if settings.pauseEnabled:
                if keyboard.is_pressed(settings.pauseInput):
                    if paused:
                        mediaPlayer.resume()
                        paused = False
                    else:
                        mediaPlayer.pause()
                        paused = True
            
        return songNumber
    except Exception:
        print("An error has occurred in the process.")

    
def playMusic() -> None:
    """Playing the music
    """
    try:
        settings = SETTINGS() #A settings object to access a set of fixed values
        if settings.endTimeEnabled:
            endtimer.createSchedule()

        #Preparing the playlist, VLC instance and VLC media player
        directoryContent    = os.listdir(settings.directory) 
        vlcInstance         = vlc.Instance()
        mediaPlayer         = vlcInstance.media_player_new()

        songNumber = 0 

        #The music player will run in this while-loop (each iteration is done when the song changes).
        while True:
            musicFile = directoryContent[songNumber] 
            musicFilePath = os.path.join(settings.directory, musicFile) #Merging the directory with the file name 

            time.sleep(0.5) #A delay to avoid issues (for instance, skipping more than one song by sending one defined input)

            #Handling the media for the vlc and playing the song
            vlcMedia = vlcInstance.media_new(musicFilePath) 
            mediaPlayer.set_media(vlcMedia)
            mediaPlayer.play()

            if settings.notifyPlay:
                print("Now playing " + musicFile)

            #Now that the song should be playing, the program prepares to respond to user inputs
            songNumber = userInteractions(mediaPlayer, settings, songNumber)      
            mediaPlayer.stop()

            songNumber += 1 #Increasing the value by one to, on default, move onto the next file on the directory (playlist)

    except Exception:
        print("An error has occurred in the process.")
