# DNN_TumorClassification

Components of Python Notebook: 'fMRI_Tumor_DNN.ipynb'

1) Problem Statement

2) Data Analysis Preparation

A) Evaluate Computational Efficiency
B) Load Packages
C) Load Data
D) Preprocess and Clean Data
3) Exploratory Data Analysis (EDA)

A) Insights from preliminary EDA
B) Create TensorFlow Dataset
C) Comparison of preliminary and final EDA
D) Visualization of fMRI data
4) Convolutional Neural Networks

A) Model 1: Standard (Vanilla)
B) Model 2: Standard + Google Brain (Strawberry)
C) Model 3: Auto-encoder + Google Brain (Chocolate)
5) Transfer Learning

A) Best fitting model
B) VGG-16
C) GoogLeNet (Inception-V3)
6) Ensemble Model

7) Best Fitting Model - Saliency Map

8) Future Directions (+ Extras)

9) Summary

10) References

    
Problem Statement
Goal: Train a Convolutional Neural Network (CNN) to classify the presence of tumors in fMRI brain images.
Malignant brain tumors are relatively rare, but they account for a disproportionate number of cancer-related mortalities due to their low survival rate – only 1/3 of individuals survive 5+ years post-diagnosis (Miller et al., 2021).Therefore, identifying brain abnormalities as soon as possible is paramount for increasing a patient’s potential for survival. However, brain tumors are incredibly complex and difficult to diagnose. Beyond requiring functional magnetic resonance imaging (fMRI) to visualize and diagnose brain tumors, a professional neurosurgeon is usually required to interpret the output of MRI analysis. This challenge is in part due to large amounts of variation among the potential size and locations of brain tumors. Moreover, the degree of educational specialization required to become a neurosurgeon poses a significant obstacle for diagnosing brain tumors in developing countries. In sum, a new approach for diagnosing malignant brain tumors is necessary which circumvents the need for advanced medical training while prioritzing speed and accuracy.

Data:

To train and evaluate my convolutional neural network I will leverage 2 distinct datasets:

A dataset from  containing 3064 T1-weighted contrast-inhanced images with three kinds of brain tumor: meningioma (708 images), glioma (1426 images), and pituitary tumor (930 images).
Note: Due to the large file size, the authors split the dataset into 4 subsets, and archived them into 4 .zip files with each containing 766 brain 'slices'.

This dataset is freely available here: https://figshare.com/articles/dataset/brain_tumor_dataset/1512427

A dataset from  including 3000 total images of 1500 healthy brains, and 1500 brains with tumors.
Note: This dataset ('Br35H') is associated with a Kaggle competition for identifying tumors in neuroimaging data and is split into two different folders indicating whether a tumor was present ('yes' & 'no').

This dataset is freely available here: https://www.kaggle.com/datasets/ahmedhamada0/brain-tumor-detection?select=no

The data is also available in this current Github Repo

Click on my Python notebook to learn more!
