# TASK 02

## Requirement

Today you noticed that functions in Python can have a variable number of parameters. For this task you will receive as input several arguments, of which you will have to keep only those that meet one of the conditions:

* be **integer** numbers
* be lowercase consonants

ATTENTION: words and phrases **are** not taken into account

## Example

```text
input:
50 'A' 8.2 'c' '_' 3 'n' True 'Z' [1,2] 't' "meow"

output:
50 'c' 3 'n' 't'
```

Solution hints:

* use the type function
* if you use the isinstance function, take into account that bool True/False type variables are considered ints 1/0

## Run | Testing

For testing, you can run the script directly from the IDE or you can run the command in the terminal:

```bash
./checker.py
```

If you cannot run this script due to permissions, use the following command first:

```bash
sudo chmod 644 checker.py
```
