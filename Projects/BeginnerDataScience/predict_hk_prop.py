import numpy as np
import pandas as pd

#Pre-processing
from sklearn.model_selection import train_test_split

# Algorithms
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.tree import DecisionTreeRegressor
#from xgboost import XGBRegressor, XGBClassifier

# Evaluation
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score #regression


def build_rf( model_data ):
    print(f'Building random forest...')
    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split( 
        model_data.drop(columns= ['adj_price_per_sqf']),
        model_data.adj_price_per_sqf,
        test_size = 0.3,
        random_state = 420
    )

    rf = RandomForestRegressor(n_estimators= 100, random_state = 420,)
    rf.fit( X_test, y_test)
    return rf

def get_predict_data( model_df , l_region):
    ser_deploy = model_df.iloc[0]
    deploy_dict = ser_deploy.to_dict()
    for i in deploy_dict:
        deploy_dict[i] = 0

    _age = input('Please enter building age: ')
    _floor_number = input('Please enter floor number: ')
    _saleablearea = input('Please enter Saleable Area: ')

    # region we need to encode
    region_dict = { i : region for i, region in enumerate(l_region)}
    print(f"Here's our region number map:\n-------------")
    for region in region_dict:
        print(f'{region}: {region_dict[region]}')
    print(f'-------------')
    region_num = input(f'Please enter region number: ')
    deploy_dict['building_age'] = int(_age)
    deploy_dict['floor_number'] = int(_floor_number)
    deploy_dict['saleablearea'] = int(_saleablearea)

    for key in deploy_dict:
        if region_dict[ int(region_num) ] in key:
            deploy_dict[ key ] = 1

    s = pd.Series( deploy_dict, index = deploy_dict.keys())
    predict_data = pd.DataFrame(s).T
    return predict_data

def main():
    fname = 'data/model_data.csv'
    data = pd.read_csv( fname , index_col= 0)
    print(f'Data from {fname} loaded...')

    region_dummies = pd.get_dummies( data.region, prefix = 'reg_')
    region_dummies.index = data.index
    l_region = list(sorted(data.region.unique()))

    l_model_col = ['saleablearea', 'building_age', 'floor_number','adj_price_per_sqf']
    df_model = data[ l_model_col + ['flat_type']].join( region_dummies )
    
    model_filter = (df_model.flat_type == 'n') & (df_model.saleablearea <= 1076)
    df_model = df_model[model_filter].drop(columns = 'flat_type')

    rf_model = build_rf( df_model)
    
    while input(f"Would you like to predict a Property's price?[Y/N] ").upper() == 'Y':
        predict_data = get_predict_data( df_model.drop(columns= ['adj_price_per_sqf']), l_region )
        prediction = float(rf_model.predict( predict_data ))
        sqft = predict_data.saleablearea.iloc[0]
        total_amt = prediction * sqft

        print( f'Results: {"{:,.0f}".format(prediction)} per square foot.\n Or total {"{:,.0f}".format(total_amt)} for {"{:,.0f}".format(sqft)} square-feet.')

main()
