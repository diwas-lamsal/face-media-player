# import configparser
#
# def set_gesture_mode(mode = 'head'):
#     config = configparser.ConfigParser()
#     config['DEFAULT']['gesturemode'] = mode
#     with open('config.ini', 'w') as configfile:
#         config.write(configfile)
#
# # https://docs.python.org/3/library/configparser.html
# def get_gesture_mode():
#     config = configparser.ConfigParser()
#     try:
#         config.read('config.ini')
#         return config['DEFAULT']['gesturemode']
#     except:
#         return 'head'
#

def set_gesture_mode(mode = 'head'):
    with open('config.txt', 'w') as f:
        f.write(mode)

# https://www.guru99.com/python-file-readline.html#:~:text=Python%20readline()%20method%20reads,will%20return%20you%20binary%20object.
def get_gesture_mode():
    try:
        f = open("config.txt", "r")
        l = f.readline()
        f.close()
        return l
    except:
        return 'head'
