print_numbers(N):-N>10,!.
print_numbers(N):-write(N),nl,N1 is N+1,print_numbers(N1).