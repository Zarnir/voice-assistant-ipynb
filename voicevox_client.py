from voicevox import Client
import asyncio


async def voice_vox(input_text = 'おはよう'):
    async with Client() as client:
        audio_query = await client.create_audio_query(
            input_text,
            speaker=2,
        )
        with open('audio_response.mp3', 'wb') as f:
            f.write(await audio_query.synthesis(speaker=2))

def run (input_text):
    asyncio.run(voice_vox(input_text))
    return 'audio_response.mp3'