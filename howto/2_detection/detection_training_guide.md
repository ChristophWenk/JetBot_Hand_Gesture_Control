# Training with the TensorFlow Object Detection API
## Introduction
This guide describes how the TensorFlow Object Detection API (TFODA) needs to be used to train a detection model for TensorFlow.
The guide has been written for Ubuntu 18.04 LTS and might not work on Windows or other Linux distributions. 
The guide assumes you use Conda environments. 

## Preconditions
* TensorFlow 1.15 installed
* Pycocotools 2.0.0 installed
* Dataset has been prepared
* CUDA and cuDNN installed

## Preparations
### Download and setup Object Detection API
TFODA is part of TensorFlow models repository. It can be found on [GitHub](https://github.com/tensorflow/models).

1. Clone the repository into a location on the target host
2. Navigate to the `models/research/` directory
3. Run `setup.py` to get the required dependencies for TFODA

You might need to compile protobufs and install the object_detection package as described in the [official installation guide](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) and the [*Install* step](https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb) of the official demo on the TF models repository.
To do so run the following commands from `models/research/`:
<pre>
protoc object_detection/protos/*.proto --python_out=.
</pre>
<pre>
pip install .
</pre>

### Datasets
Before following this guide the necessary datasets have to be loaded.

To train the detection model three different datasets are used in conjunction. <br>
The necessary datasets can be found in the directory 1_data_preprocessing. 

This package contains the data preparation instructions if you would like to train your own models. <br>
Please note that `merge_datasets_detection.ipynb` has to be only executed after the other notebooks have already been followed.

- [preprocess_data_egohands.ipynb](howto/1_data_preprocessing/preprocess_data_egohands.ipynb) - Prepare Egohands dataset for **detection**
- [preprocess_data_tinyhands.ipynb](howto/1_data_preprocessing/preprocess_data_tinyhands.ipynb) - Prepare TinyHands dataset for **detection**
- [preprocess_data_lared.ipynb](howto/1_data_preprocessing/preprocess_data_lared.ipynb) - Prepare laRED dataset for **classification and detection**.
- [merge_datasets_detection.ipynb](howto/1_data_preprocessing/merge_datasets_detection.ipynb) - Merge other datasets for **detection**.

After executing the data preprocessing script all files can be found under your defined folder name.

### Set $PYTHONPATH
Python needs to know where it can find its required dependencies. 
One of these dependencies is slim that is provided with the TF models repository.
For this you need to edit the $PYTHONPATH environment variable.

From the command line run:

<pre>
export PYTHONPATH=:'[PathToTFODAslim]':$PYTHONPATH
</pre>

where `[PathToTFODAslim]` is the absolute path of the `slim/` directory located in `models/research/slim/` within the TF models repository.
Make sure you do not forget to add `:$PYTHONPATH` to the command or you will overwrite your current $PYTHONPATH variable instead of appending values to it.

You can check if the values have been added to the environment variable like follows:

<pre>
echo $PYTHONPATH
</pre>

## TFRecord generation
TFODA needs information how the training and validation data is structured. 
This information is provided in TFRecord format.

Instructions on how to generate these records can be found in the `generate_tfrecords.ipynb` Jupyter Notebook.
This notebook needs to be placed in the `models/research/` directory within the TF models repository.

1. Place `generate_tfrecords.ipynb` in `models/research/`
2. Start JupyterLab in that directory: `jupyter notebook`
3. Open JupyterLab. By default it can be found here: http://localhost:8888
4. Open `generate_tfrecords.ipynb` and follow the instructions to generate the records
5. Place the generated records `train.record` and `val.record` like described in the folder structure

## Folder structure
The folder structure needs to match the paths set in `generate_tfrecords.ipynb`.
1. Place the images for training in `detection_training/images_train/` and the images for validation in `detection_training/images_val/`.
2. Place all other files in `detection_training/`

<pre>
detection_training/  
├── images_train/  
│   ├── train_image1.jpg  
│   ├── train_image2.jpg  
│   ├── train_image3.jpg
│   └── ... 
├── images_val/  
│   ├── val_image1.jpg  
│   ├── val_image2.jpg  
│   ├── val_image3.jpg
│   └── ...  
├── output/
├── train.record
├── val.record  
├── labels_train.csv
├── labels_val.csv
└── ssd_mobilenet_v2.config
</pre>

## Prepare config file
The training configuration must be provided in form of a `ssd_mobilenet_v2.config` file.
Various parameters like the model architecture, image size or the learning rate can be set.
You can take a provided config file or have a look at the [TFODA sample config files](https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs). 

You can find the .config file used for this work in the current folder named as `ssd_mobilenet_v2`.

## Start the training
The start command needs to be executed from the `models/research/` directory in the TF models repository.
The paths need to match the ones defined in `generate_tfrecords.ipynb`.
The number of training steps can be adjusted with `num_train_steps`.

<pre>
python3 object_detection/model_main.py \
    --pipeline_config_path=/home/jetbot/Documents/detection_training/ssd_mobilenet_v2.config \
    --model_dir=/home/jetbot/Documents/detection_training/output \
    --num_train_steps=249999 \
    --sample_1_of_n_eval_examples=1 \
    --alsologtostderr
</pre>

This will start to generate checkpoints in the `detection_training/output/` directory.
Checkpoints will allow you to stop and restart the training from that checkpoint with the command above.
Once the defined number of training steps have been reached the training cannot be restarted again unless the number of steps will be increased.

## Observe the training
The training progress can be observed with Tensorboard.
1. Navigate to the `detection_training/output/` directory
2. Start Tensorboard: `tensorboard --logdir=./`
3. Open http://localhost:6006/

## Export model graph
Once the training is finished you can find the generated checkpoints in `detection_training/output/`.
To export the model you can run the command below from the `models/research/` directory within the TF models repository.

<pre>
python3 object_detection/export_inference_graph.py \
    --input_type=image_tensor \
    --pipeline_config_path=/home/jetbot/Documents/detection_training/ssd_mobilenet_v2.config \
    --trained_checkpoint_prefix=/home/jetbot/Documents/detection_training/output/model.ckpt-249999 \
    --output_directory=/home/jetbot/Documents/detection_training/output/export
</pre>

This will generate a `saved_model/saved_model.pb` and a `frozen_inference_graph.pb` in the `export` directory.

Your model is now ready to be deployed.

## References
* TensorFlow models repository: https://github.com/tensorflow/models
* TF Object Detection API tutorial: https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb 
* TFODA config file samples: https://github.com/tensorflow/models/tree/master/research/object_detection/samples/configs