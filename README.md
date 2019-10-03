# Github Tutorial

The goal of this class is to install github, get familiar with it and start your capstone project

## Installing git
If you don't yet have a github accout, go to `github.com` and create an account with your university email and = get a pro account for free

Open a terminal and follow the instructions

### Mac Users
1. Get homebrew
    ```console
    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

2. brew git
    ```console
    $ brew install git
    ```

### Windows
Get [ubuntu](https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#2)

### Ubuntu
1. Update apt-get
    ```console
    $ sudo apt-get update
    $ sudo apt-get upgrade
    ```

2. apt-get git
    ```console
    $ apt-get install git-core
    ```

### ALL users
You should now have git, verify by executing
```console
$ git --version
git version 2.17.2 (Apple Git-113)
```

Set up your config
```console
$ git config --global user.name "YOUR NAME"
$ git config --global user.email "YOUREMAIL@berkeley.edu"
```

You can now clone this repository
```console
$ mkdir ~/github.com
$ cd ~/github.com
$ git clone https://github.com/titouanjehl/GitTutorial.git
$ cd  GitTutorial
```

## Python and Anaconda
It is time now to get python and setup your work environment

### On Mac
1. Get Anaconda with homebrew
    ```console
    $ brew cask install anaconda
    ```

2. Export the path so your computer knows where this is
    ```console
    $ export PATH="/usr/local/anaconda3/bin:$PATH"
    ```

3. restart your terminal (or run `source ~/.zshrc`) then try
    ```console
    $ jupyter notebook
    ```

### On Ubuntu
1. Get anaconda and install it
    ```console
    $ wget https://repo.continuum.io/archive/Anaconda2-4.2.0-Linux-x86_64.sh
    $ bash Anaconda2-4.2.0-Linux-x86_64.sh -b -p ~/anaconda
    $ rm Anaconda2-4.2.0-Linux-x86_64.sh
    ```

2. Export the path
    ```console
    $ echo 'export PATH="~/anaconda/bin:$PATH"' >> ~/.bashrc
    ```

3. restart your terminal (or run `source ~/.bashrc`) then try
    ```console
    $ jupyter notebook
    ```

## Time to setup a virtual environment to work on your project
1. From your terminal, you can now create a virtual environment. That will allow you to have only the library you need for your project in this environment and avoid many issues with un compatible libraries.
    ```console
    $ conda create -n capstone-env python=3.6
    ```
2. Now activate your environment
    ```console
    $ conda activate capstone-env
    ```

3. You will often use jupyter notbook, therefore you should create a kernel attached to this environment
    ```console
    $ conda install pip
    $ pip install ipykernel
    $ python -m ipykernel install --user --name capstone-env --display-name "Python (capston-env)"
    ```

4. Now is the time to install all the usefull libraries
    ```console
    $ pip install -r requirements.txt
    ```
   
## Test your code will save you precious time
Instead of re-coding the same functions (or copy paste) in every new notebook,
We encourage you to have a package for your capstone. You can test this package and 
then call it from your jupyter notebook. In this repo there is an exemple of a small package.

In python the best practice is to structure your project as follows:
* src/
    * myPackage/
        * __init__.py
        * myFile1.py
        * myFile2.py
        * SubPackage
            * __init__.py
            * yetAnotherFile.py
* tests/
    * test_myFile1.py
    * test_myFile2.py
    * test_yetAnotherFile.py
    
In your virtual environment, you can install the project and test it by running 
```console
$ python setup.py install
$ pytest
```

You can play with the test to see what happens when the test fails.

## Working in a group on github
With github, each of you can work on a seperate branch without damaging the code of others.

1. Create your capstone repo and try pushing this repository on your capstone repo
    Go to create new repository, copy the link to this repo
    then set the origin to this address:
    ```console
    $ git remote set-url origin YOUR_LINK
    $ git remote -v
     origin	YOUR_LINK (fetch)
     origin	YOUR_LINK (push)
    ```


2. By running `git branch` you will see on what branch you are
    ```console
    $ git branch
    * master
    ```

3. If you want to modify the code first create your own branch with a name desciptive enough
    for you and other to understand what it is
    ```console
    $ git branch AddingTreeBasedModels
    ```
   
3. Before modifying the code you need to go on that new branch
    ```console
    $ git checkout AddingTreeBasedModels
    $ git branch
      master
    * AddingTreeBasedModels
    ```

4. you need to set up the upstream before pushing anything on the cloud
    ```console
    $ git push --set-upstream origin AddingTreeBasedModels
   ```   
  
5. Create your new file or modify some file. Here consider we added `src/mypackage/treemodel.py`
    once you are done, add it to the repository, commit it with a short message then push
    ```console
    $ git add src/mypackage/treemodel.py
    $ git commit -m"added a tree model"
    $ git push
    ```
   
6. now every one who checks out `AddingTreeBasedModels` will be able to see your work.
    However if you checkout `master` you won't see your change
    ```console
    $ git checkout master
    ```
   Check your folder, your work isn't here anymore.
   
7. You can now try to merge your work on `master`. To do that go to github.com, locate your repo and your
    new branch. Create a pull request onto master and ask your teamates to review your code
    Once the code has been approved you can merge. Finally pull the work from the cloud
    ```console
    $ git pull
   ```
   You should now see your work from master
    
Doing so you should never run in conflicts. Keep your updates short so that reviewing is easy
      

