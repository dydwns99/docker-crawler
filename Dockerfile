FROM python:3.8 

ENV PYTHONUNBUFFERED 1 

RUN apt-get -y update 
RUN apt-get -y install vim # docker 안에서 vi 설치 안해도됨

RUN mkdir /srv/docker-server # docker안에 srv/docker-server 폴더 생성
ADD . /srv/docker-server 

WORKDIR /srv/docker-server 

RUN pip install --upgrade pip # pip 업글
Run pip install wget

Run apt install default-jdk -y # java 설치

RUN pip install -r requirements.txt # 필수 패키지 설치

#Chrome 설치
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \ 
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
RUN apt-get update && apt-get -y install google-chrome-stable
Run google-chrome --version

# Chrome driver 설치
RUN wget -N http://chromedriver.storage.googleapis.com/106.0.5249.61/chromedriver_linux64.zip -P /srv/docker-server
Run unzip /srv/docker-server/chromedriver_linux64.zip

RUN /srv/docker-server/chromedriver

EXPOSE 9515
CMD ["python3", "manage.py", "runserver", "0.0.0.0:9515"]
