##################
### BreakTimer ###
##################

BreakTimer is a simple Python script that allows users to create a daily task list. 
It then 'executes' one of these tasks every 50 minutes by opening an (intentionally) annoying browser tab.

According to MIT, the most effective method of study includes a 10-minute break for every 50 minutes of work.
8 hours * 10 minutes = almost an hour and a half of FREE time.

According to ME, 10 minutes is plenty of time to get any number of little, annoying things done. The things that stack up and create mental chaos.
It just takes a little planning and reminding.

*** Note: at this time browseLocal will create a file 'breaks.html' in the users home directory.  Apologies, until I figure out Python relative paths. ***

(The current test version executes every 10 seconds for testing)

To run, open Terminal, navigate to the breakTimer directory, and type:

python breakTimer.py
