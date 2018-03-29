#!/usr/bin/env python
import sys, os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from tsukuba2017_jrm.dict_tools import loader


def plot_pointcloud(dataset, stride = 4):

    # Plot heading
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # for track_id in dataset['pointclouds']: # Show all point clouds
    for track_id in dataset['filtered']: # Show only unfiltered pointclouds
        for timestamp in dataset['pointclouds'][track_id]: # Show all pointclouds
            pointcloud = dataset['pointclouds'][track_id][timestamp]
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(pointcloud[:,0], pointcloud[:,1], pointcloud[:,2], c='r', marker='o', depthshade=False)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_zlabel('z')
            ax.axis('square')
            plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        dir = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
        # dataset_file = dir + "/sample_data/log_2017-11-06-11-11-40/log_2017-11-06-11-11-40.pk1"
        dataset_file = "/home/kusanagi/Documents/workspaces/pflow-jrm/data/log_data/log_2017-11-03-10-30-10/log_2017-11-03-10-30-10.pk1"
    else:
        dataset_file = sys.argv[1]

    # Load data
    dataset = loader.load_dict(dataset_file)

    # Plot
    plot_pointcloud(dataset)
