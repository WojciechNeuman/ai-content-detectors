## Description

This repository contains the codebase for my thesis made at the AGH University of Krakow, titled **"Comparative Evaluation of Methods for Classifying Human-Written and AI-Generated Text."**
The research was carried out under the supervision of Dr. Eng. Krzysztof Kluza.


## Technologies Used

[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)  
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)  
[![Matplotlib](https://img.shields.io/badge/-Matplotlib-000000?style=flat&logo=python)](https://matplotlib.org/)  
[![Seaborn](https://img.shields.io/badge/seaborn-%231a1a1a.svg?style=for-the-badge&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)  
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)  
[![PyTorch](https://img.shields.io/badge/pytorch-%23EE4C2C.svg?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)  
[![TensorFlow](https://img.shields.io/badge/tensorflow-%23FF6F00.svg?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)  
[![Keras](https://img.shields.io/badge/keras-%23D00000.svg?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io/)  
[![Hugging Face](https://img.shields.io/badge/hugging%20face-%23FFDF00.svg?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)  
[![SHAP](https://img.shields.io/badge/shap-%23E94F37.svg?style=for-the-badge&logo=shap&logoColor=white)](https://shap.readthedocs.io/)  
[![LIME](https://img.shields.io/badge/lime-%2300747A.svg?style=for-the-badge&logo=lime&logoColor=white)](https://github.com/marcotcr/lime)  



## Technical information

Notebooks related to work involving CNN, BiLSTM, and BERT models, along with SHAP and LIME analyses, were executed completely with Google Colaboratory. You can access them in the [Google Colaboratory Folder](https://drive.google.com/drive/folders/1nBkuzoQO53kPTNYtXIdZPctT-E57nmQ_?usp=sharing). To run these notebooks, use the provided link and clone the specific files. 

Note: A highly capable computational engine is required to run them.


In order to download the dataset used in the model training process, run the [`utilities/download_dataset.py`](utilities/download_dataset.py) file or run one of the notebooks inside of 
[models_creation](models_creation) folder.

#### List of steps to run the notebooks

1. Clone repository & move into the directory

```shell
git clone https://github.com/WojciechNeuman/ai-content-detectors.git

cd ai-content-detectors.git
```

2. Set up the virtual environment (Mac & Linux)

```shell
pip install virtualenv

virtualenv env

source env/bin/activate
```

3. Install the requirements
```shell
pip install -r requirements.txt
```