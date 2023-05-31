## voice-assistant

Voice assistants, with Whisper, GPT-3.5 Turbo, Google Text to Speech API and Voicevox for voice changing and natural voice like in Japanese.
### Requirements

**Must have voicevox engine installed**<br>
[VOICEVOX_DOWNLOAD](https://voicevox.hiroshiba.jp/) <br>

**After Installation keep the engine or voicevox application running during the execution of the program**

### Installation
There are 2 options available for running the project, `.ipynb` or `.py` file

> Refer to this if you want to run the project via `.ipynb` file [Coming Soon]()
<br>

For `.py` file running
Install libraries and dependencies <br>

```pip install -r requirements.txt```

<br>

Generate the `.mp3` file via [ffmpeg](https://ffmpeg.org/download.html): <br>

```ffmpeg -f lavfi -i anullsrc=r=44100:cl=mono -t 10 -q:a 9 -acodec libmp3lame audio_response.mp3```
<br>

Run: <br>
```python3 voice_assistant.py```

