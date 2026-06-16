#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahr 7 — 'Heiligtuemer des Todes' (~12, Film-Niveau) — das grosse Finale.
Haengt hinter y6_s19 an. Aus Robins Sicht: Hogwarts unter dunkler Herrschaft, der
wiederbelebte DA-Widerstand (Neville als Anfuehrer), Harrys Rueckkehr, die Schlacht um
Hogwarts, Voldemorts Niederlage und ein neuer Morgen.

Ton ~12 / Film: ernst, mutig, bewegend. Echte Verluste (u. a. Lupin) werden wuerdevoll und
ohne grausige Bilder erzaehlt; die Gewalt der Schlacht bleibt unblutig (Mut, Zusammenhalt,
Hoffnung). Erwachsene fuehren und schuetzen; das Ende ist ein triumphaler, warmer Morgen.
Aufruf: python3 build_year7.py
"""
import json, os, itertools
HERE=os.path.dirname(os.path.abspath(__file__)); BOOK=os.path.join(HERE,"skill","data","books","hogwarts")
data=json.load(open(os.path.join(BOOK,"plot_graph.json"),encoding="utf-8")); existing=data["scenes"]
if any(s["id"].startswith("y7_") for s in existing): raise SystemExit("Jahr 7 existiert bereits.")
_c=itertools.count(1)
def did(): return f"d{next(_c):03d}"
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
 A("y7_s01",37,"Ein duesterer Sommer","Sommerferien — zuhause",
   [P,"marlen","maik","flocke"],"haus_familie",
   "Ueber der Zaubererwelt liegt ein langer Schatten, und von Harry, Ron und Hermine fehlt jede Spur — sie sind heimlich unterwegs, um die Finsternis zu bekaempfen. Bei dir zu Hause ist es warm und sicher, doch alle spueren: Dieses Jahr wird alles entscheiden. Du nimmst dir vor, tapfer zu sein.",
   [C("Bei Mama und Papa Kraft und Geborgenheit tanken",stats={"loyalty":5},rels={"Mama":4,"Papa":4}),
    C("Dir fest vornehmen, mutig zu bleiben, was auch kommt",stats={"combat":4}),
    C("In Gedanken bei deinen Freunden sein",rels={"Luna":3,"Neville":3})]),
 A("y7_s02",37,"Hogwarts unter neuer Herrschaft","1. September — Grosse Halle",
   [P,"snape","carrow","luna"],"grosse_halle",
   "Das Schloss ist nicht mehr dasselbe: Snape ist nun Schulleiter, und die kalten Carrows fuehren ein strenges, angstvolles Regiment. Die Stimmung ist bedrueckend — aber in den Blicken vieler Schueler glimmt trotziger Mut. Neben dir steht Luna, ruhig und unerschrocken.",
   [C("Ruhig bleiben und dir nichts anmerken lassen",stats={"wisdom":4}),
    C("Lunas stillem Mut Kraft entnehmen",rels={"Luna":5}),
    C("Dir schwoeren, dich nicht einschuechtern zu lassen",stats={"combat":4})],plot="wendepunkt"),
 A("y7_s03",37,"Die DA lebt wieder auf","September — Raum der Wuensche",cp=True,
   present=[P,"neville","ginny","luna"],loc="raum_der_wuensche",
   summ="Im Verborgenen erwacht Dumbledores Armee zu neuem Leben — und ausgerechnet der einst so schuechterne Neville waechst zum mutigen Anfuehrer heran. Heimlich, klug und voller Herz organisiert ihr den Widerstand und beschuetzt einander. Hier seid ihr nicht allein.",
   choices=[C("Dich voller Ueberzeugung dem Widerstand anschliessen",canon=True,docks=True,stats={"combat":4,"loyalty":6},rels={"Neville":8,"Ginny":4,"Luna":4}),
    C("Neville den Ruecken staerken, der so ueber sich hinauswaechst",canon=True,rels={"Neville":8}),
    C("Kluge Verstecke und Zeichen fuer die Gruppe ausdenken",canon=True,stats={"wisdom":5})],
   recap="Die DA erwachte unter Nevilles Fuehrung zu neuem Leben. Du warst diesmal nicht dabei.",plot="wendepunkt"),
 A("y7_s04",38,"Kleine Akte des Mutes","Oktober — bewegliche Treppen",
   [P,"neville","carrow"],"treppenhaus",
   "Der Widerstand zeigt Haltung: Ihr beschuetzt juengere Schueler vor der Strenge der Carrows, hinterlasst trotzige Botschaften an den Waenden und haltet die Hoffnung wach. Es ist gefaehrlich — aber jeder kleine mutige Schritt macht das Schloss ein bisschen heller.",
   [C("Juengere Schueler vor Ungerechtigkeit schuetzen",stats={"loyalty":6},rels={"Neville":4}),
    C("Mit einer trotzigen Botschaft Mut machen",stats={"combat":3,"reputation":3}),
    C("Vorsichtig sein, damit niemand erwischt wird",stats={"wisdom":4})],plot="wendepunkt"),
 A("y7_s05",38,"Zuflucht im Raum der Wuensche","November — Raum der Wuensche",cp=True,
   present=[P,"neville","luna","ginny"],loc="raum_der_wuensche",
   summ="Der Raum der Wuensche wird zum heimlichen Zuhause des Widerstands: mit Haengematten, Vorraeten und einem geheimen Durchgang. Hier finden alle Zuflucht, die sich nicht beugen wollen — eine echte Familie, die zusammenhaelt.",
   choices=[C("Beim Einrichten des Zufluchtsorts helfen und alle willkommen heissen",canon=True,docks=True,stats={"loyalty":6},rels={"Neville":5,"Luna":4,"Ginny":3}),
    C("Den Aengstlicheren Sicherheit und Trost geben",canon=True,stats={"loyalty":5}),
    C("Wache halten am geheimen Durchgang",canon=True,stats={"wisdom":4})],
   recap="Der Raum der Wuensche wurde zum Zufluchtsort des Widerstands. Du warst nicht dabei.",plot="wendepunkt"),
 A("y7_s06",38,"Nachrichten von Harry","Dezember — Gryffindor-Turm",
   [P,"ginny","neville"],"gryffindor_turm",
   "Ueber ein heimliches Radio und gefluesterte Geruechte dringt Hoffnung ins Schloss: Harry, Ron und Hermine sind da draussen und kaempfen weiter. Jede Nachricht von ihnen ist wie ein warmes Licht in der Dunkelheit und gibt euch neuen Mut.",
   [C("Mit den anderen jede Nachricht von Harry feiern",stats={"loyalty":4},rels={"Ginny":4}),
    C("Die Hoffnung weitertragen und andere aufmuntern",stats={"reputation":3},rels={"Neville":3}),
    C("Insgeheim ein Stossgebet fuer die drei sprechen",stats={"wisdom":3})]),
 A("y7_s07",39,"Die Legende der Heiligtuemer","Januar — Bibliothek",
   [P,"luna","neville"],"bibliothek",
   "Eine alte Legende macht die Runde: die drei Heiligtuemer des Todes. Und es heisst, Voldemort habe dunkle Gegenstaende versteckt, an die er sich klammert — und Harry sei ihnen auf der Spur. Luna erzaehlt es mit leuchtenden Augen, als waere es das Selbstverstaendlichste der Welt.",
   [C("Gebannt der geheimnisvollen Legende lauschen",stats={"wisdom":6},rels={"Luna":4}),
    C("Mit Neville ueberlegen, was das fuer Harry bedeutet",stats={"wisdom":4},rels={"Neville":3}),
    C("Hoffen, dass Harry findet, was er sucht",stats={"loyalty":3})]),
 A("y7_s08",39,"Mut bewahren, fuereinander da sein","Februar — Raum der Wuensche",cp=True,
   present=[P,"neville","luna","ginny"],loc="raum_der_wuensche",
   summ="Der Winter ist hart und die Herrschaft drueckt — doch der Widerstand haelt zusammen, teilt das Wenige und macht sich gegenseitig Mut. Gerade in den dunkelsten Stunden zeigt sich, wie stark Freundschaft ist.",
   choices=[C("Voll dabei sein und alle aufmuntern",canon=True,docks=True,stats={"loyalty":6,"combat":3},rels={"Neville":5,"Luna":4,"Ginny":3}),
    C("Mit Luna ruhige Zuversicht ausstrahlen",canon=True,rels={"Luna":5}),
    C("Den Juengeren Geschichten von Hoffnung erzaehlen",canon=True,stats={"wisdom":4})],
   recap="Der Widerstand hielt durch den harten Winter zusammen. Du warst diesmal nicht dabei.",plot="wendepunkt"),
 A("y7_s09",39,"Eine gefaehrliche Nacht","Maerz — bewegliche Treppen",
   [P,"neville","carrow"],"treppenhaus",
   "Beinahe waere der Widerstand aufgeflogen: Die Carrows sind euch dicht auf den Fersen, als ihr einen Mitschueler in Sicherheit bringt. Mit kuehlem Kopf, Zusammenhalt und ein bisschen Glueck entkommt ihr — das Herz pocht, aber ihr habt einander beschuetzt.",
   [C("Ruhig und entschlossen alle in Sicherheit bringen",stats={"combat":5,"loyalty":5},rels={"Neville":4}),
    C("Eine kluge Ablenkung erfinden",stats={"wisdom":5}),
    C("Erst aufatmen, als alle wieder sicher sind",stats={"loyalty":4})],plot="finale"),
 A("y7_s10",40,"Harry ist zurueck!","April — Raum der Wuensche",cp=True,
   present=[P,"harry","ron","hermine","neville"],loc="raum_der_wuensche",
   summ="Ploetzlich stehen sie im Raum der Wuensche: Harry, Ron und Hermine sind zurueck! Die Wiedersehensfreude ist ueberwaeltigend, und sofort ist klar: Der entscheidende Moment ist gekommen. Der ganze Widerstand richtet sich auf, voller Hoffnung und Entschlossenheit.",
   choices=[C("Harry und die anderen ueberglueecklich begruessen",canon=True,docks=True,stats={"loyalty":6,"reputation":3},rels={"Harry":6,"Ron":4,"Hermine":4,"Neville":3}),
    C("Sofort fragen, wie ihr helfen koennt",canon=True,stats={"combat":4}),
    C("Die Hoffnung im Raum mit allen teilen",canon=True,stats={"loyalty":4})],
   recap="Harry, Ron und Hermine kehrten nach Hogwarts zurueck. Du hast die Wiedersehensfreude verpasst.",plot="finale"),
 A("y7_s11",40,"Die Schule erhebt sich","Mai — Grosse Halle",
   [P,"mcgonagall","harry","neville"],"grosse_halle",
   "Endlich ist es so weit: Professor McGonagall und die Lehrer werfen die dunkle Herrschaft ab, und ganz Hogwarts entscheidet sich, sich zu wehren. Schutzzauber legen sich wie eine leuchtende Kuppel ueber das Schloss. Wer kaempfen will, steht auf — wer zu jung ist, wird in Sicherheit gebracht.",
   [C("Dich entschlossen zu den Verteidigern stellen",stats={"combat":5,"loyalty":5},rels={"Mcgonagall":3} if False else {"Harry":3}),
    C("Helfen, die Juengeren sicher hinauszubringen",stats={"loyalty":6}),
    C("Den Schutzzauber bestaunen und Mut fassen",stats={"wisdom":4})],plot="finale"),
 A("y7_s12",40,"Bereit fuer die Schlacht","Mai — Grosse Halle",cp=True,
   present=[P,"neville","ginny","luna","ron","hermine"],loc="grosse_halle",
   summ="Die DA und der Orden ruesten sich, Seite an Seite. Ihr nehmt euch in den Arm, sprecht euch Mut zu und wisst: Was auch kommt, ihr steht zusammen. Es ist beaengstigend — aber ihr seid nicht allein, und ihr kaempft fuer alles, was euch lieb ist.",
   choices=[C("Mit deinen Freunden fest zusammenstehen",canon=True,docks=True,stats={"combat":4,"loyalty":6},rels={"Neville":5,"Ginny":4,"Luna":4,"Ron":3,"Hermine":3}),
    C("Allen noch einmal Mut zusprechen",canon=True,stats={"reputation":4}),
    C("Tief durchatmen und dich bereitmachen",canon=True,stats={"wisdom":4})],
   recap="Die Verteidiger ruesteten sich Seite an Seite. Du warst diesmal nicht dabei.",plot="finale"),
 A("y7_s13",41,"Die Schlacht um Hogwarts beginnt","Mai — Schlosshof",
   [P,"harry","neville","ginny"],"schlacht_hof",
   "Die Schlacht bricht los: ein Sturm aus Funken, Schutzschilden und Mut. Die Verteidiger halten die Mauern, jeder an seinem Platz. Es ist gefaehrlich und ueberwaeltigend — doch ihr kaempft fuer Hogwarts, fuereinander, und gebt nicht auf. (Spannung und Gefahr, aber kein grausiges Bild.)",
   [C("Mit dem in der DA Gelernten tapfer mitkaempfen",stats={"combat":6,"loyalty":5},rels={"Neville":4,"Ginny":3}),
    C("Verwundete in Sicherheit und zu Madam Pomfrey bringen",stats={"loyalty":6}),
    C("Ruhig bleiben und anderen Halt geben",stats={"wisdom":4,"loyalty":4})],plot="finale"),
 A("y7_s14",41,"Schwere Verluste","Mai — Grosse Halle",
   [P,"lupin","ginny","neville"],"grosse_halle",
   "Die Schlacht fordert ihren Preis: Tapfere fallen fuer das, was richtig ist — unter ihnen Professor Lupin, der bis zuletzt fuer eine bessere Welt kaempfte, und andere geliebte Gefaehrten. (Erzaehlt mit Trauer und Wuerde, ohne grausige Bilder.) In der Grossen Halle haltet ihr inne, weint umeinander — und schoepft aus der Trauer neue Entschlossenheit.",
   [C("Um die Gefallenen trauern und sie ehren",stats={"loyalty":6},rels={"Lupin":4}),
    C("Einander Halt geben in der Trauer",stats={"loyalty":5},rels={"Ginny":3,"Neville":3}),
    C("Aus dem Schmerz den Mut schoepfen weiterzumachen",stats={"combat":4,"wisdom":3})],plot="finale"),
 A("y7_s15",41,"Nevilles grosser Moment","Mai — Schlosshof",cp=True,
   present=[P,"neville","harry"],loc="schlacht_hof",
   summ="Und dann der Augenblick, auf den Nevilles ganze Geschichte hinauslief: Furchtlos stellt er sich der Finsternis entgegen und erschlaegt mit dem Schwert von Gryffindor die grosse Schlange — Voldemorts letzten dunklen Halt. Aus dem schuechternen Jungen ist ein wahrer Held geworden. Ein Gaensehaut-Moment des Mutes!",
   choices=[C("Neville aus vollem Herzen zujubeln",canon=True,docks=True,stats={"reputation":5,"loyalty":6},rels={"Neville":10,"Harry":3}),
    C("Ihm in diesem Moment den Ruecken freihalten",canon=True,stats={"combat":4},rels={"Neville":6}),
    C("Stolz und geruehrt sein, wie weit er gekommen ist",canon=True,stats={"wisdom":4})],
   recap="Neville schlug mutig die grosse Schlange — ein Wendepunkt der Schlacht. Du hast es nur erzaehlt bekommen.",plot="finale"),
 A("y7_s16",42,"Der letzte Kampf: Harry gegen Voldemort","Morgengrauen — Grosse Halle",
   [P,"harry","voldemort","mcgonagall"],"grosse_halle",
   "Im ersten Licht des Morgens kommt es zum letzten Duell. Harry steht Voldemort gegenueber — ruhig, mutig, getragen von der Liebe und dem Mut aller, die fuer ihn einstanden. Mit der Wahrheit auf seiner Seite besiegt er die Finsternis: Voldemort ist endlich bezwungen, seine Macht zerfaellt. Ein Aufatmen geht durch die ganze Halle.",
   [C("Den Atem anhalten und dann jubeln, als die Finsternis faellt",stats={"reputation":5,"loyalty":4},rels={"Harry":5}),
    C("Vor Erleichterung deine Freunde umarmen",stats={"loyalty":5},rels={"Neville":3,"Ginny":3}),
    C("Den Moment in dein Herz schliessen: Mut hat gesiegt",stats={"wisdom":4})],plot="finale"),
 A("y7_s17",42,"Snapes Wahrheit","Morgen — Dumbledores Buero",
   [P,"harry"],"schulleiterbuero",
   "Eine letzte, bewegende Wahrheit kommt ans Licht: Professor Snape hat Harry die ganze Zeit heimlich beschuetzt — aus einer alten, tiefen Liebe und Treue, die niemand ahnte. Plotzlich erscheint alles in neuem Licht, und auch der strengste Lehrer wird als stiller Held geehrt.",
   [C("Ergriffen begreifen, dass Snape die ganze Zeit ein Guter war",stats={"wisdom":5}),
    C("Mit Harry diese schwere, schoene Wahrheit teilen",rels={"Harry":5}),
    C("Snape in stillem Respekt ehren",stats={"loyalty":4})],plot="wendepunkt"),
 A("y7_s18",42,"Trauer und Dankbarkeit","Morgen — Grosse Halle",
   [P,"mcgonagall","harry","ron","hermine","luna","neville","ginny"],"grosse_halle",
   "Der Morgen danach ist still und voller Gefuehle. In der Grossen Halle wird der Gefallenen gedacht — Lupin und all der Tapferen, die alles gaben. Es wird geweint und gehalten, Wunden werden versorgt, und zwischen der Trauer liegt tiefe Dankbarkeit: Die lange Nacht ist vorbei, und ihr habt sie gemeinsam durchgestanden.",
   [C("Gemeinsam der Gefallenen gedenken",stats={"loyalty":6},rels={"Harry":3,"Neville":3}),
    C("Bei der Versorgung der Verwundeten helfen",stats={"loyalty":5}),
    C("Deine Freunde dankbar an dich druecken",rels={"Luna":3,"Ginny":3,"Ron":3,"Hermine":3})],plot="ausklang"),
 A("y7_s19",42,"Ein neuer Morgen","Morgen — Laendereien am See",
   [P,"lily","harry","ron","hermine","luna","neville","ginny","flocke"],"ländereien_see",
   "Die Sonne geht ueber einem freien Hogwarts auf. Sieben Jahre voller Freundschaft, Mut und Erwachsenwerden liegen hinter dir — vom Brief zu Hause bis zu diesem Morgen. Mit deinen Freunden an der Seite und Flocke zu deinen Fuessen blickst du in eine Zukunft voller Hoffnung. Die Geschichte ist zu Ende — und ein neues Leben beginnt.",
   [C("Den Sonnenaufgang mit deinen Freunden geniessen",stats={"loyalty":5},rels={"Lily":3,"Harry":3,"Neville":3}),
    C("Dankbar zurueckblicken auf alles, was ihr zusammen erlebt habt",stats={"wisdom":5}),
    C("Voller Hoffnung in die Zukunft schauen",stats={"reputation":4})],plot="ausklang"),
]
for b in backbone: b["chapter"]=int(b["chapter"])
backbone[10]["choices"][0]=C("Dich entschlossen zu den Verteidigern stellen",stats={"combat":5,"loyalty":5},rels={"Harry":3})

SUBJ=[("Unter den Carrows (durchhalten)","klassenzimmer",["carrow","neville"],
       "Der Unterricht bei den Carrows ist streng und freudlos. Doch mit stillem Trotz und einem heimlichen Augenzwinkern an Neville haeltst du den Kopf oben."),
 ("Zauberkunst (heimlich Nuetzliches)","klassenzimmer",["flitwick","hermine"],
  "Professor Flitwick schmuggelt zwischen den Zeilen noch etwas wirklich Nuetzliches in den Unterricht. Ein kleines Licht im Grau."),
 ("Kraeuterkunde","gewaechshaeuser",["sprout","neville"],
  "Bei Professor Sprout findet Neville Halt in seinen Pflanzen — und teilt heimlich heilsame Kraeuter fuer den Widerstand."),
 ("Verwandlung","klassenzimmer",["mcgonagall","ginny"],
  "Professor McGonagall haelt mit eiserner Wuerde dagegen und gibt den Schuelern insgeheim Mut."),
 ("Pflege magischer Geschoepfe","pflege_gehege",["hagrid"],
  "Hagrid haelt trotz allem zu den Kindern und seinen Tieren — ein Fels in der Brandung.")]
def subj(i):
    n,loc,pr,s=SUBJ[i%len(SUBJ)]
    return (f"Unterricht: {n}","schule",loc,[P]+pr,s,[C("Durchhalten und heimlich lernen",stats={"wisdom":6}),
      C("Einem eingeschuechterten Mitschueler beistehen",stats={"loyalty":5},rels={"Neville":5}),C("Stillen Trotz bewahren",canon=False,stats={"combat":4})])
MEAL=["Beim Fruehstueck ist die Halle still und angespannt — aber heimliche Blicke sagen: Wir halten zusammen.",
 "Mittagessen unter wachsamen Augen; trotzdem teilt ihr leise ein Laecheln.","Abendessen; jemand schmuggelt Essen fuer die Versteckten im Raum der Wuensche.","Ein karges Mahl, das in guter Gesellschaft doch waermt."]
def meal(i): return ("In der Grossen Halle","alltag","grosse_halle",[P,"luna","ginny"],MEAL[i%len(MEAL)],
  [C("Heimlich Mut mit den Freunden teilen",stats={"loyalty":4},rels={"Luna":3}),C("Auf die Juengeren achten",rels={"Ginny":3}),C("Ruhig und wachsam bleiben",stats={"wisdom":3})])
COMMON=["Am Kamin wird leise der naechste mutige Schritt des Widerstands geplant.","Trotz allem gibt es ein bisschen Gelaechter — Hoffnung laesst sich nicht verbieten.",
 "Jemand uebt heimlich einen Schutzzauber fuer den Ernstfall.","Ihr lest gemeinsam zwischen den Zeilen einer geschmuggelten Nachricht."]
def common(i): return ("Abend im Gemeinschaftsraum","alltag","gryffindor_turm",[P,"ginny","neville","luna"],COMMON[i%len(COMMON)],
  [C("Beim Planen und Mutmachen mitwirken",stats={"loyalty":4,"combat":2},rels={"Neville":3}),C("Mit Luna Zuversicht verbreiten",rels={"Luna":4}),C("Frueh ausruhen fuer den naechsten Tag",canon=False,stats={"wisdom":2})])
GROUND=["Auf den Laendereien atmet ihr kurz frei durch, fern der strengen Mauern.","Hagrid haelt heimlich zu euch und gibt Mut.","Ein kurzer Moment Ruhe am See; Flocke weicht dir nicht von der Seite.","Am Waldrand fluestert ihr ueber Hoffnung und Zusammenhalt."]
def ground(i): return ("Auf den Laendereien","alltag","ländereien_see",[P,"hagrid","flocke"],GROUND[i%len(GROUND)],
  [C("Hagrid besuchen und Mut tanken",rels={"Hagrid":5}),C("Mit Flocke kurz durchatmen",rels={"Flocke":5}),C("Den Moment Ruhe geniessen",stats={"loyalty":3})])
def owl(i): return ("In der Eulerei","alltag","eulerei",[P,"flocke"],
  ["Du schickst heimlich eine beruhigende Nachricht nach Hause.","Du fragst vorsichtig nach Neuigkeiten von zu Hause.","Deine Lieblingseule schuhut leise, als verstuende sie."][i%3],
  [C("Heimlich nach Hause schreiben",stats={"loyalty":6},rels={"Mama":4,"Papa":4}),C("Auf ein Lebenszeichen hoffen",rels={"Mama":3,"Papa":3}),C("Der Eule sanft den Kopf kraulen",stats={"reputation":2})])
def room(i): return ("Im Zufluchtsort","alltag","raum_der_wuensche",[P,"neville","luna"],
  ["Im Raum der Wuensche versorgst du die Versteckten und gibst Trost.","Du uebst heimlich einen Schutzzauber fuer den Ernstfall.","Der Raum gibt euch genau, was ihr zum Durchhalten braucht."][i%3],
  [C("Den Versteckten beistehen",stats={"loyalty":6},rels={"Neville":4}),C("Einen Schutzzauber ueben",stats={"combat":5,"wisdom":3}),C("Mit Luna ruhige Zuversicht teilen",rels={"Luna":4})])
XPOOL=[("da","Widerstands-Treffen","raum_der_wuensche",["neville","luna","ginny"],
        "Heimlich plant und uebt der Widerstand zusammen — und wird als Familie immer enger.",{"Neville":6,"Luna":4,"Ginny":4},
        "Der Widerstand traf sich heimlich. Du warst diesmal nicht dabei."),
 ("neville","Neville staerken","raum_der_wuensche",["neville"],
   "Du staerkst Neville den Ruecken, der den Widerstand traegt — und gemeinsam wachst ihr ueber euch hinaus.",{"Neville":10},
   "Jemand staerkte Neville. Diesmal nicht du."),
 ("luna","Zeit mit Luna","ländereien_see",["luna"],
   "Lunas unerschuetterliche Ruhe gibt dir Halt; ihr seht selbst jetzt das Gute in der Welt.",{"Luna":10},
   "Luna verbrachte Zeit mit Freunden. Diesmal nicht mit dir."),
 ("ginny","Mut mit Ginny","gryffindor_turm",["ginny"],
   "Ginny ist eine mutige Saeule des Widerstands; ihr stuetzt euch gegenseitig und gebt nicht auf.",{"Ginny":9},
   "Ginny verbrachte Zeit mit Freunden. Diesmal nicht mit dir."),
 ("schutz","Juengere beschuetzen","treppenhaus",["neville","ginny"],
   "Gemeinsam beschuetzt ihr die juengeren Schueler vor der Strenge der Carrows — ein stiller, grosser Mut.",{"Neville":5,"Ginny":4},
   "Der Widerstand beschuetzte die Juengeren. Du warst diesmal nicht dabei."),
 ("hagrid","Mut bei Hagrid","hagrids_huette",["hagrid"],
   "Bei Hagrid findet ihr einen warmen, sicheren Ort und neuen Mut.",{"Hagrid":8},
   "Hagrid gab ein paar Schuelern Halt. Du warst nicht dabei.")]
def x(i):
    k,t,loc,pr,s,rels,recap=XPOOL[i%len(XPOOL)]
    return (t,"wendepunkt",loc,[P]+pr,s,[C("Voll dabei sein und mitmachen",canon=True,docks=True,stats={"loyalty":6,"combat":2},rels=dict(rels)),
       C("Eine Weile zuschauen und Halt geben",canon=True,stats={"wisdom":3},rels={list(rels)[0]:3}),
       C("Diesmal fuer dich bleiben",canon=False,stats={"wisdom":2})],recap)
def mk(t,month,chap,cross=False):
    if cross:
        title,ptype,loc,pr,s,choices,recap=t
        return {"id":did(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 7 - {month})","school_time":f"{month} (Jahr 7) - Widerstand",
                "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":3,
                "crossing_point":True,"clique_bond_delta":1,"autonomous_recap":recap,"choices":choices,"next_scenes":[]}
    title,ptype,loc,pr,s,choices=t
    return {"id":did(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 7 - {month})","school_time":f"{month} (Jahr 7) - Widerstand",
            "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":2,
            "crossing_point":False,"choices":choices,"next_scenes":[]}
GAPS=[("y7_s03",18,"September",37),("y7_s06",20,"Oktober",38),("y7_s09",24,"Dezember",39),
      ("y7_s12",24,"Februar",40),("y7_s15",14,"Mai",41)]
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
y7=[]
for a in backbone:
    y7.append(a)
    if a["id"] in gapblocks: y7.extend(gapblocks[a["id"]])
allscenes=existing+y7
for i,s in enumerate(allscenes): s["next_scenes"]=[allscenes[i+1]["id"]] if i+1<len(allscenes) else []
data["scenes"]=allscenes
json.dump(data,open(os.path.join(BOOK,"plot_graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
cross=[s for s in allscenes if s.get("crossing_point")]
print("Gesamt:",len(allscenes),"| Jahr 7:",len(y7),"| Kreuzungen:",len(cross))
print("y6_s19.next:",next(s for s in allscenes if s["id"]=="y6_s19")["next_scenes"]," | Endpunkt:",[s["id"] for s in allscenes if not s["next_scenes"]])
print("ohne recap:",[s["id"] for s in allscenes if s.get("crossing_point") and not s.get("autonomous_recap")] or "keine")
ids={s["id"] for s in allscenes}
print("kaputte Verweise:",[s["id"] for s in allscenes if s["next_scenes"] and s["next_scenes"][0] not in ids] or "keine")
