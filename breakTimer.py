##################
### BreakTimer ###
##################

'''
BreakTimer is a simple Python script that allows users to create a daily task list. 
It then 'executes' one of these tasks every 50 minutes by opening an (intentionally) annoying browser tab.
According to MIT, the most effective method of study includes a 10-minute break for every 50 minutes of work.
8 hours * 10 minutes = almost an hour and a half of FREE time.
According to ME, 10 minutes is plenty of time to get any number of little, annoying things done. The things that stack up and create mental chaos.
It just takes a little planning and reminding.
'''

import time
import webbrowser
import os.path
import random
# import pickle

def main():
    userTasks = []
    work(inputList(userTasks), 10) # Value in seconds.  Change to 50*60 for actual 50 minute block
    
def strToFile(html, filename):
    '''
    Write a file with the given name and the given text.
    '''
    output = open(filename,"w")
    output.write(html)
    output.close()

def browseLocal(currentBreak, filename='breaks.html'):
    '''
    Opens browser tab with filename url loaded
    
    Note: at this time browseLocal will create a file 'breaks.html' in the users home directory.  
    Apologies, until I figure out Python relative paths.
    
    '''
    strToFile(currentBreak, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) # elaborated for Mac

def inputList(tasks):
    '''
    Take a list and append raw_inputs until the user exits
    expects: list
    returns: list
    '''
    
    while True:
        task = raw_input('Input today\'s tasks (s to start working): ')
        
        if task == 's':
            return tasks or []
        elif task == '':
            pass
        else: 
            tasks.append(task)
        

def work(tasks, n):
    '''
    Launch a browser tab n seconds after user starts a 'block' with random task from 'tasks' list embedded in html.
    While loop continues until user exits or there are no more elements in the 'tasks' list
    
    expects: list
    returns: nothing
    '''
    if tasks == []:
        print 'You didn\'t enter any tasks!'
        return
    
    while True:    
         
        # begin = raw_input('Begin a ' + str(n / 60.0) + ' minute block (b to begin/q to quit)? ')
        begin = raw_input('Begin a 50 minute block? (b to begin/q to quit): ')
        if begin == 'q':
            return
        
        elif tasks == []:
            contents = '<center><p style="font-size:250px">No more tasks, go for a walk!</p></center>'
            browseLocal(contents)
            return
        
        #3 If yes, wait x minutes
        elif begin == 'b':
            time.sleep(n)
        
            #4 After x minutes, execute break
            randomTask = random.randint(0, len(tasks) - 1)
        
            contents = '<center><p style="font-size:250px">' + tasks[randomTask] + '</p></center>'
        
            browseLocal(contents)
          
            #5 Remove current task from list
            tasks.remove(tasks[randomTask])
            #7 Return tasklist    
      
            #print tasks
    

if __name__ == '__main__':
    main()


