import cv2
from skimage.metrics import structural_similarity as ssim

# TODO: Add contour detection for enhanced accuracy

def match(path1, path2):
    # Read the images
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    
    # Turn images to grayscale
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # Resize images for comparison
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    
    # Display both images
    cv2.imshow("One", img1)
    cv2.imshow("Two", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Calculate the similarity value
    similarity_value = "{:.2f}".format(ssim(img1, img2) * 100)
    
    return float(similarity_value)
