# Scripts to get command outputs from network devices

Using pyATS
Get outputs from commands in lists per device type, store them in separate directory for each device. 

**Install and check pyATS**

Install pyenv in _pyATSv_ directory:
```
python3 -m venv pyATSv
```

Activate pyenv:
```
source pyATSv/bin/activate
```

Install pyats:
```
pip install pyats genie
```

Check if works:
```
pyats version check
```

**Run commands**
```
python3 getRunning.py
```

**exit venv**
```
deactivate
```

**Before every new session**
```
source pyATSv/bin/activate
(see if promt changes to venv name)
python3 getRunning.py
```

