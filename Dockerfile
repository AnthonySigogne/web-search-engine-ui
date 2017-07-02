FROM python:3.5-alpine

ENV FLASK_APP index.py

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD [ "flask", "run", "--host=0.0.0.0" ]

# build example : docker build -t web-search-engine-ui .
# run example : docker run -p 80:5000 -e "HOST=<ip>" -e "PORT=<port>" web-search-engine-ui
