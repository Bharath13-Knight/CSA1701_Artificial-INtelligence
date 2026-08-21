maximum([H|T],M):-maximum(T,H,M).
maximum([],M,M).
maximum([H|T],A,M):-A1 is max(H,A),maximum(T,A1,M).

