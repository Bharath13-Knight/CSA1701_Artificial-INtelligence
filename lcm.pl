gcd(A,0,A).
gcd(A,B,G):-B>0,R is A mod B,gcd(B,R,G).
lcm(A,B,L):-gcd(A,B,G),L is abs(A*B)//G.

