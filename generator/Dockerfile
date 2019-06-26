FROM continuumio/miniconda3

RUN pip install faker
RUN pip install psycopg2-binary
ADD generator.py /
CMD [ "python", "./generator.py" ]
