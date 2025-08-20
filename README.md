# Faktus dashboard
## Create an virtual environment and install requirements
```bash
pip install pdm
pdm init
pdm install
```

## Run Streamlit
```bash
pdm run streamlit run app.py
```

## Google Console
The redirect URI (where the response is returned to) has to be registered in the APIs console.

Go to the console for your project and look under API Access. You should see your client ID & client secret there, 
along with a list of redirect URIs. If the URI you want isn't listed, click edit settings and add the URI to the list.

Note that updating the google api console and that change being present can take some time. Generally only a few minutes but sometimes it seems longer.
