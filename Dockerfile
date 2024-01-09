FROM python:3.11

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

RUN mkdir /parser
COPY . /parser/
WORKDIR /parser

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ENTRYPOINT [ "python", "main.py" ]
CMD [ "python", "main.py" ]