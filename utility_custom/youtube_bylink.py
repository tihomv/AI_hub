import cv2
from pytube import YouTube
import os

def play_youtube_video(url):
    # Download the video from YouTube
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    video_path = stream.download()

    # Play the downloaded video using OpenCV
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('YouTube Video', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything is done, release the video capture object
    cap.release()

    # Closes all the frames
    cv2.destroyAllWindows()

    # Optionally, remove the downloaded video file after playing
    os.remove(video_path)

# Example usage
youtube_url = 'https://www.youtube.com/watch?v=mCbCHbMCgoU'
play_youtube_video(youtube_url)
