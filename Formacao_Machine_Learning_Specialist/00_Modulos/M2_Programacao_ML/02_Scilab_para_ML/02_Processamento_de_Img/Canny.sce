scicv_Init();

img_gray = imread(getSampleImage("shapes.png"), CV_LOAD_IMAGE_GRAYSCALE);

subplot(1,2,1);
matplot(img_gray);

thresh = 100;
img_canny = Canny(img_gray, thresh, thresh*2, 3);

subplot(1,2,2);
matplot(img_canny);

delete_Mat(img_gray);
delete_Mat(img_canny);
