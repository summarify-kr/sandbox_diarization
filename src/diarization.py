from pyannote.audio import Pipeline
import torch

from dotenv import load_dotenv
import os

import warnings
warnings.filterwarnings("ignore", category = SyntaxWarning)

if (__name__ == "__main__") : 

    load_dotenv()

    api_key = os.getenv("HUGGINGFACE_ACCESS_TOKEN")

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token = api_key)

    pipeline.to(torch.device("cuda"))

    path = "../data/sample.wav"
    diarization = pipeline(path)

    for turn, _, speaker in diarization.itertracks(yield_label = True) :
        print(f"start={turn.start : .1f}s stop={turn.end : .1f}s speaker_{speaker}")
