import streamlit as st
import av
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

st.set_page_config(page_title="ID Guard Camera")

st.title("🪪 ID Guard")
st.write("Live camera test — AI detection will be added later.")

class CameraProcessor(VideoProcessorBase):
    def recv(self, frame):
        # Receive each frame from the webcam.
        # Return it unchanged so we can see the live video.
        return frame

webrtc_streamer(
    key="id-guard-camera",
    video_processor_factory=CameraProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False
    },
    async_processing=True
)
