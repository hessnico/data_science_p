from datetime import datetime

def classify_fit_predict(classifier, X_train, Y_train, X_test):
    '''classifier/regression algorithm, fit him to x axis train set and y axis train set and later, predict with x axis test set'''
    
    start_time = datetime.now()
    
    cl = str(classifier)
    tmp = cl.find("(")
    print("Calculating predictions for", cl[:tmp])
    
    clf = classifier
    model = clf.fit(X_train, Y_train)
    y_pred = model.predict(X_test)
    
    print(f"{cl[:-2]} is ready... \nCalculation finished in {datetime.now()-start_time}")
    
    return model, y_pred