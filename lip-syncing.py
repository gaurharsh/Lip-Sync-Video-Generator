import moviepy.editor as mp

def lip_sync_video(video_path, audio_path, output_path):
    # Convert MP3 audio to WAV format
    wav_path = 'temp_audio.wav'
    audio = mp.AudioFileClip(audio_path)
    audio.write_audiofile(wav_path, codec='pcm_s16le')

    # Load the video and WAV audio files
    video = mp.VideoFileClip(video_path)
    audio = mp.AudioFileClip(wav_path)

    # Check if audio duration is shorter than the video duration
    if audio.duration < video.duration:
        # Loop the audio to match the video duration
        loops = int(video.duration // audio.duration) + 1
        audio = mp.concatenate_audioclips([audio] * loops)

    # Set the audio duration to match the video duration
    audio = audio.set_duration(video.duration)

    # Set the audio to follow the mouth movements in the video
    synced_audio = mp.CompositeAudioClip([audio])
    synced_audio = synced_audio.set_start(0)  # Set the audio start time

    # Set the audio as the audio track of the video
    video = video.set_audio(synced_audio)

    # Write the final video with lip-synced audio
    video.write_videofile(output_path, codec='libx264')

    # Close the audio clip objects
    audio.close()

# Example usage
video_path = "C:\\Users\\HARSH VARDHAN SINGH\\Desktop\\PYTHON Project\\bba.mp4"
audio_path = "C:\\Users\\HARSH VARDHAN SINGH\\Desktop\\PYTHON Project\\baba.mp3"
output_path = "C:\\Users\\HARSH VARDHAN SINGH\\Desktop\\PYTHON Project\\output_video1.mp4"

lip_sync_video(video_path, audio_path, output_path)
