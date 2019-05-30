# 带包的file operation
# Python 3
# coding: UTF-8
import pickle


def save_file(obj, file_name):
    with open(file_name, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_file(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)
