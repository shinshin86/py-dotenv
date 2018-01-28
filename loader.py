import os
from os.path import join


def __env_load(filepath):
    env = {}
    with open(filepath) as f:
        for t in f:
            key = t.split("=")[0]
            value = t.split("=")[1]
            value = value.split("#")[0].rstrip()
            env[key] = value
        return env

def env_load():
    return __env_load(join(os.getcwd(), "./env"))
