# Koseprogg Code Warriors!

Velkommen <name-prefix>!

Du finner webappen for å teste spillet på: [aibattles.koseprogg.no](https://aibattles.koseprogg.no)

I dag skal vi programmere en BOT som spiller [TickoaTTwo](https://www.youtube.com/watch?v=ePxrVU4M9uA) (Også kjent som Better Tic-Tac-Toe)

For å gjøre dette trenger du bare å endre koden i [toc_tac.py](/src/tic_tac.py)-filen. Deretter kan du pushe til github og så vil github actions pushe dette videre i skyen og bli deployet på <function-name>

## Kjøre lokalt

Først må du installere flask og flask-cors.

```bash
pip install flask && pip install flask-cors
```

For å kjøre applikasjonen lokalt kan man bruke local_development.py til å spinne opp en "lambda" lokalt.
Bruk kommandoen:

```bash
flask --app local_development.py --debug run --host=localhost --port=8000
```

fra dev-mappen for å kjøre lokalt.

## Utvikle AI

Endre filen [tic_tac.py](/src/tic_tac.py) under [src](/src) for å utvikle ai-algoritmen videre.

## Endre lagnavn!

Dersom du ønsker å endre lagnavn kan du enkelt gjøre dette ved å endre verdien under [config.py](/src/config.py). Etter dette er pushet til github og deployed hos AWS [tar ca 20 sekunder] vil du se endringen i webappen.
