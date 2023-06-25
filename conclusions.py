from datetime import datetime
import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
def most_Drowsy():
    
    with open("times.txt", "r") as file:
        datetime_data = file.readlines()

# Create a dictionary to store the hour-wise event count
    event_counts = {}

    # Count the events in each hour, ignoring events in the same minute
    for dt_str in datetime_data:
        dt = datetime.strptime(dt_str.strip(), "%m/%d/%y:%H:%M:%S")
        hour = dt.strftime("%H")
        minute = dt.strftime("%M")
        hour_minute = f"{hour}:{minute}"
        
        if str(hour_minute)[0:5] not in event_counts:
            
            event_counts[str(hour_minute)[0:5]]=1
        else:
            event_counts[str(hour_minute)[0:5]]+=1
    final_dict={}

    for i in event_counts:
        if int(str(i[0:2])) not in final_dict:
            final_dict[int(str( i[0:2]))]=1
        else:
            final_dict[int(str( i[0:2]))]+=1
    final_dict=dict(sorted(final_dict.items(),key=lambda x:x[1],reverse=True))
    l=list(final_dict.keys())
   
    i=l[0]
    f=open('mostdrowsy.txt','w')
    f.write(str(i)+'hrs To '+str(i+1)+'hrs  '+'\n')
        
    f.close()
    i=l[0]
    with open('optimalbreak.txt','w') as f:
        
        f.write(str(i-1)+'hrs To '+str(i)+'hrs'+'\n')
        f.close()
    
    
def fatiguepredictions():
    with open("times.txt", "r") as file:
        datetime_data = file.readlines()

# Create a dictionary to store the hour-wise event count
    event_counts = {}

    # Count the events in each hour, ignoring events in the same minute
    for dt_str in datetime_data:
        dt = datetime.strptime(dt_str.strip(), "%m/%d/%y:%H:%M:%S")
        hour = dt.strftime("%H")
        minute = dt.strftime("%M")
        hour_minute = f"{hour}:{minute}"
        
        if str(hour_minute)[0:5] not in event_counts:
            
            event_counts[str(hour_minute)[0:5]]=1
        else:
            event_counts[str(hour_minute)[0:5]]+=1
    final_dict={}
    hours=[]
    frequency=[]
    for i in event_counts:
        if int(str(i[0:2])) not in final_dict:
            final_dict[int(str( i[0:2]))]=1
        else:
            final_dict[int(str( i[0:2]))]+=1
    final_dict=dict(sorted(final_dict.items()))
    
    for i in final_dict.keys():
        if final_dict[i]>20:
            hours+=[i]
            frequency+=[final_dict[i]]
            
    
    plt.bar(hours,frequency)
    plt.axhline(y=20,color='r',linestyle="-")
    plt.xticks(range(len(hours)),hours)
    
    
    plt.text(8, 25, 'Fatigue Line', fontsize=15)
    

    # Set the x-axis label
    plt.xlabel("Hour")

    # Set the y-axis label
    plt.ylabel("Frequency")

    # Set the title of the plot
    plt.title("Hourly Frequency")
    plt.savefig('./static/assets/img/FatiguePrediction.png')
    
most_Drowsy()
fatiguepredictions()


    



