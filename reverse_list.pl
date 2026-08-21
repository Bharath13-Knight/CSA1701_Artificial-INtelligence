reverse_list(L,R):-reverse_list(L,[],R).
reverse_list([],A,A).
reverse_list([H|T],A,R):-reverse_list(T,[H|A],R).

