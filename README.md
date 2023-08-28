## Tasks assigned in my design verification training at Progineer

### 1st task:
####    - Part A: create a shell script to do the following:
1. Create a tmp dir in your home dir.
2. Create 5 sub dir in tmp, with names training_project_<index num>
3. In each sub dir, create 2 txt files named module_<index num>_a.txt and module_<index num>_b.txt
4. In each file add the command: echo “Hello <your first name/ last name> welcome to file <indexnum>.<A/ B>”

####    - Part B: the same as the first, except that instead of your first and last name being hard coded, the script should read them from 2 environment variables.
####    - Part C: the first and last names should be passed using shell script args. Also add the optional -cap arg. Your script should have a help arg and the user is not required to use a specific order for the args.


### 2nd task:
Implement the scripts described in the first task in python.


### 3rd task:

Write a Python script that read from a csv file with colors data in it, it should:

- Print out the number of cells for each color.
- It should print out an error if one of the rows matches a condition given in the error arg.
- The function reading from the csv file should NOT do any processing on the data, just reading the cells and returning the info.

Think of using generators, tuples and dictionaries.

Ex: `python my_script.py -error “this is a broken cell”` Output:
```
Reading CSV file

Found a broken cell in row <> col <>
Found a broken cell in row <> col <>

Done reading CSV file

Found: <> red cells, <> blue cells ...
```
