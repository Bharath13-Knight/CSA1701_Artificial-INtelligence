queens(Q):-permutation([1,2,3,4,5,6,7,8],Q),safe(Q).
safe([]).
safe([H|T]):-safe(T,H,1),safe(T).
safe([],_,_).
safe([H|T],Q,D):-H-Q=\=D,H-Q=\= -D,D1 is D+1,safe(T,Q,D1).

