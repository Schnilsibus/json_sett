from unittest import TestCase
from pathlib import Path
from json_convenience import write_json_file, JSONKeyNotFoundError, NotAPropertyError, read_json_file
from _core.json_settings import Settings


settings = {
    "setting": "setting",
    "no_setting": {
        "key": "value"
    }
}
new_value = "settingA"

valid_path = Path(__file__).parent / "settings.json"
path_to_directory = Path(__file__).parent
path_to_no_json = Path(__file__).parent / "settings.png"


class SettingTestCase(TestCase):
    def setUp(self) -> None:
        open(file=path_to_no_json, mode="x").close()
        open(file=valid_path, mode="x").close()
        write_json_file(file_path=valid_path, data=settings)

    def tearDown(self) -> None:
        path_to_no_json.unlink()
        valid_path.unlink()


# noinspection PyStatementEffect
class TestSuiteInit(SettingTestCase):
    def test_raisesIfPathDoesntExist(self):
        try:
            Settings(path=path_to_directory / "dont_exist.json")
            self.fail(msg="should have raised FileNotFoundError")
        except FileNotFoundError:
            pass
        except BaseException:
            self.fail(msg="should have raised FileNotFoundError")

    def test_raisesIfPathIsDir(self):
        try:
            Settings(path=path_to_directory)
            self.fail(msg="should have raised FileNotFoundError")
        except FileNotFoundError:
            pass
        except BaseException:
            self.fail(msg="should have raised FileNotFoundError")

    def test_raisesIfPathIsNoJson(self):
        try:
            Settings(path=path_to_no_json)
            self.fail(msg="should have raised FileNotFoundError")
        except FileNotFoundError:
            pass
        except BaseException:
            self.fail(msg="should have raised FileNotFoundError")

    def test_worksIfPathIsValid(self):
        Settings(path=valid_path)


# noinspection PyStatementEffect
class TestSuiteGet(SettingTestCase):
    def setUp(self) -> None:
        SettingTestCase.setUp(self=self)
        self.my_settings = Settings(path=valid_path)

    def test_raisesIfSettingIsNotThere(self):
        try:
            self.my_settings.not_there
            self.fail(msg="should have raised JSONKeyNotFoundError")
        except JSONKeyNotFoundError:
            pass
        except BaseException:
            self.fail(msg="should have raised JSONKeyNotFoundError")

    def test_raisesIfSettingIsObject(self):
        try:
            self.my_settings.no_setting
            self.fail(msg="should have raised NotAPropertyError")
        except NotAPropertyError:
            pass
        except BaseException:
            self.fail(msg="should have raised NotAPropertyError")

    def test_getAddsPropertyToInternalDict(self):
        self.my_settings.setting
        self.assertTrue("setting" in self.my_settings.__dict__.keys())

    def test_loadedSettingHasCorrectData(self):
        self.assertTrue(self.my_settings.setting == settings["setting"])


# noinspection PyStatementEffect
class TestCaseSet(SettingTestCase):
    def setUp(self) -> None:
        SettingTestCase.setUp(self=self)
        self.my_settings = Settings(path=valid_path)

    def test_raisesIfKeyIsNeitherSettingNorAttribute(self):
        try:
            self.my_settings.somethingElse = "new"
            self.fail(msg="should have raised AttributeError")
        except AttributeError:
            pass
        except BaseException:
            self.fail(msg="should have raised AttributeError")

    def test_worksIfKeyIsSetting(self):
        self.my_settings.setting = new_value

    def test_worksIfKeyIsAttribute(self):
        self.my_settings._all_keys = new_value

    def test_raisesIfValueIsNoSetting(self):
        try:
            self.my_settings.setting = {}
            self.fail(msg="should have raised NotAPropertyError")
        except NotAPropertyError:
            pass
        except BaseException:
            self.fail(msg="should have raised NotAPropertyError")

    def test_worksIfValueIsCorrect(self):
        self.my_settings.setting = new_value

    def test_setsCorrectValueInInternalDict(self):
        self.my_settings.setting = new_value
        self.assertTrue(new_value == self.my_settings.__dict__["setting"])


# noinspection PyStatementEffect
class TestCaseSave(SettingTestCase):
    def setUp(self) -> None:
        SettingTestCase.setUp(self=self)
        self.my_settings = Settings(path=valid_path)

    def test_savesOnlyKeysAlreadyInFile(self):
        self.my_settings.save()
        keys = tuple(read_json_file(file_path=valid_path).keys())
        self.assertTrue(keys == tuple(settings.keys()))

    def test_savesCorrectValueToFile(self):
        self.my_settings.setting = new_value
        self.my_settings.save()
        file_value = read_json_file(file_path=valid_path)["setting"]
        self.assertTrue(file_value == new_value)

