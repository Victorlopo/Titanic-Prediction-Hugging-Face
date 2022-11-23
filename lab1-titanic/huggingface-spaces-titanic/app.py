import gradio as gr
import numpy as np
from PIL import Image
import requests

import hopsworks
import joblib

project = hopsworks.login(api_key_value="4CY1rwa8iz8Yu6gG.TwayrYmsX4GQfhSp3LNKYTLvyFMfqAvnzNUQp5ae9K5HhfYxb5mcnLAutm1K18zV")
fs = project.get_feature_store()


mr = project.get_model_registry()
model = mr.get_model("titanic_modal", version=1)
model_dir = model.download()
model = joblib.load(model_dir + "/titanic_model.pkl")


def passenger(pclass, sex, family, groupedage):
    input_list = []
    input_list.append(pclass)
    input_list.append(sex)
    input_list.append(family)
    input_list.append(groupedage)
    # 'res' is a list of predictions returned as the label.
    res = model.predict(np.asarray(input_list).reshape(1, -1)) 
    # We add '[0]' to the result of the transformed 'res', because 'res' is a list, and we only want 
    # the first element.
    if res[0] == 1:
        passenger_url =  "https://cdn.pixabay.com/photo/2018/08/02/18/58/survival-3580200_960_720.png"
    else:
        passenger_url = "https://pngimg.com/uploads/death/death_PNG55.png"
    
    img = Image.open(requests.get(passenger_url, stream=True).raw)
    return img
#return res[0]         


demo_titanic = gr.Interface(
    fn=passenger,
    title="Titanic Predictive Analytics",
    description="Experiment to predict if a passenger survived or died in the titanic",
    allow_flagging="never",
    inputs=[
        gr.inputs.Number(default=1.0, label="Pclass (Min:1, Max=3"),
        gr.inputs.Number(default=1.0, label="Sex (Female:0 and Male:1)"),
        gr.inputs.Number(default=1.0, label="Family (Number of family members in the boat[0,7])"),
        gr.inputs.Number(default=1.0, label="Age (Child:0, Adult:1 and Old:2)")
        ], 
    outputs=gr.Image(type="pil"))

#outputs=gr.Label(num_top_classes=2)
demo_titanic.launch()

