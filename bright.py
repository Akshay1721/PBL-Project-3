import cv2

# path of the image to read.
path = C:\Users\DELL\Downloads

# Read the image color or RGB format.
img_rgb=cv2.imread(path,1)

# Read image in black and white or grayscale format
img_grayscale = cv2.imread(path,0)

# Display RGB image.
cv2.imshow("rgb_img", img_rgb)
cv2.imshow("grayscale_img", img_grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
