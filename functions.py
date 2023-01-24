import plotly.express as px

def hist(df, col):
    fig = px.histogram(df, col, marginal='box',
                title='Distribution of Number of Withdrawals', 
                width=800)
    return fig.show()