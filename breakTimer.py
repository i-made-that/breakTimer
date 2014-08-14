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
'''

import time
import webbrowser
import os.path
import random

def main():
    userTasks = []
    work(createTaskList(userTasks), 2) # Value in seconds.  Change to 50*60 for actual 50 minute block

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
    webbrowser.open("file:///" + os.path.abspath(filename))

def createTaskList(tasks):
    '''
    Take a list and append raw_inputs until the user exits
    expects: list
    returns: list
    '''

    while True:
        print '\n-----------------\nCurrent tasks:'
        if tasks == []:
            print 'None'
        else:
            printTasks(tasks, 'o')
        print '-----------------\n'
        task = raw_input('Input your tasks one at a time, or hit \n(w) to start working:\n=> ')

        if task == 'w':
            return tasks or []

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
        begin = raw_input('You didn\'t enter any tasks!\n(t) to add tasks/any other key to quit\n=> ')
        if begin == 't':
            createTaskList(tasks)
        else:
            return

    while True:

        # begin = raw_input('Begin a ' + str(n / 60.0) + ' minute block (b to begin/q to quit)? ')
        print '\n-----------------\nWork Menu\n-----------------\n'
        begin = raw_input('(b) to begin a new 50 minute block\n(t) to add more tasks\n(v) to view tasks\n(q) to quit\n=> ')
        if begin == 'q':
            return

        elif begin == 'v':
            print '\nPENDING TASKS: '
            printTasks(tasks, 'o')
            print '\nCOMPLETED TASKS: '
            if completedTasks == []:
                print 'You\'ve done nothing!'
            else:
                printTasks(completedTasks, 'u')

        elif begin == 't':
            createTaskList(tasks)

         # print notification when there are no more tasks to complete
        elif tasks == []:
            contents = '<center><p style="font-size:200px">No more tasks, go for a walk!</p></center>'
            openHTMLinBrowser(contents)
            return

        #3 If yes, wait x minutes
        elif begin == 'b':
            time.sleep(n)

            #4 After x minutes, execute break
            randomTask = random.randint(0, len(tasks) - 1)

            htmlTask = '<center><p style="font-size:200px">' + tasks[randomTask] + '</p></center>'

            openHTMLinBrowser(htmlTask)

            print '\n-----------------\nDid you complete your task?\n-----------------\n'
            discard = raw_input('(y) for yes\n(d) to delete the task\nany other key to keep it in the task list\n=> ')
            if discard == 'y':
                completedTasks.append(tasks[randomTask])
                tasks.remove(tasks[randomTask])
            elif discard == 'd':
                tasks.remove(tasks[randomTask])



if __name__ == '__main__':
    main()


