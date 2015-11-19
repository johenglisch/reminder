#! /usr/bin/env python3


import sys
import re
from os.path import expanduser

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


TODO_FILE = expanduser('~/TODO')


def make_window(label):
    win = Gtk.Window(title='TODO')
    win.add(Gtk.Label(label=label))

    win.connect('delete-event', Gtk.main_quit)
    return window


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else TODO_FILE

    try:
        with open(filename, 'r', encoding='UTF-8') as todo_file:
            todo_items = '\n'.join(
                ' - {} '.format(line.strip()) for line in todo_file
                if line and not line.isspace())
    except IOError as error:
        print(error, file=sys.stderr)
        return

    if not todo_items:
        return

    win = make_window(todo_items)
    win.show_all()
    Gtk.main()


if __name__ == '__main__':
    main()
