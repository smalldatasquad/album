# Capture Your Facebook Posts


Small Data Squad invites you to take screenshots of your facebook data.


# setup

Open up an app called 'Terminal' and paste these commands in line by line, pressing 'enter' after each one. If you're asked for a password, enter the password you use to unlock your computer.
```
cd Desktop
sudo easy_install pip
git clone https://github.com/smalldatasquad/capture_facebook.git
cd capture_facebook
pip install --upgrade pip
brew install chromedriver
pip install -r requirements.txt
```


# Secrets
Open the folder you just created called 'capture_facebook' in a text editor like Atom. Duplicate the file called secrets.py.example amd rename the copy to "secrets.py". Inside secrets.py, fill in the variables with your informantion and save.

# Run
To run the file, open Terminal and enter this line.
```
python run.py
```
