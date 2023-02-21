# Koseprogg Code Warriors!

Velkommen <name-prefix>!

Du finner webappen for å teste spillet på: [aibattles.koseprogg.no](https://aibattles.koseprogg.no)

I dag skal vi programmere en BOT som spiller [TickoaTTwo](https://www.youtube.com/watch?v=ePxrVU4M9uA) (Også kjent som Better Tic-Tac-Toe)

For å gjøre dette trenger du bare å endre koden i [toc_tac.py](/src/tic_tac.py)-filen. Deretter kan du pushe til github og så vil github actions pushe dette videre i skyen og bli deployet på <function-name>

## Kjør med docker compose

Den aller letteste måten å kjøre prosjektet lokalt på er med docker compose! En kommando og du er i gang.

Vi har lagt ved en docker-compose-fil som gjør at det eneste du trenger å gjøre er å kjøre:

```bash
docker compose up
```

PS: Klager docker på at compose ikke er et keyword? Kanskje du kjører en gammel versjon av docker. Bruk da `docker-compose up`

Hint: Bruk CTRL+C for å avslutte containeren når du er ferdig.

## Kjør med docker

Vi har lagt ved en [Dockerfile](Dockerfile) som bygger et development bilde av appen.
Merk! Dockerfilen krever at man mounter filsystemet, ettersom denne er ment for å støtte [Hot Reload](https://learn.microsoft.com/en-us/visualstudio/debugger/hot-reload?view=vs-2022).

For å kjøre med docker må du først bygge bildet:

```bash
docker build -t <du-velger-selv-hva-du-vil-kalle-det> .
```

Vi foreslår at du kaller det koseprogg-ai. Da blir kommandoen:

```bash
docker build -t koseprogg-ai .
```

Mount src, samt åpne port 8000 for å kjøre koden. Husk å bruke samme tag som du har valgt over:

```bash
docker run -v $(pwd)/src:/src -p 8000:8000 koseprogg-ai
```

Kommandoen over vil gjøre at containeren kjører, og vil oppdateres når du lagrer filer i src-mappen. Det er ikke nødvendig å kjøre denne igjen etter en oppdatering.

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
