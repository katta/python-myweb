# Build

The following command generates the distribution in `CHECKOUT_DIR/dist`

```bash
./gradlew clean build 
```

# Install

* Copy the `CHECKOUT_DIR/dist/<app-version.tar.gz>` to the target machine
* Make sure the virtualenv is setup with the right python version (same as the one this project was built with)
* Run the following commands

```bash
tar -xvf <dist.tar.gz> 
pip install --force-reinstall --ignore-installed --upgrade --no-index --no-deps wheelhouse/*
```
 