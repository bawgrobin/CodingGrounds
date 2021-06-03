#einschlag,durchschlag,schnitt = 4.6,4.6,172.9 #galantine ohne mods
#einschlag,durchschlag,schnitt = 4.6,4.6,198.8 #galantine +15% schnitt
#einschlag,durchschlag,schnitt = 3.5,3.5,63 #dual-cleavers no mod
#einschlag,durchschlag,schnitt = 3.5,3.5,110.2 #dual-zoren +75% schnitt
einschlag,durchschlag,schnitt = 3.5,3.5,173.3 #dual-zoren +175%schnitt (selbst bei 199 schnitt funktioniert das rüstung stripping noch)
schaden = einschlag+schnitt+durchschlag
quant = schaden/20

print ("Gesamtschaden: "+str(schaden))
print ("Prozentualer Schaden Einschlag: "+str(round(einschlag/schaden,2)*100)+"%")
print ("Schadensquantum = "+str(quant)+", davon Einschlag "+str(einschlag/quant))
print ("Finaler Einschlagsschaden: "+str(round(einschlag/quant)*(quant)))
