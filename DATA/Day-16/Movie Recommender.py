import tkinter as ttk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

app=ttk.Tk()
app.title('Movie Recommender')
app.geometry('400x400')

cols=['user_id','movie_id','rating','ts']
item_cols=['movie_id','title']+ list(range(22))
df= pd.read_csv('u.data',sep='\t', names=cols ).drop('ts',axis=1)
df1=pd.read_csv('u.item', sep='|', encoding='ISO-8859-1', names=item_cols)[['movie_id','title']]
movie= pd.merge(df,df1, on='movie_id')

result = ttk.Variable(app)
box = ttk.Listbox(app, height=10)
for row, val in movie.iterrows():
    box.insert(row+1,val['title'])
box.place(x=10,y=10)

def get_movie():
    pass

ttk.Button(app, text='Find Recommendation', font=('Arial',22), command = get_movie).palce(x=200,y=50)
ttk.Label(app, textvariable=result, font=('Arial',22)).place(x=200,y=100)

app.mainloop()