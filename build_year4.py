#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahr 4 — 'Der Feuerkelch' (kindgerecht) als NAHTLOSE Fortsetzung. Haengt hinter y3_s18 an.

Kindgerecht-Umbau des duesteren Originals:
 - Die Turnier-Aufgaben sind spannende, GEFAHRLOSE Wettbewerbe: der Drache wird NICHT
   verletzt (nur clever umflogen), die See-Aufgabe ist eine Rettung (alle sind sicher),
   das Labyrinth ist ein Raetselspass mit wachenden Lehrern.
 - Weihnachtsball = froehliches FREUNDSCHAFTSfest (keine Romantik-Schiene).
 - Auslaendische Schueler (Cedric, Fleur, Krum) sind nett; Fairness und Zusammenhalt siegen.
 - KEIN Tod, KEIN Horror: Cedric ueberlebt; statt Schrecken nur ein angedeuteter 'Schatten',
   den die Erwachsenen abschirmen ('Wir passen auf euch auf').
Moderation + SKILL.md-Ton gelten.  Aufruf: python3 build_year4.py
"""
import json, os, itertools
HERE=os.path.dirname(os.path.abspath(__file__)); BOOK=os.path.join(HERE,"skill","data","books","hogwarts")
data=json.load(open(os.path.join(BOOK,"plot_graph.json"),encoding="utf-8")); existing=data["scenes"]
if any(s["id"].startswith("y4_") for s in existing): raise SystemExit("Jahr 4 existiert bereits.")
_c=itertools.count(1)
def vid(): return f"v{next(_c):03d}"
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
 A("y4_s01",19,"Die Quidditch-Weltmeisterschaft","Sommerferien — grosses Spiel",
   [P,"ron","hermine","harry","ginny"],"turnier_arena",
   "Was fuer ein Spektakel: In einem riesigen Stadion fiebert ihr beim Quidditch-WM-Finale mit, Feuerwerk faerbt den Himmel, und Wimpel wehen in allen Farben. Ein unvergesslicher Ferienauftakt mit den Freunden.",
   [C("Mit der ganzen Gang lautstark mitfiebern",stats={"reputation":5},rels={"Ron":4,"Harry":3}),
    C("Das Feuerwerk und die Stimmung in dich aufsaugen",stats={"wisdom":4}),
    C("Souvenirs fuer alle besorgen",rels={"Ginny":4,"Hermine":3})]),
 A("y4_s02",19,"Das Trimagische Turnier wird angekuendigt","1. September — Grosse Halle",
   [P,"dumbledore","lily","fleur","krum"],"grosse_halle",
   "Dumbledore verkuendet eine Sensation: das Trimagische Turnier! Zwei weitere Zauberschulen sind zu Gast — die elegante Beauxbatons-Kutsche und das Durmstrang-Schiff. Ploetzlich wimmelt es von neuen Gesichtern aus aller Welt.",
   [C("Die Gaeste aus den anderen Schulen neugierig begruessen",stats={"reputation":4},rels={"Fleur":4}),
    C("Mit Lily ueber das aufregende Turnier reden",rels={"Lily":4}),
    C("Dich fragen, wer wohl Champion wird",stats={"wisdom":3})],plot="wendepunkt"),
 A("y4_s03",19,"Der Feuerkelch waehlt die Champions","Oktober — Grosse Halle",
   [P,"dumbledore","cedric","fleur","krum","harry"],"grosse_halle",
   "Der Feuerkelch spuckt die Namen der Champions: Cedric Diggory, Fleur Delacour, Viktor Krum — und voellig ueberraschend auch Harry! Niemand versteht ganz, wie, aber die Freunde stehen sofort hinter ihm.",
   [C("Harry zur Seite springen und ihm Mut machen",stats={"loyalty":6},rels={"Harry":6}),
    C("Cedric fair zum Champion gratulieren",rels={"Cedric":5}),
    C("Mit Hermine ueberlegen, wie das passieren konnte",stats={"wisdom":4})],plot="wendepunkt"),
 A("y4_s04",20,"Professor Moodys erste Stunde","Oktober — Verteidigung gegen die dunklen Kuenste",
   [P,"moody","neville"],"klassenzimmer",
   "Der neue Lehrer Professor Moody ist rau und hat ein magisches Auge, das alles sieht. 'Immer wachsam!', brummt er — aber hinter der knurrigen Schale steckt jemand, der scharf auf seine Schueler aufpasst. Neville taut bei ihm sogar auf.",
   [C("Aufmerksam zuhoeren und dir 'immer wachsam' merken",stats={"wisdom":6}),
    C("Neville beistehen, der noch ein bisschen nervoes ist",stats={"loyalty":5},rels={"Neville":6}),
    C("Mutig eine Frage stellen",stats={"combat":3},rels={"Moody":4})]),
 A("y4_s05",20,"Harry fuer die erste Aufgabe vorbereiten","November — Laendereien",cp=True,
   present=[P,"harry","hermine","ron"],loc="ländereien_see",
   summ="Die erste Aufgabe steht bevor, und Harry ist nervoes. Die ganze Gang hilft ihm trainieren: Beschwoerungszauber ueben, Plaene schmieden, Mut zusprechen. Zusammen ist die Angst nur halb so gross.",
   choices=[C("Voll beim Training mitmachen und Harry staerken",canon=True,docks=True,stats={"loyalty":6,"wisdom":4},rels={"Harry":8,"Hermine":4,"Ron":4}),
    C("Kluge Tipps aus der Bibliothek beisteuern",canon=True,stats={"wisdom":5},rels={"Hermine":4}),
    C("Diesmal nur Daumen druecken",canon=False,stats={"wisdom":2})],
   recap="Die Gang half Harry, sich auf die erste Aufgabe vorzubereiten. Du warst diesmal nicht dabei.",plot="wendepunkt"),
 A("y4_s06",20,"Erste Aufgabe: der goldene Eier-Drache","November — Turnier-Arena",
   [P,"harry","cedric","hagrid","ginny"],"turnier_arena",
   "In der Arena bewacht eine grosse Drachenmutter ein goldenes Ei. Die Aufgabe: das Ei holen, OHNE dem Drachen etwas zu tun. Geschickt und auf seinem Besen umfliegt Harry das Tier, lenkt es sanft ab — und schnappt sich das Ei. Alle (auch der Drache) bleiben heil. Riesenjubel!",
   [C("Harry von der Tribuene anfeuern, bis du heiser bist",stats={"reputation":5},rels={"Harry":5}),
    C("Mitfiebern und erleichtert sein, dass dem Drachen nichts passiert",stats={"loyalty":4}),
    C("Cedric fair zujubeln, der seine Aufgabe auch meistert",rels={"Cedric":5})],plot="abenteuer"),
 A("y4_s07",21,"Vorfreude auf den Weihnachtsball","Dezember — Gryffindor-Turm",cp=True,
   present=[P,"lily","ginny","ron"],loc="gryffindor_turm",
   summ="Hogwarts steht Kopf: Es gibt einen Weihnachtsball! Festumhaenge werden ausgepackt, Tanzschritte geuebt (mit viel Gekicher), und alle ueberlegen, mit welchen FREUNDEN sie hingehen. Pure festliche Aufregung.",
   choices=[C("Mit deinen Freundinnen zusammen hingehen und euch fein machen",canon=True,docks=True,stats={"reputation":5,"loyalty":4},rels={"Lily":5,"Ginny":5}),
    C("Ron Mut machen, der vor dem Tanzen Bammel hat",canon=True,rels={"Ron":5}),
    C("In Ruhe ein Festoutfit aussuchen",canon=False,stats={"wisdom":2})],
   recap="Vor dem Ball herrschte aufgeregte Vorfreude im Turm. Du warst diesmal nicht in der Runde.",plot="ruhe"),
 A("y4_s08",21,"Der Weihnachtsball","Dezember — festliche Grosse Halle",
   [P,"lily","cedric","harry","ron","hermine","krum"],"grosse_halle",
   "Die Grosse Halle glitzert in Eis und Kerzenlicht, eine Zauberband spielt, und alle tanzen und lachen. Selbst der wortkarge Krum taut auf, Cedric strahlt, und Flocke bekommt eine festliche Schleife. Ein Maerchenabend voller Freundschaft.",
   [C("Mit deinen Freunden ausgelassen tanzen",canon=True,docks=True,stats={"reputation":6,"loyalty":4},rels={"Lily":4,"Harry":3,"Ron":3,"Hermine":3}),
    C("Mit Krum und Fleur ins Gespraech kommen",canon=True,rels={"Krum":5,"Fleur":4}),
    C("Den festlichen Abend einfach geniessen",canon=True,stats={"wisdom":3})],
   cp=True,recap="Der Weihnachtsball war ein Maerchenabend voller Tanz und Lachen. Du hast ihn diesmal verpasst.",plot="ruhe"),
 A("y4_s09",21,"Das Raetsel des goldenen Eis","Januar — Myrtes Waschraum",
   [P,"harry","hermine","myrte"],"verwunschenes_klo",
   "Das goldene Ei kreischt nur — bis Myrte kichernd verraet: unter Wasser singt es! Tatsaechlich, eingetaucht wird das Kreischen zu einer geheimnisvollen Botschaft ueber die naechste Aufgabe. Ein kniffliges Raetsel zum Knacken.",
   [C("Mit Harry und Hermine die Botschaft entschluesseln",stats={"wisdom":6},rels={"Harry":4,"Hermine":4}),
    C("Myrte fuer den Tipp danken",rels={"Hermine":2}),
    C("Ueberlegen, was 'unter Wasser' fuer die Aufgabe bedeutet",stats={"wisdom":5})],plot="wendepunkt"),
 A("y4_s10",22,"Vorbereitung auf die See-Aufgabe","Januar — Bibliothek",cp=True,
   present=[P,"hermine","neville","ron"],loc="bibliothek",
   summ="Die zweite Aufgabe spielt tief im See. In der Bibliothek waelzt ihr Buecher nach einem Weg, unter Wasser zu atmen — und Neville kennt sich mit Wasserpflanzen wie Kiemenkraut bestens aus!",
   choices=[C("Gemeinsam recherchieren und Nevilles Pflanzen-Wissen nutzen",canon=True,docks=True,stats={"wisdom":6,"loyalty":4},rels={"Hermine":5,"Neville":6,"Ron":3}),
    C("Einen klugen Plan fuer Harry ausarbeiten",canon=True,stats={"wisdom":5}),
    C("Eine kurze Pause an der frischen Luft machen",canon=False,stats={"wisdom":2})],
   recap="In der Bibliothek tueftelte die Gruppe an einem Weg unter Wasser. Du warst nicht dabei.",plot="schule"),
 A("y4_s11",22,"Zweite Aufgabe: Rettung im See","Februar — Laendereien am See",
   [P,"harry","cedric","fleur","krum","hagrid"],"ländereien_see",
   "Tief im See warten Freunde der Champions, sicher und verzaubert schlafend, darauf, geholt zu werden. Mit Kiemenkraut taucht Harry hinab — und bringt nicht nur seinen, sondern hilfsbereit auch einen anderen sicher nach oben. Alle kommen wohlbehalten an Land. Fairness vor Sieg!",
   [C("Erleichtert jubeln, als alle sicher auftauchen",stats={"reputation":4,"loyalty":4},rels={"Harry":5}),
    C("Harrys Hilfsbereitschaft bewundern",rels={"Harry":4,"Cedric":3}),
    C("Den durchgefrorenen Schwimmern Decken und Schokolade bringen",stats={"loyalty":5})],plot="abenteuer"),
 A("y4_s12",22,"Sportsgeist: zusammen feiern","Februar — Grosse Halle",cp=True,
   present=[P,"cedric","harry","ron","hermine"],loc="grosse_halle",
   summ="Nach der Aufgabe feiern alle gemeinsam — auch ueber die Schulgrenzen hinweg. Cedric und Harry klopfen sich anerkennend auf die Schulter: Hier gewinnt nicht nur, wer schnell ist, sondern wer fair und hilfsbereit bleibt.",
   choices=[C("Mit allen Champions und Freunden anstossen (mit Kuerbissaft!)",canon=True,docks=True,stats={"reputation":5,"loyalty":4},rels={"Cedric":5,"Harry":4,"Ron":3,"Hermine":3}),
    C("Cedric fuer seinen fairen Sportsgeist loben",canon=True,rels={"Cedric":5}),
    C("Den Abend ruhig ausklingen lassen",canon=False,stats={"wisdom":2})],
   recap="Champions und Freunde feierten gemeinsam den Sportsgeist. Du warst diesmal nicht dabei.",plot="ruhe"),
 A("y4_s13",23,"Freundschaft ueber Schulgrenzen","Maerz — Innenhof",
   [P,"fleur","krum","cedric"],"innenhof",
   "Im Innenhof kommt ihr mit den Gaesten ins Plaudern: Fleur erzaehlt von Beauxbatons, Krum zeigt schuechtern einen Quidditch-Trick, Cedric lacht herzlich. Aus Rivalen werden Freunde — die Welt ist groesser und freundlicher, als man dachte.",
   [C("Neugierig nach ihren Schulen und Laendern fragen",stats={"wisdom":5},rels={"Fleur":5,"Krum":4}),
    C("Krum einen Quidditch-Trick abschauen",rels={"Krum":5}),
    C("Cedric als Vorbild fuer Fairness bewundern",rels={"Cedric":5})]),
 A("y4_s14",23,"Moodys Warnung","Maerz — Klassenzimmer",
   [P,"moody","dumbledore"],"klassenzimmer",
   "Etwas liegt in der Luft dieses Jahr — Moody mahnt mit seinem 'Immer wachsam!' zur Vorsicht, und Dumbledore versichert ruhig: Was auch kommt, die Lehrer passen auf jeden einzelnen Schueler auf. Geheimnisvoll, aber sicher.",
   [C("Moodys Rat ernst nehmen und aufmerksam bleiben",stats={"wisdom":5},rels={"Moody":4}),
    C("Dumbledores beruhigenden Worten vertrauen",stats={"loyalty":4}),
    C("Vorschlagen, gut aufeinander aufzupassen",stats={"loyalty":5})],plot="wendepunkt"),
 A("y4_s15",23,"Harry fuers Labyrinth staerken","Mai — Gryffindor-Turm",cp=True,
   present=[P,"harry","ron","hermine","lily","ginny"],loc="gryffindor_turm",
   summ="Die letzte Aufgabe — das grosse Labyrinth — steht bevor. Die ganze Gang uebt mit Harry Schutz- und Hilfszauber und schmiedet einen Mutmach-Plan. Was auch im Labyrinth wartet, er geht nicht allein hinein.",
   choices=[C("Voll mitmachen und Harry den Ruecken staerken",canon=True,docks=True,stats={"loyalty":6,"combat":4},rels={"Harry":6,"Ron":4,"Hermine":4,"Lily":3}),
    C("Mit Hermine die besten Zauber heraussuchen",canon=True,rels={"Hermine":4}),
    C("Eine ruhige Runde fuer dich brauchen",canon=False,stats={"wisdom":2})],
   recap="Die Gang staerkte Harry fuer das Labyrinth. Du warst diesmal nicht dabei.",plot="finale"),
 A("y4_s16",24,"Dritte Aufgabe: das Labyrinth","Juni — das Turnier-Labyrinth",
   [P,"harry","cedric","fleur","krum"],"labyrinth",
   "Das riesige Heckenlabyrinth steckt voller kniffliger, fairer Raetsel — eine sprechende Sphinx, neckische Nebelhecken, freundliche Zauber-Hindernisse. Die Champions helfen einander sogar, statt sich auszustechen. Lehrer wachen am Rand und greifen ein, wenn jemand Hilfe braucht.",
   [C("Mitfiebern, wie Harry und Cedric sich gegenseitig helfen",stats={"reputation":5,"loyalty":4},rels={"Harry":4,"Cedric":4}),
    C("Klug das Sphinx-Raetsel mitdenken",stats={"wisdom":6}),
    C("Hoffen, dass alle sicher durchkommen",stats={"loyalty":4})],plot="finale"),
 A("y4_s17",24,"Fairness siegt: gemeinsam zum Ziel","Juni — Turnier-Labyrinth",
   present=[P,"harry","cedric","dumbledore"],loc="labyrinth",
   summ="Im Herzen des Labyrinths erreichen Harry und Cedric den Pokal — und entscheiden sich, ihn GEMEINSAM zu nehmen, als Zeichen echter Freundschaft. Ein Schatten versucht sich einzumischen, doch Dumbledore und die Lehrer sind sofort zur Stelle und sorgen dafuer, dass beide voellig sicher sind.",
   choices=[C("Den gemeinsamen, fairen Sieg von Harry und Cedric bejubeln",canon=True,docks=True,stats={"reputation":6,"loyalty":6},rels={"Harry":6,"Cedric":6}),
    C("Erleichtert sein, dass die Lehrer alle beschuetzen",canon=True,rels={"Dumbledore":4}),
    C("Stolz auf den Sportsgeist aller Champions sein",canon=True,stats={"loyalty":4})],
   cp=True,recap="Harry und Cedric teilten sich den Sieg, und die Lehrer hielten alle sicher. Du hast es nur nacherzaehlt bekommen.",plot="finale"),
 A("y4_s18",24,"Ein Schatten am Horizont — aber wir halten zusammen","Juni — Grosse Halle",
   [P,"dumbledore","mcgonagall","harry"],"grosse_halle",
   "Dumbledore spricht ernst, aber warm: Vielleicht kommen unruhigere Zeiten. Doch er verspricht allen: 'Solange wir zusammenhalten und fuereinander da sind, hat die Truebsal keine Chance. Und wir Erwachsenen passen auf euch auf.' Mut und Geborgenheit statt Angst.",
   [C("Dir das Versprechen zu Herzen nehmen: Zusammen sind wir stark",stats={"loyalty":6},rels={"Dumbledore":4}),
    C("Dir vornehmen, immer fuereinander da zu sein",stats={"loyalty":5},rels={"Harry":3}),
    C("Ruhig und zuversichtlich nach vorn schauen",stats={"wisdom":4})],plot="wendepunkt"),
 A("y4_s19",24,"Schuljahresende Jahr 4","Juni — Abschlussfest",
   [P,"lily","harry","ron","hermine","cedric","fleur","krum"],"grosse_halle",
   "Zum Abschluss feiern alle drei Schulen gemeinsam — ein Fest der Freundschaft ueber alle Grenzen. Ihr verabschiedet die neuen Freunde aus Beauxbatons und Durmstrang mit Umarmungen und Versprechen, in Kontakt zu bleiben. Ein aufregendes viertes Jahr geht warm zu Ende.",
   [C("Mit allen — auch den Gaesten — das grosse Fest feiern",rels={"Cedric":3,"Fleur":3,"Krum":3}),
    C("Adressen tauschen und versprechen zu schreiben",stats={"loyalty":5},rels={"Lily":3}),
    C("Dich aufs naechste Jahr freuen",stats={"reputation":4})],plot="ausklang"),
]
for b in backbone: b["chapter"]=int(b["chapter"])

SUBJ=[("Verteidigung gegen die dunklen Kuenste","klassenzimmer",["moody","neville"],
       "Professor Moody bellt 'Immer wachsam!' und uebt mit euch, aufmerksam und mutig zu bleiben. Sogar Neville waechst ueber sich hinaus."),
 ("Zauberkunst","klassenzimmer",["flitwick","hermine"],
  "Professor Flitwick huepft vor Begeisterung, als ein neuer Zauber gelingt. Hermine hat ihn natuerlich schon perfekt."),
 ("Kraeuterkunde","gewaechshaeuser",["sprout","neville"],
  "Professor Sprout zeigt eine Pflanze, die unter Wasser atmet — praktisch fuers Turnier! Neville glaenzt."),
 ("Pflege magischer Geschoepfe","pflege_gehege",["hagrid"],
  "Hagrid stellt stolz ein neues Geschoepf vor. Hoeflich und ruhig bleiben — dann wird's ein Freund."),
 ("Verwandlung","klassenzimmer",["mcgonagall","ron"],
  "Professor McGonagall verwandelt einen Igel in ein Nadelkissen. Heute seid ihr dran — Ron seufzt.")]
def subj(i):
    n,loc,pr,s=SUBJ[i%len(SUBJ)]
    return (f"Unterricht: {n}","schule",loc,[P]+pr,s,[C("Konzentrieren und meistern",stats={"wisdom":6}),
      C("Einem Mitschueler helfen",stats={"loyalty":5},rels={"Neville":5}),C("Mutig Neues probieren",canon=False,stats={"combat":4})])
MEAL=["Beim Fruehstueck tuscheln alle ueber das Turnier und die Gaeste aus dem Ausland.",
 "Mittagessen — am Beauxbatons- und Durmstrang-Tisch gibt es fremde Leckereien zu bestaunen.",
 "Abendessen mit Festtagsstimmung; alle freuen sich auf den Weihnachtsball.",
 "Kuerbissaft und Kuchen, waehrend die Champions getuschelt bewundert werden."]
def meal(i): return ("In der Grossen Halle","alltag","grosse_halle",[P,"lily","ron"],MEAL[i%len(MEAL)],
  [C("Zu den Freunden setzen",stats={"reputation":4},rels={"Lily":3}),C("In Ruhe geniessen",stats={"loyalty":3}),C("Mit den Gaesten plaudern",rels={"Fleur":3})])
COMMON=["Am Kamin baut Ron sein Zauberschach auf.","Alle ueben kichernd Tanzschritte fuer den Ball.",
 "Hausaufgaben-Chaos und Geruechte, wie Harry wohl in das Turnier geraten ist.","Gemuetlicher Abend mit Geschichten ueber die anderen Schulen."]
def common(i): return ("Abend im Gemeinschaftsraum","alltag","gryffindor_turm",[P,"lily","ron","harry"],COMMON[i%len(COMMON)],
  [C("Mitmachen und abhaengen",stats={"loyalty":4},rels={"Ron":3}),C("Mit Lily quatschen",rels={"Lily":4}),C("Frueh ins Bett",canon=False,stats={"wisdom":2})])
GROUND=["Auf den Laendereien staunt ihr ueber die Beauxbatons-Kutsche und das Durmstrang-Schiff.",
 "Hagrid winkt zu seiner Huette; Kakao und eine neue Tiergeschichte warten.","Spaziergang am See; Flocke flitzt froehlich voraus.","Am Ufer ueben Schueler Zauber fuer das Turnier."]
def ground(i): return ("Auf den Laendereien","alltag","ländereien_see",[P,"hagrid","flocke"],GROUND[i%len(GROUND)],
  [C("Hagrid besuchen",rels={"Hagrid":5}),C("Mit Flocke toben",rels={"Flocke":5}),C("Frische Luft geniessen",stats={"loyalty":3})])
def owl(i): return ("In der Eulerei","alltag","eulerei",[P,"flocke"],
  ["Du schreibst nach Hause vom aufregenden Turnier.","Du fragst nach Neuigkeiten von zu Hause.","Deine Lieblingseule schuhut erwartungsvoll."][i%3],
  [C("Nach Hause schreiben",stats={"loyalty":6},rels={"Mama":4,"Papa":4}),C("Auf Antwort hoffen",rels={"Mama":3,"Papa":3}),C("Der Eule einen Keks geben",stats={"reputation":2})])
def arena(i): return ("Trubel um das Turnier","alltag","turnier_arena",[P,"cedric","ginny"],
  ["Auf den Tribuenen wird schon fuer die naechste Aufgabe geprobt und geflaggt.","Die Champions trainieren; ihr schaut bewundernd zu.","Ueberall haengen Wimpel der drei Schulen."][i%3],
  [C("Den Champions zujubeln",stats={"reputation":4},rels={"Cedric":3}),C("Mit Ginny mitfiebern",rels={"Ginny":4}),C("Die Turnier-Stimmung geniessen",stats={"wisdom":3})])
XPOOL=[("gang","Abend mit der Gang","gryffindor_turm",["lily","harry","ron","hermine"],
        "Die ganze Runde sitzt zusammen, lacht und haelt fest zusammen.",{"Harry":6,"Ron":6,"Hermine":5},
        "Ein langer Kaminabend schweisste die Gang enger zusammen. Du warst woanders."),
 ("cedric","Zeit mit Cedric","innenhof",["cedric"],
   "Der freundliche Cedric nimmt sich Zeit, gibt dir faire Tipps und lacht herzlich.",{"Cedric":10},
   "Cedric verbrachte Zeit mit ein paar Schuelern. Diesmal warst du nicht dabei."),
 ("gaeste","Mit den Gaesten anfreunden","innenhof",["fleur","krum"],
   "Du kommst mit Fleur und Krum ins Gespraech — aus Fremden werden neue Freunde aus aller Welt.",{"Fleur":7,"Krum":7},
   "Einige freundeten sich mit den Gaesten an. Du hast die Gelegenheit verpasst."),
 ("hermine","Lernen mit Hermine","bibliothek",["hermine"],
   "Hermine teilt geduldig ihr Wissen, bis bei dir der Knoten platzt.",{"Hermine":10},
   "Hermine half einer Lerngruppe. Du hast allein gelernt."),
 ("ball","Tanzschritte ueben","gryffindor_turm",["lily","ginny"],
   "Mit viel Gekicher uebt ihr fuer den Weihnachtsball Tanzschritte — Spass pur.",{"Lily":6,"Ginny":5},
   "Im Turm wurde fuer den Ball geuebt. Du warst diesmal nicht dabei."),
 ("neville","Neville beistehen","gewaechshaeuser",["neville","sprout"],
   "Neville droht der Mut zu verlassen; du bleibst an seiner Seite, bis er strahlt.",{"Neville":10,"Harry":3},
   "Jemand stand Neville bei. Diesmal nicht du."),
 ("hagrid","Kakao bei Hagrid","hagrids_huette",["hagrid"],
   "Bei heissem Kakao erzaehlt Hagrid von magischen Tieren und passt herzlich auf.",{"Hagrid":8},
   "Hagrid hatte Besuch zum Kakao. Du warst nicht dabei.")]
def x(i):
    k,t,loc,pr,s,rels,recap=XPOOL[i%len(XPOOL)]
    return (t,"wendepunkt",loc,[P]+pr,s,[C("Voll dabei sein und mitmachen",canon=True,docks=True,stats={"loyalty":6,"reputation":3},rels=dict(rels)),
       C("Eine Weile zuschauen und geniessen",canon=True,stats={"wisdom":3},rels={list(rels)[0]:3}),
       C("Diesmal fuer dich bleiben",canon=False,stats={"wisdom":2})],recap)
def mk(t,month,chap,cross=False):
    if cross:
        title,ptype,loc,pr,s,choices,recap=t
        return {"id":vid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 4 - {month})","school_time":f"{month} (Jahr 4) - Schulalltag",
                "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":3,
                "crossing_point":True,"clique_bond_delta":1,"autonomous_recap":recap,"choices":choices,"next_scenes":[]}
    title,ptype,loc,pr,s,choices=t
    return {"id":vid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 4 - {month})","school_time":f"{month} (Jahr 4) - Schulalltag",
            "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":2,
            "crossing_point":False,"choices":choices,"next_scenes":[]}
GAPS=[("y4_s03",18,"Oktober",19),("y4_s06",20,"November",20),("y4_s09",24,"Dezember",21),
      ("y4_s12",24,"Februar",22),("y4_s15",14,"Mai",23)]
cats=["subj","meal","common","ground","owl","arena","subj","common"]
gi=xi=ci=0; gapblocks={}
for aid,n,month,chap in GAPS:
    block=[]
    for k in range(n):
        if k%2==1: block.append(mk(x(xi),month,chap,cross=True)); xi+=1
        else:
            cat=cats[ci%len(cats)]; ci+=1
            f={"subj":subj,"meal":meal,"common":common,"ground":ground,"owl":owl,"arena":arena}[cat](gi); gi+=1
            block.append(mk(f,month,chap,cross=False))
    gapblocks[aid]=block
y4=[]
for a in backbone:
    y4.append(a)
    if a["id"] in gapblocks: y4.extend(gapblocks[a["id"]])
allscenes=existing+y4
for i,s in enumerate(allscenes): s["next_scenes"]=[allscenes[i+1]["id"]] if i+1<len(allscenes) else []
data["scenes"]=allscenes
json.dump(data,open(os.path.join(BOOK,"plot_graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
cross=[s for s in allscenes if s.get("crossing_point")]
print("Gesamt:",len(allscenes),"| Jahr 4:",len(y4),"| Kreuzungen:",len(cross))
print("y3_s18.next:",next(s for s in allscenes if s["id"]=="y3_s18")["next_scenes"])
print("ohne recap:",[s["id"] for s in allscenes if s.get("crossing_point") and not s.get("autonomous_recap")] or "keine")
ids={s["id"] for s in allscenes}
print("kaputte Verweise:",[s["id"] for s in allscenes if s["next_scenes"] and s["next_scenes"][0] not in ids] or "keine")
