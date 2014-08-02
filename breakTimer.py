##################
### BreakTimer ###
##################

'''
BreakTimer is a simple Python script that allows users to create a daily task list. 
It then 'executes' one of these tasks every 50 minutes by opening an (intentionally) annoying browser tab.
After you complete your task you will be prompted to start another time block.

According to MIT, the most effective method of study includes a 10-minute break for every 50 minutes of work.
According to ME, 10 minutes is plenty of time to get any number of little, annoying things done. 
The things that stack up and create mental chaos. It just takes a little planning and reminding.

(The current test version launches a task every 10 seconds for testing. To change this, open breakTimer.py and follow instructions on line 22)
'''

import time
import webbrowser
import os.path
import random
# import pickle

def main():
    userTasks = []
    work(createTaskList(userTasks), 10) # Value in seconds.  Change to 50*60 for actual 50 minute block
    
def writeFile(html, filename):
    '''
    Write a file with the given name and the given text.
    '''
    output = open(filename,"w")
    output.write(html)
    output.close()

def openHTMLinBrowser(currentTask, filename='breaks.html'):
    '''
    Opens browser tab with filename url loaded
    
    Note: at this time browseLocal will create a file 'breaks.html' in the users home directory.  
    Apologies, until I figure out Python relative paths.
    
    '''
    writeFile(currentTask, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) # elaborated for Mac

def createTaskList(tasks):
    '''
    Take a list and append raw_inputs until the user exits
    expects: list
    returns: list
    '''
    
    while True:
        task = raw_input('Input your tasks one at a time (s to start working/v to view tasks): ')
        
        if task == 's':
            return tasks or []
        elif task == 'v':
            printTasks(tasks, 'o')
        elif task == '':
            pass
        else: 
            tasks.append(task)

def printTasks(tasks, orderedUnordered):
    '''
    expects: list
    prints: contents of list in numeric order
    '''
    if orderedUnordered == 'o':
        for idx in range(len(tasks)):
            print str(idx + 1) + '. ' + tasks[idx]
    elif orderedUnordered == 'u':
        for task in tasks:
            print task
    
def work(tasks, n):
    '''
    Launch a browser tab n seconds after user starts a 'block' with random task from 'tasks' list embedded in html.
    While loop continues until user exits or there are no more elements in the 'tasks' list
    
    expects: list
    returns: nothing
    '''
    completedTasks = []
    
    if tasks == []:
        begin = raw_input('You didn\'t enter any tasks! (t to add tasks/any other key to quit) ')
        if begin == 't':
            createTaskList(tasks)
        else:
            return
    
    while True:    
         
        # begin = raw_input('Begin a ' + str(n / 60.0) + ' minute block (b to begin/q to quit)? ')
        begin = raw_input('Begin a 50 minute block? (b to begin/t to add more tasks/v to view tasks/q to quit): ')
        if begin == 'q':
            return
        
        elif begin == 'v':
            print 'PENDING TASKS: '
            printTasks(tasks, 'o')
            print 'COMPLETED TASKS: '
            if completedTasks == []:
                print 'You\'ve done nothing!'
            else:
                printTasks(completedTasks, 'u')
            
        elif begin == 't':
            createTaskList(tasks)
        
        elif tasks == []:
            contents = '<center><p style="font-size:250px">No more tasks, go for a walk!</p></center>'
            openHTMLinBrowser(contents)
            return
        
        #3 If yes, wait x minutes
        elif begin == 'b':
            time.sleep(n)
        
            #4 After x minutes, execute break
            randomTask = random.randint(0, len(tasks) - 1)
        
            htmlTask = '<center><p style="font-size:250px">' + tasks[randomTask] + '</p></center>'
        
            openHTMLinBrowser(htmlTask)
            
            discard = raw_input('Did you complete your task? (y for yes, d to delete it, any other key to keep it in the task list): ')
            if discard == 'y':
                completedTasks.append(tasks[randomTask])
                tasks.remove(tasks[randomTask])
            elif discard == 'd':            
                tasks.remove(tasks[randomTask])
                
            

if __name__ == '__main__':
    main()


