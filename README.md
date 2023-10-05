# json-settings
Read settings from and save them to a json file.

## Requirements
- json-convenience

## Install
install using pip: ```python -m pip install json-settings```

## Usage
- import the 'Settings' class: ```from json_settings import Settings```  
- initialize it: ```my_settings = Settings(file=<your_file_path>```  
- then access your settings as attributes of the 'my_settings' object:  
    say your json file contains the key 'settingA' you can access its value like that: ```my_settings.settingA```
- change the value of a setting like that: ```my_settings.settingA = <your_new_value>```  
    this will NOT save that value to the file
- to save all settings use: ```my_settings.save()```

## File restrictions
The settings must all be at the top level in the json file.  
This is a valid example:
```json
{
  "settingA": "valueA",
  "settingB": 14
}
```
This is an invalid example:
```json
{
  "settingA": "valueA",
  "settingB": {
    "settingC": true
  }
}
```
Adding support for the invalid example e.g. being able to order settings in groups would be nice.
Might do that some time.
