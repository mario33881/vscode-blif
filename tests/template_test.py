"""
TEMPLATE_TEST
Tests a template (and when recording_mode is True the script records the test)
"""

__author__ = "Zenaro Stefano (mario33881)"
__version__ = "2020-12-11 01_01"

import pyautogui
import time
import keyboard
import os
import active_window as aw

recording_mode = False
table_delay = 0.002
delay = 0.05
initial_wait = 5
template_name = "all"

table = [
    "0-- ATT ATT 0",
    "1-- ATT NUL 0",
    "--1 NUL NUL 0",
    "-1- NUL NUL 0",
    "-00 NUL 00 0",
    "-00 00 00 0",
    "-1- 00 NUL 0",
    "-01 00 01 0",
    "-00 01 00 0",
    "-10 01 NUL 0",
    "-01 01 NUL 0",
    "-11 01 11 1",
    "--1 11 11 1",
    "-0- 11 11 1",
    "-10 11 ATT 0"
    ]

state_encoding = [
    {"state": "NUL", "code": "001"},
    {"state": "00", "code": "010"},
    {"state": "01", "code": "011"},
    {"state": "11", "code": "100"}
    ]


def write_key(t_key, t_delay):
    """
    Write the <t_key> char and then wait <t_delay> (if VS CODE window is focused).
    
    :param string t_key: char with a keyboard key
    :param (float, int) t_delay: seconds to wait after the char is typed
    """
    if "Visual Studio Code" in aw.get_active_window():
        time.sleep(t_delay)
        pyautogui.write(t_key)


def write_word(t_string, t_delay):
    """
    Write each char in <t_string> (wait between each char <t_delay> seconds).

    Loop for each char in <t_string> and call write_key() to visualize the char.
    
    :param string t_string: string to write
    :param (float, int) t_delay: seconds to wait after each char is typed
    """
    for c in t_string:
        write_key(c, t_delay)

        
def write_hotkey(t_key, t_delay):
    """
    Execute <t_key> hotkey and then wait <t_delay> seconds (if VS CODE window is focused).
    
    :param string t_string: string with a special key
    :param (float, int) t_delay: seconds to wait after each char is typed
    """
    if "Visual Studio Code" in aw.get_active_window():
        time.sleep(t_delay)
        pyautogui.hotkey(t_key)

    
def start_rec():
    """
    Starts recording with alt+f9 hotkey.
    """
    pyautogui.hotkey('alt', 'f9')


def stop_rec():
    """
    Stop recording using the same hotkey used to start recording.
    """
    start_rec()


def test_fsm():
    """
    Tests the FSM template.
    """
    # start from template
    write_word("!fsm", delay)
    write_hotkey("tab", delay)

    # .model automa
    write_word("automa", delay)
    write_hotkey("tab", delay)

    # .inputs START IN1 IN0
    write_word("START IN1 IN0", delay)
    write_hotkey("tab", delay)

    # .outputs OUT
    write_word("OUT", delay)
    write_hotkey("tab", delay)

    # .i 3
    write_key("3", delay)
    write_hotkey("tab", delay)

    # .o 1
    write_key("1", delay)
    write_hotkey("tab", delay)
    
    # .s 5
    write_key("5", delay)
    write_hotkey("tab", delay)

    # .p 15
    write_word("15", delay)
    write_hotkey("tab", delay)

    # .r ATT
    write_word("ATT", delay)
    write_hotkey("tab", delay)

    # FSM truth table
    for table_row in table:
        write_word(table_row, table_delay)
        write_hotkey("enter", table_delay)

    for i in range(6):
        write_hotkey("down", delay)

    # .code ...
    write_word(".code", delay)
    write_hotkey("tab", delay)
    write_word("ATT", delay)
    write_hotkey("tab", delay)
    write_word("000", delay)
    write_hotkey("tab", delay)

    for i in state_encoding:
        write_word(".co", delay)
        write_hotkey("tab", delay)
        write_word(i["state"], delay)
        write_hotkey("tab", delay)
        write_word(i["code"], delay)
        write_hotkey("tab", delay)


def test_lgate():
    """
    Tests the Logic Gate template.
    """
    # start from template
    write_word("!lgate", delay)
    write_hotkey("tab", delay)

    # .model and
    write_word("and", delay)
    write_hotkey("tab", delay)

    # .inputs IN1 IN0
    write_word("IN1 IN0", delay)
    write_hotkey("tab", delay)

    # .outputs OUT
    write_word("OUT", delay)
    write_hotkey("tab", delay)

    # .names IN1 IN0 OUT
    write_word("IN1 IN0", delay)
    write_hotkey("tab", delay)
    write_word("OUT", delay)
    write_hotkey("tab", delay)

    # 11 1
    write_word("11 1", delay)


def delete_file_content(t_delay):
    """
    Deletes a file content (if VS CODE window is focused).
    :param (float, int) t_delay: seconds to wait after each char is typed
    """
    if "Visual Studio Code" in aw.get_active_window():
        # click CTRL + A
        time.sleep(t_delay)
        pyautogui.hotkey("ctrl", "a")

        # delete selection
        time.sleep(t_delay)
        pyautogui.hotkey("del")


if __name__ == "__main__":

    # stop the program when the letter x is pressed
    keyboard.on_press_key("x", lambda _:os._exit(0))

    # * on recording mode start recording and use delays
    # * when not recording, reduce the delay to the minimum
    if recording_mode:
        for i in range(initial_wait):
            time.sleep(i)
            print("[RECORDING] recording in {} seconds".format(initial_wait-i))

        print("[RECORDING] recording now")
        start_rec()
    else:
        table_delay = 0.001
        delay = 0.001
        
    for i in range(initial_wait):
        time.sleep(i)
        print("[START] starting in {} seconds".format(initial_wait-i))
    print("[START] started")

    tests = [
        {"template_name": "fsm", "function": test_fsm},
        {"template_name": "lgate", "function": test_lgate},
    ]

    # test templates
    if template_name == "all":
        # test all the templates and 
        # delete file content in between
        for test in tests:
            if "Visual Studio Code" in aw.get_active_window():
                print("[TEST] Start test '{}'".format(test["template_name"]))
                test["function"]()
                time.sleep(initial_wait)
                delete_file_content(delay)
            else:
                print("[TEST] ERROR: no focus on the VS CODE window during '{}' test".format(test["template_name"]))
    else:
        found = False
        n = 0
        while n < len(tests) and not found:
            test = tests[n]
            if test["template_name"] == template_name:
                if "Visual Studio Code" in aw.get_active_window():
                    test["function"]()
                else:
                    print("[TEST] ERROR: no focus on the VS CODE window during '{}' test".format(template_name))
                found = True
            
            n += 1

        if not found:
            print("[TEST] ERROR: template name is invalid")

    # stop recording (if recording)
    if recording_mode:
        print("[RECORDING] Ending recording")
        time.sleep(initial_wait)
        stop_rec()
        print("[RECORDING] Done, stopped recording")
    
    print("[END] Script ended")
