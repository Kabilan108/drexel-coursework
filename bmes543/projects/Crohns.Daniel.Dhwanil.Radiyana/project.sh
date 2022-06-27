#!/bin/bash

jupyter nbconvert --execute gather-dataset.ipynb && jupyter nbconvert --execute clean-data.ipynb && jupyter nbconvert --execute model.ipynb