FROM heroku/miniconda:3

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
# RUN conda install --yes pandas

CMD gunicorn --bind 0.0.0.0:$PORT app:app
