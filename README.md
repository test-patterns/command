# Command Pattern
Sample problem featuring the command pattern.

## Task 1 - Add a command

Welcome to Pizza<sup>2</sup>! Our kitchen already outputs messages when a new order is received, and when ingredients are prepped, but we can't see when a pizza has been baked. See for yourself by running the following command:

```
python command -q 1 -s Large -c Thin -t Cheese
```

Add a new command to the command sequence in main.py to output a message when a pizza has been baked.

## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source command -m unittest discover tests
coverage report -m
```

Increase this to 100%.
