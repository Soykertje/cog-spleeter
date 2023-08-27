# Spleeter Cog model

[![Replicate](https://replicate.com/soykertje/spleeter/badge)](https://replicate.com/soykertje/spleeter)

This is an implementation of [Spleeter](https://github.com/deezer/spleeter) as a Cog model. [Cog packages machine learning models as standard containers.](https://github.com/replicate/cog)

First, run `get_weights.sh` from the project root to download pre-trained weights:

    ./download_model.sh

You can then build a container and run predictions like so:

    cog predict -i audio="<path/to/your/audio/file>"

To publish the model to Replicate, run:

    cog login
    cog push r8.im/<your-username>/<your-model-name>

