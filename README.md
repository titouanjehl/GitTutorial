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
Get [ubuntu] (https://tutorials.ubuntu.com/tutorial/tutorial-ubuntu-on-windows#2)

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
