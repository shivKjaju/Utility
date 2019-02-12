import argparse
from imutils import paths
import cv2

def var_laplacian(image):
	return cv2.Laplacian(image, cv2.CV_64F).var()
	
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required = True, help = "gives the path to the images")
ap.add_argument("-t", "--threshold", type=float, default=100.0, help="this checks the threshold for blurriness")
args = vars(ap.parse_args())

for imagePath in paths.list_images(args["images"]):
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	value = var_laplacian(gray)
	text = "Not blurry"
	
	if value < args["threshold"]:
		text = "Blurry"
	cv2.putText(image, "{}: {: .2f}".format(text, value), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255),3)
	cv2.imshow("Image", image)
	key = cv2.waitKey(0)
