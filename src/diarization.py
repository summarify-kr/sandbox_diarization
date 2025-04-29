from pyannote.audio import Pipeline
import torch

from dotenv import load_dotenv
import os

import warnings
warnings.filterwarnings("ignore", category = SyntaxWarning)
warnings.filterwarnings("ignore", category = UserWarning)

if (__name__ == "__main__") : 

    load_dotenv(dotenv_path="../.env")

    api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token = api_key)

    pipeline.to(torch.device("cpu"))

    path = "../data/sample.wav"
    diarization = pipeline(path)

    with open ("../data/sample.rttm", "w") as rttm : 
        diarization.write_rttm(rttm)

    '''
    for turn, _, speaker in diarization.itertracks(yield_label = True) :
        print(f"start={turn.start : .1f}s stop={turn.end : .1f}s speaker_{speaker}")
    '''
