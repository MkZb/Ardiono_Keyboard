import pyautogui, os


class Functionality():

    def __init__(self, profile=None):
        self.profile = profile
        self.func_list = []
        self.hotkeys = dict.fromkeys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "")
        if profile == 1:
            for i in range(10):
                self.func_list.append(self.pressHotkey)
                self.setHotkey(i + 1, ["Ctrl", str(i)])
        elif profile == 2:
            for i in range(10):
                self.func_list.append(self.pressHotkey)
            self.hotkeys = {1: ["Ctrl", "c"],
                            2: ["Ctrl", "v"],
                            3: ["Ctrl", "a"],
                            4: ["Ctrl", "shift", "esc"],
                            5: "volumeup",
                            6: "volumedown",
                            7: "volumemute",
                            8: ["", ""],
                            9: "",
                            10: ""}
        elif profile == 3:
            for i in range(10):
                self.func_list.append(self.executeCommand)
            self.hotkeys = {1: "calc",
                            2: "charmap",
                            3: "control",
                            4: "devmgmt.msc",
                            5: "explorer",
                            6: "mmsys.cpl",
                            7: "notepad",
                            8: "taskmgr",
                            9: "compmgmt.msc",
                            10: "appwiz.cpl"}

    def setHotkey(self, num, keys):
        self.hotkeys[num] = keys

    def pressHotkey(self, num):
        hotkey = self.hotkeys[num]
        if type(hotkey) is list:
            pyautogui.hotkey(*hotkey)
        else:
            pyautogui.press(hotkey)

    def setCommand(self, num, command):
        self.hotkeys[num] = command

    def executeCommand(self, num):
        command = self.hotkeys[num]
        print(os.system(command))
