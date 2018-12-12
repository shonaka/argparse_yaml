# argparse_yaml
This is a repo implementing an idea of taking default configurations from YAML file and replacing part of the configurations if the specific argument is parsed through command line.

## Usage
### Starting from the beginning
```
conda env create -f requirements.yml
source activate argparse_yaml
make -f MakeFile
```

### If you are already in the conda environment
```
make -f MakeFile
```

### If you want to perform the experiment
```
make -f MakeFile resnet
```

## Acknowledgement
Thanks to [Akitomo](https://twitter.com/akitomo_cs) and [Daichi](https://twitter.com/daich1888) for valuable feedback.