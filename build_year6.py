#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahr 6 — 'Der Halbblutprinz' (~12, Film-Niveau) als NAHTLOSE Fortsetzung. Haengt hinter y5_s19 an.

Ton ~12 / HP-Film: ernst, spannend, viel altersgerechte Romantik (verknallt, kichern, erste
Verliebtheit), aber ohne grausige Bilder. Kanon-Verlust: Dumbledore stirbt durch Snapes Verrat
auf dem Astronomieturm — wuerdevoll und traurig erzaehlt, ohne Gore; die Schule trauert, die
Erwachsenen halten zusammen, am Ende ein Versprechen, seinen Weg weiterzugehen.
Aufruf: python3 build_year6.py
"""
import json, os, itertools
HERE=os.path.dirname(os.path.abspath(__file__)); BOOK=os.path.join(HERE,"skill","data","books","hogwarts")
data=json.load(open(os.path.join(BOOK,"plot_graph.json"),encoding="utf-8")); existing=data["scenes"]
if any(s["id"].startswith("y6_") for s in existing): raise SystemExit("Jahr 6 existiert bereits.")
_c=itertools.count(1)
def nid(): return f"n{next(_c):03d}"
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
 A("y6_s01",31,"Ein wachsamer Sommer in der Winkelgasse","Ende der Ferien — Winkelgasse",
   [P,"lily","harry","hermine"],"winkelgasse",
   "Die Winkelgasse ist stiller und ernster geworden — ueberall Plakate, die zur Wachsamkeit mahnen. Trotzdem haltet ihr zusammen, besorgt eure Sachen und lasst euch die Vorfreude aufs neue Jahr nicht nehmen. Nur Malfoy wirkt seltsam verschlossen.",
   [C("Mit Lily und den Freunden zusammenbleiben",stats={"loyalty":4},rels={"Lily":3}),
    C("Aufmerksam beobachten, was um euch herum vorgeht",stats={"wisdom":4}),
    C("Dir Malfoys merkwuerdiges Verhalten merken",stats={"wisdom":4})]),
 A("y6_s02",31,"Professor Slughorn","1. September — Grosse Halle",
   [P,"slughorn","harry"],"grosse_halle",
   "Ein neuer Lehrer sorgt fuer gute Laune: der jovial-gesellige Professor Slughorn, ein Meister der Zaubertraenke, der gern begabte Schueler um sich sammelt. Schon beim Festmahl verteilt er Einladungen zu seinem 'Slug-Club'.",
   [C("Slughorns schwungvolle Art mit einem Schmunzeln nehmen",stats={"reputation":4}),
    C("Neugierig sein, was es mit dem Slug-Club auf sich hat",stats={"wisdom":3}),
    C("Dich auf richtig guten Traenkeunterricht freuen",stats={"wisdom":4})]),
 A("y6_s03",31,"Der Slug-Club","September — Slughorns Empfang",cp=True,
   present=[P,"slughorn","hermine","ginny"],loc="slug_club",
   summ="Bei kandierter Ananas und Kerzenschein laedt Slughorn zu einem gemuetlichen Empfang. Man lernt sich kennen, lacht, knuepft Freundschaften — ein harmlos-geselliger Abend, bei dem auch Ginny und Hermine dabei sind.",
   choices=[C("Mit den anderen plaudern und neue Bekanntschaften schliessen",canon=True,docks=True,stats={"reputation":5,"loyalty":3},rels={"Hermine":4,"Ginny":4}),
    C("Slughorn hoeflich Loecher in den Bauch fragen",canon=True,stats={"wisdom":4}),
    C("Den geselligen Abend einfach geniessen",canon=True,stats={"loyalty":3})],
   recap="Slughorns Empfang war ein geselliger Abend mit neuen Bekanntschaften. Du warst nicht dabei.",plot="ruhe"),
 A("y6_s04",32,"Das geheimnisvolle Traenkebuch","September — Zaubertraenke",
   [P,"slughorn","harry","hermine"],"klassenzimmer",
   "In Slughorns Unterricht entdeckt Harry ein altes Lehrbuch voller handschriftlicher Notizen, signiert vom 'Halbblutprinzen' — und ploetzlich gelingen ihm die Traenke wie von selbst. Wer war dieser geheimnisvolle Prinz? Ein spannendes kleines Raetsel.",
   [C("Mit Hermine ueber das raetselhafte Buch nachdenken",stats={"wisdom":5},rels={"Hermine":4}),
    C("Harry raten, vorsichtig mit fremden Notizen zu sein",stats={"reputation":3},rels={"Harry":3}),
    C("Selbst aufmerksam im Unterricht mittueffteln",stats={"wisdom":4})]),
 A("y6_s05",32,"Quidditch: Harry als Kapitaen","Oktober — Turnier-Arena",cp=True,
   present=[P,"harry","ron","ginny"],loc="turnier_arena",
   summ="Harry ist jetzt Kapitaen der Gryffindor-Mannschaft! Bei den Sichtungen fiebert ihr mit, Ron huetet nervoes die Tore und Ginny zeigt, was in ihr steckt. Teamgeist pur.",
   choices=[C("Die Mannschaft lautstark anfeuern",canon=True,docks=True,stats={"reputation":5,"loyalty":3},rels={"Harry":5,"Ron":4,"Ginny":3}),
    C("Ron Mut machen, der vor Aufregung zittert",canon=True,rels={"Ron":5}),
    C("Ginnys Talent bewundern",canon=True,rels={"Ginny":4})],
   recap="Bei den Quidditch-Sichtungen herrschte Teamgeist. Du warst diesmal nicht dabei.",plot="abenteuer"),
 A("y6_s06",32,"Romantik liegt in der Luft","November — Gryffindor-Turm",
   [P,"ron","lavender","hermine","ginny"],"gryffindor_turm",
   "Ploetzlich ist die Luft voller Verliebtheit: Ron und die kichernde Lavender sind ein Paar (zu Hermines Verdruss), und auch sonst wird viel geschwaermt und getuschelt. Es ist zum Schmunzeln — erstes Verknalltsein eben, mal suess, mal kompliziert.",
   [C("Hermine troesten, die eifersuechtig und traurig ist",stats={"loyalty":5},rels={"Hermine":6}),
    C("Ueber das ganze Verliebtsein herzlich schmunzeln",stats={"reputation":3}),
    C("Mit Ginny ueber Schwaermereien tuscheln",rels={"Ginny":4})],plot="ruhe"),
 A("y6_s07",33,"Dumbledores Stunden: Reise in die Vergangenheit","November — Dumbledores Buero",
   [P,"dumbledore","harry"],"schulleiterbuero",
   "In besonderen Stunden taucht Dumbledore mit Harry (und du darfst zuhoeren) in alte Erinnerungen ein — in die Vergangenheit eines einsamen Jungen, der spaeter zum gefuerchteten Voldemort wurde. Geheimnisvoll und lehrreich: Um den Feind zu verstehen, muss man seine Geschichte kennen.",
   [C("Gebannt den Erinnerungen folgen",stats={"wisdom":6}),
    C("Mit Harry ueberlegen, was die Hinweise bedeuten",stats={"wisdom":5},rels={"Harry":4}),
    C("Dumbledores ruhige Weisheit aufsaugen",rels={"Dumbledore":4})]),
 A("y6_s08",33,"Sorge um Malfoy","Dezember — bewegliche Treppen",cp=True,
   present=[P,"harry","hermine","ron"],loc="treppenhaus",
   summ="Malfoy ist blass, verschlossen und staendig irgendwo verschwunden — als trage er eine schwere Last und plane etwas im Geheimen. Harry ist alarmiert. Vorsichtig und ohne Unueberlegtheiten geht ihr der Sache nach.",
   choices=[C("Gemeinsam vorsichtig herausfinden, was mit Malfoy los ist",canon=True,docks=True,stats={"wisdom":5,"loyalty":4},rels={"Harry":5,"Hermine":4,"Ron":4}),
    C("Vorschlagen, einen Lehrer einzuweihen",canon=True,stats={"reputation":4}),
    C("Auch Mitgefuehl fuer Malfoy haben, der bedrueckt wirkt",canon=False,stats={"wisdom":4})],
   recap="Die Freunde gruebelten ueber Malfoys Geheimnis. Du warst diesmal nicht dabei.",plot="wendepunkt"),
 A("y6_s09",33,"Ein gefaehrlicher Unfall","Januar — Krankenfluegel",
   [P,"ron","pomfrey","harry"],"krankenfluegel",
   "Dunkle Dinge schleichen sich ein: Ein verfluchtes Mitbringsel und ein vergifteter Schluck — eigentlich fuer jemand anderen gedacht — erwischen aus Versehen Ron. Es ist ein Schreck, doch Madam Pomfrey hat alles im Griff, und Ron erholt sich wieder. Erleichterung nach der Angst.",
   [C("An Rons Bett wachen, bis es ihm besser geht",stats={"loyalty":6},rels={"Ron":6,"Harry":3}),
    C("Madam Pomfrey vertrauen und helfen, wo du kannst",rels={"Harry":2} if False else {"Hermine":3}),
    C("Erleichtert aufatmen, als Ron die Augen aufschlaegt",stats={"loyalty":4})],plot="wendepunkt"),
 A("y6_s10",34,"Ein warmer Moment im Winter","Dezember/Januar — Gryffindor-Turm",cp=True,
   present=[P,"lily","ron","hermine","ginny"],loc="gryffindor_turm",
   summ="Mitten in unruhigen Zeiten tut ein gemuetlicher Winterabend gut: Kaminfeuer, heisser Kakao, Geschichten und Lachen mit den Freunden. Solche warmen Momente geben Kraft fuer alles, was kommt.",
   choices=[C("Den gemuetlichen Abend mit allen geniessen",canon=True,docks=True,stats={"loyalty":5,"reputation":3},rels={"Lily":4,"Ron":3,"Hermine":3,"Ginny":3}),
    C("Hermine und Ron wieder ein bisschen zusammenbringen",canon=True,rels={"Hermine":3,"Ron":3}),
    C("Einen Brief voller Waerme nach Hause schicken",canon=True,rels={"Mama":4,"Papa":4})],
   recap="Ein warmer Winterabend gab der Gang Kraft. Du warst diesmal nicht dabei.",plot="ruhe"),
 A("y6_s11",34,"Erste Verliebtheit","Februar — Innenhof",cp=True,
   present=[P,"ginny","harry","luna"],loc="innenhof",
   summ="Die Gefuehle ordnen sich neu: Harry merkt, dass ihm Ginny mehr bedeutet, als er dachte, und ueberall wird ein bisschen geschwaermt. Alles ganz zart und altersgerecht — Schmetterlinge im Bauch, ein schuechternes Laecheln, vielleicht ein erster gemeinsamer Spaziergang.",
   choices=[C("Den Verliebten augenzwinkernd den Ruecken staerken",canon=True,docks=True,stats={"loyalty":5},rels={"Ginny":5,"Harry":4}),
    C("Mit Luna ueber das ganze Geschwaerme schmunzeln",canon=True,rels={"Luna":4}),
    C("Dir vielleicht selbst eingestehen, dass du jemanden nett findest",canon=True,stats={"reputation":3})],
   recap="Es wurde viel geschwaermt in jenen Tagen. Du hast den Trubel diesmal verpasst.",plot="ruhe"),
 A("y6_s12",34,"Die Wahrheit ueber Voldemort","Maerz — Dumbledores Buero",
   [P,"dumbledore","harry","slughorn"],"schulleiterbuero",
   "Eine entscheidende Erinnerung — Slughorn hat sie lange verborgen — bringt es ans Licht: Voldemort hat dunkle Magie benutzt, um sich an die Welt zu klammern. Dumbledore erklaert ruhig, dass man genau das verstehen muss, um ihn eines Tages aufzuhalten.",
   [C("Aufmerksam zuhoeren und dir alles merken",stats={"wisdom":6}),
    C("Slughorn fuer seinen Mut danken, die Wahrheit zu teilen",rels={"Slughorn":4}),
    C("Mit Harry ueber die schwere Aufgabe sprechen, die vor ihm liegt",rels={"Harry":4})],plot="wendepunkt"),
 A("y6_s13",35,"Dumbledore vertraut Harry","Juni — Dumbledores Buero",
   [P,"dumbledore","harry"],"schulleiterbuero",
   "Dumbledore bereitet sich vor, einer grossen Gefahr entgegenzutreten, um Voldemort zu schwaechen — und er waehlt ausgerechnet Harry, ihn zu begleiten. Ein Moment voller Vertrauen und Ernst. Euch anderen traegt er auf, in der Schule wachsam zu sein.",
   [C("Harry Mut zusprechen fuer den gefaehrlichen Weg",stats={"loyalty":5},rels={"Harry":5}),
    C("Versprechen, in der Schule gut aufzupassen",stats={"reputation":4},rels={"Dumbledore":4}),
    C("Ein mulmiges, aber entschlossenes Gefuehl annehmen",stats={"wisdom":3})],plot="finale"),
 A("y6_s14",35,"Wache halten — die DA ist bereit","Juni — Raum der Wuensche",cp=True,
   present=[P,"luna","neville","ginny","ron","hermine"],loc="raum_der_wuensche",
   summ="Waehrend Dumbledore und Harry fort sind, haelt die DA in der Schule Wache. Ihr seid vorbereitet, mutig und zusammen — bereit, einander zu schuetzen, falls in dieser Nacht etwas geschieht.",
   choices=[C("Entschlossen mit der DA Wache halten",canon=True,docks=True,stats={"combat":5,"loyalty":6},rels={"Luna":4,"Neville":4,"Ginny":3,"Ron":3,"Hermine":3}),
    C("Die Juengeren beruhigen und beschuetzen",canon=True,stats={"loyalty":5}),
    C("Auf jedes Geraeusch im Schloss achten",canon=True,stats={"wisdom":4})],
   recap="Die DA hielt in jener Nacht Wache. Du warst diesmal nicht dabei.",plot="finale"),
 A("y6_s15",35,"Die Nacht des Angriffs","Juni — im Schloss",
   [P,"harry","luna","neville","ginny"],"treppenhaus",
   "In der Nacht gelingt es dunklen Gestalten, ins Schloss einzudringen — Malfoys schwere Last hat damit zu tun. Es wird gefaehrlich und hektisch, doch die DA und der Orden stellen sich ihnen entgegen, und ihr beschuetzt einander tapfer. (Spannung und Gefahr, aber kein grausiges Bild.)",
   [C("Mit dem in der DA Gelernten zusammen standhalten",stats={"combat":6,"loyalty":5},rels={"Harry":3,"Luna":3,"Neville":3}),
    C("Ruhe bewahren und Mitschueler in Sicherheit bringen",stats={"loyalty":6}),
    C("Nach den Lehrern rufen, die sofort eingreifen",stats={"reputation":4})],plot="finale"),
 A("y6_s16",36,"Auf dem Astronomieturm","Juni — Astronomieturm",
   [P,"dumbledore","snape","malfoy"],"astronomieturm",
   "Hoch oben auf dem Turm spitzt sich alles zu: Der geschwaechte Dumbledore steht Malfoy gegenueber — der seine dunkle Aufgabe doch nicht vollbringen kann. Dann aber kommt Snape, und das Unfassbare geschieht: Dumbledore, der gueetigste Zauberer von allen, kommt ums Leben. (Erzaehlt mit Trauer und Wuerde, ohne grausige Bilder — ein Verrat, der allen das Herz bricht.)",
   [C("Fassungslos begreifen, was geschehen ist",stats={"loyalty":4}),
    C("An die anderen denken und Halt suchen",stats={"loyalty":5},rels={"Harry":4}),
    C("Dumbledores Guete fest in deinem Herzen bewahren",stats={"wisdom":4,"loyalty":4})],plot="finale"),
 A("y6_s17",36,"Trauer um Dumbledore","Juni — Grosse Halle",
   [P,"mcgonagall","harry","lily"],"grosse_halle",
   "Die ganze Schule ist wie betaeubt vor Trauer. Professor McGonagall haelt mit ruhiger Wuerde alles zusammen, und ueberall troesten sich Schueler und Lehrer gegenseitig. Der Verlust ist riesig — aber niemand traegt ihn allein.",
   [C("Mit Harry und den Freunden gemeinsam trauern",stats={"loyalty":6},rels={"Harry":5,"Lily":3}),
    C("Jemanden in den Arm nehmen, der weint",stats={"loyalty":5}),
    C("Aus McGonagalls Staerke ein wenig Halt schoepfen",stats={"wisdom":3})],plot="wendepunkt"),
 A("y6_s18",36,"Abschied am See","Juni — Laendereien am See",
   [P,"harry","ron","hermine","luna","ginny"],"ländereien_see",
   "Am Ufer des Sees nehmen alle gemeinsam Abschied von Dumbledore — Schueler, Lehrer und sogar die Geschoepfe des Sees und des Waldes. Es ist ein feierlicher, schoener Moment voller Dankbarkeit, der trotz aller Trauer Hoffnung und Zusammenhalt spuerbar macht.",
   [C("Im stillen Gedenken Dumbledore Danke sagen",stats={"loyalty":5},rels={"Harry":3}),
    C("Die Freunde fest an dich druecken",stats={"loyalty":5},rels={"Ron":3,"Hermine":3,"Luna":3}),
    C("Dir vornehmen, in seinem Sinne weiterzumachen",stats={"wisdom":4})],plot="ausklang"),
 A("y6_s19",36,"Ein Versprechen","Juni — Schuljahresende",
   [P,"harry","ron","hermine"],"grosse_halle",
   "Das Jahr endet schwer, aber nicht ohne Mut: Harry beschliesst, Dumbledores begonnenen Weg zu Ende zu gehen und Voldemort aufzuhalten — und seine treuesten Freunde stehen fest an seiner Seite. Was auch kommt, ihr geht es gemeinsam. Ein Versprechen, das traegt.",
   [C("Harry versprechen, an seiner Seite zu bleiben",stats={"loyalty":6},rels={"Harry":6,"Ron":3,"Hermine":3}),
    C("Mut aus eurer Freundschaft schoepfen",rels={"Ron":3,"Hermine":3}),
    C("Entschlossen und zuversichtlich nach vorn blicken",stats={"combat":3,"wisdom":4})],plot="ausklang"),
]
for b in backbone: b["chapter"]=int(b["chapter"])
backbone[8]["choices"][1]=C("Madam Pomfrey vertrauen und helfen, wo du kannst",stats={"loyalty":3},rels={"Hermine":3})

SUBJ=[("Zaubertraenke bei Slughorn","klassenzimmer",["slughorn","harry"],
       "Slughorn lobt ueberschwaenglich die besten Traenke und verteilt gute Laune. Heute brodeln die Kessel um die Wette."),
 ("Zauberkunst","klassenzimmer",["flitwick","hermine"],
  "Professor Flitwick huepft vor Begeisterung ueber einen anspruchsvollen Zauber. Hermine kann ihn schon."),
 ("Verwandlung","klassenzimmer",["mcgonagall","ron"],
  "Professor McGonagall fordert euch mit einer kniffligen Verwandlung. Ron seufzt, gibt aber sein Bestes."),
 ("Kraeuterkunde","gewaechshaeuser",["sprout","neville"],
  "Professor Sprout zeigt eine seltene Heilpflanze. Neville ist in seinem Element."),
 ("Verteidigung gegen die dunklen Kuenste","klassenzimmer",["snape","harry"],
  "Diesmal unterrichtet Snape Verteidigung — streng und fordernd. Ihr lernt, ernsthaft wachsam zu sein."),
 ("Pflege magischer Geschoepfe","pflege_gehege",["hagrid"],
  "Hagrid stellt stolz ein neues Geschoepf vor. Hoeflich bleiben, dann wird es ein Freund.")]
def subj(i):
    n,loc,pr,s=SUBJ[i%len(SUBJ)]
    return (f"Unterricht: {n}","schule",loc,[P]+pr,s,[C("Konzentrieren und meistern",stats={"wisdom":6}),
      C("Einem Mitschueler helfen",stats={"loyalty":5},rels={"Neville":5}),C("Mutig Neues probieren",canon=False,stats={"combat":4})])
MEAL=["Beim Fruehstueck wird ueber Slughorns naechste Feier und ueber Verknalltsein getuschelt.","Mittagessen — Lavender kichert um Ron herum, Hermine schaut betont weg.",
 "Abendessen; trotz ernster Zeiten sorgt die Gang fuereinander fuer gute Laune.","Warme Schokolade nach einem langen Tag — Freundschaft schmeckt am besten."]
def meal(i): return ("In der Grossen Halle","alltag","grosse_halle",[P,"lily","ginny"],MEAL[i%len(MEAL)],
  [C("Zu den Freunden setzen",stats={"reputation":4},rels={"Lily":3}),C("Mit Ginny tuscheln",rels={"Ginny":4}),C("In Ruhe geniessen",stats={"loyalty":3})])
COMMON=["Am Kamin tuschelt die ganze Runde ueber das geheimnisvolle Traenkebuch.","Hausaufgaben-Chaos, dazwischen viel Gekicher ueber wer-mag-wen.",
 "Gemuetlicher Abend; Ron und Lavender turteln, Hermine vergraebt sich in ein Buch.","Ron baut sein Zauberschach auf und sucht einen Gegner."]
def common(i): return ("Abend im Gemeinschaftsraum","alltag","gryffindor_turm",[P,"lily","ron","harry"],COMMON[i%len(COMMON)],
  [C("Mitmachen und abhaengen",stats={"loyalty":4},rels={"Ron":3}),C("Hermine ein bisschen aufmuntern",rels={"Hermine":4}),C("Frueh ins Bett",canon=False,stats={"wisdom":2})])
GROUND=["Auf den Laendereien geniesst ihr trotz allem die Sonne.","Hagrid winkt zu seiner Huette; Kakao und eine Tiergeschichte warten.",
 "Spaziergang am See; Flocke flitzt froehlich voraus.","Am Ufer wird ueber wer-mit-wem geschwaermt und gelacht."]
def ground(i): return ("Auf den Laendereien","alltag","ländereien_see",[P,"hagrid","flocke"],GROUND[i%len(GROUND)],
  [C("Hagrid besuchen",rels={"Hagrid":5}),C("Mit Flocke toben",rels={"Flocke":5}),C("Frische Luft geniessen",stats={"loyalty":3})])
def owl(i): return ("In der Eulerei","alltag","eulerei",[P,"flocke"],
  ["Du schreibst nach Hause, dass ihr zusammenhaltet.","Du fragst nach Neuigkeiten von zu Hause.","Deine Lieblingseule schuhut erwartungsvoll."][i%3],
  [C("Nach Hause schreiben",stats={"loyalty":6},rels={"Mama":4,"Papa":4}),C("Auf Antwort hoffen",rels={"Mama":3,"Papa":3}),C("Der Eule einen Keks geben",stats={"reputation":2})])
def club(i): return ("Bei Slughorns Empfang","alltag","slug_club",[P,"slughorn","ginny"],
  ["Kandierte Ananas, Kerzenschein und gesellige Gespraeche bei Slughorn.","Slughorn erzaehlt stolz von ehemaligen Schuelern.","Ein harmlos-gemuetlicher Abend voller Lachen."][i%3],
  [C("Gesellig plaudern und Freundschaften pflegen",stats={"reputation":4},rels={"Ginny":3}),C("Slughorn hoeflich ausfragen",stats={"wisdom":4},rels={"Slughorn":3}),C("Den Abend geniessen",stats={"loyalty":3})])
XPOOL=[("gang","Abend mit der Gang","gryffindor_turm",["harry","ron","hermine"],
        "Die ganze Runde sitzt zusammen, lacht und haelt fest zusammen.",{"Harry":6,"Ron":6,"Hermine":5},
        "Ein Kaminabend schweisste die Gang enger zusammen. Du warst woanders."),
 ("hermine","Hermine troesten","bibliothek",["hermine"],
   "Hermine ist wegen all der Verliebtheits-Wirren traurig; du hoerst ihr zu und munterst sie auf.",{"Hermine":10},
   "Jemand troestete Hermine. Diesmal nicht du."),
 ("ginny","Zeit mit Ginny","innenhof",["ginny"],
   "Mit Ginny lachen, schwaermen und ueber das Leben reden — eine warme, ehrliche Freundschaft.",{"Ginny":10},
   "Ginny verbrachte Zeit mit Freunden. Diesmal nicht mit dir."),
 ("luna","Zeit mit Luna","ländereien_see",["luna"],
   "Mit Luna die Welt mit anderen Augen sehen — ruhig, ehrlich, voller Weisheit.",{"Luna":10},
   "Luna verbrachte Zeit mit Freunden. Diesmal nicht mit dir."),
 ("neville","Neville staerken","gewaechshaeuser",["neville"],
   "Neville waechst weiter ueber sich hinaus; du uebst mit ihm, bis er strahlt.",{"Neville":10,"Harry":3},
   "Jemand staerkte Neville. Diesmal nicht du."),
 ("slug","Slughorns Runde","slug_club",["slughorn"],
   "Bei Slughorns Empfang knuepfst du nette Bekanntschaften und hoerst spannende Geschichten.",{"Slughorn":8},
   "Slughorn hatte Gaeste zur Runde. Du warst nicht dabei."),
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
        return {"id":nid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 6 - {month})","school_time":f"{month} (Jahr 6) - Schulalltag",
                "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":3,
                "crossing_point":True,"clique_bond_delta":1,"autonomous_recap":recap,"choices":choices,"next_scenes":[]}
    title,ptype,loc,pr,s,choices=t
    return {"id":nid(),"chapter":chap,"scene_index":0,"title":f"{title} (Jahr 6 - {month})","school_time":f"{month} (Jahr 6) - Schulalltag",
            "characters_present":pr,"location":loc,"summary":s,"plot_type":ptype,"challenge_potential":2,
            "crossing_point":False,"choices":choices,"next_scenes":[]}
GAPS=[("y6_s03",18,"September",31),("y6_s06",20,"November",32),("y6_s09",24,"Dezember",33),
      ("y6_s12",24,"Februar",34),("y6_s15",14,"Juni",35)]
cats=["subj","meal","common","ground","owl","club","subj","common"]
gi=xi=ci=0; gapblocks={}
for aid,n,month,chap in GAPS:
    block=[]
    for k in range(n):
        if k%2==1: block.append(mk(x(xi),month,chap,cross=True)); xi+=1
        else:
            cat=cats[ci%len(cats)]; ci+=1
            f={"subj":subj,"meal":meal,"common":common,"ground":ground,"owl":owl,"club":club}[cat](gi); gi+=1
            block.append(mk(f,month,chap,cross=False))
    gapblocks[aid]=block
y6=[]
for a in backbone:
    y6.append(a)
    if a["id"] in gapblocks: y6.extend(gapblocks[a["id"]])
allscenes=existing+y6
for i,s in enumerate(allscenes): s["next_scenes"]=[allscenes[i+1]["id"]] if i+1<len(allscenes) else []
data["scenes"]=allscenes
json.dump(data,open(os.path.join(BOOK,"plot_graph.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
cross=[s for s in allscenes if s.get("crossing_point")]
print("Gesamt:",len(allscenes),"| Jahr 6:",len(y6),"| Kreuzungen:",len(cross))
print("y5_s19.next:",next(s for s in allscenes if s["id"]=="y5_s19")["next_scenes"])
print("ohne recap:",[s["id"] for s in allscenes if s.get("crossing_point") and not s.get("autonomous_recap")] or "keine")
ids={s["id"] for s in allscenes}
print("kaputte Verweise:",[s["id"] for s in allscenes if s["next_scenes"] and s["next_scenes"][0] not in ids] or "keine")
