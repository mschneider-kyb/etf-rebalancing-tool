# 📈 ETF Rebalancing Calculator

Ein modernes GUI-Tool zur automatischen Berechnung der optimalen Kaufanteile für ein
Zwei-ETF-Portfolio (z.B. 70/30-Strategie).

## ❓ Das Problem

Viele Investoren nutzen eine feste Zielgewichtung (z.B. 70% MSCI World, 30% Emerging
Markets). Durch Marktschwankungen verschiebt sich dieses Verhältnis ständig. Werden neue
Beträge investiert, stellt sich die Frage: **Wie viel von welchem ETF muss ich kaufen,
um wieder exakt bei 70/30 zu landen?**

## 💡 Die Lösung

Dieses Programm berechnet basierend auf deinen aktuellen Depotwerten und deiner
geplanten Einzahlung die ideale Verteilung.

### Besondere Logik: "No-Sell-Rebalancing"

Oft ist die geplante Einzahlung zu gering, um das Gleichgewicht allein durch Käufe
wiederherzustellen. In diesem Fall müsste man Anteile des übergewichteten ETFs **verkaufen**.

* **Das Problem:** Verkäufe lösen Steuern und Gebühren aus und kosten Performance.
* **Die Lösung des Tools:** Wenn ein Verkauf nötig wäre (negatives Ergebnis), berechnet
  das Programm automatisch den **Mindestinvestitionsbetrag**, der nötig ist, um das
  Zielportfolio allein durch Käufe (ohne Verkäufe) wieder ins Lot zu bringen.

## ✨ Features

* **Interaktive GUI:** Erstellt mit `CustomTkinter` (Dark Mode Support).
* **Live-Slider:** Intuitive Einstellung der Zielgewichtung für ETF 1.
* **Intelligente Fehlerkorrektur:** Akzeptiert sowohl Punkte (`.`) als auch deutsche
  Kommata (`,`) bei der Eingabe.
* **Validierung:** Verhindert Abstürze durch ungültige Zeichen oder negative Werte.
* **Kein Installation:** Kann mit PyInstaller als eigenständige Anwendung exportiert
  werden.

## 🚀 Installation & Benutzung

### Für Nutzer (MacOS)

1. Lade den `dist`-Ordner herunter.
2. Starte die Datei `main.app` per Doppelklick (keine Python-Installation nötig).

### Für Entwickler

1. Repository klonen:
   ```bash
   git clone [https://github.com/mschneider-kyb/etf-rebalancing-tool.git](https://github.com/mschneider-kyb/etf-rebalancing-tool.git)

## ⚖️ Lizenzen von Drittanbietern

Dieses Projekt verwendet die folgende Open-Source-Software:

- **CustomTkinter** (MIT-Lizenz) – Copyright (c) 2023 Tom Schimansky
  Verwendet für die moderne grafische Benutzeroberfläche.

- **PyInstaller** (GPL-Lizenz mit Ausnahmeregelung) – Copyright (c) 2010-2026
  PyInstaller Development Team
  Verwendet zum Erstellen der ausführbaren (.exe) Datei. Die "Bootloader-Exception"
  erlaubt es, Programme zu verbreiten, ohne den eigenen Quellcode offenlegen zu müssen.

- **Python** (PSF-Lizenz) – Copyright (c) Python Software Foundation
  Die zugrunde liegende Programmiersprache.

Alle Lizenzen der verwendeten Bibliotheken sind in der kompilierten Anwendung enthalten
oder werden durch die Nutzung der Standard-Distributionen anerkannt.