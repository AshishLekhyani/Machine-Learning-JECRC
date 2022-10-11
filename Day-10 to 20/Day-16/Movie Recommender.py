import tkinter as ttk
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import os
print('Location is:',os.getcwd(),'\n\n\n\n')

app=ttk.Tk()
app.title('Movie Recommender')
app.geometry('450x400')

cols=['user_id','movie_id','rating','ts']
item_cols=['movie_id','title']+ list(range(22))
df= pd.read_csv('u.data',sep='\t', names=cols ).drop('ts',axis=1)
df1=pd.read_csv('u.item', sep='|', encoding='ISO-8859-1', names=item_cols)[['movie_id','title']]
movie= pd.merge(df,df1, on='movie_id')

result = ttk.Variable(app)

frame = ttk.Frame(app)
frame.place(x=10,y=10)

box = ttk.Listbox(frame, height=10, width=50)
for title in movie['title'].unique():
    box.insert(ttk.END, title)
# box.grid(row = 0, column=0)
box.pack(side='left', fill = 'y')
# box.place(x=10,y=10)

scroll = ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(command = box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right', fill='y')

def get_movie():
    movie_selected = box.get(box.curselection())
    print('Movie Selected',movie_selected)
    
    #Create The Pivot Table
    movie_pivot = movie.pivot_table(index='user_id',columns = 'title',values='rating')
    
    #Find Similarities for Selected Movie
    corrs = movie_pivot.corrwith(movie_pivot[movie_selected])
    corrs_df=pd.DataFrame(corrs,columns=['correlation'])
    corrs_df['rating']=movie.groupby('title')['rating'].mean()
    corrs_df['count']=movie['title'].value_counts()
    
    #Find Top 2-3 Recommendations
    top_recom = list(corrs_df[corrs_df['count']>50].sort_values(by='correlation',ascending=False).head(3).index)

    ## Important
    if movie_selected in top_recom:
        top_recom.remove(movie_selected)
    print('Recommendations:', top_recom)

    if top_recom:
        result.set(top_recom[0])
    else:
        result.set('Sorry No Recommendations Found!!')
        
ttk.Button(app, text='Find Recommendation', font=('Arial',22), command = get_movie).place(x=10,y=230)
ttk.Label(app, textvariable=result, font=('Arial',22)).place(x=10,y=330)

app.mainloop()