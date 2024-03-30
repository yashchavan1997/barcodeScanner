import cv2
from pyzbar.pyzbar import decode

def read_barcodes(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Decode barcodes
    barcodes = decode(image)
    
    # Process each barcode found
    for barcode in barcodes:
        # Extract barcode data
        barcode_data = barcode.data.decode('utf-8')
        
        # Extract barcode bounding box coordinates
        (x, y, w, h) = barcode.rect
        
        # Draw the bounding box and barcode data on the image
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(image, barcode_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        
        # Print barcode data
        print("Barcode detected:", barcode_data)
    
    # Display the image with detected barcodes
    cv2.imshow("Detected Barcodes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    # Provide path to the image containing barcodes
    image_path = "/home/y/Pictures/customerLogos/tmp.jpg"
    read_barcodes(image_path)

if __name__ == "__main__":
    main()
