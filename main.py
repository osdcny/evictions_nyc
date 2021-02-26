import pandas as pd
from sodapy import Socrata
import datetime


if __name__ == '__main__':
    
    client = Socrata("data.cityofnewyork.us", '9qYS11lW1LB57v1Pd5qnhcGqM')
    results = client.get("6z8x-wfk4", limit=100000000)
    df = pd.DataFrame.from_records(results)
    
    # cols_to_use = ['borough', 'eviction_zip', 'executed_date', 'residential_commercial_ind', 'eviction_address', 'docket_number'] #'eviction_apt_num'
    
    # df = df[cols_to_use]
    
    df = df.astype({'borough': str, 'eviction_zip': 'int32', 'executed_date': 'datetime64[ns]', 
                    'residential_commercial_ind': str,'eviction_address': str, 'docket_number': 'int' }) #'eviction_apt_num': str
    
    
    # Correct a mistake
    # The executed_date for the case 317112 (docket_number) is mistakenly labelled as 2070-03-29.
    # We assume it was 2007.
    df.loc[df['docket_number'] == 317112, 'executed_date'] = datetime.datetime(2007,3,29)
    # Zip correction based on addresses, original zip was incomplete
    df.loc[df['docket_number'] == 68131, 'eviction_zip'] = 10001 
    df.loc[df['docket_number'] == 154216, 'eviction_zip'] = 10459 
    df.loc[df['docket_number'] == 384362, 'eviction_zip'] = 11229 
    df.loc[df['docket_number'] == 3704, 'eviction_zip'] = 10037 
    df.loc[df['docket_number'] == 405079, 'eviction_zip'] = 10463
    df.loc[df['docket_number'] == 14066, 'eviction_zip'] = 10035   
    df.loc[df['docket_number'] == 10526, 'eviction_zip'] = 11423       
    df.loc[df['docket_number'] == 75494, 'eviction_zip'] = 10474
    df.loc[df['docket_number'] == 11816, 'eviction_zip'] = 10017   
    df.loc[df['docket_number'] == 388467, 'eviction_zip'] = 10039       
    df.loc[df['docket_number'] == 13893, 'eviction_zip'] = 11377
    df.loc[df['docket_number'] == 14695, 'eviction_zip'] = 11377
    df.loc[df['docket_number'] == 64784, 'eviction_zip'] = 11234
    df.loc[df['docket_number'] == 20089, 'eviction_zip'] = 11226    
    df.loc[df['docket_number'] == 87289, 'eviction_zip'] = 11222
    df.loc[df['docket_number'] == 150547, 'eviction_zip'] = 10306
    df.loc[df['docket_number'] == 11763, 'eviction_zip'] = 11385
    df.loc[df['docket_number'] == 16144, 'eviction_zip'] = 11385
    df.loc[df['docket_number'] == 11762, 'eviction_zip'] = 11385
    df.loc[df['docket_number'] == 11761, 'eviction_zip'] = 11385
    df.loc[df['docket_number'] == 8453, 'eviction_zip'] = 11434
    df.loc[df['docket_number'] == 7808, 'eviction_zip'] = 11691
    df.loc[df['docket_number'] == 115774, 'eviction_zip'] = 11694
    df.loc[df['docket_number'] == 388557, 'eviction_zip'] = 11221
    
    # These properties had zip codes on long island. corrected based on addresses
    df.loc[df['docket_number'] == 9038, 'eviction_zip'] = 10472
    df.loc[df['docket_number'] == 99183, 'eviction_zip'] = 10301
    df.loc[df['docket_number'] == 11884, 'eviction_zip'] = 11204
    df.loc[df['docket_number'] == 22516, 'eviction_zip'] = 11422
    df.loc[df['docket_number'] == 22517, 'eviction_zip'] = 11422
    
    
    
    
    df.to_csv('evictions_nyc.csv', index=False)
    
    
    