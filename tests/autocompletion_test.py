"""
AUTOCOMPLETION_TEST:
Tests autocompletions (and when recording_mode is True the script records the tests)
"""

__author__ = "Zenaro Stefano (mario33881)"
__version__ = "2020-12-11 01_01"

import pyautogui
import time
import keyboard
import os
import template_test as tt
import active_window as aw

recording_mode = False
delay = 0.05
initial_wait = 5
keyword_name = "all"


def test_model():
    """
    Tests .model
    """
    tt.write_word(".model", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("mycircuit", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_inputs():
    """
    Tests .inputs
    """
    tt.write_word(".inputs", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("IN2 IN1 IN0", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_outputs():
    """
    Tests .outputs
    """
    tt.write_word(".outputs", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("OUT2 OUT1 OUT0", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_names():
    """
    Tests .names
    """
    tt.write_word(".names", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("IN2 IN1 IN0", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("OUT0", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_exdc():
    """
    Tests .exdc
    """
    tt.write_word(".exdc", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_start_kiss():
    """
    Tests .start_kiss
    """
    tt.write_word(".start_kis", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_end_kiss():
    """
    Tests .end_kiss
    """
    tt.write_word(".end_kiss", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_i():
    """
    Tests .i
    """
    tt.write_word(".i", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("3", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_o():
    """
    Tests .o
    """
    tt.write_word(".o", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("5", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_s():
    """
    Tests .s
    """
    tt.write_word(".s", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("10", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_p():
    """
    Tests .p
    """
    tt.write_word(".p", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("13", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_r():
    """
    Tests .r
    """
    tt.write_word(".r", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("START", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_code():
    """
    Tests .code
    """
    tt.write_word(".code", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("A", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("010", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_subckt():
    """
    Tests .subckt
    """
    tt.write_word(".subckt", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("COMPONENT", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("IN_MODEL1=IN_INPUT_OF_CURRENT_FILE1 IN_MODEL2=IN_INPUT_OF_CURRENT_FILE2", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("OUT_MODEL1=OUT_OUTPUT_OF_CURRENT_FILE1 OUT_MODEL2=OUT_OUTPUT_OF_CURRENT_FILE2", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_search():
    """
    Tests .search
    """
    tt.write_word(".search", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("componentfile.blif", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_latch():
    """
    Tests .latch
    """
    tt.write_word(".latch", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("prop1 prop2", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


def test_end():
    """
    Tests .end
    """
    tt.write_word(".end", delay)
    tt.write_hotkey("tab", delay)
    tt.write_word("rest of file should go here", delay)


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
        tt.start_rec()
    else:
        delay = 0.001

    for i in range(initial_wait):
        time.sleep(i)
        print("[START] starting in {} seconds".format(initial_wait-i))
    print("[START] started")

    tests = [
        {"keyword_name": "model", "function": test_model},
        {"keyword_name": "inputs", "function": test_inputs},
        {"keyword_name": "outputs", "function": test_outputs},
        {"keyword_name": "names", "function": test_names},
        {"keyword_name": "exdc", "function": test_exdc},
        {"keyword_name": "start_kiss", "function": test_start_kiss},
        {"keyword_name": "end_kiss", "function": test_end_kiss},
        {"keyword_name": "i", "function": test_i},
        {"keyword_name": "o", "function": test_o},
        {"keyword_name": "s", "function": test_s},
        {"keyword_name": "p", "function": test_p},
        {"keyword_name": "r", "function": test_r},
        {"keyword_name": "code", "function": test_code},
        {"keyword_name": "subckt", "function": test_subckt},
        {"keyword_name": "search", "function": test_search},
        {"keyword_name": "latch", "function": test_latch},
        {"keyword_name": "end", "function": test_end},
    ]

    # test keywords
    if keyword_name == "all":
        # test all the keywords and 
        # delete file content in between
        for test in tests:
            if "Visual Studio Code" in aw.get_active_window():
                test["function"]()
                time.sleep(initial_wait)
                tt.delete_file_content(delay)
            else:
                print("ERROR: no focus on the VS CODE window during '{}' test".format(test["keyword_name"]))
    else:
        found = False
        n = 0
        while n < len(tests) and not found:
            test = tests[n]
            if test["keyword_name"] == keyword_name:
                if "Visual Studio Code" in aw.get_active_window():
                    test["function"]()
                else:
                    print("ERROR: no focus on the VS CODE window during '{}' test".format(keyword_name))
                found = True
            
            n += 1

        if not found:
            print("ERROR: keyword name is invalid")

    # stop recording (if recording)
    if recording_mode:
        print("[RECORDING] Ending recording")
        time.sleep(initial_wait)
        tt.stop_rec()
        print("[RECORDING] Done, stopped recording")

    print("[END] Script ended")
