import argparse
from modules.whisper_Inference import WhisperInference
from modules.faster_whisper_inference import FasterWhisperInference
from modules.nllb_inference import NLLBInference
import os


class App:
    def __init__(self, args):
        self.folder_name = "simpsons"
        self.args = args
        self.whisper_inf = (
            WhisperInference()
            if self.args.disable_faster_whisper
            else FasterWhisperInference()
        )
        if isinstance(self.whisper_inf, FasterWhisperInference):
            print("Use Faster Whisper implementation")
        else:
            print("Use Open AI Whisper implementation")
        print(f'Device "{self.whisper_inf.device}" is detected')
        self.nllb_inf = NLLBInference()

    def paths(self) -> list:
        all_files = []
        for root, dirs, files in os.walk(f"/home/elios/audios/{self.folder_name}/"):
            for file in files:
                file_path = os.path.join(root, file)
                all_files.append(file_path)
        return sorted(all_files)

    def launch(self):
        model_size = "large-v3"  # Set your desired model size
        lang = "italian"  # Set your desired source language
        file_format = "SRT"  # Set your desired output format
        istranslate = False  # Set to True if you want to enable translation
        add_timestamp = False  # Set to True if you want to add a timestamp
        beam_size = 2  # Set your desired beam size
        log_prob_threshold = -0.8  # Set your desired log probability threshold
        no_speech_threshold = 0.5  # Set your desired no_speech threshold
        compute_type = "float32"  # Set your desired compute type

        self.whisper_inf.transcribe_file(
            self.paths(),
            model_size,
            lang,
            file_format,
            istranslate,
            add_timestamp,
            beam_size,
            log_prob_threshold,
            no_speech_threshold,
            compute_type,
            self.folder_name
        )
        #     btn_run.click(fn=self.whisper_inf.transcribe_youtube,
        #                   inputs=params + advanced_params,
        #                   outputs=[tb_indicator])

        #     btn_run.click(fn=self.whisper_inf.transcribe_mic,
        #                   inputs=params + advanced_params,
        #                   outputs=[tb_indicator])

        #     btn_run.click(fn=self.nllb_inf.translate_file,
        #                   inputs=[file_subs, dd_nllb_model, dd_nllb_sourcelang, dd_nllb_targetlang, cb_timestamp],
        #                   outputs=[tb_indicator])


# Create the parser for command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    "--disable_faster_whisper",
    type=bool,
    default=False,
    nargs="?",
    const=True,
    help="Disable the faster_whisper implementation. faster_whipser is implemented by https://github.com/guillaumekln/faster-whisper",
)
_args = parser.parse_args()

if __name__ == "__main__":
    app = App(args=_args)
    app.launch()
