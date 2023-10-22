import os
from modules.whisper_Inference import WhisperInference
from modules.faster_whisper_inference import FasterWhisperInference
from modules.nllb_inference import NLLBInference
from modules.youtube_manager import get_ytmetas

class App:
    def __init__(self):
        self.whisper_inf = FasterWhisperInference()  # Change this to use the faster whisper implementation
        self.nllb_inf = NLLBInference()

    @staticmethod
    def open_folder(folder_path: str):
        if os.path.exists(folder_path):
            os.system(f"start {folder_path}")
        else:
            print(f"The folder {folder_path} does not exist.")

    def transcribe_file(self, input_file, model_size, lang, file_format, translate, timestamp, beam_size, log_prob_threshold, no_speech_threshold, compute_type):
        # Your transcribe file logic here


if __name__ == "__main__":
    app = App()
    app.launch()
