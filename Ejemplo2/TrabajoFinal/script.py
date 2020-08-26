import requests
import os
import urllib.request
url = 'https://www.datos.gov.co/resource/gt2j-8ykr.json?ciudad_de_ubicaci_n=Medell%C3%ADn'
#url = 'https://www.datos.gov.co/api/views/gt2j-8ykr/rows.csv?accessType=DOWNLOAD'
## Se obtiene el código html de la página
response = requests.get(url)

## Se imprime la respuesta. Un valor de
## <Response [200]> indica que fue correcta
## la apertura
response
med=pd.read_json(response.text)
import matplotlib.pyplot as plt
def graficar(x, y, labelX, labelY):
    plt.figure()
    plt.scatter(x, y)
    plt.xlabel(labelX)
    plt.ylabel(labelY)
    plt.savefig('figura2')
    plt.show()

graficar(med['tipo'], med['edad'], 'tipo', 'edad')