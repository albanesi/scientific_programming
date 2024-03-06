#-------------------------------------------------------------------------------
# Docker: Jupyter notebook with PostgreSQL database
#-------------------------------------------------------------------------------

Note that this is an exercise that must be accomplished on your local computer!

--> Run Docker Desktop on your computer
--> Be sure, the Docker extension is installed in Visual Studio Code
--> In Visual Studio Code, open a new Terminal (Upper Menu or CTRL+SHIFT+¨)

#-------------------------------------------------------------------------------
# In Visual Studio Code ...
#-------------------------------------------------------------------------------

# Go to the folder with your files from Moodle, this should look like:
  Week_03
    |--challenge
    |--exercises
      |--Docker_Compose_Jupyter_Notebook_PostgreSQL
        |--apartments_data_prepared.csv
        |--docker-compose.yml
        |--Dockerfile
        |--HOW_TO_README.txt
        |--jupyter_postgres_db.ipynb

#-------------------------------------------------------------------------------
# In Visual Studio Code ...
#-------------------------------------------------------------------------------

--> cd into the folder 'Docker_Compose_Jupyter_Notebook_PostgreSQL'

# Execute docker-compose.yml 
right click on docker-compose.yml -> Compose up

# Alternatively in the Terminal type:
docker compose up

# Show docker image
docker images

# To access the Jupyter notebook, open the following url in a web browser
# http://127.0.0.1:8888

#-------------------------------------------------------------------------------
# In your Jupyter notebook in a web browser ...
#-------------------------------------------------------------------------------

# Drag and drop the two files to your Jupyter notebook
- jupyter_postgres_db.ipynb
- apartments_data_prepared.csv

# Run the Jupyter notebook 'jupyter_postgres_db.ipynb'

# Include additional SQL queries and save the Jupyter notebook.

# Stop the Jupyter notebook server
CTRL+C

#-------------------------------------------------------------------------------
# In Docker Desktop ...
#-------------------------------------------------------------------------------

# Stop all running containers
# right menu -> Containers -> check all containers -> pause button -> delete button
