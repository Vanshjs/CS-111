import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()
std_dev=statistics.stdev(data)
mean=statistics.mean(data)
print(f"Mean of the population:{mean}\nStandard Deviation of the population : {std_dev}")

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range(0,1000):
    set_of_means=random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation=statistics.stdev(mean_list)
print("Standard deviation of sampling distribution:-",std_deviation)

z_score=(mean_list-mean)/std_deviation
print (f"The z score is={z_score}")

first_std_dev_start,first_std_dev_end=mean-std_deviation,mean+std_deviation
second_std_dev_start,second_std_dev_end=mean-(2*std_deviation),mean+(
    2 * std_deviation
)
third_std_dev_start,third_std_dev_end=mean-(3*std_deviation),mean+(
    3*std_deviation
)

fig=ff.create_distplot([mean_list],["Reading Time"],show_hist=False,show_rug=False)
fig.add_trace(go.Scatter(x=[mean, mean],y=[0, 0.17],mode="lines", name="Mean"))
fig.add_trace(
    go.Scatter(
        x=[first_std_dev_end,first_std_dev_end],
        y=[0,0.17],
        mode="lines",
        name="Standard Deviation 1"
    )
)
fig.add_trace(
    go.Scatter(
        x=[second_std_dev_end,second_std_dev_end],
        y=[0, 0.17],
        mode="lines",
        name="Standard Deviation 2"
    )
)
fig.add_trace(
    go.Scatter(
        x=[third_std_dev_end,third_std_dev_end],
        y=[0, 0.17],
        mode="lines",
        name="Standard Deviation 3"
    )
)
fig.show()