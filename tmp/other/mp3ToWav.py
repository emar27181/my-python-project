import librosa
import soundfile as sf


y, sr = librosa.core.load('src/assets/sayonara_01.wav', sr=11025,
                          mono=True)  # 22050Hz、モノラルで読み込み
sf.write("new_sayonara_01.wav", y, sr, subtype="PCM_16")  # 1

y, sr = librosa.core.load('src/assets/sayonara_02.wav', sr=11025,
                          mono=True)  # 22050Hz、モノラルで読み込み
sf.write("new_sayonara_02.wav", y, sr, subtype="PCM_16")  # 1

"""
y, sr = librosa.core.load('sayonara_01.wav', sr=11025, mono=True) # 22050Hz、モノラルで読み込み
sf.write("new_sayonara_01.wav", y, sr, subtype="PCM_16") #1

y, sr = librosa.core.load('sayonara_02.wav', sr=11025, mono=True) # 22050Hz、モノラルで読み込み
sf.write("new_sayonara_02.wav", y, sr, subtype="PCM_16") #1
"""
