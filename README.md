# Quickstart
Use this template to start your own PyCob app
https://github.com/pycob/quickstart/blob/main/src/main.py

# Running
This repo contains a `Makefile` so you can just run the following to set up a virtual environment, install dependencies, and run locally:

```bash
make
```

# Deploy to PyCob
## Manual Deployment
You can use the `Makefile` by running:
```bash
make deploy
```

Or if you prefer, you can run
```bash
python -m pycob.deploy
```

## CD
On GitHub, you can use a GitHub workflow to automatically deploy your site to PyCob Hosting
https://github.com/pycob/quickstart/actions/workflows/pycob-deploy.yaml

[![.github/workflows/pycob-deploy.yaml](https://github.com/pycob/quickstart/actions/workflows/pycob-deploy.yaml/badge.svg)](https://github.com/pycob/quickstart/actions/workflows/pycob-deploy.yaml)

# Deploy to other Cloud Services
Running on PyCob Infrastructure is optional. You can run PyCob apps anywhere.

