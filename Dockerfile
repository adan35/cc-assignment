FROM python:3
WORKDIR /cc
ADD . /cc
RUN pip3 install -r requirements.txt
CMD ["python", "main.py"]