from pydub import AudioSegment

import os

class RTTM2TTS : 
    
    def __init__ (self, rttm_path, audio_path, output_path) : 
        self.rttm_path = rttm_path
        self.audio_path = audio_path
        self.output_path = output_path

        self.segments = []

    def read_rttm (self) : 

        # rttm format : [0]EVENT [1]FILENAME [2]CHANNEL [3]START [4]END [5]<NA> [6]<NA> [7]SPEAKER_ID [8]<NA> [9]<NA>
        with open ("../data/sample.rttm", "r") as rttm : 
            for line in rttm : 
                parts = line.strip().split()
                if (parts[0] == "speaker") : 
                    start, end, speaker = float(parts[3]), float(parts[4]), start[7]
                    self.segments.append((speaker, start, end))

                    
if (__name__ == "__main__") :
