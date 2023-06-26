def generateGraph():
    from datetime import datetime
    import matplotlib.pyplot as plt
    # Read the datetime data from a file
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
    final_dict=dict(sorted(final_dict.items()))
    hours = list(final_dict.keys())
    frequencies = list(final_dict.values())

    # Plot the data
    plt.plot(hours, frequencies, marker='o')
    #plt.scatter(hours, frequencies)
    plt.xticks(range(len(hours)),hours)

    # Set the x-axis label
    plt.xlabel("Hour")

    # Set the y-axis label
    plt.ylabel("Frequency")

    # Set the title of the plot
    plt.title("Hourly Frequency")

    # Display the plot

    plt.savefig('./static/assets/img/drowsygraph.png')
generateGraph()