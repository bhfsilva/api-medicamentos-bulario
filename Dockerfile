FROM python:3.12-slim-bullseye

WORKDIR /app
COPY . .

# install python and chrome linux requirements
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    unzip \
    bzip2 \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxcb1 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon-x11-0 \
    libxcomposite-dev \
    libxdamage1 \
    libxext6 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libpango-1.0-0 \
    libcairo2 \ 
    libasound2 \
    libdbus-glib-1-2 \
    libxt6 \
    libx11-xcb1 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libxtst6 \
    libgtk-3-0 \
    xdg-utils \
    --no-install-recommends

ADD https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/linux64/chrome-linux64.zip /opt/
RUN unzip /opt/chrome-linux64.zip -d /opt/

ADD https://storage.googleapis.com/chrome-for-testing-public/131.0.6778.264/linux64/chromedriver-linux64.zip /opt/
RUN unzip /opt/chromedriver-linux64.zip -d /opt/

# RUN chmod +x /opt/chrome-linux64.zip /opt/chromedriver-linux64.zip
RUN rm /opt/chrome*.zip

EXPOSE 8000

ENTRYPOINT ["fastapi", "run", "main.py"]
