import json_convenience as jsonx
from pathlib import Path
from typing import Any

# TODO: add documentation
# TODO: make it its own thing and add to git / pip


Setting = jsonx.Property


class Settings(object):
    def __init__(self, path: Path):
        if not path.exists():
            raise FileNotFoundError(f"{path} doesn't exist")
        elif not path.is_file() or not path.suffix == ".json":
            raise FileNotFoundError(f"{path} is no .json file")
        self.__dict__["_all_keys"] = tuple(jsonx.read_json_file(file_path=path).keys())
        self.__dict__["_file"] = path

    def __getattr__(self, name: str) -> Setting:
        if name not in self.__dict__:
            self.__dict__[name] = jsonx.get_property(file_path=self._file, keys=(name, ))
        return self.__dict__[name]

    def __setattr__(self, name: str, value: Any) -> None:
        if name not in self._all_keys:
            if name not in self.__dict__.keys():
                raise AttributeError(f"'{self.__class__}' object has no setting or attribute '{name}'")
            else:
                self.__dict__[name] = value
            return
        if not isinstance(value, Setting):
            raise jsonx.NotAPropertyError(no_property_object=value)
        self.__dict__[name] = value

    def save(self) -> int:
        counter = 0
        for name in self.__dict__:
            if jsonx.contains_property(file_path=self._file, keys=(name, )):
                file_property = jsonx.get_property(file_path=self._file, keys=(name, ))
                if not file_property == self.__dict__[name]:
                    jsonx.set_property(file_path=self._file, keys=(name, ), value=self.__dict__[name])
                    counter += 1
        return counter
