# Introduction
Abstract: Even though the game of Cricket is the most popular sport in the country, the relative applications of artificial intelligence has been minimal in the past. We develop multiple use-cases of state of the art computer vision techniques over video data of cricket matches:
* Firstly, batsman and bowler are segmented from the image using Mask-RCNN as an approach for instance level video object segmentation of the batsman and bowler.
* Secondly, the scorecard is read from the video on a frame by frame basis using Optical Character Recognition. We then use this information to index the video by the index of the ball being bowled. ESPNCricInfo (a popular Cricket commentary website) was also scraped for expert commentary corresponding to the ball index.
* Finally, we develop various preprocessing techniques for removing jargon (like crowd shots, commentary box shots, interviews, fielder shots etc.) from the video so that we have only the batsman playing a cricket shot in our video sample.
* We thus built a dataset creation pipeline for cricket videos. The videos first go through preprocessing to remove jargon video segments, OCR indexes the frames to the ball index and data scrapper finds the corresponding expert commentary for that shot. The video goes through the batsman segmentation algorithm in the final stage.
* We also develop a type-of-shot classifier using deep learning over the videos as a precursor to our broader goal which is detailed below.
* The broad goal of the project is to, in the future, develop a performance analyzer of the batsman’s shot.

# Methodology
* Image Segmentation: We used Mask-RCNN which extends Faster-RCNN by adding a branch for predicting an object mask in parallel with the existing branch for bounding box recognition. The loss function for model is the total loss in doing the classification , generating bounding box and the mask. We used the pre-trained model trained on COCO dataset for the segmentation of the batsman and bowler for our videos. Initially background subtraction method was also tried (Background Subtractor 2 notebook) but the results were not godd due to movement in the positions of camera therefore we approached Mask-RCNN.(out.mp4 was created out of data.mp4 using Mask-RCNN)
* OCR: We used package called Pytesseract to extract the text data from image. It is an optical character recognition tool for python and can recognize and read text embedded in images.

![image](https://user-images.githubusercontent.com/42550496/77932162-cad2e300-72ca-11ea-8677-96e6988ab925.png)




* Data Scrapping: We used the selenium web driver to scrape the data (commentary and match stats) from online sources.
* Preprocessing Techniques:(To extract the frames we wanted  in the video which can be fed in the network). When the batsmen is about to strike the ball, the pitch can be seen clearly in the front view. So, we used masking, and other Image processing techniques to detect the pitch. Then we can take footage of 4 seconds from the time the pitch is seen for the first time.
* Dataset Creation: The overall data processing output is a CSV file containing following things: Initial frame(bowler delivering ball), Final Frame(End of a ball),OCR Text, Commentary, Ball no.(img: The final data generated.)

![image](https://user-images.githubusercontent.com/42550496/77932180-d0c8c400-72ca-11ea-808b-71e8e0d5f6d8.png)




* Deep Learning for shot classification: We are using ResNet-50 network to create the fixed dimensional feature vectors for each frame in the designated video section of 4 seconds or some fixed fames and then used these feature vectors to feed into the LSTM network and finally found classifications for the shot played. 

# Results 
* The pre-trained model for classifying our ROI(Region of Interest) has shown a very good segmentation mask as well as the bounding box prediction for the batsman and the bowler present on the pitch

![image](https://user-images.githubusercontent.com/42550496/77931936-76c7fe80-72ca-11ea-899f-32cb895fccbc.png)
![image](https://user-images.githubusercontent.com/42550496/77931973-80e9fd00-72ca-11ea-9e62-64d1f1dc596e.png)

  
  
* Frame when the bowler is about to bowl the ball and masked output.
  
![image](https://user-images.githubusercontent.com/42550496/77931990-85aeb100-72ca-11ea-9b63-62cc49aa7805.png)
![image](https://user-images.githubusercontent.com/42550496/77932006-8b0bfb80-72ca-11ea-8d0c-e59e579062e4.png)




# Successive Work:
* Currently we are trying to create the dataset for input to the ResNet-50-LSTM network manually by cropping the frames for each shot played , we are collecting about 300 shots for each of our five classes of shots as training data. The video frame number has been working well on one type of camera in a particular match played which may not work so well in general cases.
* The ResNet-50-LSTM notebook can be adjusted for running on a single video shot to extract features and feed it into LSTM block which we will be updating soon for running over all class of shots after creation of dataset.
* The next work will be the classification of the shots played by a batsman which will be the output of the ResNet-50-LSTM network.Note:ResNet-50-LSTM notebook has to be updated in further time.






