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
