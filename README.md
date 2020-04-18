# Machine Learning Based Autonomous Robot with NVIDIA Jetson Nano

<img src="doc/images/JetBot.jpg" width="50%"/>

## About
This repository contains the code and guides that have been produced for the bachelor thesis "Machine Learning Based Autonomous Robot with NVIDIA Jetson Nano".

The goal was to build a JetBot according to the instructions provided by [NVIDIA on GitHub](https://github.com/NVIDIA-AI-IOT/jetbot).
The JetBot platform had to be evaluated and a demo case had to be implemented. 
In addition how to guides that allow the easy repetition of the conducted steps had to be written.

This guide provides instructions on how to setup the demo case and the model trainings. <br>
For instructions on how to use the packages please have a look at the corresponding guides.

If you just want to try out the demonstration case you can skip chapters 5-8 and go directly to chapter 9.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Order JetBot Parts](#order-jetBot-parts)
3. [Build JetBot](#build-jetBot)
4. [Setup Software](#setup-software) <br>
4.1 [Camera Tint Fix](#camera-tint-fix) <br>
4.2 [RAM Fix](#ram-fix) 
5. [Data Preprocessing](#data-preprocessing)
6. [Setup Detection Training](#setup-detection-training)
7. [Setup Classification Training](#setup-classification-training)
8. [Evaluation](#evaluation)
9. [Setup Demo Case](#setup-demo-case)
10. [Team](#team)

## Prerequisites
To follow the guides in this repository the following prerequisites have to be satisfied.

We strongly recommend to use Ubuntu and cannot guarantee that everything will run on Windows.

On the host computer:
- Ubuntu 18.04 LTS installed (recommended)
- Jupyter Notebook installed
- CUDA 10.0 or higher installed
- cuDNN 7.6.5 installed
- [CUDA-capable NVIDIA GPU](https://developer.nvidia.com/cuda-gpus)

On the Jetson Nano:
- JetPack 4.3 installed (comes with JetCard image)
- [tensorflow-gpu 2.0.0+nv20.1.tf2 installed](https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform/index.html)
- RAM fix executed (see below)
- Camera tint fix installed (see below)

## Order JetBot Parts
We provide a customized version of the NVIDIA bill of materials.
This order list fits better to the Swiss market and can be found [here](howto/bill_of_materials.adoc).

## Build JetBot
Build the JetBot according to the [NVIDIA hardware guide](https://github.com/NVIDIA-AI-IOT/jetbot/wiki/Hardware-Setup).

## Setup Software
Setup the JetBot software according to the [NVIDIA software guide](https://github.com/NVIDIA-AI-IOT/jetbot/wiki/Software-Setup).

Connect a display and a keyboard and login with credentials: <br>
Username: jetbot <br>
Password: jetbot

Then execute the fixes below.

### Camera Tint Fix
You will have to install a new camera profile to fix the red tint on the Jetson Nano camera profile.

<span>1. Download the new camera profile:</span>

`wget https://www.waveshare.com/w/upload/e/eb/Camera_overrides.tar.gz
tar zxvf Camera_overrides.tar.gz`

<span>2. Unpack the archive:</span>
`tar --xzvf Camera_overrides.tar.gz`
 
<span>3. Copy the new profile to the target directory:</span>

`sudo cp camera_overrides.isp /var/nvidia/nvcam/settings/`

<span>4. Set the owner specifications:</span>

`sudo chmod 664 /var/nvidia/nvcam/settings/camera_overrides.isp`

`sudo chown root:root /var/nvidia/nvcam/settings/camera_overrides.isp`

<span>5. Reboot the Jetson Nano.</span>

### RAM Fix
To free up additional RAM on the Jetson Nano the GUI can be disabled:
 
`sudo systemctl set-default multi-user.target`

To enable it again execute: 

`sudo systemctl set-default graphical.target`

Note that this will deactivate the auto-login. 
You will have to connect at least a keyboard and maybe a display to login to the JetBot.

## Data Preprocessing
This package contains the data preparation instructions if you would like to train your own models. <br>
Please note that `merge_datasets_detection.ipynb` has to be only executed after the other notebooks have already been followed. 

- [preprocess_data_egohands.ipynb](howto/1_data_preprocessing/preprocess_data_egohands.ipynb) - Prepare Egohands dataset for **detection**
- [preprocess_data_tinyhands.ipynb](howto/1_data_preprocessing/preprocess_data_tinyhands.ipynb) - Prepare TinyHands dataset for **detection**
- [preprocess_data_lared.ipynb](howto/1_data_preprocessing/preprocess_data_lared.ipynb) - Prepare laRED dataset for **classification and detection**.
- [merge_datasets_detection.ipynb](howto/1_data_preprocessing/merge_datasets_detection.ipynb) - Merge other datasets for **detection**. 
 
## Setup Detection Training
If you wish to train your own hand detection model, you can follow the guide in this package.

Please see [detection_training_guide.md](howto/2_detection/detection_training_guide.md) for the setup details.

## Setup Classification Training
You can follow the guide in this package if you wish to train your own gesture classification model .

Please see [classification_training_guide.ipynb](howto/3_classification/classification_training_guide.ipynb) for the setup details.

## Evaluation
To evaluate the trained model you can follow the notebooks in this package.

Please see [evaluation_classification.ipynb](howto/4_evaluation/evaluation_classification.ipynb) for the walkthrough details to evaluate the classification model.

Please see [evaluation_end_to_end.ipynb](howto/4_evaluation/evaluation_end_to_end.ipynb) for the walkthrough details to evaluate the pipeline with the classification and the detection model.

Please see [evaluation_webcam_demo.ipynb](howto/4_evaluation/evaluation_webcam_demo.ipynb) for the walkthrough details to run the pipeline with the classification and the detection model using a webcam.

## Setup Demo Case
To setup the demo case perform the following steps.

1. Download this repository.
2. Copy the folder `howto/5_demo_case/` to the `/home/jetbot/notebooks/` directory on the JetBot.
3. Connect to the JetBot JupyterLab, open `gesture_demo_case.ipynb` and follow the instructions.

## Team
- Dimitri Muralt
  - dimitri.muralt@students.fhnw.ch
  - Skype: dimitri.muralt
  - FHNW GitLab: @dimitri.muralt

- Christoph Wenk
  - christoph.wenk@students.fhnw.ch
  - Skype: christoph_wenk
  - FHNW GitLab: @christoph.wenk