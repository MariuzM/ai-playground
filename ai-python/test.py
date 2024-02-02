from transformers import pipeline

# Allocate a pipeline for sentiment-analysis
pipe = pipeline('sentiment-analysis')

out = pipe('I love transformers!')
print(out)
# [{'label': 'POSITIVE', 'score': 0.999806941}]






# import cv2

# img = cv2.imread("img.png")

# cv2.imshow("image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
