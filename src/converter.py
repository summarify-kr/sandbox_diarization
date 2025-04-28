from pydub import AudioSegment
import os

def convert_m4a_to_wav (m4a_path, wav_path) : 
    
    audio = AudioSegment.from_file(m4a_path, format = "m4a")

    audio.export(wav_path, format = "wav")

if (__name__ == "__main__") : 
    m4a_file = "../data/sample.m4a"
    wav_file = "../data/sample.wav"

    convert_m4a_to_wav(m4a_file, wav_file)
    print("Convert Completed")