#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Jahres-Generator: webt viele varied Szenen-Seeds (Unterricht, Mahlzeiten,
Gemeinschaftsraum, Bibliothek, Ländereien, Eulerei, Nebenfiguren-Stränge) und
Kreuzungspunkte zwischen die handkuratierten Kanon-Beats. Ergebnis: ein
ausführliches Schuljahr (>=120 Szenen, >=50 Kreuzungen), linear verdrahtet.

Die Beats sind SEEDS — der Spielleiter (GPT-5.5) erzählt sie zur Laufzeit im
kindgerechten, coolen-Lily-Ton aus. Kanon-Rückgrat + Test-IDs bleiben erhalten.
Aufruf:  python3 build_year.py
"""
import json, os, itertools

HERE = os.path.dirname(os.path.abspath(__file__))
BOOK = os.path.join(HERE, "skill", "data", "books", "hogwarts")

data = json.load(open(os.path.join(BOOK, "plot_graph.json"), encoding="utf-8"))
existing = data["scenes"]

# Zähler für eindeutige IDs
_counter = itertools.count(1)
def gid():
    return f"g{next(_counter):03d}"

def C(desc, canon=True, stats=None, rels=None, docks=None):
    c = {"description": desc, "canon": canon}
    if stats: c["stat_effects"] = stats
    if rels: c["relationship_effects"] = rels
    if docks is not None: c["docks"] = docks
    return c

# ── Inhalts-Pools (Szenen-Seeds), bewusst variantenreich ──────────────────────
SUBJECTS = [
    ("Verwandlung", "klassenzimmer", ["mcgonagall", "ron"],
     "Professor McGonagall verwandelt ihr Pult in ein Schwein und zurück — heute sollt ihr ein Streichholz in eine silberne Nadel verwandeln. Neben dir murmelt Ron den Zauberspruch."),
    ("Kräuterkunde", "gewaechshaeuser", ["neville"],
     "In den dampfenden Gewächshäusern zeigt Professor Sprout, wie man zappelnde Springkraut-Schoten erntet, ohne nass zu werden. Neville ist hier in seinem Element."),
    ("Verteidigung gegen die dunklen Künste", "klassenzimmer", ["harry"],
     "Im Klassenzimmer von Professor Quirrell riecht es streng nach Knoblauch. Ihr übt einen einfachen Schutzzauber gegen kichernde Wichtel im Käfig."),
    ("Geschichte der Zauberei", "klassenzimmer", ["hermine", "ron"],
     "Der durchsichtige Professor Binns schwebt durch die Tafel und murmelt von alten Koboldkriegen. Die halbe Klasse döst; Hermine schreibt eifrig mit."),
    ("Astronomie", "treppenhaus", ["lily"],
     "Um Mitternacht steigt ihr mit Teleskopen hinauf und tragt die Monde des Jupiter in eure Sternenkarten ein. Lily zeigt dir lässig das beste Sichtfeld."),
    ("Zauberkunst", "klassenzimmer", ["hermine"],
     "Professor Flitwick lässt euch Gegenstände in leuchtenden Farben erstrahlen. Hermine bekommt sofort ein perfektes Goldgelb hin und schielt zu dir."),
    ("Zaubertränke", "klassenzimmer", ["snape", "malfoy"],
     "Im kühlen Kerker braut ihr unter Snapes strengem Blick einen einfachen Heiltrank. Ein falscher Tropfen, und der Kessel zischt bedrohlich."),
    ("Flugstunde", "ländereien_see", ["harry", "neville"],
     "Auf dem Trainingsrasen übt ihr enge Kurven auf den Schulbesen. Der Wind zerrt an euren Umhängen, und Harry zieht mühelos seine Bahnen."),
]
def subject_beat(i):
    name, loc, present, summ = SUBJECTS[i % len(SUBJECTS)]
    helper = present[-1]
    return ("Unterricht: " + name, "schule", loc, ["player_heroine"] + present, summ,
        [C("Dich konzentrieren und den Zauber meistern", stats={"wisdom": 6}),
         C(f"Einem Mitschüler helfen, der nicht weiterkommt", stats={"loyalty": 5},
           rels={helper.capitalize() if helper in ("ron","harry","neville","hermine") else "Neville": 6}),
         C("Heimlich ein bisschen herumexperimentieren", canon=False, stats={"combat": 4, "wisdom": 2})])

MEALS = [
    "Beim Frühstück türmen sich Toast und Marmelade; die Posteulen segeln herein und werfen Briefe und Pakete ab.",
    "Mittagessen in der Großen Halle: dampfender Eintopf, Stimmengewirr, und am Lehrertisch tuschelt das Kollegium.",
    "Beim Abendessen erzählt man sich die neuesten Schul-Gerüchte; der Kürbissaft fließt in Strömen.",
    "Ein Festtagsessen mit besonders vielen Nachtischen — Lily wettet, wer mehr Pudding schafft.",
    "Verschlafenes Frühstück nach einer kurzen Nacht; jemand hat schon wieder die letzten Schokobrötchen geschnappt.",
    "In der Großen Halle liegt der Tagesprophet aus; eine Schlagzeile sorgt für aufgeregtes Geraune.",
]
def meal_beat(i):
    return ("In der Großen Halle", "alltag", "grosse_halle",
        ["player_heroine", "lily", "ron"], MEALS[i % len(MEALS)],
        [C("Dich zu deinen Freunden setzen und mitlachen", stats={"reputation": 4}, rels={"Lily": 3}),
         C("In Ruhe essen und Kräfte sammeln", stats={"loyalty": 3}),
         C("Die Schlagzeile im Tagespropheten lesen", stats={"wisdom": 4})])

COMMON = [
    "Am Kamin knistert das Feuer; Ron baut sein Zauberschach auf und sucht einen Gegner.",
    "Über den Sesseln liegt fauler Sonntagsfrieden; jemand spielt Snape explodierende Schnippschnapp.",
    "Spät am Abend tuschelt eine kleine Runde über die Geheimnisse des Schlosses.",
    "Hausaufgaben-Chaos: Pergamentrollen, Tintenkleckse und Ron, der über Verwandlung stöhnt.",
    "Draußen prasselt Regen, drinnen ist es warm; Lily hat die Beine über die Sessellehne geschwungen.",
    "Die älteren Schüler erzählen Gruselgeschichten über den Verbotenen Wald — halb so wild, sagt Lily.",
]
def common_beat(i):
    return ("Abend im Gemeinschaftsraum", "alltag", "gryffindor_turm",
        ["player_heroine", "lily", "ron", "harry"], COMMON[i % len(COMMON)],
        [C("Mitspielen und den Abend genießen", stats={"loyalty": 4}, rels={"Ron": 3}),
         C("Mit Lily quatschen und abhängen", rels={"Lily": 4}),
         C("Früh schlafen gehen und ausruhen", canon=False, stats={"wisdom": 2})])

LIBRARY = [
    "Zwischen hohen Regalen sucht ihr Stoff für einen Aufsatz; Hermine hat schon den halben Tisch mit Büchern belegt.",
    "Madam Pince wacht streng über die Stille; ein Buch flüstert leise, als du es aufschlägst.",
    "Du stöberst in der Abteilung für magische Geschöpfe und stößt auf erstaunliche Bilder.",
    "Lerngruppe in der Bibliothek: Hermine erklärt geduldig, Ron kaut am Federkiel.",
]
def library_beat(i):
    return ("In der Bibliothek", "alltag", "bibliothek",
        ["player_heroine", "hermine"], LIBRARY[i % len(LIBRARY)],
        [C("Mit Hermine zusammen recherchieren", stats={"wisdom": 6}, rels={"Hermine": 4}),
         C("Ein Buch über magische Geschöpfe ausleihen", stats={"wisdom": 4}),
         C("Eine kurze Pause an der frischen Luft machen", canon=False, stats={"wisdom": 2})])

GROUNDS = [
    "Auf den Ländereien hebt der Riesenkrake harmlos eine Tentakel aus dem schwarzen See.",
    "Hagrid winkt euch zu seiner Hütte; es duftet nach Kakao und Hundefell.",
    "Ein Spaziergang am Waldrand in der Nachmittagssonne; Vögel zwitschern in den hohen Bäumen.",
    "Auf der Wiese tobt eine Gruppe Erstklässler; Flocke flitzt aufgeregt hinterher.",
    "Am Ufer übt jemand Steine flach übers Wasser springen zu lassen — mit ein bisschen Magie.",
]
def grounds_beat(i):
    return ("Auf den Ländereien", "alltag", "ländereien_see",
        ["player_heroine", "hagrid", "flocke"], GROUNDS[i % len(GROUNDS)],
        [C("Hagrid besuchen und von den Tieren hören", rels={"Hagrid": 5}),
         C("Mit Flocke über die Wiese toben", rels={"Flocke": 5}),
         C("Einfach die frische Luft genießen", stats={"loyalty": 3})])

def owlery_beat(i):
    txt = [
        "Im zugigen Eulenturm wählst du eine Schuleule, um einen Brief nach Hause zu schicken.",
        "Du schreibst Mama und Papa, was du Neues gelernt hast, und legst eine kleine Zeichnung bei.",
        "Eine braune Eule legt den Kopf schief, als wollte sie wissen, wohin die Reise geht.",
    ][i % 3]
    return ("In der Eulerei", "alltag", "eulerei", ["player_heroine", "flocke"], txt,
        [C("Mama und Papa von deinen Abenteuern schreiben", stats={"loyalty": 6}, rels={"Mama": 4, "Papa": 4}),
         C("Nach einer Antwort von zu Hause fragen", rels={"Mama": 3, "Papa": 3}),
         C("Deiner Lieblingseule ein Stück Keks geben", stats={"reputation": 2})])

def courtyard_beat(i):
    txt = [
        "Im steinernen Innenhof tummeln sich Schüler in der Pause; ein kleiner Zauber geht schief und alle lachen.",
        "Malfoy gibt mal wieder an; Lily verdreht nur lässig die Augen.",
        "Zwischen zwei Stunden schnappst du frische Luft; Tauben gurren auf den Arkaden.",
    ][i % 3]
    present = ["player_heroine", "lily"] + (["malfoy"] if i % 3 == 1 else [])
    return ("Im Innenhof", "alltag", "innenhof", present, txt,
        [C("Mit Lily über den Schultag plaudern", rels={"Lily": 4}),
         C("Dich nicht von Malfoy provozieren lassen", stats={"wisdom": 4}),
         C("Einem Erstklässler den verpatzten Zauber erklären", stats={"loyalty": 4})])

# ── Kreuzungs-Varianten (Bindungsmomente) ────────────────────────────────────
CROSSINGS = [
    ("gang", "Abend mit der Gang", "gryffindor_turm", ["lily", "harry", "ron", "hermine"],
     "Die ganze Runde sitzt am Kamin zusammen, lacht über den Tag und schmiedet Pläne fürs Wochenende.",
     {"Harry": 6, "Ron": 6, "Hermine": 5}, "An einem langen Kaminabend wuchs die Gryffindor-Clique enger zusammen. Du warst diesmal woanders."),
    ("hermine", "Lernen mit Hermine", "bibliothek", ["hermine"],
     "Hermine teilt ihren farbigen Lernplan mit dir und erklärt geduldig, bis es Klick macht.",
     {"Hermine": 10}, "Hermine half einer kleinen Lerngruppe durch den schwierigen Stoff. Du hast allein gelernt."),
    ("ron", "Zauberschach mit Ron", "gryffindor_turm", ["ron"],
     "Ron fordert dich zu einer Partie Zauberschach heraus und feuert seine Figuren lautstark an.",
     {"Ron": 10}, "Ron besiegte am Kamin einen nach dem anderen im Zauberschach. Du warst nicht dabei."),
    ("harry", "Mit Harry am See", "ländereien_see", ["harry"],
     "Harry und du sitzt am Ufer, werft Steine ins Wasser und redet über das, was euch beschäftigt.",
     {"Harry": 10}, "Harry verbrachte einen ruhigen Nachmittag am See. Du warst woanders unterwegs."),
    ("lily", "Streifzug mit Lily", "treppenhaus", ["lily"],
     "Lily kennt eine Abkürzung hinter einem Wandteppich und zeigt dir lässig die geheimen Ecken des Schlosses.",
     {"Lily": 8}, "Lily erkundete die geheimen Gänge des Schlosses. Du hast den Abend anders verbracht."),
    ("neville", "Neville beistehen", "gewaechshaeuser", ["neville"],
     "Neville droht in Kräuterkunde der Mut zu verlassen; du bleibst an seiner Seite, bis er es schafft.",
     {"Neville": 10, "Harry": 3}, "Jemand stand Neville in Kräuterkunde bei, bis er aufblühte. Diesmal warst du es nicht."),
    ("hagrid", "Kakao bei Hagrid", "hagrids_huette", ["hagrid"],
     "Bei einer Tasse (sehr heißem) Kakao erzählt Hagrid von seinen Lieblingsgeschöpfen und passt herzlich auf euch auf.",
     {"Hagrid": 8}, "Hagrid hatte Besuch zum Kakao und erzählte von magischen Tieren. Du warst nicht dabei."),
    ("quidditch", "Quidditch anfeuern", "ländereien_see", ["harry", "ron", "hermine", "lily"],
     "Auf den Rängen feuert ihr Gryffindor an, malt Banner und jubelt, bis ihr heiser seid.",
     {"Harry": 5, "Ron": 5, "Hermine": 4, "Lily": 4}, "Beim Quidditch tobte die Gryffindor-Kurve. Du hast das Spiel verpasst."),
]
def crossing_beat(i, month):
    key, title, loc, present, summ, rels, recap = CROSSINGS[i % len(CROSSINGS)]
    # eine andockende Kanon-Wahl + eine ruhige Kanon-Wahl + eine Nicht-Andock-Wahl
    dock_rels = dict(rels)
    return (title, "wendepunkt", loc, ["player_heroine"] + present, summ,
        [C("Voll dabei sein und mitmachen", canon=True, docks=True,
           stats={"loyalty": 6, "reputation": 3}, rels=dock_rels),
         C("Eine Weile zuschauen und genießen", canon=True, stats={"wisdom": 3},
           rels={list(rels.keys())[0]: 3}),
         C("Diesmal lieber für dich bleiben", canon=False, stats={"wisdom": 2})], recap)

# ── Gap-Plan: nach welchem Anker wie viele Füll-Beats, welcher Monat/Kapitel ──
GAPS = [
    ("y1_s04b", 16, "September",  2),
    ("y1_s05b", 12, "September",  3),
    ("y1_s06b", 16, "Oktober",    3),
    ("y1_s07",  20, "November",   5),
    ("y1_s08a", 12, "Dezember",   5),
    ("y1_s09a", 18, "Januar/Februar", 6),
    ("y1_s10b", 14, "März/April/Mai", 6),
]

# Rotationsreihenfolge der Alltags-Kategorien (variiert)
def filler(cat_i, idx, month, chapter, cross_counter):
    cats = ["subject", "meal", "common", "library", "grounds", "owlery", "courtyard", "subject", "common"]
    cat = cats[cat_i % len(cats)]
    recap = None
    if cat == "subject":   title, ptype, loc, present, summ, choices = subject_beat(idx)
    elif cat == "meal":    title, ptype, loc, present, summ, choices = meal_beat(idx)
    elif cat == "common":  title, ptype, loc, present, summ, choices = common_beat(idx)
    elif cat == "library": title, ptype, loc, present, summ, choices = library_beat(idx)
    elif cat == "grounds": title, ptype, loc, present, summ, choices = grounds_beat(idx)
    elif cat == "owlery":  title, ptype, loc, present, summ, choices = owlery_beat(idx)
    else:                  title, ptype, loc, present, summ, choices = courtyard_beat(idx)
    beat = {"chapter": chapter, "title": f"{title} ({month})", "school_time": f"{month} — Schulalltag",
            "characters_present": present, "location": loc, "summary": summ,
            "plot_type": ptype, "challenge_potential": 2, "crossing_point": False,
            "choices": choices, "next_scenes": []}
    return beat

def make_crossing(idx, month, chapter):
    title, ptype, loc, present, summ, choices, recap = crossing_beat(idx, month)
    return {"chapter": chapter, "title": f"{title} ({month})", "school_time": f"{month} — Schulalltag",
            "characters_present": present, "location": loc, "summary": summ,
            "plot_type": ptype, "challenge_potential": 3, "crossing_point": True,
            "clique_bond_delta": 1, "autonomous_recap": recap,
            "choices": choices, "next_scenes": []}

# Füll-Blöcke je Gap erzeugen: ~45% Kreuzungen
gap_blocks = {}
cat_i = 0
xi = 0   # crossing-Index
fi = 0   # filler-Index
for anchor, n, month, chapter in GAPS:
    block = []
    for k in range(n):
        # jede ~2. Szene eine Kreuzung (Bindungsmoment)
        if k % 2 == 1:
            b = make_crossing(xi, month, chapter); xi += 1
        else:
            b = filler(cat_i, fi, month, chapter, xi); cat_i += 1; fi += 1
        b["id"] = gid()
        block.append(b)
    gap_blocks[anchor] = block

# In die bestehende (chain-geordnete) Szenenliste einweben
ordered = []
for s in existing:
    ordered.append(s)
    if s["id"] in gap_blocks:
        ordered.extend(gap_blocks[s["id"]])

# Komplett linear neu verdrahten (single next), letzte -> []
for i, s in enumerate(ordered):
    s["next_scenes"] = [ordered[i + 1]["id"]] if i + 1 < len(ordered) else []

data["scenes"] = ordered
json.dump(data, open(os.path.join(BOOK, "plot_graph.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

crossings = [s["id"] for s in ordered if s.get("crossing_point")]
print(f"Szenen gesamt: {len(ordered)}")
print(f"Kreuzungen gesamt: {len(crossings)}")
# Sanity: alle Kreuzungen haben recap + docks
bad = [s["id"] for s in ordered if s.get("crossing_point") and not s.get("autonomous_recap")]
print("Kreuzungen ohne recap:", bad or "keine")
nodock = [s["id"] for s in ordered if s.get("crossing_point") and not any(c.get("docks") for c in s["choices"])]
print("Kreuzungen ohne docks-Wahl:", nodock or "keine")
# Test-Anker noch da?
need = ["y1_s01","y1_s02","y1_s06","y1_s07","y1_s08","y1_s11"]
print("Test-Anker vorhanden:", all(any(s["id"]==a for s in ordered) for a in need))
