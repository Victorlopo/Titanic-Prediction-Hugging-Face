# ScalableMachineLearningLab1


Order of the execution files:

1) python titanic-feature-pipeline.py
2) python titanic-training-pipeline.py
3) python titanic-feature-pipeline-daily.py (this command should be executed until getting 2 different passengers to plot the confusion matrix afterwards)
4) python titanic-batch-inference-pipeline.py (this command should be executed until getting 2 different passengers to plot the confusion matrix afterwards)

To set up the hugging face UI the following commands should be executed:

1) Interactive UI for entering feature values and predicting if a passenger would survive the titanic or not

    1.1) Online Link: https://huggingface.co/spaces/Victorlopo21/Titanic1
    
    1.2) Console commands
        - cd huggingface-spaces-titanic
        - python app.py

2) Dashboard UI showing a prediction of survival for the most recent
passenger added to the Feature Store and the outcome (label) if that
passenger survived or not. Include a confusion matrix to show historical
model performance.

    1.1) Online Link: https://huggingface.co/spaces/Victorlopo21/Titanic2
    
    1.2) Console commands
        - cd huggingface-spaces-titanic-monitor
        - python app.py
