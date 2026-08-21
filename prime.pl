prime(N):-N>1, \+ composite(N,2).
composite(N,D):-D*D=<N, (N mod D=:=0 ; D1 is D+1, composite(N,D1)).

