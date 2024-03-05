scicv_Init();

img_gray = imread(getSampleImage("lena.jpg"), CV_LOAD_IMAGE_GRAYSCALE);

matplot(img_gray);

delete_Mat(img_gray);
