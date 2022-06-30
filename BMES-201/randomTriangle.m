% Plotting randon triangles

gca.XLim(1) =-5;
gca.Xlim(2) = 55;

gca.YLim = [-5 55];

x = randi(50,1,3);
y = randi(50,1,3);

x = [x x(1)];
y = [y y(1)];

plot(x,y)