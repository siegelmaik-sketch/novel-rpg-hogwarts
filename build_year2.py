#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahr 2 — „Die Kammer des Schreckens“ (kindgerecht) als NAHTLOSE Fortsetzung.
Hängt hinter y1_s12 an, gleicher Spielstand (Ansatz A): Robin wächst durch,
Beziehungen/Flocke/Clique/Attribute bleiben erhalten.

Kindgerecht-Regeln: Versteinerungen = „eingefroren, vollständig reversibel“; die
Riesenschlange wird abenteuerlich statt gruselig erzählt; Erwachsene beschützen und
führen; Phönix heilt; gutes, fröhliches Ende. Moderation + SKILL.md-Ton gelten.

Aufruf: python3 build_year2.py
"""
import json, os, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "skill", "data", "books", "hogwarts")
data = json.load(open(os.path.join(BOOK, "plot_graph.json"), encoding="utf-8"))
existing = data["scenes"]
if any(s["id"].startswith("y2_") for s in existing):
    raise SystemExit("Jahr 2 ist bereits vorhanden — Abbruch (keine Doppelung).")

_c = itertools.count(1)
def hid(): return f"h{next(_c):03d}"
def C(desc, canon=True, stats=None, rels=None, docks=None):
    c = {"description": desc, "canon": canon}
    if stats: c["stat_effects"] = stats
    if rels: c["relationship_effects"] = rels
    if docks is not None: c["docks"] = docks
    return c
def anchor(id_, ch, title, st, present, loc, summ, choices, cp=False, recap=None, plot="kanon"):
    b = {"id": id_, "chapter": ch, "scene_index": 0, "title": title, "school_time": st,
         "characters_present": present, "location": loc, "summary": summ,
         "plot_type": plot, "challenge_potential": 3 if cp else 2,
         "crossing_point": cp, "choices": choices, "next_scenes": []}
    if cp:
        b["clique_bond_delta"] = 1
        b["autonomous_recap"] = recap
    return b

P = "player_heroine"
# ── Kanon-Rückgrat Jahr 2 (kindgerecht) ──────────────────────────────────────
backbone = [
 anchor("y2_s01",7,"Sommer zu Hause & ein seltsamer Besuch","Sommerferien — zuhause zu Hause",
   [P,"marlen","maik","dobby"],"haus_sosa",
   "Mitten in den Ferien plumpst mit einem Plopp ein winziges Wesen mit Fledermausohren in Robins Zimmer: der Hauself Dobby. Hände ringend warnt er dramatisch, Robin solle dieses Jahr „ganz besonders vorsichtig“ in Hogwarts sein — und ist schon wieder verschwunden. Mama und Papa staunen Bauklötze.",
   [C("Mama und Papa beruhigen, dass alles gut wird",stats={"loyalty":5},rels={"Mama":4,"Papa":4}),
    C("Neugierig rätseln, was der kleine Elf wohl meinte",stats={"wisdom":5}),
    C("Tapfer beschließen: Du freust dich trotzdem aufs neue Jahr",stats={"combat":4})]),
 anchor("y2_s02",7,"Zurück in der Winkelgasse","Ende der Ferien — Winkelgasse",
   [P,"lily","lockhart","ron","hermine","ginny"],"winkelgasse",
   "Die Bücherliste ist diesmal lang — und fast alles stammt von einem gewissen Gilderoy Lockhart, der bei Flourish & Blotts strahlend Autogramme verteilt. Im Gewühl triffst du die Gang wieder und lernst Rons schüchterne kleine Schwester Ginny kennen. Lily verdreht bei Lockhart lässig die Augen.",
   [C("Die Gang freudig begrüßen",rels={"Ron":4,"Hermine":4,"Lily":3}),
    C("Dich über Lockharts Angeberei amüsieren",stats={"wisdom":4,"reputation":3}),
    C("Der schüchternen Ginny das Ankommen leichter machen",stats={"loyalty":4},rels={"Ginny":8})]),
 anchor("y2_s03",7,"Wieder im Hogwarts-Express","1. September — der Express rollt",
   [P,"lily","ron","hermine","ginny"],"gleis_neun_dreiviertel",
   "Vertrautes Rattern, vertraute Gesichter: Im Abteil tauscht ihr die Ferien-Geschichten aus, Flocke schnüffelt jeden ab, und Ginny lugt etwas scheu hinter Ron hervor. Hogwarts, ihr kommt!",
   [C("Mit allen die Ferien-Erlebnisse teilen",rels={"Ron":3,"Hermine":3}),
    C("Ginny in die Runde holen",rels={"Ginny":6}),
    C("Mit Lily entspannt aus dem Fenster schauen",rels={"Lily":4}),
    C("Flocke ein Leckerli geben",rels={"Flocke":3})]),
 anchor("y2_s04",8,"Lockharts erste Stunde","September — Verteidigung gegen die dunklen Künste",
   [P,"lockhart","neville"],"klassenzimmer",
   "Stolz öffnet Professor Lockhart einen Käfig voller frecher Wichtel — und im Nu schwirrt das halbe Klassenzimmer durch die Luft, Tintenfässer fliegen, Lockhart sucht Deckung unterm Pult. Reines Chaos, aber zum Schießen komisch.",
   [C("Beherzt helfen, die Wichtel wieder einzufangen",stats={"combat":6,"reputation":3}),
    C("Ruhe bewahren und Neville in Sicherheit bringen",stats={"loyalty":5},rels={"Neville":6}),
    C("Dir das Lachen über Lockhart kaum verkneifen",stats={"wisdom":4})]),
 anchor("y2_s05",8,"Kräuterkunde: Die Alraunen","September — Gewächshäuser",
   [P,"neville","hermine"],"gewaechshaeuser",
   "Mit dicken Ohrenschützern topft ihr quäkende Alraunen-Babys um — pummelige, schlammige Pflänzchen, die zappeln und brüllen wie Kleinkinder. Professor Sprout verspricht: Ausgewachsen sind sie eine wichtige Medizin.",
   [C("Die Alraunen vorsichtig und richtig umtopfen",stats={"wisdom":6}),
    C("Mit Neville als Team arbeiten",rels={"Neville":6}),
    C("Mit Hermine über die Heilkraft der Alraunen fachsimpeln",rels={"Hermine":5})]),
 anchor("y2_s06",8,"Quidditch: der wilde Klatscher","Oktober — Quidditch-Spiel",cp=True,
   present_=None) if False else anchor("y2_s06",8,"Quidditch: der wilde Klatscher","Oktober — Quidditch-Spiel",
   [P,"harry","ron","hermine","lily"],"ländereien_see",
   "Beim Spiel dreht plötzlich ein Klatscher durch und jagt nur hinter Harry her! Auf den Rängen bangt und jubelt ihr gemeinsam, bis Harry den Schnatz schnappt und sicher landet. Was für ein Spektakel.",
   [C("Mit der ganzen Kurve mitfiebern und Harry anfeuern",canon=True,docks=True,stats={"reputation":5,"loyalty":4},rels={"Harry":6,"Ron":5,"Hermine":4,"Lily":3}),
    C("Gebannt zuschauen und mitzittern",canon=True,stats={"wisdom":3},rels={"Harry":3}),
    C("Diesmal nicht zum Spiel gehen",canon=False,stats={"wisdom":2})],
   cp=True,recap="Beim Spiel sorgte ein außer Kontrolle geratener Klatscher für Aufregung; die ganze Gryffindor-Kurve fieberte zusammen. Du hast das Spiel verpasst.",plot="abenteuer"),
 anchor("y2_s07",9,"Die Schrift an der Wand","31. Oktober — nach dem Halloween-Fest",
   [P,"lily","ron","hermine"],"treppenhaus",
   "Auf dem Heimweg vom Fest leuchtet an einer Wand eine Botschaft: „Die Kammer des Schreckens ist geöffnet.“ Daneben sitzt die Katze des Hausmeisters reglos da — wie zu Stein erstarrt. Sofort sind Lehrer zur Stelle und versichern ruhig: Es ist ungefährlich und vollständig heilbar, niemandem passiert etwas.",
   [C("Bei deinen Freunden bleiben und ruhig Atem holen",stats={"loyalty":5},rels={"Ron":3,"Hermine":3}),
    C("Den beruhigenden Worten der Lehrer vertrauen",stats={"reputation":4}),
    C("Dich fragen, was diese geheimnisvolle Kammer ist",stats={"wisdom":5})],plot="wendepunkt"),
 anchor("y2_s08",9,"Rätselraten im Gemeinschaftsraum","November — abends am Kamin",cp=True,
   present_=None) if False else anchor("y2_s08",9,"Rätselraten im Gemeinschaftsraum","November — abends am Kamin",
   [P,"harry","ron","hermine","lily"],"gryffindor_turm",
   "Am Feuer steckt ihr die Köpfe zusammen: Was ist die Kammer des Schreckens, und wer hat sie geöffnet? Hermine hat schon drei Theorien, Ron drei Gegentheorien, und Lily wirft trocken die vierte ein.",
   [C("Bei der Detektivrunde voll mitmachen",canon=True,docks=True,stats={"wisdom":6,"loyalty":4},rels={"Harry":5,"Ron":5,"Hermine":6,"Lily":3}),
    C("Zuhören und gute Fragen stellen",canon=True,stats={"wisdom":4},rels={"Hermine":3}),
    C("Lieber früh schlafen — morgen sieht man klarer",canon=False,stats={"wisdom":2})],
   cp=True,recap="Am Kamin zerbrach sich die Gang die Köpfe über die Kammer des Schreckens. Du warst diesmal nicht in der Rätselrunde.",plot="wendepunkt"),
 anchor("y2_s09",9,"Der Duellierclub","November — Große Halle",
   [P,"lockhart","snape","harry"],"duellierclub",
   "Auf einer langen Bühne führen Lockhart und Professor Snape vor, wie man Zauber höflich abwehrt. Als eine herbeigezauberte Schlange auftaucht, spricht Harry sie ganz selbstverständlich an — und plötzlich tuschelt die ganze Halle. Robin merkt: Harry ist genauso überrascht wie alle anderen.",
   [C("Die Vorführung aufmerksam verfolgen",stats={"wisdom":5}),
    C("Zu Harry halten, als alle ihn anstarren",stats={"loyalty":5},rels={"Harry":6}),
    C("Selbst einen höflichen Schutzzauber üben",stats={"combat":5})],plot="wendepunkt"),
 anchor("y2_s10",10,"Hermines Plan","November/Dezember — Myrtes Waschraum",cp=True,
   present_=None) if False else anchor("y2_s10",10,"Hermines Plan","November/Dezember — Myrtes Waschraum",
   [P,"hermine","ron","harry","myrte"],"verwunschenes_klo",
   "In Myrtes selten benutztem Waschraum hat Hermine einen verwegenen Plan ausgeheckt, um dem Geheimnis auf die Spur zu kommen. Das gutmütige Klo-Gespenst Myrte schmollt zuerst, hilft dann aber doch.",
   [C("Bei Hermines Plan mit anpacken",canon=True,docks=True,stats={"wisdom":5,"loyalty":5},rels={"Hermine":6,"Ron":4,"Harry":4}),
    C("Vorsichtig mahnen, lieber einen Lehrer einzuweihen",canon=True,stats={"reputation":4}),
    C("Myrte ein bisschen aufmuntern",canon=False,stats={"loyalty":3})],
   cp=True,recap="Hermine tüftelte mit den anderen an einem kniffligen Plan in Myrtes Waschraum. Du warst nicht mit dabei.",plot="abenteuer"),
 anchor("y2_s11",10,"Das geheimnisvolle Tagebuch","Dezember — Bibliothek",
   [P,"harry","hermine"],"bibliothek",
   "Ein altes, leeres Tagebuch taucht auf — und schreibt zurück, wenn man hineinschreibt! Es zeigt verblasste Bilder aus Hogwarts' Vergangenheit. Spannend und ein bisschen unheimlich, aber ihr seid zu dritt und passt aufeinander auf.",
   [C("Das Tagebuch vorsichtig untersuchen",stats={"wisdom":6}),
    C("Auf Nummer sicher gehen und es einem Lehrer zeigen",stats={"reputation":4,"loyalty":3}),
    C("Mit Hermine seine Herkunft erforschen",rels={"Hermine":5})],plot="wendepunkt"),
 anchor("y2_s12",10,"Recherche mit Hermine","Januar — Bibliothek",cp=True,
   present_=None) if False else anchor("y2_s12",10,"Recherche mit Hermine","Januar — Bibliothek",
   [P,"hermine","ron"],"bibliothek",
   "Halbe Nachmittage verbringt ihr zwischen staubigen Wälzern über Hogwarts' Geschichte. Hermine führt akribisch Listen, und langsam fügt sich ein Bild zusammen.",
   [C("Mit Hermine systematisch die alten Bücher durchgehen",canon=True,docks=True,stats={"wisdom":7,"loyalty":3},rels={"Hermine":7,"Ron":3}),
    C("Einen klugen Querverweis vorschlagen",canon=True,stats={"wisdom":4}),
    C("Eine Pause an der frischen Luft einlegen",canon=False,stats={"wisdom":2})],
   cp=True,recap="Hermine wälzte halbe Nächte Bücher über Hogwarts' Geschichte. Du hast woanders nach Hinweisen gesucht.",plot="schule"),
 anchor("y2_s13",11,"Sorge macht sich breit","Februar — Große Halle",
   [P,"lily","ginny"],"grosse_halle",
   "Die Schule ist still geworden; noch jemand wurde „eingefroren“ gefunden — und auch das, versichern die Lehrer, ist heilbar. Vorsichtshalber werden alle in Gruppen von Lehrern begleitet, niemand ist allein. Ginny wirkt blass und in sich gekehrt; du setzt dich zu ihr.",
   [C("Der besorgten Ginny gut zureden",stats={"loyalty":5},rels={"Ginny":8}),
    C("Wie empfohlen dicht bei den Freunden bleiben",rels={"Lily":3}),
    C("Einen kühlen Kopf bewahren und Mut machen",stats={"wisdom":4})],plot="wendepunkt"),
 anchor("y2_s14",11,"Auch Hermine eingefroren","Februar — Krankenflügel",
   [P,"ron","harry"],"klassenzimmer",
   "Es trifft Hermine: Auch sie wird reglos gefunden. Es tut weh, sie so zu sehen — aber Madam Pomfrey ist zuversichtlich, denn die Alraunen sind fast reif, und dann wachen alle wieder auf. Ron ist ganz still; du legst ihm die Hand auf die Schulter.",
   [C("Hermine besuchen und ihr versprechen, dass alles gut wird",stats={"loyalty":6},rels={"Harry":4,"Ron":5}),
    C("Überlegen, wie du jetzt helfen kannst",stats={"reputation":4,"wisdom":3}),
    C("Für Ron stark sein",rels={"Ron":6})],plot="wendepunkt"),
 anchor("y2_s15",11,"Die Spur zur Kammer","Mai — Myrtes Waschraum",
   [P,"harry","ron","myrte"],"verwunschenes_klo",
   "Stück für Stück fügt es sich: Der verborgene Eingang liegt ausgerechnet in Myrtes Waschraum, und die Gefahr ist eine uralte, riesige Schlange, deren Blick „einfriert“ — also niemals direkt hinsehen! Sofort beschließt ihr, das Wichtigste zu tun: die Lehrer holen.",
   [C("Schnurstracks zu McGonagall und Dumbledore laufen",stats={"loyalty":5,"reputation":5},rels={"Harry":3,"Ron":3}),
    C("Den letzten Hinweis gemeinsam zu Ende denken",stats={"wisdom":6}),
    C("Darauf achten, dass keiner allein losgeht",stats={"loyalty":5})],plot="finale"),
 anchor("y2_s16",12,"Die Lehrer übernehmen — ihr helft mutig","Mai — Eingang zur Kammer",
   [P,"harry","ron","dumbledore","mcgonagall"],"kammer_eingang",
   "Die Lehrer machen sich auf den Weg nach unten und nehmen die Sache in die Hand. Eure entscheidenden Hinweise gebt ihr weiter — mutig, aber in Sicherheit. Dumbledore nickt euch ernst und freundlich zu: Gut gemacht.",
   [C("Den Lehrern all eure Hinweise übergeben",stats={"reputation":6}),
    C("Tapfer zusammenstehen und abwarten",stats={"loyalty":5},rels={"Harry":3,"Ron":3}),
    C("Auf Ginny und die Jüngeren aufpassen",rels={"Ginny":6})],plot="finale"),
 anchor("y2_s17",12,"Mut in der Tiefe","Mai — tief unter der Schule",cp=True,
   present_=None) if False else anchor("y2_s17",12,"Mut in der Tiefe","Mai — tief unter der Schule",
   [P,"harry","ron"],"kammer_eingang",
   "Tief unten wird es spannend — doch mit dem Mut aller, der Hilfe der Lehrer und sogar dem Phönix Fawkes, der heilend herbeifliegt, wird die Gefahr gebannt und das verzauberte Tagebuch unschädlich gemacht. Niemandem geschieht etwas Bleibendes.",
   [C("Zusammenhalten und füreinander einstehen",canon=True,docks=True,stats={"combat":5,"loyalty":6},rels={"Harry":6,"Ron":6}),
    C("Ruhe bewahren und den Lehrern vertrauen",canon=True,stats={"wisdom":4,"reputation":3}),
    C("Im Hintergrund bleiben und mitbangen",canon=False,stats={"wisdom":2})],
   cp=True,recap="Tief unter der Schule wurde die Gefahr gebannt — Fawkes der Phönix half. Du hast die entscheidenden Momente nur später erzählt bekommen.",plot="finale"),
 anchor("y2_s18",12,"Alle wieder wach","Juni — Krankenflügel & Große Halle",
   [P,"hermine","ron","harry","ginny","dobby"],"grosse_halle",
   "Die Alraunen sind reif, die Medizin wirkt — und alle „Eingefrorenen“ wachen wieder auf, allen voran Hermine! Es gibt Umarmungen, Lachen und Tränen der Erleichterung. Und Dobby? Der hüpft frei und überglücklich umher.",
   [C("Hermine überglücklich in den Arm nehmen",stats={"loyalty":6},rels={"Hermine":6}),
    C("Mit allen ausgelassen feiern",rels={"Harry":3,"Ron":3,"Ginny":3}),
    C("Für den befreiten Dobby jubeln",stats={"reputation":4})],plot="ausklang"),
 anchor("y2_s19",12,"Schuljahresende, Jahr 2","Juni — Abschlussfest",
   [P,"lily","harry","ron","hermine","ginny","dumbledore"],"grosse_halle",
   "Die Große Halle erstrahlt zum Abschlussfest. Dumbledore vergibt die letzten Hauspunkte, und du blickst auf ein aufregendes zweites Jahr zurück — voller Rätsel, Mut und Freundschaft. Das dritte Jahr kann kommen.",
   [C("Das Jahr mit deinen Freunden feiern",rels={"Harry":3,"Ron":3,"Hermine":3,"Lily":3,"Ginny":3}),
    C("Versprechen, euch über den Sommer zu schreiben",stats={"loyalty":5},rels={"Mama":3,"Papa":3}),
    C("Dich schon auf nächstes Jahr freuen",stats={"reputation":4})],plot="ausklang"),
]

# ── Filler-Pools (Schulalltag, Jahr-2-Flavor) ────────────────────────────────
SUBJECTS=[("Verwandlung","klassenzimmer",["mcgonagall","ron"],"In Verwandlung sollt ihr heute einen Käfer in einen Knopf verwandeln. Ron seufzt, McGonagall hebt mahnend die Braue."),
 ("Zauberkunst","klassenzimmer",["hermine"],"Professor Flitwick übt mit euch einen kniffligen Schwebezauber für mehrere Gegenstände. Hermine jongliert schon drei auf einmal."),
 ("Zaubertränke","klassenzimmer",["snape","malfoy"],"Im Kerker braut ihr unter Snapes Adlerblick einen Schwelltrank. Malfoy gibt nebenbei mit seinem an."),
 ("Kräuterkunde","gewaechshaeuser",["neville","hermine"],"Bei Professor Sprout pflegt ihr eine bissige Pflanze, die nach Fingern schnappt. Neville hat den Dreh raus."),
 ("Verteidigung","klassenzimmer",["lockhart","harry"],"Lockhart liest theatralisch aus einem seiner Bücher vor, statt etwas Nützliches zu zeigen. Ihr nehmt euch insgeheim selbst etwas vor."),
 ("Astronomie","treppenhaus",["lily"],"Mitternachts auf dem Turm kartiert ihr ferne Sterne. Lily zeigt dir lässig den hellsten Punkt am Himmel."),
 ("Geschichte der Zauberei","klassenzimmer",["hermine","ron"],"Professor Binns murmelt von uralten Schulgründern. Ausnahmsweise spitzt ihr die Ohren — vielleicht steckt ein Hinweis drin.")]
def subj(i):
    n,loc,present,s=SUBJECTS[i%len(SUBJECTS)]
    return (f"Unterricht: {n}","schule",loc,[P]+present,s,
     [C("Dich konzentrieren und es meistern",stats={"wisdom":6}),
      C("Einem Mitschüler helfen",stats={"loyalty":5},rels={"Neville":5}),
      C("Heimlich ein wenig experimentieren",canon=False,stats={"combat":4})])
MEALS=["Beim Frühstück segeln die Posteulen herein; ein Paket von zu Hause lässt Robins Herz hüpfen.",
 "Mittagessen in der Großen Halle — überall wird über die Kammer getuschelt, aber das Essen schmeckt trotzdem.",
 "Abendessen mit Kürbissaft und Kuchen; Lily macht trockene Witze über Lockharts neue Frisur.",
 "Verschlafenes Frühstück; Ginny setzt sich zaghaft näher zu euch.",
 "Festtagsschmaus mit Bergen von Nachtisch; Ron schafft erstaunlich viel."]
def meal(i): return ("In der Großen Halle","alltag","grosse_halle",[P,"lily","ron"],MEALS[i%len(MEALS)],
  [C("Dich zu den Freunden setzen",stats={"reputation":4},rels={"Lily":3}),C("In Ruhe essen",stats={"loyalty":3}),C("Ginny an euren Tisch winken",rels={"Ginny":4})])
COMMON=["Am Kamin baut Ron sein Zauberschach auf und sucht einen Gegner.",
 "Hausaufgaben-Chaos: Pergament, Tinte, und Lockharts seltsame Quizfragen.",
 "Gemütlicher Regenabend; jemand erzählt (harmlose) Schauergeschichten über die Kammer.",
 "Die Gang sitzt zusammen und schmiedet Pläne fürs Wochenende.",
 "Lily lümmelt im Sessel und kommentiert lässig das Treiben."]
def common(i): return ("Abend im Gemeinschaftsraum","alltag","gryffindor_turm",[P,"lily","ron","harry"],COMMON[i%len(COMMON)],
  [C("Mitspielen und abhängen",stats={"loyalty":4},rels={"Ron":3}),C("Mit Lily quatschen",rels={"Lily":4}),C("Früh ins Bett",canon=False,stats={"wisdom":2})])
GROUNDS=["Auf den Ländereien hebt der Riesenkrake harmlos eine Tentakel.",
 "Hagrid winkt euch zu seiner Hütte; es duftet nach Kakao.",
 "Spaziergang am Waldrand; Flocke flitzt fröhlich voraus.",
 "Am Seeufer lässt jemand mit Magie Steine übers Wasser tanzen."]
def grounds(i): return ("Auf den Ländereien","alltag","ländereien_see",[P,"hagrid","flocke"],GROUNDS[i%len(GROUNDS)],
  [C("Hagrid besuchen",rels={"Hagrid":5}),C("Mit Flocke toben",rels={"Flocke":5}),C("Frische Luft genießen",stats={"loyalty":3})])
def owl(i): return ("In der Eulerei","alltag","eulerei",[P,"flocke"],
  ["Du schickst Mama und Papa einen Brief, was du Neues erlebt hast.","Du fragst nach Neuigkeiten von zu Hause.","Deine Lieblingseule schuhut erwartungsvoll."][i%3],
  [C("Mama & Papa schreiben",stats={"loyalty":6},rels={"Mama":4,"Papa":4}),C("Auf Antwort von zuhause hoffen",rels={"Mama":3,"Papa":3}),C("Der Eule einen Keks geben",stats={"reputation":2})])
def court(i):
    txt=["Im Innenhof geht ein kleiner Zauber daneben — alle lachen.","Malfoy gibt an; Lily verdreht lässig die Augen.","Pause an der frischen Luft, Tauben gurren auf den Arkaden."][i%3]
    pres=[P,"lily"]+(["malfoy"] if i%3==1 else [])
    return ("Im Innenhof","alltag","innenhof",pres,txt,
     [C("Mit Lily plaudern",rels={"Lily":4}),C("Malfoy ignorieren",stats={"wisdom":4}),C("Einem Erstklässler helfen",stats={"loyalty":4},rels={"Ginny":3})])

XPOOL=[("gang","Abend mit der Gang","gryffindor_turm",["lily","harry","ron","hermine"],
        "Die ganze Runde sitzt zusammen, lacht über den Tag und hält fest zusammen.",{"Harry":6,"Ron":6,"Hermine":5},
        "Ein langer Kaminabend schweißte die Gang enger zusammen. Du warst woanders."),
 ("ginny","Ginny aufmuntern","grosse_halle",["ginny"],
   "Die schüchterne Ginny taut bei dir auf, und ihr lacht zusammen — eine neue Freundschaft.",{"Ginny":10},
   "Jemand nahm sich Zeit für die stille Ginny. Diesmal warst du es nicht."),
 ("hermine","Lernen mit Hermine","bibliothek",["hermine"],
   "Hermine teilt geduldig ihr Wissen, bis bei dir der Knoten platzt.",{"Hermine":10},
   "Hermine half einer Lerngruppe durch den Stoff. Du hast allein gelernt."),
 ("ron","Zauberschach mit Ron","gryffindor_turm",["ron"],
   "Ron fordert dich zu Zauberschach heraus und feuert lautstark seine Figuren an.",{"Ron":10},
   "Ron besiegte am Kamin alle im Zauberschach. Du warst nicht dabei."),
 ("mystery","Der Kammer auf der Spur","bibliothek",["harry","hermine","ron"],
   "Zu viert verfolgt ihr eine neue Spur zur Kammer — leise, vorsichtig, und immer zusammen.",{"Harry":5,"Ron":5,"Hermine":5},
   "Die anderen verfolgten eine Spur zur Kammer. Du hast davon nur gehört."),
 ("lily","Streifzug mit Lily","treppenhaus",["lily"],
   "Lily kennt geheime Ecken des Schlosses und nimmt dich lässig mit auf Entdeckungstour.",{"Lily":8},
   "Lily erkundete die verborgenen Gänge. Du hast den Abend anders verbracht."),
 ("hagrid","Kakao bei Hagrid","hagrids_huette",["hagrid"],
   "Bei (sehr heißem) Kakao erzählt Hagrid von seinen Lieblingstieren und passt herzlich auf.",{"Hagrid":8},
   "Hagrid hatte Besuch zum Kakao. Du warst nicht dabei."),
 ("neville","Neville beistehen","gewaechshaeuser",["neville"],
   "Neville verliert beinahe den Mut; du bleibst an seiner Seite, bis er strahlt.",{"Neville":10,"Harry":3},
   "Jemand stand Neville bei, bis er aufblühte. Diesmal nicht du.")]
def xbeat(i,month):
    k,title,loc,present,s,rels,recap=XPOOL[i%len(XPOOL)]
    return (title,"wendepunkt",loc,[P]+present,s,
      [C("Voll dabei sein und mitmachen",canon=True,docks=True,stats={"loyalty":6,"reputation":3},rels=dict(rels)),
       C("Eine Weile zuschauen und genießen",canon=True,stats={"wisdom":3},rels={list(rels)[0]:3}),
       C("Diesmal für dich bleiben",canon=False,stats={"wisdom":2})],recap)

def mk(beat_tuple,month,chapter,cross=False):
    if cross:
        title,ptype,loc,present,s,choices,recap=beat_tuple
        b={"id":hid(),"chapter":chapter,"scene_index":0,"title":f"{title} (Jahr 2 · {month})",
           "school_time":f"{month} (Jahr 2) — Schulalltag","characters_present":present,"location":loc,
           "summary":s,"plot_type":ptype,"challenge_potential":3,"crossing_point":True,
           "clique_bond_delta":1,"autonomous_recap":recap,"choices":choices,"next_scenes":[]}
    else:
        title,ptype,loc,present,s,choices=beat_tuple
        b={"id":hid(),"chapter":chapter,"scene_index":0,"title":f"{title} (Jahr 2 · {month})",
           "school_time":f"{month} (Jahr 2) — Schulalltag","characters_present":present,"location":loc,
           "summary":s,"plot_type":ptype,"challenge_potential":2,"crossing_point":False,
           "choices":choices,"next_scenes":[]}
    return b

GAPS=[("y2_s03",18,"September",8),("y2_s06",20,"Oktober",8),("y2_s09",20,"November",9),
      ("y2_s12",24,"Januar",10),("y2_s15",12,"April",11),("y2_s18",10,"Juni",12)]
cats=["subj","meal","common","grounds","owl","court","subj","common"]
gi=0; xi=0; ci=0
gapblocks={}
for anchor_id,n,month,chap in GAPS:
    block=[]
    for k in range(n):
        if k%2==1:
            b=mk(xbeat(xi,month),month,chap,cross=True); xi+=1
        else:
            cat=cats[ci%len(cats)]; ci+=1
            f={"subj":subj,"meal":meal,"common":common,"grounds":grounds,"owl":owl,"court":court}[cat](gi); gi+=1
            b=mk(f,month,chap,cross=False)
        block.append(b)
    gapblocks[anchor_id]=block

# Jahr-2-Reihe zusammensetzen (Backbone + Filler in Lücken)
y2=[]
for a in backbone:
    y2.append(a)
    if a["id"] in gapblocks: y2.extend(gapblocks[a["id"]])

# An bestehende Liste hängen, dann ALLES linear neu verdrahten
allscenes=existing+y2
for i,s in enumerate(allscenes):
    s["next_scenes"]=[allscenes[i+1]["id"]] if i+1<len(allscenes) else []
data["scenes"]=allscenes
json.dump(data,open(os.path.join(BOOK,"plot_graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

cross=[s for s in allscenes if s.get("crossing_point")]
print("Gesamt-Szenen:",len(allscenes),"| davon Jahr 2:",len(y2))
print("Kreuzungen gesamt:",len(cross))
bad=[s["id"] for s in allscenes if s.get("crossing_point") and not s.get("autonomous_recap")]
print("Kreuzungen ohne recap:",bad or "keine")
ids={s["id"] for s in allscenes}
broken=[s["id"] for s in allscenes if s["next_scenes"] and s["next_scenes"][0] not in ids]
print("kaputte Verweise:",broken or "keine","| y1_s12.next:",next(s for s in allscenes if s["id"]=="y1_s12")["next_scenes"])
