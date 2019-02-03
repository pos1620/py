from conta import conta;

c1 = conta();

print "Welcome to teh Economiestier"
print "seus investimento a longo prazo retornara:",c1.Trial();
print "seus investimento no prazo de "+str(c1.months)+" meses retornara:" +str(c1.Trial()+c1.months*4);
print("\n\n");

real=180/9;
print str(c1.months)+" meses,equivalente a "+str(c1.months*30);

print str(float(real))+" meses";

print "{:.2f}".format(real);