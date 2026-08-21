bill(Units,Amount):-Units=<100,Amount is Units*1.
bill(Units,Amount):-Units>100,Units=<200,Amount is 100+(Units-100)*2.
bill(Units,Amount):-Units>200,Amount is 300+(Units-200)*3.

