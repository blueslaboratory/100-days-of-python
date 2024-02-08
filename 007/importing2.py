# 08/02/2024
# Day - 007

import importlib, importlib.util

def module_directory(name_module, path):
    P = importlib.util.spec_from_file_location(name_module, path)
    import_module = importlib.util.module_from_spec(P)
    P.loader.exec_module(import_module)
    return import_module

hangman = module_directory("hangman_art", "007\hangman5\hangman_art.py")

print(hangman.logo)