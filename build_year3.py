#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahr 3 — 'Der Gefangene von Askaban' (kindgerecht) als NAHTLOSE Fortsetzung.
Haengt hinter y2_s19 an, gleicher Spielstand (Ansatz A).

Kindgerecht-Regeln:
 - Dementoren = kalte, traurige Schatten-Waechter; man vertreibt sie mit GLUECKLICHEN
   Erinnerungen (Patronus) und Schokolade. Kein echter Schrecken, eher 'Mut gegen Truebsal'.
 - Sirius Black = zunaechst missverstanden, in Wahrheit warmherzig (Harrys Patenonkel) — gutes Ende.
 - Niemand kommt zu Schaden; Erwachsene (v.a. Lupin) beschuetzen und fuehren; Hippogreif wird gerettet.
Moderation + SKILL.md-Ton gelten.  Aufruf: python3 build_year3.py
"""
import json, os, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "skill", "data", "books", "hogwarts")
data = json.load(open(os.path.join(BOOK, "plot_graph.json"), encoding="utf-8"))
existing = data["scenes"]
if any(s["id"].startswith("y3_") for s in existing):
    raise SystemExit("Jahr 3 ist bereits vorhanden — Abbruch.")

_c = itertools.count(1)
def kid(): return f"k{next(_c):03d}"
def C(desc, canon=True, stats=None, rels=None, docks=None):
    c = {"description": desc, "canon": canon}
    if stats: c["stat_effects"] = stats
    if rels: c["relationship_effects"] = rels
    if docks is not None: c["docks"] = docks
    return c
def A(id_, ch, title, st, present, loc, summ, choices, cp=False, recap=None, plot="kanon"):
    b = {"id": id_, "chapter": ch, "scene_index": 0, "title": title, "school_time": st,
         "characters_present": present, "location": loc, "summary": summ, "plot_type": plot,
         "challenge_potential": 3 if cp else 2, "crossing_point": cp,
         "choices": choices, "next_scenes": []}
    if cp:
        b["clique_bond_delta"] = 1
        b["autonomous_recap"] = recap
    return b

P = "player_heroine"
backbone = [
 A("y3_s01",13,"Ein grosser schwarzer Hund","Sommerferien — zuhause",
   [P,"marlen","maik","flocke"],"haus_sosa",
   "In den Ferien taucht abends am Gartenzaun ein riesiger, zotteliger schwarzer Hund auf und schaut dich mit klugen Augen an — dann ist er weg. Flocke wedelt freundlich, also kann er nicht boese sein. Mama und Papa schmunzeln ueber den 'Riesenhund'.",
   [C("Dem Hund vorsichtig zuwinken",stats={"loyalty":4},rels={"Flocke":3}),
    C("Mama und Papa von dem Tier erzaehlen",rels={"Mama":3,"Papa":3}),
    C("Dir merken: Das war bestimmt kein Zufall",stats={"wisdom":5})]),
 A("y3_s02","13","Hogsmeade-Erlaubnis & der Zug","1. September — im Hogwarts-Express",
   [P,"lily","lupin","ron","hermine"],"gleis_neun_dreiviertel",
   "Drittklaesslern winkt etwas Neues: Mit Erlaubnis darf man ins Dorf Hogsmeade! Im Zug wird es ploetzlich eisig kalt, als eine traurige Schattengestalt vorbeischwebt. Da steht schon der neue Lehrer Professor Lupin auf, vertreibt die Kaelte und teilt ruhig Schokolade aus: 'Hilft gegen den Schreck.'",
   [C("Dankbar die Schokolade nehmen und tief durchatmen",stats={"loyalty":4},rels={"Lupin":6}),
    C("Lily und die anderen fragen, ob es ihnen gut geht",rels={"Lily":3,"Ron":3}),
    C("Dich auf Hogsmeade freuen, um die Kaelte zu vergessen",stats={"reputation":4})],plot="wendepunkt"),
 A("y3_s03",13,"Lupins erste Stunde: der Irrwicht","September — Verteidigung gegen die dunklen Kuenste",
   [P,"lupin","neville"],"klassenzimmer",
   "Professor Lupin hat einen Schrank mit einem Irrwicht darin — einem Wesen, das sich in deine groesste Angst verwandelt. Der Trick: Mit dem Zauber 'Riddikulus' macht man sie einfach laecherlich! Reihum verwandelt ihr Schrecken in Slapstick, und die ganze Klasse lacht Traenen.",
   [C("Deine Angst beherzt in etwas Albernes verwandeln",stats={"combat":6,"reputation":3}),
    C("Neville Mut machen, der als Erster dran ist",stats={"loyalty":5},rels={"Neville":8}),
    C("Aufmerksam zusehen und den Zauber lernen",stats={"wisdom":5},rels={"Lupin":4})],plot="wendepunkt"),
 A("y3_s04",14,"Wahrsagen bei Trelawney","September — Wahrsage-Turm",
   [P,"trelawney","lily","ron"],"wahrsageturm",
   "Im stickigen, kerzenwarmen Turmzimmer raunt Professor Trelawney ueber Teeblaetter und Kristallkugeln und sieht in deiner Tasse gleich ein 'grosses Unheil' (einen 'Grimm'). Lily verdreht hinter ihrem Ruecken lAessig die Augen und fluestert: 'Sieht in jeder Tasse Unheil.'",
   [C("Hoeflich nicken und es nicht zu ernst nehmen",stats={"wisdom":5}),
    C("Mit Lily ueber das Drama schmunzeln",rels={"Lily":4}),
    C("Trotzdem neugierig in die Kristallkugel schauen",stats={"wisdom":4})]),
 A("y3_s05",14,"Hagrids erste Stunde: Seidenschnabel","September — Gehege fuer magische Geschoepfe",
   [P,"hagrid","harry","seidenschnabel"],"pflege_gehege",
   "Hagrid ist jetzt Lehrer! Stolz fuehrt er Seidenschnabel vor, einen praechtigen Hippogreif — halb Adler, halb Pferd. Die goldene Regel: erst hoeflich verbeugen, abwarten, ob er zurueckgruesst. Wer Respekt zeigt, gewinnt einen treuen Freund.",
   [C("Dich tief und respektvoll verbeugen — und Seidenschnabel gruesst zurueck!",canon=True,docks=True,stats={"reputation":5,"loyalty":5},rels={"Hagrid":6,"Seidenschnabel":12,"Harry":4}),
    C("Erst zuschauen, wie Harry es vormacht",canon=True,stats={"wisdom":3},rels={"Harry":3}),
    C("Vorsichtig auf Abstand bleiben",canon=False,stats={"wisdom":2})],
   cp=True,recap="In Hagrids erster Stunde verbeugten sich einige mutig vor dem Hippogreif Seidenschnabel und gewannen sein Vertrauen. Du hast an dem Tag nur davon gehoert.",plot="abenteuer"),
 A("y3_s06",14,"Erster Ausflug nach Hogsmeade","Oktober — Dorf Hogsmeade",
   [P,"lily","ron","hermine"],"hogsmeade",
   "Endlich Hogsmeade! Im Honigtopf tuermen sich Suessigkeiten bis zur Decke, und in den Drei Besen gibt es schaumiges Butterbier, das von innen waermt. Ein perfekter Tag mit den Freunden im verschneiten Dorf.",
   [C("Mit der ganzen Gang den Honigtopf pluendern und Butterbier trinken",canon=True,docks=True,stats={"reputation":5,"loyalty":4},rels={"Lily":4,"Ron":5,"Hermine":4}),
    C("In Ruhe durch die verschneiten Gassen schlendern",canon=True,stats={"wisdom":3}),
    C("Suessigkeiten fuer Neville mitnehmen, der nicht mit durfte",canon=False,stats={"loyalty":4},rels={"Neville":5})],
   cp=True,recap="Beim ersten Hogsmeade-Ausflug zog die Gang durch Honigtopf und Drei Besen. Du warst diesmal nicht dabei.",plot="abenteuer"),
 A("y3_s07",15,"Die Waechter am Tor","Oktober — Laendereien",
   [P,"lupin","lily"],"ländereien_see",
   "Rund um die Schule halten die Dementoren Wache — kalte, traurige Schatten, die einen frAesteln und an truebe Gedanken denken lassen. Lupin erklaert ruhig: Sie koennen niemandem etwas tun, solange man zusammenhaelt — und gegen die Truebsal hilft etwas Gutes im Herzen (und Schokolade).",
   [C("Lupins ruhigen Worten vertrauen und an etwas Schoenes denken",stats={"loyalty":5},rels={"Lupin":5}),
    C("Dich bei Lily unterhaken — zusammen ist es halb so kalt",rels={"Lily":4}),
    C("Beschliessen, diesen Schutzzauber unbedingt zu lernen",stats={"wisdom":5})],plot="wendepunkt"),
 A("y3_s08",15,"Lupin lehrt den Patronus","November — Extra-Stunde bei Lupin",
   [P,"lupin","harry"],"klassenzimmer",
   "In einer Extra-Stunde zeigt Lupin den Patronus-Zauber: Man denkt an die schoenste, gluecklichste Erinnerung, die man hat — und aus dem Zauberstab stroemt silbernes, warmes Licht, das alle Truebsal vertreibt. Es braucht Uebung, aber es fuehlt sich wunderbar an.",
   [C("Mit voller Kraft an deine gleucklichste Erinnerung denken",canon=True,docks=True,stats={"combat":6,"wisdom":5},rels={"Lupin":8,"Harry":5}),
    C("Harry Mut machen, der auch noch uebt",canon=True,rels={"Harry":5}),
    C("Geduldig weiterprobieren, bis ein Fuenkchen Licht kommt",canon=True,stats={"wisdom":5})],
   cp=True,recap="In Lupins Extra-Stunden lernten einige den Patronus-Zauber. Du hast diesmal nicht teilgenommen.",plot="wendepunkt"),
 A("y3_s09",15,"Die Karte des Rumtreibers","November — Gryffindor-Turm",
   [P,"harry","ron"],"gryffindor_turm",
   "Harry zeigt euch ein altes Pergament, das sich auf ein Codewort hin entfaltet: die Karte des Rumtreibers! Sie zeigt jeden Gang, jede Geheimtuer und sogar, wer gerade wo durchs Schloss laeuft. Ein Schatz fuer kleine Entdecker — natuerlich nur fuer Gutes.",
   [C("Staunend die Geheimgaenge auf der Karte erkunden",stats={"wisdom":6}),
    C("Ueberlegen, die Karte lieber verantwortungsvoll zu nutzen",stats={"reputation":4,"loyalty":3}),
    C("Mit Ron ueber die lustigen Namen darauf lachen",rels={"Ron":4})],plot="abenteuer"),
 A("y3_s10",16,"Geruechte ueber Sirius Black","Dezember — Grosse Halle",
   [P,"lily","hermine"],"grosse_halle",
   "Die ganze Schule tuschelt: Ein Mann namens Sirius Black sei entkommen, und alle tun so, als sei er furchtbar gefAehrlich. Doch je mehr du hoerst, desto mehr passt etwas nicht zusammen. Die Lehrer passen gut auf, niemand ist allein unterwegs.",
   [C("Ruhig bleiben und den Lehrern vertrauen",stats={"reputation":4}),
    C("Mit Hermine ueberlegen, ob an den Geruechten wirklich was dran ist",stats={"wisdom":6},rels={"Hermine":5}),
    C("Dich fragen, ob der schwarze Hund etwas damit zu tun hat",stats={"wisdom":4})],plot="wendepunkt"),
 A("y3_s11",16,"Quidditch im Sturm","Dezember — Quidditch-Stadion",
   [P,"harry","hooch","lupin"],"ländereien_see",
   "Bei Regen und Wind findet ein Quidditch-Spiel statt. Als die Kaelte der Dementoren aufzieht, behalten Madam Hooch und Professor Lupin alles fest im Griff — und ein heller Patronus verscheucht die Truebsal. Am Ende ueberwiegt der Jubel.",
   [C("Mit der Kurve anfeuern und an Schoenes denken",stats={"reputation":5,"loyalty":3},rels={"Harry":4}),
    C("Lupin zur Hand gehen, der die Schueler beschuetzt",rels={"Lupin":5}),
    C("Ruhig und mutig bleiben, als es kalt wird",stats={"combat":4})],plot="abenteuer"),
 A("y3_s12",16,"Zusammenhalten","Januar — Gryffindor-Turm",
   [P,"harry","ron","hermine","lily"],"gryffindor_turm",
   "Der Winter ist trueb mit all den Waechtern ums Schloss — aber am Kamin haelt die Gang zusammen, uebt heimlich den Patronus und macht sich gegenseitig Mut. Zusammen ist jede Truebsal nur halb so gross.",
   [C("Voll dabei sein und alle aufmuntern",canon=True,docks=True,stats={"loyalty":6},rels={"Harry":5,"Ron":5,"Hermine":5,"Lily":3}),
    C("Mit Hermine ueber Sirius' Geheimnis gruebeln",canon=True,rels={"Hermine":4}),
    C("Eine ruhige Runde fuer dich brauchen",canon=False,stats={"wisdom":2})],
   cp=True,recap="Am Kamin hielt die Gang durch den trueben Winter zusammen und uebte den Patronus. Du warst diesmal nicht dabei.",plot="wendepunkt"),
 A("y3_s13",17,"Der schwarze Hund fuehrt euch","Fruehjahr — durchs Schloss",
   [P,"harry","ron","hermine"],"treppenhaus",
   "Der grosse schwarze Hund taucht wieder auf — und diesmal wirkt er gar nicht boese, sondern als wolle er euch etwas zeigen. Vorsichtig und zusammen (und mit einem Lehrer in der Naehe) folgt ihr ihm zu einem versteckten Gang Richtung Hogsmeade.",
   [C("Gemeinsam und vorsichtig dem Hund folgen",stats={"combat":4,"loyalty":5},rels={"Harry":4,"Ron":4,"Hermine":4}),
    C("Sicherheitshalber Professor Lupin Bescheid geben",stats={"reputation":5,"loyalty":4},rels={"Lupin":4}),
    C("Mutig vorangehen, aber niemanden allein lassen",stats={"combat":4})],plot="finale"),
 A("y3_s14",17,"Die Wahrheit ueber Sirius","Fruehjahr — am Rand von Hogsmeade",
   [P,"sirius","lupin","harry"],"hogsmeade",
   "In einem alten, knarrenden Haus kommt die Wahrheit ans Licht: Der schwarze Hund IST Sirius Black — und er ist gar kein Boesewicht, sondern wurde zu Unrecht verdaechtigt. Er ist Harrys Patenonkel und wollte ihn die ganze Zeit nur beschuetzen. Lupin buergt fuer ihn, und alle atmen auf.",
   [C("Sirius eine Chance geben und zuhoeren",stats={"wisdom":5,"loyalty":5},rels={"Sirius":12,"Harry":5}),
    C("Dich fuer Harry freuen, der endlich Familie findet",rels={"Harry":6}),
    C("Lupin danken, dass er die Wahrheit ans Licht bringt",rels={"Lupin":5})],plot="finale"),
 A("y3_s15",17,"Die Dementoren am See — der grosse Patronus","Fruehjahr — Nacht am See",
   [P,"harry","lupin","sirius"],"ländereien_see",
   "Am dunklen Seeufer ziehen die Dementoren zusammen und es wird eisig truebe. Jetzt zahlt sich alle Uebung aus: Mit der staerksten glueecklichen Erinnerung im Herzen ruft ihr einen grossen, silbern leuchtenden Patronus — und das warme Licht vertreibt die Schatten. Alle sind in Sicherheit.",
   [C("Zusammen mit Harry den grossen Patronus heraufbeschwoeren",canon=True,docks=True,stats={"combat":8,"loyalty":6},rels={"Harry":6,"Lupin":5}),
    C("Ganz fest an deine schoenste Erinnerung denken",canon=True,stats={"wisdom":5}),
    C("Den Juengeren Mut zurufen und sie schuetzen",canon=True,stats={"loyalty":5})],
   cp=True,recap="In jener Nacht am See vertrieb ein grosser Patronus die Dementoren. Du hast die Heldentat nur nacherzaehlt bekommen.",plot="finale"),
 A("y3_s16",18,"Der Zeitumkehrer: Seidenschnabel retten","Fruehjahr — eine Stunde zurueck",
   [P,"hermine","harry","seidenschnabel"],"pflege_gehege",
   "Hermine hat ein Geheimnis: einen kleinen Zeitumkehrer, mit dem man ein Stueeck in die Vergangenheit reisen kann! Ganz vorsichtig nutzt ihr ihn, um den Hippogreif Seidenschnabel vor Unrecht zu bewahren — und Sirius einen sicheren Fluchtweg zu schenken. Ein kluges, aufregendes Abenteuer mit gutem Ausgang.",
   [C("Mit Hermine den klugen Plan ausfuehren und Seidenschnabel befreien",canon=True,docks=True,stats={"wisdom":8,"loyalty":6},rels={"Hermine":8,"Harry":4,"Seidenschnabel":8}),
    C("Genau auf Hermines Anweisungen achten (Zeitreisen sind knifflig)",canon=True,stats={"wisdom":6}),
    C("Seidenschnabel beruhigen, damit er mitkommt",canon=True,rels={"Seidenschnabel":6})],
   cp=True,recap="Mit einem Zeitumkehrer wurde Seidenschnabel gerettet und Sirius ein Fluchtweg geschenkt. Du hast davon erst spaeter erfahren.",plot="finale"),
 A("y3_s17",18,"Sirius fliegt in die Freiheit","Fruehjahr — Nacht",
   [P,"sirius","harry","seidenschnabel"],"ländereien_see",
   "Auf Seidenschnabels Ruecken steigt Sirius in den Sternenhimmel — frei, dankbar und mit einem warmen Versprechen an Harry, in Kontakt zu bleiben. Zum ersten Mal hat Harry so etwas wie Familie. Ein Abschied, der sich richtig gut anfuehlt.",
   [C("Sirius und Seidenschnabel zum Abschied zuwinken",stats={"loyalty":5},rels={"Sirius":5,"Seidenschnabel":4}),
    C("Dich mit Harry ueber seinen Patenonkel freuen",rels={"Harry":6}),
    C("Den Moment tief in dein Herz schliessen",stats={"wisdom":4})],plot="ausklang"),
 A("y3_s18",18,"Abschied von Lupin & Schuljahresende","Juni — Abschlussfest",
   [P,"lupin","lily","harry","ron","hermine"],"grosse_halle",
   "Professor Lupin verabschiedet sich leise — der beste Lehrer, den ihr hattet — und schenkt euch zum Schluss ein warmes Laecheln und ein Stueck Schokolade. Beim Abschlussfest blickt ihr auf ein Jahr voller Mut, Raetsel und Freundschaft zurueck. Das vierte Jahr wartet schon.",
   [C("Lupin von Herzen fuer alles danken",stats={"loyalty":6},rels={"Lupin":6}),
    C("Mit deinen Freunden das Jahr feiern",rels={"Harry":3,"Ron":3,"Hermine":3,"Lily":3}),
    C("Versprechen, euch ueber den Sommer zu schreiben",stats={"loyalty":4})],plot="ausklang"),
]
# scene_index/chapter Typ-Korrektur (y3_s02 hatte ch als String)
for b in backbone: b["chapter"]=int(b["chapter"])

# ── Filler-Pools (Jahr-3-Flavor, ASCII-Quotes) ───────────────────────────────
SUBJ=[("Verteidigung gegen die dunklen Kuenste","klassenzimmer",["lupin","neville"],
       "Professor Lupin uebt mit euch geduldig einen neuen Schutzzauber. Bei ihm traut sich sogar Neville etwas zu."),
 ("Wahrsagen","wahrsageturm",["trelawney","ron"],
  "Im Kerzenlicht deutet Professor Trelawney Wolken in Teetassen. Ron entdeckt darin angeblich 'einen Klecks, der Unheil bedeutet'."),
 ("Pflege magischer Geschoepfe","pflege_gehege",["hagrid"],
  "Hagrid stellt ein neues, wundersames Tier vor und strahlt vor Stolz. Hauptsache: hoeflich und ruhig bleiben."),
 ("Zauberkunst","klassenzimmer",["flitwick","hermine"],
  "Der winzige Professor Flitwick haengt fast vom Buecherstapel, so begeistert ist er von einem neuen Zauber. Hermine kann ihn natuerlich schon."),
 ("Kraeuterkunde","gewaechshaeuser",["sprout","neville"],
  "Professor Sprout zeigt mit erdigen Haenden, wie man eine zickige Pflanze baendigt. Neville hat hier den gruenen Daumen."),
 ("Verwandlung","klassenzimmer",["mcgonagall","ron"],
  "Professor McGonagall verwandelt vor euren Augen einen Becher in eine Maus. Heute uebt ihr etwas Kniffliges.")]
def subj(i):
    n,loc,present,s=SUBJ[i%len(SUBJ)]
    return (f"Unterricht: {n}","schule",loc,[P]+present,s,
     [C("Dich konzentrieren und es meistern",stats={"wisdom":6}),
      C("Einem Mitschueler helfen",stats={"loyalty":5},rels={"Neville":5}),
      C("Mutig etwas Neues ausprobieren",canon=False,stats={"combat":4})])
MEAL=["Beim Fruehstueck segeln die Posteulen herein; ein Paeckchen von zu Hause macht gute Laune.",
 "Mittagessen in der Grossen Halle — alle reden ueber den naechsten Hogsmeade-Ausflug.",
 "Abendessen mit dampfendem Eintopf; Lily macht trockene Witze ueber Trelawneys Unheils-Prophezeiungen.",
 "Warme Schokolade nach einem kalten Tag — gegen Dementoren-Truebsal das beste Mittel."]
def meal(i): return ("In der Grossen Halle","alltag","grosse_halle",[P,"lily","ron"],MEAL[i%len(MEAL)],
  [C("Dich zu den Freunden setzen",stats={"reputation":4},rels={"Lily":3}),C("In Ruhe geniessen",stats={"loyalty":3}),C("Ginny mit an den Tisch holen",rels={"Ginny":4})])
COMMON=["Am Kamin baut Ron sein Zauberschach auf und sucht einen Gegner.",
 "Die Gang uebt heimlich den Patronus — silberne Fuenkchen tanzen durch den Turm.",
 "Hausaufgaben-Chaos: Pergament, Tinte, und Trelawneys 'sage dein Unheil voraus'-Aufgabe.",
 "Gemuetlicher Regenabend; jemand erzaehlt von der Karte des Rumtreibers."]
def common(i): return ("Abend im Gemeinschaftsraum","alltag","gryffindor_turm",[P,"lily","ron","harry"],COMMON[i%len(COMMON)],
  [C("Mitmachen und abhaengen",stats={"loyalty":4},rels={"Ron":3}),C("Mit Lily quatschen",rels={"Lily":4}),C("Frueh ins Bett",canon=False,stats={"wisdom":2})])
GROUND=["Auf den Laendereien hebt der Riesenkrake harmlos eine Tentakel.",
 "Hagrid winkt zu seiner Huette; es duftet nach Kakao und es gibt eine neue Tiergeschichte.",
 "Ein Spaziergang am Waldrand; Flocke flitzt froehlich voraus.",
 "Am Seeufer uebt jemand, mit Magie Steine ueber das Wasser tanzen zu lassen."]
def ground(i): return ("Auf den Laendereien","alltag","ländereien_see",[P,"hagrid","flocke"],GROUND[i%len(GROUND)],
  [C("Hagrid besuchen",rels={"Hagrid":5}),C("Mit Flocke toben",rels={"Flocke":5}),C("Frische Luft geniessen",stats={"loyalty":3})])
def owl(i): return ("In der Eulerei","alltag","eulerei",[P,"flocke"],
  ["Du schickst einen Brief nach Hause, was du Neues erlebt hast.","Du fragst nach Neuigkeiten von zu Hause.","Deine Lieblingseule schuhut erwartungsvoll."][i%3],
  [C("Nach Hause schreiben",stats={"loyalty":6},rels={"Mama":4,"Papa":4}),C("Auf Antwort hoffen",rels={"Mama":3,"Papa":3}),C("Der Eule einen Keks geben",stats={"reputation":2})])
def hog(i): return ("Ausflug nach Hogsmeade","alltag","hogsmeade",[P,"lily","ron"],
  ["Im Honigtopf gibt es Zuckerfedern und Schokofroesche, so weit das Auge reicht.","In den Drei Besen waermt ihr euch mit schaumigem Butterbier.","Durch die verschneiten Gassen schlendern, Schaufenster bestaunen."][i%3],
  [C("Mit den Freunden den Tag geniessen",stats={"reputation":4},rels={"Lily":3,"Ron":3}),C("Etwas fuer Neville mitnehmen",rels={"Neville":4}),C("Eine ruhige Runde drehen",stats={"wisdom":3})])

XPOOL=[("gang","Abend mit der Gang","gryffindor_turm",["lily","harry","ron","hermine"],
        "Die ganze Runde sitzt zusammen, lacht und haelt fest zusammen.",{"Harry":6,"Ron":6,"Hermine":5},
        "Ein langer Kaminabend schweisste die Gang enger zusammen. Du warst woanders."),
 ("patronus","Patronus ueben","klassenzimmer",["lupin","harry"],
   "Gemeinsam uebt ihr den Patronus, bis silbernes Licht den Raum waermt. Lupin nickt stolz.",{"Lupin":8,"Harry":5},
   "In einer Uebungsrunde gelang einigen ein heller Patronus. Du warst diesmal nicht dabei."),
 ("hippogreif","Besuch bei Seidenschnabel","pflege_gehege",["hagrid","seidenschnabel"],
   "Du besuchst den stolzen Hippogreif, verbeugst dich hoeflich und buerstest sein glaenzendes Gefieder.",{"Seidenschnabel":10,"Hagrid":4},
   "Jemand kuemmerte sich liebevoll um Seidenschnabel. Diesmal warst du es nicht."),
 ("hogsmeade","Hogsmeade mit der Gang","hogsmeade",["lily","ron","hermine"],
   "Honigtopf, Butterbier, verschneite Gassen — ein rundum schoener Tag im Dorf.",{"Lily":5,"Ron":5,"Hermine":4},
   "Die Gang verbrachte einen schoenen Tag in Hogsmeade. Du hast den Ausflug verpasst."),
 ("hermine","Lernen mit Hermine","bibliothek",["hermine"],
   "Hermine teilt geduldig ihr Wissen, bis bei dir der Knoten platzt.",{"Hermine":10},
   "Hermine half einer Lerngruppe durch den Stoff. Du hast allein gelernt."),
 ("lupin","Gespraech mit Lupin","klassenzimmer",["lupin"],
   "Nach dem Unterricht nimmt sich Lupin Zeit, hoert dir zu und macht dir mit ruhigen Worten Mut.",{"Lupin":9},
   "Lupin nahm sich fuer ein paar Schueler Zeit. Diesmal warst du nicht dabei."),
 ("neville","Neville beistehen","gewaechshaeuser",["neville","sprout"],
   "Neville droht der Mut zu verlassen; du bleibst an seiner Seite, bis er strahlt.",{"Neville":10,"Harry":3},
   "Jemand stand Neville bei, bis er aufbluehte. Diesmal nicht du.")]
def x(i):
    k,t,loc,present,s,rels,recap=XPOOL[i%len(XPOOL)]
    return (t,"wendepunkt",loc,[P]+present,s,
      [C("Voll dabei sein und mitmachen",canon=True,docks=True,stats={"loyalty":6,"reputation":3},rels=dict(rels)),
       C("Eine Weile zuschauen und geniessen",canon=True,stats={"wisdom":3},rels={list(rels)[0]:3}),
       C("Diesmal fuer dich bleiben",canon=False,stats={"wisdom":2})],recap)

def mk(t,month,chap,cross=False):
    if cross:
        title,ptype,loc,present,s,choices,recap=t
        return {"id":kid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 3 - {month})",
                "school_time":f"{month} (Jahr 3) - Schulalltag","characters_present":present,"location":loc,
                "summary":s,"plot_type":ptype,"challenge_potential":3,"crossing_point":True,
                "clique_bond_delta":1,"autonomous_recap":recap,"choices":choices,"next_scenes":[]}
    title,ptype,loc,present,s,choices=t
    return {"id":kid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 3 - {month})",
            "school_time":f"{month} (Jahr 3) - Schulalltag","characters_present":present,"location":loc,
            "summary":s,"plot_type":ptype,"challenge_potential":2,"crossing_point":False,
            "choices":choices,"next_scenes":[]}

GAPS=[("y3_s03",18,"September",13),("y3_s06",20,"Oktober",14),("y3_s09",24,"November",15),
      ("y3_s12",24,"Januar",16),("y3_s15",12,"Fruehjahr",17)]
cats=["subj","meal","common","ground","owl","hog","subj","common"]
gi=xi=ci=0; gapblocks={}
for aid,n,month,chap in GAPS:
    block=[]
    for k in range(n):
        if k%2==1:
            block.append(mk(x(xi),month,chap,cross=True)); xi+=1
        else:
            cat=cats[ci%len(cats)]; ci+=1
            f={"subj":subj,"meal":meal,"common":common,"ground":ground,"owl":owl,"hog":hog}[cat](gi); gi+=1
            block.append(mk(f,month,chap,cross=False))
    gapblocks[aid]=block

y3=[]
for a in backbone:
    y3.append(a)
    if a["id"] in gapblocks: y3.extend(gapblocks[a["id"]])

allscenes=existing+y3
for i,s in enumerate(allscenes):
    s["next_scenes"]=[allscenes[i+1]["id"]] if i+1<len(allscenes) else []
data["scenes"]=allscenes
json.dump(data,open(os.path.join(BOOK,"plot_graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
cross=[s for s in allscenes if s.get("crossing_point")]
print("Gesamt-Szenen:",len(allscenes),"| Jahr 3:",len(y3),"| Kreuzungen gesamt:",len(cross))
print("y2_s19.next:",next(s for s in allscenes if s["id"]=="y2_s19")["next_scenes"])
bad=[s["id"] for s in allscenes if s.get("crossing_point") and not s.get("autonomous_recap")]
print("Kreuzungen ohne recap:",bad or "keine")
ids={s["id"] for s in allscenes}
print("kaputte Verweise:",[s["id"] for s in allscenes if s["next_scenes"] and s["next_scenes"][0] not in ids] or "keine")
