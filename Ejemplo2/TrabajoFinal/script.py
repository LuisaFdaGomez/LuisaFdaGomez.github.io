import requests
import os
import urllib.request

url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
## Se obtiene el código html de la página
response = requests.get(url)

## Se imprime la respuesta. Un valor de
## <Response [200]> indica que fue correcta
## la apertura
response

with open("covid.txt", "w") as text_file:
    text_file.write(response.text)

df=pd.read_csv("covid.txt", sep=',')
df.head()