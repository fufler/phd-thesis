% сетка
\draw[step=1,gray,very thin] (-5,-5) grid (5,5);

% граничные ячейки
\filldraw[fill=blue!40!white, draw=black,thick](-1,3) rectangle (0,4);
\filldraw[fill=blue!40!white, draw=black,thick](-1,2) rectangle (0,3);
\filldraw[fill=blue!40!white, draw=black,thick](-2,2) rectangle (-1,3);
\filldraw[fill=blue!40!white, draw=black,thick](-2,1) rectangle (-1,2);
\filldraw[fill=blue!40!white, draw=black,thick](-3,1) rectangle (-2,2);
\filldraw[fill=blue!40!white, draw=black,thick](-3,0) rectangle (-2,1);
\filldraw[fill=blue!40!white, draw=black,thick](-4,0) rectangle (-3,1);

\filldraw[fill=blue!40!white, draw=black,thick](-1,-3) rectangle (0,-4);
\filldraw[fill=blue!40!white, draw=black,thick](-1,-2) rectangle (0,-3);
\filldraw[fill=blue!40!white, draw=black,thick](-2,-2) rectangle (-1,-3);
\filldraw[fill=blue!40!white, draw=black,thick](-2,-1) rectangle (-1,-2);
\filldraw[fill=blue!40!white, draw=black,thick](-3,-1) rectangle (-2,-2);
\filldraw[fill=blue!40!white, draw=black,thick](-3,0) rectangle (-2,-1);
\filldraw[fill=blue!40!white, draw=black,thick](-4,0) rectangle (-3,-1);

\filldraw[fill=blue!40!white, draw=black,thick](1,3) rectangle (0,4);
\filldraw[fill=blue!40!white, draw=black,thick](1,2) rectangle (0,3);
\filldraw[fill=blue!40!white, draw=black,thick](2,2) rectangle (1,3);
\filldraw[fill=blue!40!white, draw=black,thick](2,1) rectangle (1,2);
\filldraw[fill=blue!40!white, draw=black,thick](3,1) rectangle (2,2);
\filldraw[fill=blue!40!white, draw=black,thick](3,0) rectangle (2,1);
\filldraw[fill=blue!40!white, draw=black,thick](4,0) rectangle (3,1);

\filldraw[fill=blue!40!white, draw=black,thick](1,-3) rectangle (0,-4);
\filldraw[fill=blue!40!white, draw=black,thick](1,-2) rectangle (0,-3);
\filldraw[fill=blue!40!white, draw=black,thick](2,-2) rectangle (1,-3);
\filldraw[fill=blue!40!white, draw=black,thick](2,-1) rectangle (1,-2);
\filldraw[fill=blue!40!white, draw=black,thick](3,-1) rectangle (2,-2);
\filldraw[fill=blue!40!white, draw=black,thick](3,0) rectangle (2,-1);
\filldraw[fill=blue!40!white, draw=black,thick](4,0) rectangle (3,-1);

% граница
\draw[red,thick] (0,3.5) -- (-3.5,0) -- (0,-3.5) -- (3.5,0) -- cycle;
