# CNN-ModelNet-40
A CNN model trained on the [ModelNet 40 dataset.](https://modelnet.cs.princeton.edu/)

**About the dataset:**

The Princeton ModelNet40 contains 3D models in the form of .off files.This implementation uses data in the form of .h5py files, which can be found [here.](https://github.com/lmb-freiburg/orion)

**How it works:**

* Point cloud data is read from the .h5py files. 
* It is then voxelised to reduce dimensionality. 
* The voxelised array is fed as input to the model defined in train.py.
* Set the path to save the model in  train.py.
* Use test.py to visualise misclassified results.

**Requirements**
* Tensorflow 1.x
* Numpy
* Open3D
* Matplotlib
