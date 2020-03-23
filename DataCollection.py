import OpenBlender
import pandas as pd
import json


action = 'API_getObservationsFromDataset'

# ANCHOR: 'COVID19 Confirmed Cases'
#This data is heavily limited due to payment required to download OpenBlender Data sets

        
parameters = { 
    	'token':'5e77a74195162926d7d24132f5X0cUlVBS1W2lMhDuq7MTXRCHk4ye',
	'id_user':'5e77a74195162926d7d24132',
	'id_dataset':'5e6ac97595162921fda18076',
	'last_100_observations':'on',
	'drop_features':["confirmed","recovered","longitude","latitude"] 
}
        

df = pd.read_json(json.dumps(OpenBlender.call(action, parameters)['sample']), convert_dates=False, convert_axes=False).sort_values('timestamp', ascending=False)
df.reset_index(drop=True, inplace=True)
df.head()