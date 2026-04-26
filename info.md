URL für Tankstellenliste:
https://creativecommons.tankerkoenig.de/json/list.php?lat=49.1337354&lng=10.0633573&rad=4&sort=price&type=diesel&apikey={APIKEY-EINSETZEN}

URL für Details einer Tankstelle:
https://creativecommons.tankerkoenig.de/json/detail.php?id={TANKSTELLEN-ID}&apikey={APIKEY-EINSETZEN}


API-Methode 2 - Preisabfrage

Die Preisabfrage erfolgt über die API-Methode prices.php. Damit können die Preise von bis zu 10 bekannten Tankstellen gleichzeitig abgefragt werden.

Die Parameter dieses Request sind die IDs der entsprechenden Tankstellen:
Parameter 	Bedeutung 	Format
ids 	IDs der Tankstellen 	UUIDs, durch Komma getrennt
apikey 	Der persönliche API-Key 	UUID
Beispielaufruf
https://creativecommons.tankerkoenig.de/json/prices.php?ids=4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8,446bdcf5-9f75-47fc-9cfa-2c3d6fda1c3b,60c0eefa-d2a8-4f5c-82cc-b5244ecae955,44444444-4444-4444-4444-444444444444&apikey=00000000-0000-0000-0000-000000000002 

Beispielantwort

{
    "ok": true,
    "license": "CC BY 4.0 -  https:\/\/creativecommons.tankerkoenig.de",
    "data": "MTS-K",
    "prices": {
        "60c0eefa-d2a8-4f5c-82cc-b5244ecae955": {
            "status": "open",                               - Tankstelle ist offen
            "e5": false,                                    - kein Super
            "e10": false,                                   - kein E10
            "diesel": 1.189                                 - Tankstelle führt nur Diesel
        },
        "446bdcf5-9f75-47fc-9cfa-2c3d6fda1c3b": {
            "status": "closed"                              - Tankstelle ist zu
        },
        "4429a7d9-fb2d-4c29-8cfe-2ca90323f9f8": {
            "status": "open",
            "e5": 1.409,
            "e10": 1.389,
            "diesel": 1.129
        },
        "44444444-4444-4444-4444-444444444444": {
            "status": "no prices"                           - keine Preise für Tankstelle verfügbar
        }
    }
}
                    