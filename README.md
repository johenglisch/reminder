Reminder
========


## DESCRIPTION

`Reminder` creates a small window, which shows the content of a TODO list file.
It is best added to the auto-start section of the operating system, so that the
user is reminded of their agenda on every system start.

## REQUIREMENTS

 * Python3
 * PyGObject3

## USAGE

The programme is reading the TODO data from a simple plain text file.  Each
non-empty line in the file is considered a TODO list item.  The name of the TODO
file can be specified as a command-line argument.  If no command-line arguments
are supplied `Reminder` defaults to using the file `$HOME/TODO`.

## LICENSE

See `LICENSE` file.
