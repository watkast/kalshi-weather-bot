# 1¢ Study

*Updated Mon Oct 5, 2:30 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 444 finished bets | 0% | -$38.60 | -58% | -8.69¢ | -$19.30 / -$19.30 |

*Expect about **57 buys a day**, roughly **$8.58/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 444 | -$46.35 | -70% |
| ESPN-verified leagues only, sell at 2¢ | 444 | -$51.00 | -77% |
| ESPN-verified leagues only, sell at 10¢ | 444 | -$52.19 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4449 | 444 | 2 (0%) | 1.1% | -$38.60 (-58%) | Hold to the end: -$38.60 (-58%) |

*In play right now: 11. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 91 | 2.7% | 0.0% (0) | -225% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 91 | 0 | -100% | -71% | -71% | -76% |
| ESPN win probability ≥ 2% | 17 | 0 | -100% | -59% | -54% | -100% |
| ESPN win probability ≥ 5% | 7 | 0 | -100% | -75% | -63% | -100% |
| ESPN win probability ≥ 10% | 4 | 0 | -100% | -57% | -35% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 444 | 14% | 8% | 5% | 2% | 1% | 1% |
| Unverified | 3994 | 5% | 4% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 2 | 0% | -$38.60 | -58% |
| Sell at 2¢ | 60 | 14% | -$51.00 | -77% |
| Sell at 3¢ | 36 | 8% | -$52.56 | -79% |
| Sell at 5¢ | 22 | 5% | -$52.30 | -79% |
| Sell at 10¢ | 11 | 2% | -$52.19 | -78% |
| Sell at 25¢ | 4 | 1% | -$53.36 | -80% |
| Sell at 50¢ | 3 | 1% | -$46.35 | -70% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 287 | 1 | 4% | 3% | -67% | -93% | 9 min |
| ITF Women's Match | ✘ | 279 | 0 | 11% | 5% | -100% | -81% | 4 min |
| ITF Men's Match | ✘ | 272 | 1 | 10% | 5% | -66% | -83% | 4 min |
| Challenger ATP  | ✘ | 228 | 1 | 8% | 2% | -59% | -86% | 5 min |
| TT Star Series Match | ✘ | 127 | 1 | 2% | 2% | -27% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 106 | 0 | 8% | 4% | -100% | -85% | 7 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| League of Legends Game | ✘ | 93 | 0 | 6% | 2% | -100% | -89% | 12 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| CONCACAF Nations League Game | partly | 84 | 2 | 21% | 10% | +122% | -63% | 22 min |
| Darts Match | ✘ | 65 | 0 | 2% | 2% | -100% | -97% | 9 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| Men's T20 Cricket Match | ✘ | 50 | 0 | 16% | 6% | -100% | -72% | 17 min |
| Challenger WTA | ✘ | 48 | 0 | 19% | 10% | -100% | -68% | 9 min |
| Dota 2 Game | ✘ | 47 | 0 | 2% | 2% | -100% | -96% | 28 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| International Friendly Game | partly | 43 | 0 | 12% | 2% | -100% | -80% | 14 min |
| NHL Game | ✔ | 39 | 0 | 13% | 5% | -100% | -78% | 4 min |
| R6 Game | ✘ | 36 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| KBO Game | ✘ | 28 | 0 | 7% | 7% | -100% | -88% | 7 min |
| KHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 5 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Liga DIMAYOR Game | ✘ | 26 | 0 | 4% | 0% | -100% | -93% | 9 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| ATP Tennis Match | ✘ | 25 | 0 | 12% | 4% | -100% | -79% | 3 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| Japan NPB Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Uruguay Primera Division Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 12 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| WTA Tennis Match | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 3 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| LaLiga 2 Game | partly | 20 | 0 | 10% | 5% | -100% | -83% | 9 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Overwatch Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Argentina Primera Division Game | ✘ | 17 | 0 | 18% | 12% | -100% | -69% | 12 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Valorant game winner | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 15 min |
| NFL Game | ✔ | 15 | 0 | 27% | 7% | -100% | -54% | 3 min |
| DEL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's Pro Basketball Game | ✔ | 10 | 0 | 30% | 10% | -100% | -48% | 9 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 9 | 0 | 22% | 11% | -100% | -61% | 5 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 9 | 1 | 44% | 44% | +937% | -23% | 32 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Adriatic ABA Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 6 min |
| College Hockey Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Russia VTB United Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Turkey BSL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| NBA Game | ✔ | 3 | 0 | 33% | 0% | -100% | -42% | 15 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 175 | 6% | 1% | 0% | -89% |
| 5–15 min | 77 | 14% | 4% | 1% | -75% |
| 15–30 min | 79 | 29% | 11% | 1% | -50% |
| 30–60 min | 57 | 12% | 5% | 0% | -79% |
| Over 60 min | 55 | 15% | 11% | 0% | -75% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 42 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-05 20:29 | UEFA Nations League Game | Tie | ✔ | 88' · TUR 1 - ITA 2 | — | In play | — |
| 10-05 20:29 | UEFA Nations League Game | Ukraine | ✔ | 87' · HUN 2 - UKR 1 | — | In play | — |
| 10-05 20:27 | UEFA Nations League Game | Romania | ✔ | 84' · SWE 1 - ROU 0 | — | In play | — |
| 10-05 20:26 | International Friendly Game | Tie | ✔ | 81' · GIB 2 - LIE 0 | — | In play | — |
| 10-05 20:25 | UEFA Nations League Game | Turkiye | ✔ | 83' · TUR 1 - ITA 2 | — | In play | — |
| 10-05 20:24 | UEFA Nations League Game | Belgium | ✔ | 82' · BEL 1 - FRA 2 | — | In play | — |
| 10-05 20:21 | ITF Men's Match | Gonzalo Zeitune | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 20:20 | LaLiga 2 Game | Tenerife | ✔ | 83' · TEN 2 - COR 3 | — | In play | — |
| 10-05 20:11 | Counter-Strike 2 Game | BetBoom Team | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 20:10 | Italy Serie A Game | Pallacanestro Cantu | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 20:03 | Adriatic ABA Game | KK Studentski centar Podgorica | ✘ | — | — | In play | — |
| 10-05 20:02 | International Friendly Game | Liechtenstein | ✔ | 58' · GIB 2 - LIE 0 | — | In play | — |
| 10-05 19:56 | Counter-Strike 2 Game | Team LEISURE | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 19:51 | R6 Game | Virtus.pro | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 19:50 | ITF Women's Match | Ana Victoria Gobbi Monllau | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 19:47 | Bundesliga Basketball Game | Rasta Vechta | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-05 19:17 | Counter-Strike 2 Game | Team Falcons | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 19:17 | Counter-Strike 2 Game | MOUZ NXT | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 19:06 | ITF Women's Match | Charlotte Narti | ✘ | — | 12¢ | ❌ Lost | -$0.15 |
| 10-05 19:00 | ITF Women's Match | Nalah Kaler | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-05 18:56 | Counter-Strike 2 Game | WRAITH PCIFIC | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:53 | Counter-Strike 2 Game | XI Esport | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:43 | ITF Women's Match | Pietra Rivoli | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-05 18:40 | Men's T20 Cricket Match | Bangladesh Champions | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:40 | ITF Men's Match | Diego Giraldo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:13 | ITF Men's Match | Julien Dando | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:08 | Challenger ATP  | Louis Wessels | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:07 | Challenger ATP  | Juan Estevez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 18:02 | ITF Women's Match | Guadalupe Rondinoni | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 17:58 | International Friendly Game | Kenya | ✔ | 90'+5' · KEN 0 - RWA 0 | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
