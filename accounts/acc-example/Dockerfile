FROM python:3.6
RUN mkdir /code
RUN mkdir /config
RUN mkdir /personal
ENV TZ=America/Sao_Paulo
RUN echo $TZ > /etc/timezone && \
    rm /etc/localtime && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata
RUN apt update && apt -y install xvfb
RUN pip install --upgrade pip
RUN pip install --upgrade schedule
WORKDIR /code
COPY /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt