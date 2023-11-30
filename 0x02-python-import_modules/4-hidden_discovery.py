#!/usr/bin/python3
import importlib
import types

def print_module_names(module_name):
    try:
        module = importlib.import_module(module_name)
        all_names = [name for name in dir(module) if not name.startswith('__')]
        all_names.sort()
        for name in all_names:
            print(name)
    except (ModuleNotFoundError, FileNotFoundError):
        print(f"Module {module_name} not found.")

print_module_names("hidden_4")
