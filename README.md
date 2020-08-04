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


* Run a container dynamically providing mount points for image and config files

```
docker run -it -v <absolute-path-to>/test_data/:/images -v <absolute-path-to>/test_configs/:/configs \
compound-image-classifier python run_classification.py --imageDir /images/mdc_comp_test_data/ --config=/configs/config.yml
```

## TODOs
* Find a suitable base container with Keras & Tensorflow to improve docker build times

## License
Copyright (c) 2019, Medicines Discovery Catapult All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. * Neither the name of the Medicines Discovery Catapult nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL MEDICINES DISCOVERY CATAPULT BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
