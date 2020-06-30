FROM python:3.7

RUN mkdir -p /srv
WORKDIR /srv
COPY requirements.txt /srv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY src/ /srv

# ENTRYPOINT ["python","/srv/run_classification.py"]
