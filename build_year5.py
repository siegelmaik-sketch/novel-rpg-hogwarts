#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahr 5 — 'Der Orden des Phoenix' (~12, Film-Niveau) als NAHTLOSE Fortsetzung. Haengt hinter y4_s19 an.

Ton: altersgerecht fuer ~12 (Niveau der HP-Buecher/Filme). Ernst, spannend, traurig erlaubt,
aber ohne grausige Bilder/Gore. Herzstueck: Dumbledores Armee (Zusammenhalt, echte Verteidigung
lernen). Umbridge = institutionelle Haerte/Ungerechtigkeit, KEINE grafische Selbstverletzung
(kein Blutfeder-Detail). Kanon-Verlust: Sirius stirbt im Ministerium — wuerdevoll und traurig
erzaehlt, ohne Gore; die Erwachsenen schirmen die Kinder ab und troesten.
Aufruf: python3 build_year5.py
"""
import json, os, itertools
HERE=os.path.dirname(os.path.abspath(__file__)); BOOK=os.path.join(HERE,"skill","data","books","hogwarts")
data=json.load(open(os.path.join(BOOK,"plot_graph.json"),encoding="utf-8")); existing=data["scenes"]
if any(s["id"].startswith("y5_") for s in existing): raise SystemExit("Jahr 5 existiert bereits.")
_c=itertools.count(1)
def wid(): return f"w{next(_c):03d}"
def C(d,canon=True,stats=None,rels=None,docks=None):
    c={"description":d,"canon":canon}
    if stats:c["stat_effects"]=stats
    if rels:c["relationship_effects"]=rels
    if docks is not None:c["docks"]=docks
    return c
def A(id_,ch,title,st,present,loc,summ,choices,cp=False,recap=None,plot="kanon"):
    b={"id":id_,"chapter":ch,"scene_index":0,"title":title,"school_time":st,"characters_present":present,
       "location":loc,"summary":summ,"plot_type":plot,"challenge_potential":3 if cp else 2,
       "crossing_point":cp,"choices":choices,"next_scenes":[]}
    if cp: b["clique_bond_delta"]=1; b["autonomous_recap"]=recap
    return b
P="player_heroine"
backbone=[
 A("y5_s01",25,"Ein unheimlicher Sommer","Sommerferien — zuhause",
   [P,"marlen","maik","flocke"],"haus_sosa",
   "Die Zaubererwelt will nicht wahrhaben, dass die Finsternis zurueck ist — und so liegt ueber den Ferien eine wachsame Anspannung. Doch in deiner Familie ist es warm und sicher, und Flocke weicht dir nicht von der Seite.",
   [C("Dich bei Mama und Papa geborgen fuehlen",stats={"loyalty":5},rels={"Mama":4,"Papa":4}),
    C("Aufmerksam und mutig bleiben, falls etwas kommt",stats={"combat":4}),
    C("Den Freunden schreiben, dass ihr zusammenhaltet",rels={"Harry":3})]),
 A("y5_s02",25,"Das Hauptquartier des Ordens","Spaetsommer — Grimmauldplatz",
   [P,"sirius","lupin","harry"],"grimmauldplatz",
   "Du wirst an einen geheimen Ort gebracht: das Hauptquartier des Ordens, wo die Erwachsenen sich gegen die Finsternis organisieren. Und da ist er wieder — Sirius! Die Wiedersehensfreude ist riesig; er ist warmherzig wie eh und je und passt auf alle auf.",
   [C("Sirius freudig wiedersehen",stats={"loyalty":5},rels={"Sirius":8,"Harry":4}),
    C("Den Erwachsenen aufmerksam zuhoeren",stats={"wisdom":4},rels={"Lupin":4}),
    C("Dich sicher fuehlen, weil so viele zusammenhalten",stats={"reputation":3})],plot="wendepunkt"),
 A("y5_s03",25,"Die neue Lehrerin Umbridge","1. September — Grosse Halle",
   [P,"umbridge","harry"],"grosse_halle",
   "Das Ministerium setzt eine neue Lehrerin ein: Professorin Umbridge, ganz in Rosa, mit zuckersuessem Laecheln und einem kleinen 'Hem, hem'. Doch hinter der Suesse steckt eiserne Kontrolle — und sie tut so, als gaebe es keine Gefahr.",
   [C("Hoeflich, aber wachsam bleiben",stats={"wisdom":4}),
    C("Dir denken, dass mit ihr etwas nicht stimmt",stats={"wisdom":4}),
    C("Harry zur Seite stehen, den sie schon im Blick hat",stats={"loyalty":4},rels={"Harry":4})],plot="wendepunkt"),
 A("y5_s04",26,"Umbridges Unterricht","September — Verteidigung gegen die dunklen Kuenste",
   [P,"umbridge","hermine"],"klassenzimmer",
   "Bei Umbridge gibt es nur trockene Theorie aus dem Buch — keinen einzigen echten Zauber. 'Es gibt da draussen nichts zu fuerchten', saeuselt sie. Hermine kocht innerlich: Wie sollen sie sich verteidigen lernen, wenn niemand es ihnen beibringt?",
   [C("Mit Hermine den stillen Aerger ueber den nutzlosen Unterricht teilen",stats={"wisdom":4},rels={"Hermine":5}),
    C("Hoeflich, aber bestimmt eine kritische Frage stellen",stats={"combat":3,"reputation":3}),
    C("Dir vornehmen, echte Verteidigung anders zu lernen",stats={"wisdom":5})]),
 A("y5_s05",26,"Ungerechte Strafarbeit","September — Umbridges Buero",
   [P,"umbridge"],"klassenzimmer",
   "Umbridge teilt fuer Kleinigkeiten harte, ungerechte Strafarbeiten aus und genoesst ihre Macht. Es ist zermuerbend und unfair — aber du behaeltst still deine Wuerde und deinen Mut. (Keine Gewalt, nur eiskalte Ungerechtigkeit.)",
   [C("Die Ungerechtigkeit still und wuerdevoll ertragen",stats={"loyalty":5,"wisdom":3}),
    C("Dir merken: So jemand darf den Mut nicht brechen",stats={"combat":4}),
    C("Hinterher Freunden davon erzaehlen und Trost finden",rels={"Hermine":3,"Harry":3})],plot="wendepunkt"),
 A("y5_s06",26,"Luna Lovegood","Oktober — Laendereien",cp=True,
   present=[P,"luna","ginny"],loc="ländereien_see",
   summ="Du lernst Luna Lovegood kennen — vertraeumt, eigen, herzensgut. Andere finden sie seltsam, du findest sie wunderbar ehrlich und mutig. Eine echte, treue Freundschaft beginnt, ganz ohne Wenn und Aber.",
   choices=[C("Dich mit Luna anfreunden, so wie sie ist",canon=True,docks=True,stats={"loyalty":6},rels={"Luna":12,"Ginny":4}),
    C("Luna gegen spoettische Bemerkungen verteidigen",canon=True,stats={"reputation":4},rels={"Luna":6}),
    C("Ihren ungewoehnlichen Blick auf die Welt bestaunen",canon=True,stats={"wisdom":4})],
   recap="Einige schlossen die vertraeumte Luna ins Herz. Du hast die Gelegenheit diesmal verpasst.",plot="wendepunkt"),
 A("y5_s07",27,"Die Idee: Dumbledores Armee","Oktober — Hogsmeade, Zu den Drei Besen",cp=True,
   present=[P,"hermine","harry","ron"],loc="hogsmeade",
   summ="Bei Butterbier hat Hermine eine kuehne Idee: Wenn Umbridge keine echte Verteidigung lehrt, dann lernen sie eben heimlich selbst — und Harry, der schon so viel erlebt hat, soll es ihnen beibringen. Eine geheime Gruppe, die zusammenhaelt.",
   choices=[C("Sofort begeistert mitmachen und dich anschliessen",canon=True,docks=True,stats={"loyalty":6,"combat":3},rels={"Hermine":5,"Harry":6,"Ron":4}),
    C("Kluge Vorschlaege machen, wie man es geheim haelt",canon=True,stats={"wisdom":5}),
    C("Andere mutige Mitschueler dafuer gewinnen",canon=True,rels={"Luna":4,"Neville":4})],
   recap="In den Drei Besen entstand die Idee einer geheimen Verteidigungs-Gruppe. Du warst nicht dabei.",plot="wendepunkt"),
 A("y5_s08",27,"Der Raum der Wuensche","November — verborgen im Schloss",
   [P,"harry","luna","neville"],"raum_der_wuensche",
   "Ihr entdeckt einen verborgenen Raum, der sich in genau das verwandelt, was ihr braucht: einen sicheren Uebungsort mit Kissen, Zielscheiben und allem Noetigen. Der perfekte geheime Treffpunkt fuer Dumbledores Armee.",
   [C("Den magischen Raum staunend erkunden",stats={"wisdom":5}),
    C("Beim Einrichten des Uebungsraums helfen",stats={"loyalty":4},rels={"Neville":4}),
    C("Dich auf das erste Training freuen",stats={"reputation":3},rels={"Harry":3})]),
 A("y5_s09",27,"DA-Training: echte Verteidigung","November — Raum der Wuensche",cp=True,
   present=[P,"harry","neville","luna","ginny"],loc="raum_der_wuensche",
   summ="Harry bringt euch echte Schutzzauber bei — und es funktioniert! Neville, sonst so unsicher, gelingt ein Zauber nach dem anderen und er strahlt ueber das ganze Gesicht. Hier seid ihr nicht nur eine Gruppe, sondern eine Familie, die fuereinander einsteht.",
   choices=[C("Voller Eifer mitueben und auch anderen helfen",canon=True,docks=True,stats={"combat":6,"loyalty":5},rels={"Harry":6,"Neville":6,"Luna":4,"Ginny":3}),
    C("Neville zujubeln, der ueber sich hinauswaechst",canon=True,rels={"Neville":8}),
    C("Den Patronus ueben, bis silbernes Licht kommt",canon=True,stats={"combat":5,"wisdom":4})],
   recap="Im Raum der Wuensche uebte Dumbledores Armee echte Verteidigung. Du hast diese Stunde verpasst.",plot="wendepunkt"),
 A("y5_s10",28,"Umbridge wird Grossinquisitorin","Dezember — Grosse Halle",
   [P,"umbridge","mcgonagall"],"grosse_halle",
   "Erlass um Erlass: Umbridge reisst immer mehr Macht an sich und kontrolliert die ganze Schule. Professor McGonagall haelt mit ruhiger Wuerde dagegen. Es wird enger — aber euer heimlicher Zusammenhalt waechst gerade deshalb.",
   [C("McGonagalls stille Staerke bewundern",stats={"wisdom":4},rels={"Mcgonagall":4} if False else {"Harry":2}),
    C("Dich erst recht der DA verbunden fuehlen",stats={"loyalty":5}),
    C("Mut bewahren, auch wenn die Regeln druecken",stats={"combat":4})],plot="wendepunkt"),
 A("y5_s11",28,"Mut im Verborgenen","Januar — Raum der Wuensche",cp=True,
   present=[P,"harry","hermine","ron","luna"],loc="raum_der_wuensche",
   summ="Trotz aller Gefahr trifft sich die DA weiter und uebt. Jeder weiss: Wenn Umbridge sie erwischt, gibt es Aerger. Doch zusammen seid ihr mutig — und das Gefuehl, das Richtige zu tun, schweisst euch enger zusammen als alles andere.",
   choices=[C("Voll dabei sein und die Gruppe staerken",canon=True,docks=True,stats={"loyalty":6,"combat":4},rels={"Harry":5,"Hermine":4,"Ron":4,"Luna":3}),
    C("Wache halten, damit niemand euch erwischt",canon=True,stats={"wisdom":4}),
    C("Den Aengstlicheren Mut zusprechen",canon=True,rels={"Neville":4})],
   recap="Die DA uebte trotz der Gefahr weiter. Du warst diesmal nicht dabei.",plot="wendepunkt"),
 A("y5_s12",28,"Eine beunruhigende Vision","Februar — Gryffindor-Turm",
   [P,"harry","hermine"],"gryffindor_turm",
   "Harry hat seltsame, beunruhigende Traeume — als spuere er etwas Dunkles weit weg im Zaubereiministerium. Er macht sich Sorgen um jemanden, der ihm wichtig ist. Ihr nehmt ihn ernst und beratet, was zu tun ist, ohne unueberlegt zu handeln.",
   [C("Harry ernst nehmen und gemeinsam ueberlegen",stats={"wisdom":5,"loyalty":4},rels={"Harry":5}),
    C("Vorschlagen, einen Erwachsenen einzuweihen",stats={"reputation":4}),
    C("Hermine zustimmen, vorsichtig und klug zu bleiben",rels={"Hermine":4})],plot="wendepunkt"),
 A("y5_s13",29,"Die DA fliegt auf — Dumbledore schuetzt euch","Maerz — Grosse Halle",
   [P,"dumbledore","umbridge","harry"],"grosse_halle",
   "Umbridge kommt der geheimen Gruppe auf die Spur. Um die Schueler zu schuetzen, nimmt Dumbledore die ganze Verantwortung auf sich und verlaesst die Schule — eine noble Geste, damit euch nichts geschieht. Sein ruhiger Blick sagt: 'Haltet zusammen.'",
   [C("Dumbledore dankbar nachblicken, der euch schuetzt",stats={"loyalty":5},rels={"Dumbledore":5}),
    C("Dir schwoeren, die DA und den Zusammenhalt am Leben zu halten",stats={"combat":4,"loyalty":4}),
    C("Harry troesten, der sich Vorwuerfe macht",rels={"Harry":5})],plot="finale"),
 A("y5_s14",29,"Aufbruch zum Ministerium","Juni — Laendereien",cp=True,
   present=[P,"harry","luna","neville","ginny"],loc="ländereien_see",
   summ="Harry ist ueberzeugt, dass Sirius in Gefahr ist. Mutig — vielleicht zu mutig — beschliesst ihr, ihm zu helfen, und reist auf den ruhigen, geheimnisvollen Thestralen zum Ministerium. Ihr geht nicht allein: Freunde stehen zusammen.",
   choices=[C("Fest an Harrys Seite mitgehen",canon=True,docks=True,stats={"combat":5,"loyalty":6},rels={"Harry":6,"Luna":4,"Neville":4,"Ginny":3}),
    C("Vorschlagen, unterwegs doch noch Hilfe zu holen",canon=True,stats={"wisdom":4,"reputation":3}),
    C("Auf die anderen aufpassen, damit alle zusammenbleiben",canon=True,stats={"loyalty":5})],
   recap="Eine mutige Gruppe brach auf, um Harry zu helfen. Du warst diesmal nicht dabei.",plot="finale"),
 A("y5_s15",29,"Die Mysteriumsabteilung","Juni — Zaubereiministerium",
   [P,"harry","neville","luna"],"mysteriumsabteilung",
   "Tief im Ministerium liegt die unheimliche Mysteriumsabteilung mit ihrer hallenden Halle der Prophezeiungen. Hier wird es ernst und gefaehrlich: dunkle Gestalten tauchen auf. Doch ihr steht Ruecken an Ruecken und erinnert euch an alles, was ihr in der DA gelernt habt.",
   [C("Mit dem in der DA Gelernten zusammen standhalten",stats={"combat":6,"loyalty":5},rels={"Harry":4,"Neville":4,"Luna":4}),
    C("Ruhig bleiben und die Juengeren schuetzen",stats={"loyalty":6}),
    C("Nach einem Weg suchen, alle in Sicherheit zu bringen",stats={"wisdom":5})],plot="finale"),
 A("y5_s16",30,"Der Orden kommt zu Hilfe","Juni — Mysteriumsabteilung",cp=True,
   present=[P,"sirius","lupin","harry"],loc="mysteriumsabteilung",
   summ="Im gefaehrlichsten Moment stuermt der Orden herein — Sirius, Lupin und die anderen Erwachsenen kaempfen, um euch zu retten. Endlich seid ihr nicht mehr allein; mutige Verbuendete stehen an eurer Seite gegen die Finsternis.",
   choices=[C("Erleichtert mit dem Orden zusammenstehen",canon=True,docks=True,stats={"loyalty":6,"combat":4},rels={"Sirius":5,"Lupin":4,"Harry":4}),
    C("Tun, was die Erwachsenen sagen, und in Deckung gehen",canon=True,stats={"wisdom":4}),
    C("Den Freunden Mut zurufen",canon=True,rels={"Neville":3,"Luna":3})],
   recap="Der Orden kam den Kindern zu Hilfe. Du hast davon nur gehoert.",plot="finale"),
 A("y5_s17",30,"Ein schwerer Verlust: Sirius","Juni — Mysteriumsabteilung",
   [P,"sirius","harry","lupin"],"mysteriumsabteilung",
   "Im Kampf trifft das Unfassbare ein: Sirius — Harrys Patenonkel, der warmherzige Freund — wird von einer dunklen Hexe getroffen und ist fort. (Erzaehlt mit Trauer und Wuerde, ohne grausige Bilder.) Lupin haelt Harry fest, der vor Schmerz fast zerbricht, und bringt alle Kinder behutsam in Sicherheit.",
   [C("Bei Harry sein und seinen Schmerz teilen",stats={"loyalty":6},rels={"Harry":6}),
    C("Lupin helfen, alle ruhig in Sicherheit zu bringen",stats={"wisdom":4,"loyalty":4},rels={"Lupin":4}),
    C("Selbst um Sirius weinen und ihn in Erinnerung behalten",stats={"loyalty":5},rels={"Sirius":3})],plot="finale"),
 A("y5_s18",30,"Dumbledores Wahrheit","Juni — Dumbledores Buero",
   [P,"dumbledore","harry"],"schulleiterbuero",
   "Zurueck in Hogwarts nimmt Dumbledore Harry behutsam beiseite und erzaehlt ihm endlich die ganze Wahrheit ueber die Prophezeiung — und ueber die schwere Last, die Harry traegt. Es ist traurig, aber auch ein Trost: Niemand muss seinen Weg allein gehen. Und die ganze Welt weiss nun: Die Finsternis ist zurueck.",
   [C("Harry zur Seite stehen, als er die Wahrheit hoert",stats={"loyalty":6},rels={"Harry":5}),
    C("Aus Dumbledores ruhigen Worten Kraft schoepfen",stats={"wisdom":5},rels={"Dumbledore":4}),
    C("Erleichtert sein, dass nun alle die Gefahr ernst nehmen",stats={"reputation":3})],plot="wendepunkt"),
 A("y5_s19",30,"Schuljahresende Jahr 5","Juni — Abschluss",
   [P,"lily","harry","ron","hermine","luna","ginny","neville"],"grosse_halle",
   "Das Jahr endet ernst, aber nicht ohne Hoffnung. Im Gedenken an Sirius rueckt ihr enger zusammen — Dumbledores Armee ist zu einer echten Familie geworden, die fuereinander einsteht. Was auch kommt: Ihr seid bereit, gemeinsam.",
   [C("Im Gedenken an Sirius fest zusammenhalten",stats={"loyalty":6},rels={"Harry":4,"Luna":3,"Neville":3}),
    C("Aus der Freundschaft der DA Mut schoepfen",rels={"Hermine":3,"Ron":3,"Ginny":3}),
    C("Mit Zuversicht nach vorn schauen",stats={"wisdom":4,"reputation":3})],plot="ausklang"),
]
for b in backbone: b["chapter"]=int(b["chapter"])
# kleine Korrektur: y5_s10 erste Wahl hatte einen unsauberen rels-Ausdruck
backbone[9]["choices"][0]=C("McGonagalls stille Staerke bewundern",stats={"wisdom":4})

SUBJ=[("Verteidigung (nur Theorie bei Umbridge)","klassenzimmer",["umbridge","hermine"],
       "Bei Umbridge wird wieder nur trocken aus dem Buch gelesen — kein echter Zauber. Du nimmst dir heimlich vor, das Wichtige woanders zu lernen."),
 ("Zauberkunst","klassenzimmer",["flitwick","hermine"],
  "Professor Flitwick huepft vor Begeisterung ueber einen neuen Zauber. Hermine kann ihn natuerlich schon."),
 ("Kraeuterkunde","gewaechshaeuser",["sprout","neville"],
  "Professor Sprout zeigt eine zickige Pflanze. Neville glaenzt hier wie immer."),
 ("Verwandlung","klassenzimmer",["mcgonagall","ron"],
  "Professor McGonagall ist diesen Strenge-Jahr ein Fels in der Brandung. Heute uebt ihr etwas Kniffliges."),
 ("Pflege magischer Geschoepfe","pflege_gehege",["hagrid"],
  "Hagrid stellt ein scheues Geschoepf vor — die ruhigen Thestrale. Hoeflich bleiben, dann sind sie ganz sanft."),
 ("Wahrsagen","wahrsageturm",["trelawney","ron"],
  "Professor Trelawney raunt von dunklen Zeichen. Diesmal hat man fast das Gefuehl, ein Koernchen Wahrheit ist dabei.")]
def subj(i):
    n,loc,pr,s=SUBJ[i%len(SUBJ)]
    return (f"Unterricht: {n}","schule",loc,[P]+pr,s,[C("Konzentrieren und meistern",stats={"wisdom":6}),
      C("Einem Mitschueler helfen",stats={"loyalty":5},rels={"Neville":5}),C("Heimlich Wichtigeres ueben",canon=False,stats={"combat":4})])
MEAL=["Beim Fruehstueck tuscheln alle ueber Umbridges neueste Erlasse.","Mittagessen — leise wird ueber die geheime Gruppe geredet, mit einem Augenzwinkern.",
 "Abendessen; trotz allem sorgen die Freunde fuereinander fuer gute Laune.","Warme Schokolade nach einem harten Tag — Zusammenhalt schmeckt am besten."]
def meal(i): return ("In der Grossen Halle","alltag","grosse_halle",[P,"lily","luna"],MEAL[i%len(MEAL)],
  [C("Zu den Freunden setzen",stats={"reputation":4},rels={"Lily":3}),C("Luna an euren Tisch holen",rels={"Luna":4}),C("In Ruhe geniessen",stats={"loyalty":3})])
COMMON=["Am Kamin uebt die DA heimlich Handzeichen und Zauberspruch-Bewegungen.","Hausaufgaben-Chaos und leises Planen des naechsten Treffens.",
 "Gemuetlicher Abend; Luna erzaehlt von wundersamen Wesen, an die nur sie glaubt.","Ron baut sein Zauberschach auf und sucht einen Gegner."]
def common(i): return ("Abend im Gemeinschaftsraum","alltag","gryffindor_turm",[P,"lily","ron","harry"],COMMON[i%len(COMMON)],
  [C("Mitmachen und abhaengen",stats={"loyalty":4},rels={"Ron":3}),C("Mit Lily quatschen",rels={"Lily":4}),C("Frueh ins Bett",canon=False,stats={"wisdom":2})])
GROUND=["Auf den Laendereien begegnet ihr den ruhigen, geheimnisvollen Thestralen.","Hagrid winkt zu seiner Huette; Kakao und eine Tiergeschichte warten.",
 "Spaziergang am See; Flocke flitzt froehlich voraus.","Am Ufer haelt Luna nach unsichtbaren Wesen Ausschau und lacht herzlich."]
def ground(i): return ("Auf den Laendereien","alltag","ländereien_see",[P,"hagrid","flocke"],GROUND[i%len(GROUND)],
  [C("Hagrid besuchen",rels={"Hagrid":5}),C("Mit Flocke toben",rels={"Flocke":5}),C("Mit Luna die Natur geniessen",rels={"Luna":4})])
def owl(i): return ("In der Eulerei","alltag","eulerei",[P,"flocke"],
  ["Du schreibst nach Hause, dass ihr zusammenhaltet.","Du fragst nach Neuigkeiten von zu Hause.","Deine Lieblingseule schuhut erwartungsvoll."][i%3],
  [C("Nach Hause schreiben",stats={"loyalty":6},rels={"Mama":4,"Papa":4}),C("Auf Antwort hoffen",rels={"Mama":3,"Papa":3}),C("Der Eule einen Keks geben",stats={"reputation":2})])
def room(i): return ("Stille Stunde im Raum der Wuensche","alltag","raum_der_wuensche",[P,"neville","luna"],
  ["Allein uebst du im Raum der Wuensche einen Zauber, bis er sitzt.","Du hilfst Neville, der heimlich weiter trainiert.","Der Raum gibt dir genau, was du zum Ueben brauchst."][i%3],
  [C("Fleissig einen Schutzzauber ueben",stats={"combat":5,"wisdom":3}),C("Neville beim Ueben helfen",rels={"Neville":5}),C("Mit Luna eine ruhige Pause machen",rels={"Luna":4})])
XPOOL=[("da","DA-Training","raum_der_wuensche",["harry","neville","luna","ginny"],
        "Im Raum der Wuensche uebt ihr zusammen echte Verteidigung — und werdet als Gruppe immer enger.",{"Harry":6,"Neville":5,"Luna":4,"Ginny":3},
        "Die DA uebte wieder gemeinsam. Du hast die Stunde verpasst."),
 ("luna","Zeit mit Luna","ländereien_see",["luna"],
   "Mit Luna die Welt mit anderen Augen sehen — ehrlich, ruhig und voller unerwarteter Weisheit.",{"Luna":10},
   "Luna verbrachte Zeit mit ein paar Freunden. Diesmal nicht mit dir."),
 ("gang","Abend mit der Gang","gryffindor_turm",["harry","ron","hermine"],
   "Die ganze Runde sitzt zusammen, lacht und haelt fest zusammen.",{"Harry":6,"Ron":6,"Hermine":5},
   "Ein Kaminabend schweisste die Gang enger zusammen. Du warst woanders."),
 ("neville","Neville staerken","raum_der_wuensche",["neville"],
   "Neville waechst ueber sich hinaus; du uebst mit ihm, bis er strahlt und an sich glaubt.",{"Neville":10,"Harry":3},
   "Jemand staerkte Neville beim Ueben. Diesmal nicht du."),
 ("hermine","Lernen mit Hermine","bibliothek",["hermine"],
   "Hermine teilt geduldig ihr Wissen, bis bei dir der Knoten platzt.",{"Hermine":10},
   "Hermine half einer Lerngruppe. Du hast allein gelernt."),
 ("ginny","Mut mit Ginny","innenhof",["ginny"],
   "Ginny ist mutiger geworden; ihr stuetzt euch gegenseitig und lacht trotz der schweren Zeiten.",{"Ginny":9},
   "Ginny verbrachte Zeit mit Freunden. Diesmal nicht mit dir."),
 ("hagrid","Kakao bei Hagrid","hagrids_huette",["hagrid"],
   "Bei heissem Kakao erzaehlt Hagrid von seinen Tieren und passt herzlich auf.",{"Hagrid":8},
   "Hagrid hatte Besuch zum Kakao. Du warst nicht dabei.")]
def x(i):
    k,t,loc,pr,s,rels,recap=XPOOL[i%len(XPOOL)]
    return (t,"wendepunkt",loc,[P]+pr,s,[C("Voll dabei sein und mitmachen",canon=True,docks=True,stats={"loyalty":6,"reputation":3},rels=dict(rels)),
       C("Eine Weile zuschauen und geniessen",canon=True,stats={"wisdom":3},rels={list(rels)[0]:3}),
       C("Diesmal fuer dich bleiben",canon=False,stats={"wisdom":2})],recap)
def mk(t,month,chap,cross=False):
    if cross:
        title,ptype,loc,pr,s,choices,recap=t
        return {"id":wid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 5 - {month})","school_time":f"{month} (Jahr 5) - Schulalltag",
                "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":3,
                "crossing_point":True,"clique_bond_delta":1,"autonomous_recap":recap,"choices":choices,"next_scenes":[]}
    title,ptype,loc,pr,s,choices=t
    return {"id":wid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 5 - {month})","school_time":f"{month} (Jahr 5) - Schulalltag",
            "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":2,
            "crossing_point":False,"choices":choices,"next_scenes":[]}
GAPS=[("y5_s03",18,"September",25),("y5_s06",20,"Oktober",26),("y5_s09",24,"November",27),
      ("y5_s12",24,"Januar",28),("y5_s15",14,"Mai",29)]
cats=["subj","meal","common","ground","owl","room","subj","common"]
gi=xi=ci=0; gapblocks={}
for aid,n,month,chap in GAPS:
    block=[]
    for k in range(n):
        if k%2==1: block.append(mk(x(xi),month,chap,cross=True)); xi+=1
        else:
            cat=cats[ci%len(cats)]; ci+=1
            f={"subj":subj,"meal":meal,"common":common,"ground":ground,"owl":owl,"room":room}[cat](gi); gi+=1
            block.append(mk(f,month,chap,cross=False))
    gapblocks[aid]=block
y5=[]
for a in backbone:
    y5.append(a)
    if a["id"] in gapblocks: y5.extend(gapblocks[a["id"]])
allscenes=existing+y5
for i,s in enumerate(allscenes): s["next_scenes"]=[allscenes[i+1]["id"]] if i+1<len(allscenes) else []
data["scenes"]=allscenes
json.dump(data,open(os.path.join(BOOK,"plot_graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
cross=[s for s in allscenes if s.get("crossing_point")]
print("Gesamt:",len(allscenes),"| Jahr 5:",len(y5),"| Kreuzungen:",len(cross))
print("y4_s19.next:",next(s for s in allscenes if s["id"]=="y4_s19")["next_scenes"])
print("ohne recap:",[s["id"] for s in allscenes if s.get("crossing_point") and not s.get("autonomous_recap")] or "keine")
ids={s["id"] for s in allscenes}
print("kaputte Verweise:",[s["id"] for s in allscenes if s["next_scenes"] and s["next_scenes"][0] not in ids] or "keine")
