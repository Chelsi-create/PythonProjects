from datetime import datetime

with open("2.ico", 'ab') as a:
    a.write(str(datetime.now()).split('.')[0] + '\n')
    a.close()