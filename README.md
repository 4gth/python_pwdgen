# python_pwdgen
A simple password generator that allows a user to generate one or many passwords that contain letters with options to include numbers and special characters.

This version uses Python's `secrets` module for cryptographically secure randomness.

You can pass arguments to the program

- `-l`, `--length` Length of each generated password (default: 8)
- `-g`, `--count`  How many passwords to generate (default: 1)
- `-s`, `--symbols` Include symbols (punctuation)
- `-n`, `--numbers` Include numbers (0-9)

Example

```bash
python pwdgen.py -l 16 -g 20 -s -n
```

This will print 20 passwords, each 16 characters long, using symbols and numbers.
