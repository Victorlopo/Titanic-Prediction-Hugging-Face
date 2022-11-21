import os
import modal
#import great_expectations as ge
import hopsworks
import pandas as pd
import numpy as np

vitikey = "4CY1rwa8iz8Yu6gG.TwayrYmsX4GQfhSp3LNKYTLvyFMfqAvnzNUQp5ae9K5HhfYxb5mcnLAutm1K18zV"
markinkey = 'oJo7VPKFodTZfXGO.L416PPtrYEVAPX6nLRN0JFzyoPTpclqJu2kcecxftkXlqdnbZbtoDiwREBI6tlFt'
project = hopsworks.login(api_key_value=vitikey)
fs = project.get_feature_store()

titanic_df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
titanic_df = titanic_df.drop(["Name", "Ticket", "Cabin", "Embarked","Fare"],axis=1)
titanic_df.isnull().any()
titanic_df = titanic_df.dropna()
titanic_df['Family'] = titanic_df['SibSp'] + titanic_df['Parch']
titanic_df = titanic_df.drop(['SibSp', 'Parch', 'PassengerId'], axis=1)
titanic_df.loc[titanic_df['Age'].between(0,18,'left'), 'GroupedAge'] = int(0)
titanic_df.loc[titanic_df['Age'].between(18,50,'both'), 'GroupedAge'] = int(1)
titanic_df.loc[titanic_df['Age'].between(50,200,'right'), 'GroupedAge'] = int(2)
titanic_df['Sex'] = titanic_df['Sex'].replace(['female','male'],[0,1])
titanic_df['GroupedAge'] = titanic_df['GroupedAge'].astype('int64')
titanic_df = titanic_df.drop(['Age'], axis=1)


#titanic_df['GroupedAge'] = titanic_df['GroupedAge'].replace(['Child','Adult','Old'],[0,1,2])
#titanic_df['GroupedAge'] = titanic_df['GroupedAge'].replace(['Child','Adult','Old'],[0,1,2])

#print(type(titanic_df.columns))
#titanic_fg=fs.get_feature_group('titanic_modal', version=2)

titanic_fg = fs.get_or_create_feature_group(
    name="titanic_modal",
    version=1,
    primary_key=['GroupedAge', 'Sex', 'Family', 'Pclass'],
    #features=['GroupedAge', 'Sex', 'Family', 'Pclass'],
    #primary_key=["GroupedAge","Sex","Family","PClass"], 
    description="titanic dataset")

titanic_fg.insert(titanic_df, write_options={"wait_for_job" : False})

#expectation_suite = ge.core.ExpectationSuite(expectation_suite_name="iris_dimensions")    
#value_between(expectation_suite, "sepal_length", 4.5, 8.0)
#value_between(expectation_suite, "sepal_width", 2.1, 4.5)
#value_between(expectation_suite, "petal_length", 1.2, 7)
#value_between(expectation_suite, "petal_width", 0.2, 2.5)
#iris_fg.save_expectation_suite(expectation_suite=expectation_suite, validation_ingestion_policy="STRICT")    
    

