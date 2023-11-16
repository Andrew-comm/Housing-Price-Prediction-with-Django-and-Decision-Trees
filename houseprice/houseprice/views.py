from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import numpy as np

def home(request):
    return render(request, 'index.html')

def predict(request):
    return render(request, 'f.html')

def result(request):
    data = pd.read_csv("cleaning_2.csv")
    data['price'] = data['price'].apply(lambda x: int(x))
    prices = data['price']
    features = data[['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'sqft_above', 'sqft_basement', 'Quality', 'city']]
    X_train, X_test, Y_train, Y_test = train_test_split(features, prices, test_size=0.20, random_state=42)

    dtr = DecisionTreeRegressor()
    dtr.fit(X_train, Y_train)

    if request.method == 'POST':
        # Extracting form data
        bedrooms = int(request.POST.get('n1'))
        bathrooms = int(request.POST.get('n2'))
        sqft_living = int(request.POST.get('n3'))
        sqft_lot = int(request.POST.get('n4'))
        floors = int(request.POST.get('n5'))
        waterfront = 1 if request.POST.get('water') == 'oui' else 0
        view1 = {'bad': 0, 'average': 1, 'good': 2, 'verygood': 3, 'perfect': 4}
        view = view1.get(request.POST.get('view'))
        condition1 = {'bad': 1, 'average': 2, 'good': 3, 'verygood': 4, 'perfect': 5}
        condition = condition1.get(request.POST.get('condition'))
        sqft_above = int(request.POST.get('sqftA'))
        sqft_basement = int(request.POST.get('sqftB'))
        Quality = int(request.POST.get('age'))
        city = int(request.POST.get('city'))

        # Predicting price
        pred = dtr.predict(np.array([bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, Quality, city]).reshape(1, -1))
        pred = round(pred[0])
        
        # Check if the predicted price is close to any actual prices in the CSV
        close_prices = prices[(prices - pred).abs() < 10000]  # Adjust the threshold as needed
        if not close_prices.empty:
            price = f"The predicted price is $ {pred}"
        else:
            price = f"No close match found. The predicted price is $ {pred}"

        return render(request, 'f.html', {"result2": price})

    return render(request, 'f.html')
