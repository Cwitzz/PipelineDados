# Daten-Pipeline für ein Produkt-Empfehlungssystem

Dieses Projekt repräsentiert eine ausgeklügelte Daten-Pipeline, die darauf abzielt, ein Produkt-Empfehlungssystem unter Berücksichtigung bewährter Verfahren der Datenverarbeitung, des maschinellen Lernens und der automatisierten Tests zu entwickeln.

## 🧱 Komponenten der Pipeline

### 1. Erstellung der Datenbank

Das Skript `create_database.py` erstellt eine SQLite-Datenbank mit dem Namen `DBFIC.db`. Die Datenbank enthält eine Sammlung von Transaktionen für Gartenprodukte mit fiktiven Daten, die mithilfe der Faker-Bibliothek generiert wurden, einschließlich Namen, Adressen, Preise, Mengen und mehr.

### 2. Datenbereinigung und -transformation

Das Skript `data_cleaning_transform.py` führt verschiedene Operationen zur Datenbereinigung und -transformation durch, einschließlich der Behandlung fehlender Werte, der Konvertierung von Formaten und der Normalisierung numerischer Merkmale unter Verwendung von Pandas, scikit-learn und NumPy.

### 3. Schulung des Empfehlungsmodells

Das Skript `model_training_product_recomm.py` ist für die Schulung eines maschinellen Lernmodells zur Produkt-Empfehlung verantwortlich. Das Modell und die Encoder werden zur Wiederverwendung in Dateien im `.pkl`-Format serialisiert.

### 4. Einfügen von Empfehlungen in die Datenbank

Das Skript `insert_recommendations.py` wendet das geschulte Modell an, um personalisierte Empfehlungen zu generieren, die in die Datenbank `DBFIC.db` eingefügt werden.

### 5. Bewertung der Leistung

Das Skript `evaluate_perfomance_model.py` berechnet Leistungsmetriken, die für Empfehlungssysteme relevant sind, wie Genauigkeit, Recall, F1-Score und andere.

### 6. Automatisierte Tests

Das Projekt enthält automatisierte Tests in den Skripten `Test_model_training_product_recomm.py` und `test_data_cleaning_transform.py`, um die Integrität der Funktionen und Ergebnisse zu überprüfen.

### 7. Dokumentation

Die Datei `README.md` enthält Informationen zur Konfiguration, den Projektzielen, den Ausführungsanweisungen und Erläuterungen zu den Komponenten der Pipeline.

## ⚙️ Skalierbarkeit und Leistung

Das Projekt ist darauf ausgelegt, skalierbar und leistungsstark zu sein und kann mit größeren Datensätzen umgehen sowie in Cloud-Datenplattformen integriert werden.

## 🚀 Fazit

Diese Pipeline ist eine robuste Lösung für den Aufbau eines Produkt-Empfehlungssystems. Sie umfasst alles von der Erstellung der Datenbank bis zur Bewertung der Leistung des Modells und stellt Qualität, Testbarkeit und Skalierbarkeit sicher. Die Datenanalysephasen wurden bisher nicht entwickelt, da der Schwerpunkt des Projekts nicht darauf lag.

## 👨‍💻 Ausführung

### Voraussetzungen
Stellen Sie sicher, dass Sie Python 3.11 auf Ihrem Rechner installiert haben. Zusätzlich benötigen Sie einige Python-Bibliotheken. Sie können sie mit pip installieren:
`pip install pandas scikit-learn sqlite3 joblib faker numpy random`

Es kann sein, dass nicht alle Bibliotheken benötigt werden, daher empfiehlt es sich, eine integrierte Entwicklungsumgebung (IDE) zu verwenden, um das Projekt zu öffnen.

### Schritt 1: Einrichten der Datenbank
Erstellen und befüllen Sie zunächst die Datenbank mit fiktiven Daten. Verwenden Sie das Skript `create_database.py` dafür.
`python create_database.py`

### Schritt 2: Datenbereinigung, Vorverarbeitung und Transformation
Nachdem die Datenbank eingerichtet ist, führen Sie das Skript `data_cleaning_transform.py` aus, um die Daten zu bereinigen und zu transformieren.
`python data_cleaning_transform.py`

### Schritt 3: Schulung des Empfehlungsmodells
Jetzt, da die Daten bereit sind, können Sie das Empfehlungsmodell trainieren. Führen Sie das Skript `model_training_product_recomm.py` aus.
`python model_training_product_recomm.py`

### Schritt 4: Bewertung der Modellleistung
Bewerten Sie die Leistung des Modells mithilfe des Skripts `evaluate_performance_model.py`. Dadurch erhalten Sie nützliche Metriken, um den tatsächlichen Wert des Modells zu verstehen.
`python evaluate_performance_model.py`

### Schritt 5: Einfügen von Empfehlungen in die Datenbank
Verwenden Sie schließlich das Skript `insert_recommendations.py`, um die generierten Empfehlungen in die Datenbank einzufügen.
`python insert_recommendations.py`

Dieser Schritt ist möglicherweise nicht relevant, da diese Funktion mit Aktualisierungen direkt in das Modelltrainings-Skript eingefügt wurde.

### Ausführungsfazit
Nachdem Sie diese Skripte in der angegebenen Reihenfolge ausgeführt haben, verfügen Sie über ein geschultes Modell für Produkt-Empfehlungen, das einsatzbereit ist. Die Empfehlungen werden in der SQLite-Datenbank gespeichert und können bei Bedarf abgerufen werden.

## Hinweise
Ich möchte klarstellen, dass Sie, wenn Sie diese Pipeline zu Studienzwecken verwenden möchten, alle Aspekte des Codes an Ihre eigenen Bedingungen anpassen müssen. Beispielsweise den Namen der Datenbank, die Pfade und sogar das verwendete DBMS für die Datenbank oder auch keine Datenbank verwenden und sie beispielsweise in das Excel-Format ändern.

Darüber hinaus sind die Skripte speziell für die von dem ursprünglichen Skript erstellte Tabelle geschrieben. Wenn Sie unterschiedliche Tabellen mit unterschiedlichen Merkmalen verwenden möchten, müssen Sie die gesamte Skriptkette anpassen.

## 📄 Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Details finden Sie in der Datei [LICENSE](LICENSE).
