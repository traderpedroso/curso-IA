FROM python:3


WORKDIR /root

COPY requirements.txt ./
ADD main.py /
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]