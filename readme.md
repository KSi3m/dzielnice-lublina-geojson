# Dzielnice Lublina w formacie GeoJSON

## Wymagania
Do uruchomienia tego programu potrzebny jest Python. Korzystam z wersji 3.7, więc jeśli program nie działa na Twojej wersji, zaktualizuj Pythona lub wykonaj refactor pod starsze wersje.

Program korzysta z modułu `requests`, który służy do wykonywania żądań HTTP. Można go zainstalować, wpisując w terminalu:

`pip install requests`

Sam program uruchamia się tak:

`python program.py`

## Opis działania programu
Program wykonuje dwa żądania `GET` na odpowiednie endpointy:

1. **Pobranie danych z pliku dzielnice.json**

     Niżej więcej informacji o strukturze tego pliku

3. **Żądanie do API Nominatim (OpenStreetMap)**  
   Endpoint:  
   `https://nominatim.openstreetmap.org/search.php?q={parameter}&format=jsonv2`  
   Gdzie `{parameter}` to nazwa dzielnicy. Żądanie zwraca obiekt OSM (OpenStreetMap), z którego wyciągnam `osm_id`.

4. **Pobranie danych GeoJSON**  
   Endpoint:  
   `https://polygons.openstreetmap.fr/get_geojson.py?id={osm_id}&params=0`  
   Używając `osm_id`, program pobiera dane obiektu w formacie GeoJSON i zapisuje je do pliku.

5. **Zapis do pliku**  
   Po pobraniu danych następuje zapis do pliku w formacie .geojson z nazwą dzielnicy

## Format pliku `dzielnice.json`
Plik ma następującą strukturę:

- Klucz `"city"`: nazwa miasta.
- Klucz `"category"`: typ szukanego obiektu OSM (dla dzielnic powinno to być `"boundary"`)
  Więcej informacji w dokumentacji: [Nominatim API Output](https://nominatim.org/release-docs/develop/api/Output/).
- Klucz `"names"`: lista nazw dzielnic.

Przykładowy plik dla Lublina:

```json
{
  "city": "Lublin",
  "category": "boundary",
  "names": [
    "Abramowice", "Bronowice", "Czechów Południowy", "Czechów Północny", "Czuby Południowe", "Czuby Północne",
    "Dziesiąta", "Felin", "Głusk", "Hajdów-Zadębie", "Kalinowszczyzna", "Konstantynów", "Kośminek", "Ponikwoda",
    "Rury", "Sławin", "Sławinek", "Stare Miasto", "Szerokie", "Śródmieście", "Tatary", "Węglin Południowy",
    "Węglin Północny", "Wieniawa", "Wrotków", "Za Cukrownią", "Zemborzyce"
  ]
}
```
## Uwagi
Program działa dla dzielnic Lublina, Warszawy, i Krakowa, ale może wymagać dodatkowej obsługi edge caseów dla innych miast (być może, na ten moment nie wiem). W przyszłości postaram się to sprawdzić.