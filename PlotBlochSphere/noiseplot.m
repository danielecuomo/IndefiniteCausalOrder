[X, Y, Z] = sphere;
surf(X,Y,Z,'facecolor','none');
[X, Y, Z] = supermap(X, Y, Z, chi); %please define a process matrix chi of 4x4 complex numbers
surface(X,Y,Z);
axis equal;