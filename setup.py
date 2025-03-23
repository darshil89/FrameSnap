from setuptools import setup, find_packages

setup(
    name="video_frame_extractor",
    version="1",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
    ],
    entry_points={
        "console_scripts": [
            "extract-frames=video_frame_extractor.cli:main",
        ],
    },
    author="Darshil",
    description="A Python library to extract frames from videos and save them as images.",
    url="https://github.com/darshil89/video-frame-extractor",
)
