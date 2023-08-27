#!/bin/bash

mkdir -p pretrained_models
mkdir -p pretrained_models/2stems
curl -o pretrained_models/2stems.tar.gz -L https://github.com/deezer/spleeter/releases/download/v1.4.0/2stems.tar.gz
tar -xvzf pretrained_models/2stems.tar.gz -C pretrained_models/2stems
