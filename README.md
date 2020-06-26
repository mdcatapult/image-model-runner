# Echo Image Model Runner

A simple prototype for packaging image classification models and running within a docker container.

## Running a model from the command line

* Set up a virtual python environment and install requirements
* Execute the `run_classification` module with suitable arguments

```
python run_classification.py --imageDir ../test_data/chief-ai_test_data/ --config=../test_configs/config_histo.yml
```

## Running a model within a docker container

* Build the docker image

```
docker build -t compound-image-classifier .
```


* Run the 

```
docker run -it -v <absolute-path-to>/test_data/:/images -v <absolute-path-to>/test_configs/:/configs compound-image-classifier python run_classification.py --imageDir /images/mdc_comp_test_data/ --config=/configs/config.yml
```

