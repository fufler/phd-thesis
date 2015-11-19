\input{tikz/markers_border_reconstruction_border_cells.inc}

% внутренние ячейки
\filldraw[fill=green!40!white, draw=black,thick] (0,0) rectangle (-1,1);
\filldraw[fill=green!40!white, draw=black,thick] (-1,0) rectangle (-2,1);
\filldraw[fill=green!40!white, draw=black,thick] (0,1) rectangle (-1,2);

\filldraw[fill=green!40!white, draw=black,thick] (0,0) rectangle (-1,-1);
\filldraw[fill=green!40!white, draw=black,thick] (-1,0) rectangle (-2,-1);
\filldraw[fill=green!40!white, draw=black,thick] (0,-1) rectangle (-1,-2);

\filldraw[fill=green!40!white, draw=black,thick] (0,0) rectangle (1,1);
\filldraw[fill=green!40!white, draw=black,thick] (1,0) rectangle (2,1);
\filldraw[fill=green!40!white, draw=black,thick] (0,1) rectangle (1,2);

\filldraw[fill=green!40!white, draw=black,thick] (0,0) rectangle (1,-1);
\filldraw[fill=green!40!white, draw=black,thick] (1,0) rectangle (2,-1);
\filldraw[fill=green!40!white, draw=black,thick] (0,-1) rectangle (1,-2);
