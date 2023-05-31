# Import all of the necessary libraries
import whisper
import gradio as gr
import openai
from gtts import gTTS
from voicevox_client import run
from constants import KEYS

# Global variables for whisper base model
# Load base model of the whisper
model = whisper.load_model('base')
model.device

# Define a function to pass the input to chatGPT api
def chat_completion_gpt(text: str):
  messages = [{'role': 'user', 'content': text }] if text else [{ 'role': 'system', 'content': 'Goodbye have a nice day' }]

  response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = messages,
  )

  return response.choices[0].message.content

def text_voice(input_text, language = 'en'):
  generated_audio = gTTS(
    text = input_text,
    lang = language,
    slow = False,
  )

  generated_audio.save('audio_response.mp3')

  return 'audio_response.mp3'

# Define a function to transcribe the 
def transcribe_audio(audio):

  # Load the audio and trim it to fit 30s
  audio = whisper.load_audio(audio)
  audio = whisper.pad_or_trim(audio)

  # make log-Mel spectrogram and move to the same device as the model
  mel = whisper.log_mel_spectrogram(audio).to(model.device)

  # Detect the language
  _, probs = model.detect_language(mel)
  print(f'Detected Language: {max(probs, key = probs.get)}')
  language = max(probs, key = probs.get)

  # Decode the the audio
  options = whisper.DecodingOptions()
  decode_obj = whisper.decode(model, mel, options)
  text = decode_obj.text
  
  # Pass the result to the chatGPT
  response = chat_completion_gpt(text)

  # Call the text_to_voice function
  result = run(input_text = response) if language == 'ja' else text_voice(input_text = response, language = language)

  return [text, response, result]

# Run with gradio interface
def run_gradio():
    speech_text = gr.Textbox(label = 'Speech to text')
    response_text = gr.Textbox(label = 'Response in text')
    text_speech = gr.Audio('audio_response.mp3')

    gr.Interface(
    title = 'Voice assistant with ChatGPT Whisper and Google Voice Generation',
    fn = transcribe_audio,
    inputs = [gr.inputs.Audio(source = 'microphone', type = 'filepath')],
    outputs = [
        speech_text,
        response_text,
        text_speech,
    ],
    live = True,
    ).launch(share = True)


def main():
    # Load openai api key
    openai.api_key = KEYS['OPEN_AI']

    # Launch the gradio interface and call transcribe_audio within it
    run_gradio()

main()
