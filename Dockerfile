FROM python:3.11-slim

WORKDIR /app
 
COPY ./src/ /app

#  Update apt and install Pip and FFMPEG
RUN apt-get update && \
    apt-get install -y python3-pip ffmpeg

# Install our project dependencies
RUN python -m pip install -r requirements.txt

CMD ["python", "main.py"]