# Streakers

## A Flashcard Program for the Terminal

This is the code for a very simple flashcard program that can be run from the terminal.

## How to run

To use the default flashcards file (`flashcards.csv`), type:

```shell
 $ python flashcards.py
 ...
```

To use your own flashcards file called `myownflashcardsfile.csv`, type:

```shell
 $ python flashcards.py myownflashcardsfile.csv
 ...
```

Here assume that `myownflashcardsfile.csv` is in the same directory as `flashcards.py`.

## How to play

Simply guess what's on the other side of the displayed flaschcard. After you see the other side, input a rating of how well you knew the answer. The program will show flashcards that you are less confident in more often, assuming your assesments are truthful.

## Format of `flashcards.csv`

This file must be a 5 column `.csv`, with the columns

+ **knowledge_level**: a float indicating used for learning. The lower the number, the less often that flashcard will appear.
+ **short_question**: Usually a "What is *blank*?" kind of question. Short, requiring a good amount of exposition.
+ **detail_answer**: The good amount of exposition referred to in **short_question**.
+ **detail_question**: This is a question version of **detail_answer**.
+ **short_answer**: This is a single phrase answer to **detail_question**. Usually the same as *blank* in **short_question**.

It isn't necessary, but a header row is assumed.
