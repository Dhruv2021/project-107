import csv
import pandas as pd
import plotly.express as ex

df=pd.read_csv("data.csv")
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()

figure=ex.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
figure.show()