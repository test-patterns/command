# Command Pattern
Sample problem featuring the command pattern.

Use this pattern if you require the executor of the command to not know anything about the command, what context information it needs, or what it does. This pattern encapsulates everything required to take an action and allows the execution of the action to occur completely independently.

## Task 1 - Add a command

Welcome to Pizza<sup>2</sup>! Our kitchen already outputs messages when a new order is received, and when ingredients are prepped, but we can't see when a pizza has been baked. See for yourself by running the following command:

```
python command -q 1 -s Large -c Thin -t Cheese
```

Add a new command to the command sequence in main.py to output a message when a pizza has been baked.

### UML

![alt text](http://yuml.me/ac98beb8.png)
[edit](http://yuml.me/edit/ac98beb8)

### Previous output

```
Recorded a new pizza order: 1 Large Thin pizza with Cheese
Prepped 1 Large Thin crust
Prepped 1 Cheese
```

### Desired output

```
Recorded a new pizza order: 1 Large Thin pizza with Cheese
Prepped 1 Large Thin crust
Prepped 1 Cheese
Baked 1 Large Thin pizza with Cheese
```


## Task 2 - Testing

Our test coverage is pretty terrible. See for yourself by running the following commands:

```
coverage run --source command -m unittest discover tests
coverage report -m
```

Increase this to 100%.
