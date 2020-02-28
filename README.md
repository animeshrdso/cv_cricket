# Action Recognition in Sports

* The following project is on action recognition in sports videos , specially in cricket.
* Our main goal is to predict the type of shot(cover drive, straight drive, cut etc.) played by a batsman in live cricket videos.
* We will be training our networks by the videos by taking the ground truth present on some famous cricket broadcasting sites such as cricinfo.com etc.
* We are trying to segment the batsman in the live video and predict the quality of shot played by the batsman and the run scored out of that ball.
* While training the runs scored out of a particular ball will be fetched by web scraping the details from the broadcasting websites and the quality of shot played by the batsman will be learned by using sentiment analysis in the audio data of the commentators who are considered as experts.
# Segmentation 
* Initially we tried the background subtraction for extracting the batsman in video but it did not give satisfactory results, which can be found out by implementing the two notebooks Background Subtraction 1 and 2.
* We have used Mask RCNN for the segmentation of the batsman in the video.
* Open the notebook - MRCNN_Video for its implementation.
* Download the pre-trained weights from the coco-dataset for using the weights for our model.
* For our input video "data.mp4" the output video "out.mp4" was obtained after implementing Mask RCNN.

# OCR building
* We are trying to crop the video by extracting each frame out of it and trying to read the text given on the bottom part of our frames for optical character reading of the details about the batsman , the current score and over and delivery number.


The Speech to text conversion and the web scraping part is still in progress.


