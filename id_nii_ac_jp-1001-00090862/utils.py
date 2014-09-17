#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    pass


if __name__ == '__main__':
    main()


def print_and_exit(*args):
    try:
        print(type(*args))
    except TypeError:
        pass
    print(*args)
    exit()
