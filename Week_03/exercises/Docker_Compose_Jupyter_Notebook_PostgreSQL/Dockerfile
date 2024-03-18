FROM jupyter/datascience-notebook

# Install additional Python libraries
RUN pip install psycopg2-binary
RUN pip install --upgrade 'sqlalchemy<2.0'

# Add files
ADD  apartments_data_prepared.csv /home/jovyan/work/
ADD jupyter_postgres_db.ipynb /home/jovyan/work/

WORKDIR /home/jovyan/work/