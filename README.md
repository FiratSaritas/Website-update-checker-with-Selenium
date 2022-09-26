# Website-update-checker with Selenium

## About project
This repository covers a simple function, but one that makes life easier for some: It uses Selenium to visually check if the webpage has changed every 20 seconds (the [`time`](https://github.com/FiratSaritas/Website-update-checker-with-Selenium/blob/d2ebf43fbf380bd7d65831ab1225c9e5fb9b8255/website_update_checker.py#L33) can be adjusted in the code).
If there is a change in the webpage, you can send a message on telegram. this code can be used for many different websites, because it checks visually and no source code in the background.

## Folder Structure Conventions

```
    ├── Checklists             # Checklists for a clean code and project (files type: pdf)
    ├── augmentation           # Use of different data augmentations (files type: ipynb)
    ├── data                   # Data of the project (files type: csv)
    │   ├── archive
    ├── eda                    # Exploratory data analysis (files type: ipynb)
    ├── model                  # Different trained models (files type: ipynb)
    │   ├── final              # Calls final model and makes a prediction (files type: py)
    ├── utils                  # outsourced functions (files type: py)
    │   ├── archive
    │   ├── dataset            # dataset functions (files type: py)
    │   │   ├── tests
    │   ├── plots              # plot functions (files type: py)
    │   │   ├── tests
    │   ├── training           # training functions (files type: py)
    │   │   ├── tests
    └── README.md             
    └── git_workflow.md
    └── requirements.txt
```

## Getting Started

### Installation
Clone project locally
 ```sh
    git@github.com:FiratSaritas/manhole-cover-classification.git
 ```

### Downloads

#### Model:
Download model from Google Drive and add it to the folder ./model here:
**link** (not ready yet)

#### Images (optional):
Download images as Folder (images_transformed) from Google Drive and add it to the folder ./data here:
([https://drive.google.com/drive/folders/1y5T1-WUZB1Vsp87aBiU6hDxagiY2mGgi?usp=sharing](https://drive.google.com/drive/folders/1y5T1-WUZB1Vsp87aBiU6hDxagiY2mGgi?usp=sharing))



### Prerequisites 
Install required packages
 ```sh
    pip install -r requirements.txt
 ```

### Run project

### Run test

There are tests for the outsourced python files. These python files are located in the "utils" folder. There are subfolders of the corresponding classes (e.g. dataset). There is a folder with the name "tests" and there are the unittests. 
You can run a test with the following code:
```sh
    python -m unittest [name of the testfile]
 ```

## Project status
This project is still in progress.

## Contact

firat.saritas@students.fhnw.ch<br />
simon.staehli@students.fhnw.ch<br />
kajenthini.kobivasan@students.fhnw.ch
