

#ntfy messaging thing
import requests
import time
import pandas as pd
import os


def push_latest_timestamp( tval ): 
    tnow = time.time() 
    
    #update the project file with current time
    f = open( "./timestamp.txt", "w")
    f.write(str(tval))
    f.close()
    
    #push that to git
    os.system('git pull origin main --no-edit --allow-unrelated-histories') #the no-edit is so it merges automatically 
    
    os.system( ' \n git add . \n  git commit -a -m "data_automatic" ')
            
    os.system( ' \n git push origin main')
    print("backup via git is done")

   
#send a message saysing all's well, I'm alive, here's the latest timestamp
while True: 
    try: 
        #look up the file:
        filepath = "/home/cjchandler/Git_Projects/incubator/incubator/today_dataVDP.csv"
        #look at the pandas thing for last timestamp
        df = pd.read_csv(filepath)
        print(df.tail(20))
        tsaved = df[df.columns[2]].iloc[-1] #2 is the last time saved column
        
        push_latest_timestamp( tsaved  )

    except Exception as e:
        print(e)
        
    time.sleep(1*60)
