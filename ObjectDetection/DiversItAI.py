import imutils
import cv2

def multiple_contours(path):
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	
	thresh = cv2.threshold(gray, 20, 200, cv2.THRESH_BINARY)[1]
	thresh = cv2.erode(thresh, None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=2)
	
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key=cv2.contourArea)
	
	
	
	cv2.drawContours(image, cnts, -1, (0, 255, 255), 2)
	return (image)

def single_contours(path):
	image = cv2.imread(path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)

	thresh = cv2.threshold(gray,20, 200, cv2.THRESH_BINARY)[1]
	thresh = cv2.erode(thresh, None, iterations=2)
	thresh = cv2.dilate(thresh, None, iterations=2)

	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key=cv2.contourArea)

	extLeft = tuple(c[c[:, :, 0].argmin()][0])
	extRight = tuple(c[c[:, :, 0].argmax()][0])
	extTop = tuple(c[c[:, :, 1].argmin()][0])
	extBot = tuple(c[c[:, :, 1].argmax()][0])

	# draw the outline of the object, then draw each of the extreme points, where the left-most is red, right-most is green, top-most is blue, and bottom-most is teal
	cv2.drawContours(image, [c], -1, (0, 255, 255), 2)
	cv2.circle(image, extLeft, 6, (0, 0, 255), -1)
	cv2.circle(image, extRight, 6, (0, 255, 0), -1)
	cv2.circle(image, extTop, 6, (255, 0, 0), -1)
	cv2.circle(image, extBot, 6, (255, 255, 0), -1)
	return (image)



