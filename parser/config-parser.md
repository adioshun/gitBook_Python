# [Config Parger ](https://cozyboy.tistory.com/entry/python-config-%EC%84%A4%EC%A0%95-%EC%9A%94%EC%95%BDConfigParser)


`pip install configparser`


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

# Save
configFile = open("config.cfg", "w") 
config.write(configFile) 
configFile.close()

with open('example.cfg', 'wb') as configfile:
    config.write(configfile)  ##마지막에 꼭 write 해줘야 한다

# Read
config = ConfigParser.ConfigParser() 
#config = ConfigParser.RawConfigParser()
config.read("config.cfg")

print config.sections()
print config.get("First Section", "test2") 
print config.options("Second Section") 
```

Or

```python 

import configparser

config = configparser.ConfigParser()
CONFIG_FILE_NAME = 'server.config'

# config file write to server.config
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'port': 8080
}
config['db_server'] = {
    'host': '127.0.0.1',
    'port': 3306
}

with open(CONFIG_FILE_NAME,'w') as config_file:
    config.write(config_file)

# write to config file
[DEFAULT]
debug = True

[web_server]
host = 127.0.0.1
port = 8080

[db_server]
host = 127.0.0.1
port = 3306


# config file read from server.config
config.read(CONFIG_FILE_NAME)
print(config['web_server'])
print(config['web_server']['host'])
print(config['web_server']['port'])
```