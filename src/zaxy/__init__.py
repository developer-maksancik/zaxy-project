import os as _os
import random as _random 
import sys as _sys

tx = print
md = _os.mkdir
rm = _os.remove
ls = _os.listdir
gwd = _os.getcwd
ren = _os.rename

def ir(_name, _text=""):
    globals()[_name] = input(f"{_text}" if _text else "")
    
def irn(_name1, _num=0):
    globals()[_name1] = int(input(f"{_num}" if _num else ""))
    
def irf(_name2, _text1=""):
    globals()[_name2] = float(input(f"{_text1}" if _text1 else ""))
    
def pause(_text3=""):
    input(_text3)

def pau(_text4=""):
    input(_text4)

def clear():
    _os.system('cls' if _os.name == 'nt' else 'clear')

def clr():
    _os.system('cls' if _os.name == 'nt' else 'clear')
    
def rn(_a, _b): 
    return _random.randint(_a, _b)

def rc(_list): 
    return _random.choice(_list)

def sh(_list): 
    _random.shuffle(_list)
    return _list

def _xa_wrapper_logic():
    if 'md' in globals():
        __original_md = globals()['md']
        def __safe_md(_path):
            if _os.path.exists(_path):
                print(f"Xa-System-Warning: directory '{_path}' already exists.")
            else:
                try: __original_md(_path)
                except Exception as __e: print(f"Xa-System-Error: {__e}")
        globals()['md'] = __safe_md

    if 'rm' in globals():
        __original_rm = globals()['rm']
        def __safe_rm(_path):
            if not _os.path.exists(_path):
                print(f"Xa-System-Error: path '{_path}' not found.")
            else:
                try: __original_rm(_path)
                except Exception as __e: print(f"Xa-System-Error: {__e}")
        globals()['rm'] = __safe_rm

    if 'irn' in globals():
        def __safe_irn(_var_name, _prompt=""):
            while True:
                __input_val = input(f"{_prompt}" if _prompt else "")
                try:
                    globals()[_var_name] = int(__input_val)
                    break
                except ValueError:
                    print(f"Xa-Runtime-Error: invalid literal for irn(): '{__input_val}' (expected integer)")
        globals()['irn'] = __safe_irn

    if 'irf' in globals():
        def __safe_irf(_var_name, _prompt=""):
            while True:
                __input_val = input(f"{_prompt}" if _prompt else "").replace(',', '.')
                try:
                    globals()[_var_name] = float(__input_val)
                    break
                except ValueError:
                    print(f"Xa-Runtime-Error: invalid literal for irf(): '{__input_val}' (expected float)")
        globals()['irf'] = __safe_irf

def _xa_emergency_handler(_exctype, _value, _tb):
    if issubclass(_exctype, KeyboardInterrupt): return
    
    __err_type = _exctype.__name__.replace('Error', '-Error')
    print(f"\n[Xa-{__err_type}]: {_value}")

_xa_wrapper_logic()
_sys.excepthook = _xa_emergency_handler

del _xa_wrapper_logic 