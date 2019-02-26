# Config Parger 


## 1. Config.ini

```python 
[Section]
option=value # 주석

[Section2]
option=value
```

## 2. confParser.py

```python 
import ConfigParser

config = ConfigParser.ConfigParser() 
config.add_section("First Section") 
config.set("First Section", "test1", "1") 
config.set("First Section", "test2", "2") 
config.add_section("Second Section") 
config.set("Second Section", "test1", "1") 
config.set("Second Section", "test2", "2")

configFile = open("config.cfg", "w") 
config.write(configFile) 
configFile.close()


config = ConfigParser.ConfigParser() 
config.read("config.cfg")

print config.sections()
print config.get("First Section", "test2") 
print config.options("Second Section") 
```