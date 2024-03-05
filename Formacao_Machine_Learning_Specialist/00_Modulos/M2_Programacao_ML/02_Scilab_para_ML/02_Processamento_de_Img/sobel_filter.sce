scicv_Init();

img = imread(getSampleImage("lena.jpg"));
ksize = 3;

// First order derivative on x
dx = 1;
dy = 0;
img_grad_x = Sobel(img, CV_16S, dx, dy, ksize);
subplot(1,2,1);
matplot(img_grad_x);

// First order derivative on y
dx = 0;
dy = 1;
img_grad_y = Sobel(img, CV_16S, dx, dy, ksize);
subplot(1,2,2);
matplot(img_grad_y);

delete_Mat(img);
delete_Mat(img_grad_x);
delete_Mat(img_grad_y);
