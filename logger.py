import os

def log(participant, task, state, time):
    """
    :param participant: The participant name or id, a folder will be created
    :param task: The task ID
    :param state: The state (Start or stop)
    :param time: The timestamp of the state
    """
    if not participant or not task:
        return
    path = f'logs/{participant}'
    if not os.path.exists(path):
        os.makedirs(path)

    # https://stackoverflow.com/questions/20432912/writing-to-a-new-file-if-it-doesnt-exist-and-appending-to-a-file-if-it-does
    textToWrite = str(participant) + ',' + str(task) + ',' + str(state) + ',' + str(time) + '\n'
    if state == 'Stop':
        textToWrite = textToWrite + '\n'
    taskFilePath = f'logs/{participant}/{task}.txt'
    if os.path.exists(taskFilePath):
        append_write = 'a'  # append if already exists
    else:
        append_write = 'w'  # make a new file if not
    file = open(taskFilePath, append_write)
    file.write(textToWrite)
    file.close()
