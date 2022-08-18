import VideoControls as videoController



if __name__ == '__main__':
    videoC = videoController.VideoController()
    videoC.add_shows()
    videoC.add_commercials()
    videoC.playvideo()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
