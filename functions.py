import plotly.express as px

def hist(df, col, title):
    fig = px.histogram(df, col, marginal='box',
                title=title, 
                width=800)
    return fig.show()