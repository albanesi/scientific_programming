#-------------------------------------------------------------------------------
# Docker: Jupyter Datascience Notebook
#-------------------------------------------------------------------------------

Note that this is an exercise that must be accomplished on your local computer!

--> Run Docker Desktop on your computer
--> Be sure, the Docker extension is installed in Visual Studio Code
--> In Visual Studio Code, open a new Terminal window (Upper Menu or CTRL+SHIFT+¨)

#-------------------------------------------------------------------------------
# In Visual Studio Code ...
#-------------------------------------------------------------------------------

# Go to the folder with your files from Moodle, this should look like:
  Week_03
    |--challenge
    |--exercises
      |--Docker_Jupyter_Datascience_Notebook
        |--apartments_data_kt_zuerich.ipynb
        |--apartments_data_prepared.csv
        |--HOW_TO_README.txt

# To show the available Docker images, in the Terminal window type:
docker images

# To show the running Docker container, in the Terminal Window type:
docker ps

# To show the running and stopped Docker containers, in the Terminal Window type:
docker ps -a

# To pull a specific docker image from Docker Hub and run the container type:
docker run -it --rm -p 8888:8888 jupyter/datascience-notebook

# To access the container, click on the link in the VS Code terminal (token=... contains the access token)
 http://127.0.0.1:8888/lab?token=...

#-------------------------------------------------------------------------------
# In the Jupyter notebook ...
#-------------------------------------------------------------------------------

# In JupyterLab upload the two files to your Jupyter Lab environment
- apartments_data_prepared.csv
- apartments_data_kt_zuerich.ipynb

# Run the Jupyter notebook 'apartments_data_kt_zuerich.ipynb'

# To stop the Jupyter notebook server, type in your Terminal
CTRL+C

#-------------------------------------------------------------------------------
# In VS Code ...
#-------------------------------------------------------------------------------

# Stop all running containers
# Docker menu -> CONTAINERS -> right click -> Stop
# Docker menu -> IMAGES -> right click -> Remove