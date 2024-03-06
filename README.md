# Scientific programming

## Table of Contents
- [Scientific programming](#scientific-programming)
  - [Table of Contents](#table-of-contents)
  - [Module description](#module-description)
  - [Working directories](#working-directories)
  - [Installations](#installations)
  - [Settings in VS Code](#settings-in-vs-code)
  - [Generate SSH key pair](#generate-ssh-key-pair)
  - [GitHub repository](#github-repository)
  - [Sync origin with upstream](#sync-origin-with-upstream)
  - [Solve merge conflicts](#solve-merge-conflicts)

## Module description

This module teaches the fundamentals of scientific programming. The focus is on scientific programming for data science applications. The programming language is Python. Python as an object-oriented programming language has caught up with other programming languages in terms of popularity and distribution in recent years and is thus becoming increasingly important. Students learn the most important programming paradigms. Due to the application-oriented nature of the module, students acquire the necessary knowledge that allows them to apply Python in practice.

## Working directories

**NOTICE:** Please note that the weekly material will continously provided and always be available shortly before the course starts. In the course, we will use the following folder structure:

```plaintext
|--scientific_programming
  |--Week_01
    |--exercises
    |--challenge
  |--Week_02
    |--exercises
    |--challenge
  ...
  ...
  ...
  |--Week_13
    |--exercises
    |--challenge
  |--Week_14
    |--exercises
    |--challenge
```

## Installations

**Installations (Windows, macOS)**

1. Install the latest Anaconda version  
   * Download-Link:  https://www.anaconda.com/products/individual  
   * Under Windows: make sure that Anaconda is specified in your path e.g. on Windows: C:\Users\your_username\Anaconda3\Scripts    
   * See: https://youtu.be/z84UIZy_qgE  
	
2. Install the latest version of Visual Studio Code    
   * Download-Link: https://code.visualstudio.com/download    
   * Video-Tutorials: Visual Studio Code -> Menu -> Help -> Video-Tutorials    
   * Make sure that Visual Studio Code is specified in your path under user variables e.g. on Windows: C:\Users\your_username\AppData\Local\Programs\Microsoft VS Code\bin    
   * See also: https://youtu.be/z84UIZy_qgE  

3. Install the 'Python' and 'Jupyter' extension in Visual Studio Code    
   * See: https://code.visualstudio.com/docs/getstarted/introvideos    
   * Video Tutorial: Visual Studio Code -> Menu -> Help -> Video-Tutorials -> Extensions    

4. Create a new conda environment and install the required Python libraries      
   * Windows: Open Anaconda Prompt (command line tool which comes with the Anaconda installation)
   * macOS: Open terminal  
   
    Type: 

    ```bash
    conda info --envs                   # shows all available conda environments
    conda create -n spenv python=3.10   # creates a new conda environment 'spenv' with Python 3.10
    conda activate spenv                # activates the new conda environment 'spenv'
    ```

    Copy the 'requirements.txt' from the GitHub repository to a local working folder then cd into that folder. Make sure that the conda environment 'spenv' is activated. To install the required Python libraries listed in 'requirements.txt', type:

    ```bash
    pip install -r requirements.txt
    ```

5. Install Git and [if not yet done] create a GitHub Account  
   * Git download-link: https://git-scm.com/downloads  
   * GitHub Homepage: https://github.com  
   * Video-Tutorial: Visual Studio Code -> Menu -> Help -> Video-Tutorials -> Version Control  

6. Install Docker Desktop (macOS users: consider the installation for 'Apple Chip' or 'Intel Chip')  
   * Download Link: https://www.docker.com/products/docker-desktop  

7. Install the Docker extension in Visual Studio Code  

8. Install the Copilot extension in Visual Studio Code and activate the [free] GitHub Global campus licence on:
   - https://tat.zhaw.ch/github-map/index.jsp?nav=act

9. Create a Kaggle account and get the kaggle.json file with your username and kaggle API key.

   - Create account on https://www.kaggle.com  
   - On https://www.kaggle.com/settings -> API -> Create New Token  
   - This will trigger the download of kaggle.json, a file containing your API credentials.  

## Settings in VS Code

Make the following settings using the VS Code Command Palette (CTRL+SHIFT+P) and VS Code settings.  

In VS Code Command Palette (CTRL+SHIFT+P):      
* Python: Select Interpreter -> select your interpreter (name of the new conda environment 'spdev'
* Terminal: Select Default Profile -> under Window, change to 'Command Prompt'
* Configure Display Language -> change to 'en' (English)

For Windows users, define the path to the conda executable: VS Code -> Settings -> type 'conda' -> include the path here
* Under Windows, this is typically: C:\Users\YOUR-USERNAME\Anaconda3\Scripts\conda.exe

## Generate SSH key pair

An SSH key pair is used to establish a secure connection between your local computer and the remote server (like GitHub). It is highly recommended to use an SSH-key.  

First, look at this video: https://www.youtube.com/watch?v=snCP3c7wXw0

In VS Code -> open a Terminal, then type:  

```bash
# Email must be the one provided on GitHub
ssh-keygen -t ed25519 -C "your-email-on-github@example.com"
```
This will generate two files with SSH-Keys on your computer (public & privat key)  
```plaintext
* Windows-Users look under: C:\Users\your-username\.ssh\id_ed25519.pub
* Mac-Users look under: /Users/your-username/.ssh/id_ed25519.pub
```
```bash
# To copy the ssh-key to your clipboard
Windows-Users (change your-username): 'type C:\Users\your-username\.ssh\id_ed25519.pub | clip'
Mac-Users: 'pbcopy < ~/.ssh/id_ed25519.pub'
```

**Note that .ssh is a hidden folder, so on Windows and macOS you first must make this folder visible to have access to the files with the ssh-keys**

**To make the folder .ssh visible**
```plaintext
--> Windows-Users: File Explorer -> View > Show > Hidden items (or in germ.: Anzeigen -> Einblenden -> Ausgeblendete Elemente)

--> Mac-Users, type (in Terminal):
  defaults write com.apple.Finder AppleShowAllFiles true 
  killall Finder

  to hide again, type:

  defaults write com.apple.Finder AppleShowAllFiles false 
  killall Finder
```

If you have the public ssh-key, go to GitHub -> Account Icon top left -> Settings -> SSH and GPG keys -> New SSH key -> include the newly generated public key

See also: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent  

## GitHub repository
The course material is available on GitHub. To make the material available on your local computer and keep it updated, follow the steps below. Note that it is assumed that you have Git installed and a GitHub account.

**Fork/Clone a GitHub repository and keep the fork/clone up to date**
```bash
# 1.) To fork the GitHub repository with the course material, navigate to:

https://github.com/mario-gellrich-zhaw/scientific_programming.git

# --> Click on the "Fork" button at the top right of the page.
# --> This will generate a fork (copy) of the repository in your GitHub account.

# For the following steps, make sure that Git is installed on your computer (see 'Installations' above)!!!

# 2. In VS Code -> Terminal, clone your fork (creates a copy of the repository on your local computer):
git clone git@github.com:YOUR-USERNAME/scientific_programming.git

# --> Note that this is the SSH URL requiring an ssh key, not the HTTPS URL!

# 3. In VS Code -> Terminal ...

# --> open the folder which include the cloned GitHub repository
# --> open a Terminal to execute the Git commands below

# 4. Set the upstream repository (= official course repository)
git remote add upstream https://github.com/mario-gellrich-zhaw/scientific_programming.git

# 5. Set the url of the origin (= your forked repository with the SSH URL)
git remote set-url origin git@github.com:YOUR-USERNAME/scientific_programming.git

# 6. View the current configured remote repositories
git remote -v

# The output should look like (replace YOUR-USERNAME with your user name) ...
# origin  git@github.com:YOUR-USERNAME/scientific_programming.git (fetch)
# origin  git@github.com:YOUR-USERNAME/scientific_programming.git (push)
# upstream        https://github.com/mario-gellrich-zhaw/scientific_programming.git (fetch)
# upstream        https://github.com/mario-gellrich-zhaw/scientific_programming.git (push)

# 7. Retrieve the latest changes from upstream repository
git fetch upstream

# 8. Updating your fork from upstream repository
git pull upstream master
```

## Sync origin with upstream

To sync your fork (origin) and clone with the upstream repository you can use the following Git commands:

```bash
# Make sure the upstream has been added and the origin's url is set
git remote -v

# The output should look like (replace YOUR-USERNAME with your user name) ...
# origin  git@github.com:YOUR-USERNAME/scientific_programming.git (fetch)
# origin  git@github.com:YOUR-USERNAME/scientific_programming.git (push)
# upstream        https://github.com/mario-gellrich-zhaw/scientific_programming.git (fetch)
# upstream        https://github.com/mario-gellrich-zhaw/scientific_programming.git (push)

# If this is not set correctly, type (replace YOUR-USERNAME with your user name on GitHub) ...
git remote add upstream https://github.com/mario-gellrich-zhaw/scientific_programming.git
git remote set-url origin git@github.com:YOUR-USERNAME/scientific_programming.git

# Option (1): Sync your fork/clone to exactly match the upstream (your local changes will be overwritten)
git fetch upstream
git checkout master
git reset --hard upstream/master
git push origin master --force

# Option (2): Sync your fork/clone with the upstream (your local changes are preserved but merge conflicts may have to be resolved)
git fetch upstream
git checkout master
git merge upstream/master
git push origin master
```

## Solve merge conflicts

Later in the course you will modify the Python code provided on GitHub. When you modify Python code, merge conflicts may occur which is when two or more changes conflict with each other. This usually happens when multiple people are working on the same project and they try to merge their changes into a common codebase.

In VS Code, you can use the Merge Editor to solve merge conflics.

The following video explains how this works: https://www.youtube.com/watch?v=KuB6hYoLozw
