# ScalableMachineLearningLab1

After activating the conda environment the following commands should be executed:

-  SET CONDA_DLL_SEARCH_MODIFICATION_ENABLE=1

-  set HOPSWORKS_API_KEY=("your_api_key")

Order of the execution files:

1) python titanic-feature-pipeline.py
2) python titanic-training-pipeline.py
3) python titanic-feature-pipeline-daily.py (this command should be executed until getting 2 different passengers to plot the confusion matrix afterwards)
4) python titanic-batch-inference-pipeline.py (this command should be executed until getting 2 different passengers to plot the confusion matrix afterwards)

To set up the hugging face UI the following commands should be executed:

1) Interactive UI for entering feature values and predicting if a passenger would survive the titanic or not
    
    - cd huggingface-spaces-titanic
    - python app.py

2) Dashboard UI showing a prediction of survival for the most recent
passenger added to the Feature Store and the outcome (label) if that
passenger survived or not. Include a confusion matrix to show historical
model performance.

    - cd huggingface-spaces-titanic-monitor
    - python app.py
