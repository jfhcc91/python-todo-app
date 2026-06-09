# Python To-Do App 🐹

A command-line task manager built in Python, using SQLite for persistent data storage.

## What it does

- Add tasks and save them to a local database
- View all current tasks
- Delete tasks by ID
- Data persists between sessions (stored in `todo.db`)

## What I learned

- Working with SQLite databases in Python (`sqlite3` module)
- Writing and executing SQL queries (SELECT, INSERT, DELETE)
- Building interactive CLI menus with loops and input validation
- Handling user errors gracefully (e.g. invalid input types)

## How to run it

Make sure you have Python 3 installed, then:

```bash
python todo.py
```

## Built with

- Python 3
- SQLite3 (built into Python)

## Status

Work in progress — planned improvements include marking tasks as complete 
and filtering by status.
