from flask import Flask, render_template, request
from pytrends.request import TrendReq
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from google_images_search import GoogleImagesSearch

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profit_maximize', methods = ['GET', 'POST'])
def profir_maximize():
    training_set = pd.read_excel("Data_Train.xlsx")
    test_set = pd.read_excel("Data_Test.xlsx")


    #Training Set
    print("\nEDA on Training Set\n")
    print("#"*30)
    print("\nFeatures/Columns : \n", training_set.columns)
    print("\n\nNumber of Features/Columns : ", len(training_set.columns))
    print("\nNumber of Rows : ",len(training_set))
    print("\n\nData Types :\n", training_set.dtypes)
    print("\nContains NaN/Empty cells : ", training_set.isnull().values.any())
    print("\nTotal empty cells by column :\n", training_set.isnull().sum(), "\n\n")

    # Test Set
    print("#"*30)
    print("\nEDA on Test Set\n")
    print("#"*30)
    print("\nFeatures/Columns : \n",test_set.columns)
    print("\n\nNumber of Features/Columns : ",len(test_set.columns))
    print("\nNumber of Rows : ",len(test_set))
    print("\n\nData Types :\n", test_set.dtypes)
    print("\nContains NaN/Empty cells : ", test_set.isnull().values.any())
    print("\nTotal empty cells by column :\n", test_set.isnull().sum())

    data_temp = [training_set[['TITLE', 'RESTAURANT_ID', 'CUISINES', 'TIME', 'CITY', 'LOCALITY','RATING', 'VOTES']], test_set]

    data_temp = pd.concat(data_temp)

    titles = list(data_temp['TITLE'])

    maxim = 1
    for i in titles :
        if len(i.split(',')) > maxim:
            maxim = len(i.split(','))
            
    print("\n\nMaximum Titles in a Cell : ", maxim)    

    all_titles = []

    for i in titles :
        if len(i.split(',')) == 1:
            all_titles.append(i.split(',')[0].strip().upper())
        else :
            for it in range(len(i.split(','))):
                all_titles.append(i.split(',')[it].strip().upper())

    print("\n\nNumber of Unique Titles : ", len(pd.Series(all_titles).unique()))
    print("\n\nUnique Titles:\n", pd.Series(all_titles).unique())

    all_titles = list(pd.Series(all_titles).unique())

    cuisines = list(data_temp['CUISINES'])

    maxim = 1
    for i in cuisines :
        if len(i.split(',')) > maxim:
            maxim = len(i.split(','))
            
    print("\n\nMaximum cuisines in a Cell : ", maxim)    

    all_cuisines = []

    for i in cuisines :
        if len(i.split(',')) == 1:
            all_cuisines.append(i.split(',')[0].strip().upper())
        else :
            for it in range(len(i.split(','))):
                all_cuisines.append(i.split(',')[it].strip().upper())

    print("\n\nNumber of Unique Cuisines : ", len(pd.Series(all_cuisines).unique()))
    print("\n\nUnique Cuisines:\n", pd.Series(all_cuisines).unique())

    all_cuisines = list(pd.Series(all_cuisines).unique())
    all_cities = list(data_temp['CITY'])

    for i in range(len(all_cities)):
        if type(all_cities[i]) == float:
            all_cities[i] = 'NOT AVAILABLE'
        all_cities[i] = all_cities[i].strip().upper()
            
    print("\n\nNumber of Unique cities (Including NOT AVAILABLE): ", len(pd.Series(all_cities).unique()))
    print("\n\nUnique Cities:\n", pd.Series(all_cities).unique())
    
    all_cities = list(pd.Series(all_cities).unique())
    all_localities = list(data_temp['LOCALITY'])

    for i in range(len(all_localities)):
        if type(all_localities[i]) == float:
            all_localities[i] = 'NOT AVAILABLE'
        all_localities[i] = all_localities[i].strip().upper()
            
    print("\n\nNumber of Unique Localities (Including NOT AVAILABLE) : ", len(pd.Series(all_localities).unique()))
    print("\n\nUnique Localities:\n", pd.Series(all_localities).unique())

    all_localities = list(pd.Series(all_localities).unique())

    titles = list(training_set['TITLE'])

    T1 = []
    T2 = []

    for i in titles:
        T1.append(i.split(',')[0].strip().upper())
        try :
            T2.append(i.split(',')[1].strip().upper())
        except :
            T2.append('NONE')

    all_titles.append('NONE')
    cuisines = list(training_set['CUISINES'])
    
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    C8 = []


    for i in cuisines:
            try :
                C1.append(i.split(',')[0].strip().upper())
            except :
                C1.append('NONE')
            try :
                C2.append(i.split(',')[1].strip().upper())
            except :
                C2.append('NONE')
            try :
                C3.append(i.split(',')[2].strip().upper())
            except :
                C3.append('NONE')
            try :
                C4.append(i.split(',')[3].strip().upper())
            except :
                C4.append('NONE')
            try :
                C5.append(i.split(',')[4].strip().upper())
            except :
                C5.append('NONE')
            try :
                C6.append(i.split(',')[5].strip().upper())
            except :
                C6.append('NONE')
            try :
                C7.append(i.split(',')[6].strip().upper())
            except :
                C7.append('NONE')
            try :
                C8.append(i.split(',')[7].strip().upper())
            except :
                C8.append('NONE')

    all_cuisines.append('NONE')

    cities = list(training_set['CITY'])

    for i in range(len(cities)):
        if type(cities[i]) == float:
            cities[i] = 'NOT AVAILABLE'
        cities[i] = cities[i].strip().upper()
            
    localities = list(training_set['LOCALITY'])

    for i in range(len(localities)):
        if type(localities[i]) == float:
            localities[i] = 'NOT AVAILABLE'
        localities[i] = localities[i].strip().upper()   
        
    rates = list(training_set['RATING'])

    for i in range(len(rates)) :
        try:
            rates[i] = float(rates[i])
        except :
            rates[i] = np.nan

    votes = list(training_set['VOTES'])

    for i in range(len(votes)) :
        try:
            votes[i] = int(votes[i].split(" ")[0].strip())
        except :
            pass               

    new_data_train = {}

    new_data_train['TITLE1'] = T1
    new_data_train['TITLE2'] = T2
    new_data_train['RESTAURANT_ID'] = training_set["RESTAURANT_ID"]
    new_data_train['CUISINE1'] = C1
    new_data_train['CUISINE2'] = C2
    new_data_train['CUISINE3'] = C3
    new_data_train['CUISINE4'] = C4
    new_data_train['CUISINE5'] = C5
    new_data_train['CUISINE6'] = C6
    new_data_train['CUISINE7'] = C7
    new_data_train['CUISINE8'] = C8
    new_data_train['CITY'] = cities
    new_data_train['LOCALITY'] = localities
    new_data_train['RATING'] = rates
    new_data_train['VOTES'] = votes
    new_data_train['COST'] = training_set["COST"]

    new_data_train = pd.DataFrame(new_data_train)
    titles = list(test_set['TITLE'])

    T1 = []
    T2 = []

    for i in titles:
        T1.append(i.split(',')[0].strip().upper())
        try :
            T2.append(i.split(',')[1].strip().upper())
        except :
            T2.append('NONE')

    cuisines = list(test_set['CUISINES'])
    
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    C6 = []
    C7 = []
    C8 = []

    for i in cuisines:
            try :
                C1.append(i.split(',')[0].strip().upper())
            except :
                C1.append('NONE')
            try :
                C2.append(i.split(',')[1].strip().upper())
            except :
                C2.append('NONE')
            try :
                C3.append(i.split(',')[2].strip().upper())
            except :
                C3.append('NONE')
            try :
                C4.append(i.split(',')[3].strip().upper())
            except :
                C4.append('NONE')
            try :
                C5.append(i.split(',')[4].strip().upper())
            except :
                C5.append('NONE')
            try :
                C6.append(i.split(',')[5].strip().upper())
            except :
                C6.append('NONE')
            try :
                C7.append(i.split(',')[6].strip().upper())
            except :
                C7.append('NONE')
            try :
                C8.append(i.split(',')[7].strip().upper())
            except :
                C8.append('NONE')


    cities = list(test_set['CITY'])

    for i in range(len(cities)):
        if type(cities[i]) == float:
            cities[i] = 'NOT AVAILABLE'
        cities[i] = cities[i].strip().upper()
            

    localities = list(test_set['LOCALITY'])

    for i in range(len(localities)):
        if type(localities[i]) == float:
            localities[i] = 'NOT AVAILABLE'
        localities[i] = localities[i].strip().upper()   
        
    rates = list(test_set['RATING'])

    for i in range(len(rates)) :
        try:
            rates[i] = float(rates[i])
        except :
            rates[i] = np.nan

    votes = list(test_set['VOTES'])

    for i in range(len(votes)) :
        try:
            votes[i] = int(votes[i].split(" ")[0].strip())
        except :
            pass       
        
    new_data_test = {}

    new_data_test['TITLE1'] = T1
    new_data_test['TITLE2'] = T2
    new_data_test['RESTAURANT_ID'] = test_set["RESTAURANT_ID"]
    new_data_test['CUISINE1'] = C1
    new_data_test['CUISINE2'] = C2
    new_data_test['CUISINE3'] = C3
    new_data_test['CUISINE4'] = C4
    new_data_test['CUISINE5'] = C5
    new_data_test['CUISINE6'] = C6
    new_data_test['CUISINE7'] = C7
    new_data_test['CUISINE8'] = C8
    new_data_test['CITY'] = cities
    new_data_test['LOCALITY'] = localities
    new_data_test['RATING'] = rates
    new_data_test['VOTES'] = votes

    new_data_test = pd.DataFrame(new_data_test)

    print("\n\nnew_data_train: \n", new_data_train.head())
    print("\n\nnew_data_test: \n", new_data_test.head())
    print("\n\nMissing Values in Training Set\n","#"*60)
    print("\nContains NaN/Empty cells : ", new_data_train.isnull().values.any())
    print("\nTotal empty cells by column\n","_"*60,"\n", new_data_train.isnull().sum())

    new_data_train.fillna(0, inplace = True)

    print("\n\nAfter Filling 0:\n","_"*60,"\n")
    print("\nContains NaN/Empty cells : ", new_data_train.isnull().values.any())
    print("\n\nMissing Values in Test Set \n","#"*60)
    print("\nContains NaN/Empty cells : ", new_data_test.isnull().values.any())
    print("\nTotal empty cells by column\n","_"*60,"\n", new_data_test.isnull().sum())


    new_data_test.fillna(0, inplace = True)

    print("\n\nAfter Filling 0 :\n","_"*60,"\n")
    print("\nContains NaN/Empty cells : ", new_data_test.isnull().values.any())
    print("\n\n")

    le_titles = LabelEncoder()
    le_cuisines = LabelEncoder()

    le_city = LabelEncoder()

    le_locality = LabelEncoder()


    le_titles.fit(all_titles)
    le_cuisines.fit(all_cuisines)

    le_city.fit(all_cities)
    le_locality.fit(all_localities)


    # Training Set  
    new_data_train['TITLE1'] = le_titles.transform(new_data_train['TITLE1'])
    new_data_train['TITLE2'] = le_titles.transform(new_data_train['TITLE2'])


    new_data_train['CUISINE1'] = le_cuisines.transform(new_data_train['CUISINE1'])
    new_data_train['CUISINE2'] = le_cuisines.transform(new_data_train['CUISINE2'])
    new_data_train['CUISINE3'] = le_cuisines.transform(new_data_train['CUISINE3'])
    new_data_train['CUISINE4'] = le_cuisines.transform(new_data_train['CUISINE4'])
    new_data_train['CUISINE5'] = le_cuisines.transform(new_data_train['CUISINE5'])
    new_data_train['CUISINE6'] = le_cuisines.transform(new_data_train['CUISINE6'])
    new_data_train['CUISINE7'] = le_cuisines.transform(new_data_train['CUISINE7'])
    new_data_train['CUISINE8'] = le_cuisines.transform(new_data_train['CUISINE8'])


    new_data_train['CITY'] = le_city.transform(new_data_train['CITY'])
    new_data_train['LOCALITY'] = le_locality.transform(new_data_train['LOCALITY'])

    # Test Set
    new_data_test['TITLE1'] = le_titles.transform(new_data_test['TITLE1'])
    new_data_test['TITLE2'] = le_titles.transform(new_data_test['TITLE2'])


    new_data_test['CUISINE1'] = le_cuisines.transform(new_data_test['CUISINE1'])
    new_data_test['CUISINE2'] = le_cuisines.transform(new_data_test['CUISINE2'])
    new_data_test['CUISINE3'] = le_cuisines.transform(new_data_test['CUISINE3'])
    new_data_test['CUISINE4'] = le_cuisines.transform(new_data_test['CUISINE4'])
    new_data_test['CUISINE5'] = le_cuisines.transform(new_data_test['CUISINE5'])
    new_data_test['CUISINE6'] = le_cuisines.transform(new_data_test['CUISINE6'])
    new_data_test['CUISINE7'] = le_cuisines.transform(new_data_test['CUISINE7'])
    new_data_test['CUISINE8'] = le_cuisines.transform(new_data_test['CUISINE8'])


    new_data_test['CITY'] = le_city.transform(new_data_test['CITY'])
    new_data_test['LOCALITY'] = le_locality.transform(new_data_test['LOCALITY'])

    Y_train = new_data_train.iloc[:, -1].values  
    X_train = new_data_train.iloc[:,0 : -1].values
    X_test = new_data_test.iloc[:,:].values

    sc = StandardScaler()

    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    Y_train = Y_train.reshape((len(Y_train), 1)) 
    Y_train = sc.fit_transform(Y_train)
    Y_train = Y_train.ravel()

    gbr=GradientBoostingRegressor( loss = 'huber',learning_rate=0.001,n_estimators=350, max_depth=6, subsample=1, verbose=False, random_state=126)
    gbr.fit(X_train,Y_train)
    y_pred_gbr = sc.inverse_transform(gbr.predict(X_test))

    y_pred_gbr = pd.DataFrame(y_pred_gbr, columns = ['COST']) # Converting to dataframe
    print(y_pred_gbr)

