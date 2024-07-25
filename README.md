<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
<body>
    <div class="container">
        <h1>YOLOv5 Number Plate Detection</h1>
        <p>This repository contains the implementation of a YOLOv5 model fine-tuned for detecting number plates in images and videos. The model is also integrated with EasyOCR for recognizing the text on detected number plates.</p>

  <h2>Requirements</h2>
  <p>Make sure you have the following libraries installed:</p>
  <pre><code>pip install torch opencv-python-headless pytesseract easyocr numpy pandas</code></pre>

  <h2>Usage</h2>
   <p>To detect number plates run the <code>Detection.py</code>. In this python there are three different input options, which are given below ...</p>
  <h3>Detect Number Plates in an Image</h3>
  <p>To detect number plates from an image, use the following command:</p>
  <pre><code>main(img_path='path_to_your_image.jpg')</code></pre>

  <h3>Detect Number Plates in a Video</h3>
  <p>To detect number plates from a video, use the following command:</p>
  <pre><code>main(vid_path='path_to_your_video.mp4', vid_out='output_video.mp4')</code></pre>

  <h3>Real-time Number Plate Detection Using Webcam</h3>
  <p>To use your webcam for real-time number plate detection, use the following command:</p>
  <pre><code>main(vid_path=0, vid_out='webcam_output.mp4')</code></pre>

  <h2>Description</h2>
  <p>This project involves detecting number plates using the YOLOv5 model. After detecting the number plates, the text on the plates is recognized using EasyOCR. The following steps outline the main functionalities:</p>
  <ul>
      <li><strong>Loading the model:</strong> The YOLOv5 model is loaded and ready for detection.</li>
      <li><strong>Detecting objects:</strong> The model detects number plates in images or video frames.</li>
      <li><strong>Recognizing text:</strong> EasyOCR is used to read the text on the detected number plates.</li>
      <li><strong>Displaying results:</strong> The detected number plates and recognized text are displayed on the image or video frames.</li>
  </ul>

  <h2>Model Training and Fine-Tuning</h2>
  <p>To fine-tune the YOLOv5 model with new data, follow these steps:</p>
  
  <h3>Labeling Data</h3>
      <p>Use <a href="https://www.makesense.ai">makesense.ai</a> to label your license plate images. Save the labeled images and corresponding label files in the <code>train</code>, <code>test</code>, and <code>val</code> folders.</p>
  <h3>Folder Structure</h3>
  <p>Organize your data in the following folder structure:</p>
  <pre><code>
model_training/
├── train/
│   ├── images/
│   └── labels/
├── test/
│   ├── images.jpg
├── val/
│   ├── images/
│   └── labels/
├── custom.yaml
└── Train_Code.txt
        </code></pre>
      

  <h3>Custom YAML File</h3>
  <p>Create a <code>custom.yaml</code> file with the following content:</p>
  <pre><code>
train: /path/to/model_training/train
val: /path/to/model_training/val
test: /path/to/model_training/test

nc: 1  # number of classes
names: ['licence']  # class names
        </code></pre>

  <h3>Training the Model</h3>
  <p>Use the code in <code>Train_Code.txt</code> to train the model. Run the following command in the terminal where YOLOv5 is located:</p>
  <pre><code>python train.py --img 640 --batch 16 --epochs 100 --data /path/to/model_training/custom.yaml --weights yolov5s.pt --cache</code></pre>

  <h2>Integrating EasyOCR</h2>
  <p>EasyOCR is integrated into the project to read the text on detected number plates. This involves:</p>
  <ul>
      <li>Extracting the region of interest (ROI) containing the number plate.</li>
      <li>Applying EasyOCR to the ROI to recognize the text.</li>
      <li>Filtering and displaying the recognized text.</li>
  </ul>
  <h2>Example Output</h2>
  <p>Below is an example output image showing detected number plates and recognized text:</p>
  <img src="https://github.com/anandakumarak/Number-Plate-Detection-Using-YoloV5/blob/main/Output_image.png" alt="Output Image" width = 690>
  <h2>Contact</h2>
  <p>For any questions or issues, please contact.</p>
</div>
</body>
</html>
