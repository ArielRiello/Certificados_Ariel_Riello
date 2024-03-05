scicv_Init();

img_gray = imread(getSampleImage("shapes.png"), CV_LOAD_IMAGE_GRAYSCALE);

thresh = 100;
img_canny = Canny(img_gray, thresh, thresh*2, 3);

lines = HoughLines(img_canny, 1, %pi/180, 50);

rho = lines(1,:);
theta = lines(2,:);
a = cos(theta);
b = sin(theta);
xy0 = [rho; rho] .* [a; b];
xy1 = xy0 - 1000 * [-b; a];
xy2 = xy0 + 1000 * [-b; a];

img_out = new_Mat(size(img_gray, 'r'), size(img_gray, 'c'), CV_8UC3);
nb_lines = size(lines, 'c');
for i=1:nb_lines
    line(img_out, xy1(:,i), xy2(:,i), [0,0,255]);
end

matplot(img_out);

delete_Mat(img_gray);
delete_Mat(img_canny);
delete_Mat(img_out);
