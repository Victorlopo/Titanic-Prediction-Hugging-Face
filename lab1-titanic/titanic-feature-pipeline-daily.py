import os
import modal
from random import randint

LOCAL=False

if LOCAL == False:
   stub = modal.Stub()
   image = modal.Image.debian_slim().pip_install(["hopsworks==3.0.4"]) 

   @stub.function(image=image, schedule=modal.Period(days=1), secret=modal.Secret.from_name("ScalableSecret"))
   def f():
       g()

# Pclass min (1) max(3)
# Sex min (1) max(2)
# Family min(0) max(7)
# GroupedAge min(0) max(2)
# passengerid min(3) max(888)
def generate_passenger(name, pclass_max, pclass_min, sex_max, sex_min, 
                    family_max, family_min, groupedage_max, groupedage_min):
    """
    Returns a single passenger as a single row in a DataFrame
    """
    import pandas as pd
    import random

    df = pd.DataFrame({ "pclass": [randint(pclass_min, pclass_max)],
                       "sex": [randint(sex_min, sex_max)],
                       "family": [randint(family_min, family_max)],
                       "groupedage": [randint(groupedage_min, groupedage_max)]
                      })
    df['survived'] = name
    return df


def get_random_passenger():
    """
    Returns a DataFrame containing one random passenger
    """
    import pandas as pd
    import random

    survived_df = generate_passenger(1, 1, 1, 0, 0, 4, 4, 1, 1)
    died_df = generate_passenger(0, 3, 3, 1, 1, 7, 0, 2,2)

    # randomly pick one of these 2 and write it to the featurestore
    pick_random = random.uniform(0,2)
    #pick_random = 1.5
    if pick_random >= 1:
        titanic_df = survived_df
        print("Survived passenger added")
    else:
        titanic_df = died_df
        print("Dead passenger added")

    return titanic_df


def g():
    import hopsworks
    import pandas as pd

    project = hopsworks.login()
    fs = project.get_feature_store()

    titanic_df = get_random_passenger()

    titanic_fg = fs.get_feature_group(name="titanic_modal",version=1)
    titanic_fg.insert(titanic_df, write_options={"wait_for_job" : False})

if __name__ == "__main__":
    if LOCAL == True :
        g()
    else:
        with stub.run():
            f()