@app.route('/trends', methods = ['GET', 'POST'])
def trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    print(pytrends)
    kw_list = ['Ice Cream']
    pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='', gprop='')

    def trendy(kw_list) :
        pytrends.build_payload(kw_list, cat=0, timeframe='all', geo='', gprop='')
        interest_over_time_df = pytrends.related_topics()
        print(interest_over_time_df)

    # if you don't enter api key and cx, the package will try to search
    # them from environment variables GCS_DEVELOPER_KEY and GCS_CX
    gis = GoogleImagesSearch('your_dev_api_key', 'your_project_cx')

    # example: GoogleImagesSearch('ABcDeFGhiJKLmnopqweRty5asdfghGfdSaS4abC', '012345678987654321012:abcde_fghij')

    #define search params:
    _search_params = {
        'q': '...',
        'num': 1-50,
        'safe': 'high|medium|off',
        'fileType': 'jpg|gif|png',
        'imgType': 'clipart|face|lineart|news|photo',
        'imgSize': 'huge|icon|large|medium|small|xlarge|xxlarge',
        'searchType': 'image',
        'imgDominantColor': 'black|blue|brown|gray|green|pink|purple|teal|white|yellow'
    }

    # this will only search for images:
    gis.search(search_params=_search_params)

    # this will search and download:
    gis.search(_search_params=_search_params, path_to_dir='.')

    # this will search, download and resize:
    gis.search(_search_params=_search_params, path_to_dir='/path/', width=500, height=500)

    # search first, then download and resize afterwards
    gis.search(_search_params=_search_params)
    for image in gis.results():
        image.download('/path/')
        image.resize(500, 500)    

if __name__=="__main__":
    app.run(debug = True)