# ⚔️ Herausforderungen

## Daten Erstellung:
Ursprünglich bestand die Idee darin, eine sehr einfache Datenbank in einer txt-Datei zu erstellen, aber ich habe sofort erkannt, dass dies den Prozess viel schwieriger machen würde.
Die erste Änderung bestand darin, Daten über Bücher im Excel-Format mit wenigen Spalten wie Veröffentlichungsdatum, Autor usw. zu erstellen.

Nach dem Übergang zu den nächsten Schritten sind mir verschiedene Probleme aufgefallen, wobei das Hauptproblem der Mangel an Komplexität dieser Daten war. Im Grunde genommen wäre es sinnlos, die Dinge, die ich in Zukunft anwenden wollte, auf diese Daten anzuwenden, da nichts daraus abgeleitet werden konnte.
#### 🏁 Schließlich, nachdem ich mehr Zeit investiert hatte, habe ich eine Datenbank erstellt, die zwar nicht komplex war, aber bereits in Datenbankformat vorlag: eine Tabelle mit Spalten und 1000 Kundennamen, die eine Bibliothek zur Erzeugung von fiktiven Daten verwendet. Diese Tabelle hatte 1000 Zeilen mit 8 Spalten. Sofort eröffneten sich viele Möglichkeiten.

## 🧹 Datenbereinigung, Vorverarbeitung und Transformation
Zu Beginn hat alles reibungslos funktioniert, aber dieser Schritt hängt stark vom nächsten ab. Beim Entwickeln der Trainingsmodelle stellte ich zusätzliche Anforderungen an die Komplexität fest. Zum Beispiel verlangsamte der ursprüngliche Datenformat die Modellausführung erheblich, wirklich sehr langsam!

Nach einiger Zeit des Nachdenkens kam ich zu einigen Schlussfolgerungen. Ich habe die Werte in der `sex`-Spalte in binäre Werte geändert, was die Trainingsgeschwindigkeit des Modells erheblich verbessert hat. Darüber hinaus habe ich die Spalten `customer_name` und `product` codiert, was die Verwendung von Machine Learning-Methoden erheblich erleichtert hat.

Mit der Methode k-means habe ich eine Clusteranalyse der Daten durchgeführt, um zukünftige Prozesse weiter zu vereinfachen. Für weitere Informationen kannst du dich über die k-means-Methode und die Clusteranalyse von Daten informieren.

Es gab viele weitere Anpassungen, die zu einer signifikanten Steigerung der Trainingsgeschwindigkeit geführt haben. Ich habe die Steigerung der Geschwindigkeit überwacht und die Zahlen waren beeindruckend.
#### ursprüngliche Ausführungszeit: 48 min 50 s
#### endgültige Ausführungszeit: 22.56 s
#### Gesamte Zeitreduktion von 99,2% und 128-fache Geschwindigkeitserhöhung

## 🤖 Modelltraining für Produktempfehlungen
Erstaunlicherweise war dieser Schritt einer der unkompliziertesten. Alle erforderlichen Implikationen für eine reibungslose Ausführung wurden im vorherigen Schritt umgesetzt. Ich hatte einige Probleme mit Syntax und Einrückung, aber sie wurden schnell gelöst. Eine der Herausforderungen bestand darin, eine Bibliothek namens `surprise` zu verwenden, da ich sie nicht optimal einsetzen und Kompatibilitätsprobleme hatte. Daher bin ich wieder zu `scikit-learn` zurückgekehrt. Dieser Schritt hat sich sicherlich verändert, aber der bedeutendste war das Aufteilen der Skripte in Mikrofunktionen, um die Implementierung der Testgetriebenen Entwicklung (TDD) zu erleichtern.

Das Aufteilen des Skripts in Mikrofunktionen war eine der größten Herausforderungen.

## ✔️ Bewertung der Modellleistung
Ich hatte keine Probleme mit diesem Skript. Ich war mit den verwendeten Anwendungen sehr zufrieden, und es wurde nach dem Ausführen des Modellskripts viel einfacher. Die Überlegungen für diesen Schritt konzentrieren sich mehr auf die Ergebnisse selbst.

#### Vergleich der Metriken:

#### Erste Bewertung (Modell 1):

#### MSE: 103.782312548213  MAE: 27.321351528391  R-Quadrat (R2): -1.2131267381625
#### Um das besser zu verstehen, recherchiere die 3 Methoden: MSE, MAE, R2. Die erste Bewertung zeigte jedoch, dass das Modell SCHRECKLICH war.
#### Zweite Bewertung:
#### MSE: 23.85376567930002  MAE: 3.605650000000001  R-Quadrat (R2): 0.7809557859075236

##### Bei der zweiten Bewertung haben sich sowohl MSE als auch MAE gegenüber der ersten Bewertung signifikant verringert. MSE ist eine Metrik, die den mittleren quadratischen Fehler misst, daher ist ein niedrigerer Wert besser. MAE ist eine Metrik, die den mittleren absoluten Fehler misst, und auch hier ist ein niedrigerer Wert wünschenswert.

##### Darüber hinaus hat sich der Wert des R-Quadrats (R2) in der zweiten Bewertung erhöht. R2 ist eine Metrik, die den Anteil der Varianz in den Ziel Daten angibt, der vom Modell erfasst wird. Ein Wert näher an 1 gilt als gute Anpassung des Modells an die Daten.
