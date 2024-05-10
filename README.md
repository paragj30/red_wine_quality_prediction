# This is end to end wine quality prediction Machine learning project.

## Workflow

1. Update the config/config.yaml file
2. update the schema.yaml file (for model training part)
3. update the params.yaml file (for hyperparameter part)
4. update the entity 
5. update the src/mlproject/config/configuration.py file
6. update the components (create all the components)
7. update the pipeline (create the training and prediction pipeline)
8. update the main.py file (This is endpoint/root file. Once it triggered, it executes the training pipeline)
9. update the app.py file (contains the frontend(API) part. It will trigger the training and prediction pipeline)

## How to run?

### STEPS:

```bash
conda create -p venv python=3.10
```

```bash
conda activate venv
```

```bash
pip install -r "requirements.txt"
```

