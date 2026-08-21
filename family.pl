parent(ann,bob). parent(bob,cal).
father(X,Y):-parent(X,Y),male(X).
male(ann). male(bob).
grandparent(X,Z):-parent(X,Y),parent(Y,Z).

