FROM python:3.5
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . /capra
WORKDIR /capra

CMD ["/capra/start_capra.sh"]
