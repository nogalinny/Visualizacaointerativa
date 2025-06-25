import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Carregar os dados
df = pd.read_excel('ecommerce_estatistica.xlsx')

# Gráfico de Pizza - Distribuição por Gênero
fig = px.pie(df, names='Gênero', values='Quantidade Vendida', title='Distribuição de Vendas por Gênero')

# Inicializar o app Dash
app = dash.Dash(__name__)

# Layout do app
app.layout = html.Div([
    html.H1('Dashboard Interativo - E-commerce'),
    dcc.Graph(figure=fig)
])

# Rodar o servidor
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8050)))
