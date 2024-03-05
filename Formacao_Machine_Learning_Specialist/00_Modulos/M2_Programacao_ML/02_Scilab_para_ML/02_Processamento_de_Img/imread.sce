scicv_Init();

img = imread(getSampleImage("lena.jpg"));

matplot(img);

delete_Mat(img);
