# Utiliza una imagen base de Python
FROM python:3.11-slim

ENV SERVICE_NAME=aws-credentials-python

# Instala todas las dependencias del sistema necesarias para Chrome
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg \
    libatk-bridge2.0-0 libgtk-3-0 libatk1.0-0 \
    libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 \
    libx11-xcb1 libxcomposite1 libxrandr2 libxdamage1 \
    libxi6 libxtst6 libnss3-dev libxss1 libasound2 \
    xauth xvfb libgbm1 libxshmfence1 \
    libpci3 libxinerama1 libxcursor1 \
    && rm -rf /var/lib/apt/lists/*

# Descargar e instalar Google Chrome
RUN wget -O /tmp/chrome-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/128.0.6613.119/linux64/chrome-linux64.zip && \
    unzip /tmp/chrome-linux64.zip -d /opt/ && \
    chmod +x /opt/chrome-linux64/chrome && \
    rm /tmp/chrome-linux64.zip && \
    #ln -s /opt/chrome/chrome /usr/bin/google-chrome && \
    ln -s /opt/chrome-linux64/chrome /usr/local/bin && \
    echo "Verificando la instalación de Chrome:" && \
    chrome --version && \
    echo "Symlink creado en /usr/bin/google-chrome"


# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al contenedor
COPY . /app

RUN chmod +x /app/chromedriver && \
    ln -s /app/chromedriver /usr/local/bin

# Instala las dependencias de Python --no-cache-dir
#RUN pip install -r requirements.txt

# Define las opciones de Chrome para Selenium
ENV CHROME_BIN=/usr/local/bin/chrome
ENV CHROMEDRIVER_BIN=/usr/local/bin/chromedriver

# Establecer la variable de entorno PYTHONPATH para incluir el directorio actual y el submódulo
ENV PYTHONPATH="./.python_packages/lib/site-packages:${PYTHONPATH}"

# Imprimimos los valores de las variables de entorno
RUN echo "CHROME_BIN: $CHROME_BIN"
RUN echo "CHROMEDRIVER_BIN: $CHROMEDRIVER_BIN"

#mostrar la versión de python y los modulos instalados
RUN python --version
RUN pip --version
RUN py -m venv venv
RUN source venv/bin/activate
#RUN venv\Scripts\activate
RUN pip install --no-cache-dir -r requirements.txt
RUN pip list


# Comando para ejecutar tu script de automatización
CMD ["python", "run.py"]
