
# UltimakerVideoRecording

Python script for recording the video stream of an Ultimaker's build in camera.
Tested with Ultimaker S5 on MacOS.

## Requirements

- python3
- OpenCV (opencv-python)

## Usage

```bash
python record.py <IP_address>
```

After setting up a network connection
you can read the IP-adress from the printer by navigating to `Settings > Network`.
To check if the adress is working,
you can add the printer to cura to access the camera.

