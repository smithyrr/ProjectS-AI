# Project Structure

Created time: May 15, 2023 9:28 AM
Last edited time: May 16, 2023 4:04 PM
Owner: R.Smith

This project has the following directory structure:

```
ProjectSAi
│
├───Preprocesseddata
│   ├── input_encodings.pt
│   └── label_encodings.pt
│
├───Pyscripts for future
│   ├── database.py
│   └── emotion_detection.py
│
├───results
│   └── # results files go here
│
├───TrainedModels
│   └── # saved trained model files go here
│
├───TrainScripts
│   └── # future py files go here
│
├───validation
│   └── # validation files go here
│
└───wandb
    └── # wandb files go here

[train.py](<http://train.py/>) is the main training script.
```