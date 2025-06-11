# MPFDA-bespinosa
Author: **Brian Espinosa Acosta**  
email: bespinosaaco@mun.ca
--
Github Repository for the Microcredential in Practical Foundations for Data Analytics course.  
GitHub Link: https://github.com/bespinosaaco/MPFDA-bespinosa

## Directory structure
```text
\project_HPC
    -bespinosa_acosta.py # Python Script for weekly report using HPC
    -bespinosa_acosta.sh
    -requirements.txt 
    -Assigment3_Instructions.txt
    -dictionaries.txt
    -...
\project_weekly_tracker
    -bespinosa_acosta.ipynb # Habits Tracker
    -bespinosa_acosta_cleared.ipynb # Same but without instructions
```

## How to use the weekly tracker

For a cleaner user experience use the `bespinosa_acosta_cleared.ipynb`.  
To see all the workings and instructions use the `bespinosa_acosta.ipynb`.

The usage is simple. Run the cell titled functions and imports to define all the functions of the weekly tracker. Then run the **Main Logic (Part 6)** cell which will initialize the program.

Decide wether to initiate a new weekly tracker or continue with the one on the saved Jupyter running instance.

Then follow the prompt to add, mark as complete, remove or print task and habits.

Here is the option menu for the program.

```text
Weekly Habit Tracker Menu:
1. Add a task to a day
2. Add a habit for the week
3. Mark a task as completed
4. Mark a habit as completed
5. Remove a task from a day
6. Remove a habit from the tracker
7. View weekly summary of tasks and habits
8. View activity for a specific day
9. Print all tasks
10. Print all habits
11. Exit
12. Print Menu
```

## How to run the HPC job

1. Log in to the remote server
```bash
ssh <user>@mokey.micro.ace-net.training # User given by Acenet
```
```bash
ssh bespinosaaco@mokey.micro.ace-net.training 
```

2. Copy project folder from local to remote
```bash
scp -r path/to/local/folder <user>@mokey.micro.ace-net.training:path/to/remote/
```
Use the `pwd` command to find the working directory path
**Note** the parent directory for my project_HPC folder on the server will be assignment3

3. Create the `job.sh`

4. Ensure that in the working directory this list of files exist
- bespinosa_acosta.py
- bespinosa_acosta.sh
- requirements.txt
- dictionaries_1.txt
- ...

5. Run the job `bespinosa_acosta.sh`

```bash
sbatch bespinosa_acosta.sh
```

6. Double-Check the results `cat bespinosa_acosta.out`

#### Troubleshooting

- Run `squeue -u bespinosaaco` to check status
- Check efficiency `seff <ID>`
- Cancel a job
```bash
scancel <ID>
scancel <ID> <ID2> <ID3>
scancel -u user1
scancel -u user1 -t PENDING
```

