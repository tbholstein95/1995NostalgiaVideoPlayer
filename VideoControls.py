import vlc
import time

parseReady = 0

def ParseReceived(event):
    global parseReady
    #set a flag that your data is ready
    parseReady = 1


def playvideo():
    media_player = vlc.MediaPlayer()
    media = vlc.Media("1.mp4")
    media_player.set_media(media)
    media.parse_with_options(1,0)
    while True:
        if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
            break
        print("big boy")
        value = media.get_duration()
    media_player.play()
    #value = vlc.libvlc_media_player_get_length(media_player)
    time.sleep(value/1000)
    media_player.stop()

    # ...
    # events = media_player.event_manager()
    # events.event_attach(vlc.EventType.MediaParsedChanged, ParseReceived)
    # ...
    # parseReady = 0
    # media.parse_with_options(1, 0)
    # while parseReady == 0:
    #  print("working on it")
    #
    # # Once the flag is set, your data is ready
    # print(media.get_parsed_status())
    # print (media.get_duration())


