FROM python:2.7-alpine

ENV FLASK_APP index.py

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]

# build example : docker build -t search-engine-ui .
# run example : docker run -p 80:5000 -e "HOST=<ip>" -e "PORT=<port>" -e "USERNAME=<username>" -e "PASSWORD=<password>" search-engine-ui
