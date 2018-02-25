FROM heroku/miniconda:3

ADD requirements.txt /app/requirements.txt
WORKDIR /app

RUN pip install -r requirements.txt
RUN conda install --yes pandas scikit-learn

COPY . /app

CMD gunicorn --bind 0.0.0.0:$PORT app:app
