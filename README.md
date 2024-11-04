<div align="center">

# YOLO11n-pose Hand Keypoint Detection

<img src="/readme-media/hand-landmarks.jpg" alt="Demo" width="100%">
<img src="/readme-media/test.gif" alt="Demo" width="100%">

##### As shown in this test video, the trained model struggles to accurately detect keypoints for gestures like pinching and swiping. However, it performs well in identifying keypoints on open hands, whether facing forward or backward.

</div>

<br>

## Run your own tests with this model
Clone the repository
```
git clone https://github.com/chrismuntean/YOLO11n-pose-hands.git
```

Install dependencies (just need `Ultralytics` and its dependencies)
```
pip install -r requirements.txt
```
Run the webcam test on your machine
```
python webcam-test.py
```
**Note:** Test videos saved to `/runs/pose/output/test/<#>.avi`

<br>

## Model Metrics

<div align="center">
<img src="runs/pose/train/results.png" alt="Model Results" width="100%">

### Download the trained `best.pt` file [here](https://github.com/chrismuntean/YOLO11n-pose-hands/blob/bda894403f378d2a298d2f88ae9d5ed6d4e9f8e3/runs/pose/train/weights/best.pt)

</div>

<br>

## How this model was trained

### Dataset
This model was trained on the ["Hand Keypoint Dataset 26K"](https://www.kaggle.com/datasets/riondsilva21/hand-keypoint-dataset-26k) made by [Rion Dsilva](https://www.linkedin.com/in/rion-dsilva-043464229/)

The hand keypoint dataset is split into two subsets:

1. **Train**: This subset contains 18,776 images from the hand keypoints dataset, annotated for training pose estimation models.
2. **Val**: This subset contains 7992 images that can be used for validation purposes during model training.

<br>

### Mosaiced Images
<div align="center">
<img src="runs/pose/train/train_batch2.jpg" alt="Model Results" width="100%">
</div>
<br>

> This image demonstrates a training batch composed of mosaiced dataset images. Mosaicing is a technique used during training that combines multiple images into a single image to increase the variety of objects and scenes within each training batch. This helps improve the model's ability to generalize to different object sizes, aspect ratios, and contexts. - [Ultralytics](https://docs.ultralytics.com/datasets/pose/hand-keypoints/#sample-images-and-annotations)

<br>

## Citations and Acknowledgments

### Big thanks @IsaacTheDev for letting me use his 4070 for training <3

If you use the hand-keypoints dataset in your research or development work, please acknowledge the following sources:
```
@article{afifi201911kHands,
  title = {11K Hands: gender recognition and biometric identification using a large dataset of hand images},
  author = {Afifi, Mahmoud},
  journal = {Multimedia Tools and Applications},
  doi = {10.1007/s11042-019-7424-8},
  url = {https://doi.org/10.1007/s11042-019-7424-8},
  year={2019}
}

@misc{imsparsh2020gesture,
  title = {Gesture Recognition Dataset},
  author = {Sparsh, Imsparsh},
  year = {2020},
  url = {https://www.kaggle.com/datasets/imsparsh/gesture-recognition}
}

@misc{giridhar2020hand,
  title = {2000 Hand Gestures},
  author = {Giridhar, Ritika},
  year = {2020},
  url = {https://www.kaggle.com/datasets/ritikagiridhar/2000-hand-gestures}
}
```