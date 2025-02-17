#reprodutor mp3
from pygame import mixer
mixer.init()
mixer.music.load('musica21.mp3')
mixer.music.play()
input('\033[31mPrecione enter para encerrar\033[m')
mixer.music.stop()
