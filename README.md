# Scripts to get command outputs from network devices

Using pyATS for interaction to devices.\
Get outputs from multiple commands per device type, store them in separate directory for each device.\
Commands to run defined in python code in lists per device type.

**Install and check pyATS**

Install python virtual environment in _pyATSv_ directory:
```
python3 -m venv pyATSv
```

Activate virtual environment:
```
source pyATSv/bin/activate
```
See if prompt changes to virtual environment name.

Install pyats:
```
pip install pyats genie
```

Check if it works:
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
```
(see if promt changes to virtual environment name)
```
python3 getRunning.py
```
