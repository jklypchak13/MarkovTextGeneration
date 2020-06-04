# Markov Text Generation

This project is a simple implementation of Markov Models being used for Text Generation. An n-gram model was implemented
using words as the n-grams.

The sample training data used was scripts from the NBC TV Show [The Office](https://en.wikipedia.org/wiki/The_Office_(American_TV_series)).
The setup file will fetch the scripts from [Forever Dreaming Transcripts](https://transcripts.foreverdreaming.org/). A huge shout out to them for putting these together and providing a good source of training data for this project.

## Instructions to Run

To manage the dependencies of the project, a Pipfile was used. You will need [pipenv](https://pypi.org/project/pipenv/)

Then, to install the dependencies run

```shell
pipenv install
```

### Setup File

After cloning the repo, simply run the setup file from the parent directory

```shell
python setup.py
```

### Generating Scripts

As of right now, the main function is rather simple, providing only some basics. It will train a model with the office scripts, and generate its own.
To do this,  execute the following command

```shell
python src/main.py
```

### Future Improvements

As of right now error checking is rather simple, and will be improved. In addition, further improvements in the interface and accessibility of this tool will be improved.
