# gitusr

by Jeffrey Rutledge

gitusr is a shell script that allows you to easily manage using multiple git hub accounts.
The script adds a shell command `gitusr`.
This shell command allows you to change or check the current git hub account with a simple flag.
For example, to change to your work email you might type `gitusr -w`.

_(Full feature list below)_

## Setup
Run the setup.py script and answer the questions.
When in the directory containing setup.py, you can run the python script using:
```sh
./setup.py
```
The script will ask you for an email and then a flag to use with that email.
It will continue doing this until you type `done` for an email.
Then it will output the shell script to `/usr/local/bin/gitusr`.
This will allow you to use the `gitusr` command in your shell.

### Reconfigure
Run the setup.py script again.
This will ask you the same questions and overwrite the existing shell script.

## Uninstall
Delete the shell script file.
This can be done with the command:
```sh
rm /usr/local/bin/gitusr
```

## Features
* Check git email of current repository
  ```sh
  gitusr
  ```
  
  _or check global git email_
  
  ```sh
  gitusr -g
  ```

* Change the current git email
  _(Assuming you have an email set to use the -w flag)_

  ```sh
  gitusr -w
  ```
  
  _or change the global git email_

  ```sh
  gitusr -g -w
  ```

* Display a help message _(including set email flags)_
  ```sh
  gitusr -h
  ```
  
#### System Requirements
The setup script is written in python 3 so you will need python 3.
