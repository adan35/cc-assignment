FROM python:3
WORKDIR /cc
ADD . /cc
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD ["python", "main.py"]