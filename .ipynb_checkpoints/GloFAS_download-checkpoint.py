# download control and ensemble GloFAS forecasts (version 4)

import cdsapi
import os

c = cdsapi.Client()

output_directory = "/Users/jamietowner/Documents/flood_aa_training/zimbabwe/data/forecasts/glofas"  # insert directory to store data 

for year in range(2004,2006): # put the year after the one that is needed (e.g., 2004,2006 to get data for 2004 and 2005)
    for month in ['10']:
        for day in ['02','05']: # days will change depending on month selected
                file_name = f'GloFAS_{year}-{month}-{day}.grib'
                file_path = os.path.join(output_directory, file_name)
                
                if not(os.path.exists(file_path)):
                    c.retrieve(
                        'cems-glofas-reforecast',
                        {
                            'system_version': 'version_4_0',
                            'hydrological_model': 'lisflood',
                            'product_type': ['control_reforecast', 'ensemble_perturbed_reforecast'],
                            'variable': 'river_discharge_in_the_last_24_hours',
                            'hyear': str(year),
                            'hmonth': month,
                            'hday': day,
                            'leadtime_hour': [
                                '24', '48', '72',
                                '96', '120', '144',
                                '168',
                            ],
                            'format': 'grib',
                            'area': [
                                0, 20, -28,
                                42,
                                ],
                            },
                        file_path)