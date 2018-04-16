# for linux?
#from pydub import AudioSegment
from pygame import mixer # Load the required library
import matplotlib.pyplot as plt
#import vlc

# wav, mp3, ogg, flv, (need ffmpeg supports ->)mp4, wma, aac 
#sound = AudioSegment.from_file("sound.m4a", "m4a")
path = u".\\sound\\sound.mp3"
print( path )

# for windows
#pip install playsound
import playsound
playsound.playsound(path, True)

"""
p = vlc.MediaPlayer(path)
p.play()
"""

"""
mixer.init()
mixer.music.load(path)
mixer.music.play()
"""

"""
#for linux
sound = AudioSegment.from_mp3(path)
#チャンネル数(1:mono, 2:stereo)
channel_count = sound.channels
print( 'チャンネル数：' + str(channel_count ) )

#サンプルレート(Hz)
frames_per_second = sound.frame_rate
print( 'サンプルレート：' + str(frames_per_second ) )

#再生時間(秒)
duration = sound.duration_seconds
print( '再生時間（秒）：' + str(duration ) )

samples = sound.get_array_of_samples()
sample2 = samples[30000:30500]

sound.export('mashup.mp3', format='mp3', tags={'artist': 'Various artists', 'album': 'Best of 2017', 'comments': 'This album is awesome!'})
plt.plot(sample2)
plt.show()
"""
