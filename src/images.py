import requests
import json
def getLogoUri(jsonfile):
  file =open(jsonfile)
  
  data = json.load(file)
  for i in data['tokens']:
    print(i)
    try:
      img_data = requests.get(i['logoURI']).content
      imgName = 'images/' + i['symbol']+'.jpg'
      with open(imgName, 'wb') as handler:
        handler.write(img_data)
    except:
      continue

# getLogoUri('coingecko.json')
getLogoUri('1inch.json')