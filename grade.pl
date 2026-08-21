grade(M, A):-M>=90,A='A'.
grade(M, B):-M>=75,M<90,B='B'.
grade(M, C):-M>=50,M<75,C='C'.
grade(M, F):-M<50,F='F'.

