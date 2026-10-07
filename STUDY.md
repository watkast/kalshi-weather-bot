# 1¢ Study

*Updated Wed Oct 7, 5:47 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 544 finished bets | 1% | -$39.60 | -49% | -7.28¢ | -$26.80 / -$12.80 |

*Expect about **57 buys a day**, roughly **$8.56/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 544 | -$47.85 | -59% |
| ESPN-verified leagues only, sell at 5¢ | 544 | -$61.45 | -75% |
| ESPN-verified leagues only, sell at 2¢ | 544 | -$61.58 | -75% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4938 | 544 | 3 (1%) | 1.1% | -$39.60 (-49%) | Hold to the end: -$39.60 (-49%) |

*In play right now: 10. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 106 | 2.7% | 0.0% (0) | -225% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 106 | 0 | -100% | -74% | -73% | -75% |
| ESPN win probability ≥ 2% | 22 | 0 | -100% | -68% | -65% | -100% |
| ESPN win probability ≥ 5% | 8 | 0 | -100% | -78% | -68% | -100% |
| ESPN win probability ≥ 10% | 5 | 0 | -100% | -65% | -48% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 544 | 14% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 4384 | 6% | 4% | 3% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 3 | 1% | -$39.60 | -49% |
| Sell at 2¢ | 77 | 14% | -$61.58 | -75% |
| Sell at 3¢ | 51 | 9% | -$61.71 | -76% |
| Sell at 5¢ | 31 | 6% | -$61.45 | -75% |
| Sell at 10¢ | 15 | 3% | -$61.95 | -76% |
| Sell at 25¢ | 6 | 1% | -$61.74 | -76% |
| Sell at 50¢ | 5 | 1% | -$47.85 | -59% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 379 | 0 | 12% | 5% | -100% | -80% | 4 min |
| ITF Men's Match | ✘ | 330 | 1 | 9% | 5% | -72% | -84% | 5 min |
| Counter-Strike 2 Game | ✘ | 310 | 1 | 4% | 3% | -70% | -94% | 9 min |
| Challenger ATP  | ✘ | 254 | 1 | 9% | 2% | -63% | -84% | 5 min |
| TT Star Series Match | ✘ | 149 | 1 | 3% | 3% | -37% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| League of Legends Game | ✘ | 106 | 0 | 7% | 3% | -100% | -89% | 11 min |
| College Football Game | partly | 98 | 2 | 14% | 6% | +90% | -75% | 48 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| Darts Match | ✘ | 85 | 0 | 1% | 1% | -100% | -98% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| Men's T20 Cricket Match | ✘ | 57 | 0 | 16% | 7% | -100% | -73% | 19 min |
| Dota 2 Game | ✘ | 55 | 0 | 2% | 2% | -100% | -97% | 28 min |
| Challenger WTA | ✘ | 54 | 0 | 17% | 9% | -100% | -71% | 8 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| NHL Game | ✔ | 52 | 0 | 13% | 6% | -100% | -77% | 4 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| R6 Game | ✘ | 38 | 0 | 0% | 0% | -100% | -100% | 9 min |
| KBO Game | ✘ | 33 | 0 | 6% | 6% | -100% | -89% | 8 min |
| Brasileiro Serie B Game | ✘ | 32 | 0 | 3% | 0% | -100% | -95% | 13 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| ATP Tennis Match | ✘ | 30 | 0 | 10% | 3% | -100% | -83% | 3 min |
| KHL Game | ✘ | 30 | 0 | 3% | 3% | -100% | -94% | 5 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| Liga DIMAYOR Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LNBP Basketball Game | ✘ | 23 | 0 | 4% | 0% | -100% | -92% | 12 min |
| Argentina Primera Division Game | ✘ | 23 | 0 | 22% | 13% | -100% | -62% | 9 min |
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| Japan NPB Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| WTA Tennis Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 3 min |
| EuroCup Basketball Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 10 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Overwatch Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liiga Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| Valorant game winner | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 15 min |
| NFL Game | ✔ | 16 | 0 | 25% | 6% | -100% | -57% | 3 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Finland Korisliiga Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 9 min |
| DEL Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| Professional Baseball Game | partly | 13 | 0 | 15% | 8% | -100% | -73% | 3 min |
| APF Division de Honor Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 5 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| NBA Game | ✔ | 12 | 0 | 8% | 0% | -100% | -86% | 14 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Women's Pro Basketball Game | ✔ | 10 | 0 | 30% | 10% | -100% | -48% | 9 min |
| Australia NBL Game | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 14 min |
| Slovakia SBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Canadian Premier League | ✘ | 9 | 1 | 44% | 44% | +937% | -23% | 32 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Major League Soccer Game | partly | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| College Hockey Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Men's ODI Cricket Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Russia VTB United Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Turkey BSL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| China League 1 Game | ✘ | 3 | 0 | 33% | 33% | -100% | -42% | 17 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 213 | 7% | 1% | 0% | -89% |
| 5–15 min | 106 | 15% | 5% | 1% | -74% |
| 15–30 min | 89 | 27% | 11% | 2% | -53% |
| 30–60 min | 68 | 13% | 6% | 0% | -77% |
| Over 60 min | 67 | 21% | 15% | 0% | -64% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 44 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-07 11:46 | TT Star Series Match | Loso Sebastian | ✘ | — | — | In play | — |
| 10-07 11:45 | ITF Women's Match | Carlota Martinez Cirez | ✘ | — | — | In play | — |
| 10-07 11:41 | Darts Match | Conor Heneghan | ✘ | — | — | In play | — |
| 10-07 11:39 | ITF Women's Match | Enola Chiesa | ✘ | — | — | In play | — |
| 10-07 11:35 | ITF Women's Match | Agnese Gentili | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:33 | ITF Women's Match | Simona Ogescu | ✘ | — | — | In play | — |
| 10-07 11:33 | ITF Men's Match | Rodrigo Alujas | ✘ | — | — | In play | — |
| 10-07 11:33 | Counter-Strike 2 Game | STATE | ✘ | — | — | In play | — |
| 10-07 11:28 | ITF Women's Match | Victoria Kapcia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:26 | Darts Match | Alex Spellman | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:23 | Challenger WTA | Noma Noha Akugue | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:12 | TT Star Series Match | Franco Carlos | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:09 | Darts Match | Andreas Harrysson | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:08 | ITF Women's Match | Sofia Shapatava | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:07 | Liiga Game | Mikkelin Jukurit | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:04 | Counter-Strike 2 Game | OG | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:04 | ITF Men's Match | Aaron Gabet | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:01 | Valorant game winner | T1 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 11:01 | ITF Men's Match | Hugo Car | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:58 | ITF Men's Match | Georgios Dimitriou | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:58 | ITF Men's Match | Rahul Dhokia | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-07 10:58 | Counter-Strike 2 Game | SINQU | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:58 | ITF Men's Match | Stefan Storch | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:54 | Darts Match | Conor Heneghan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:53 | Counter-Strike 2 Game | Orion Wanderers | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:47 | TT Star Series Match | Koszyk Boguslaw | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:45 | ITF Men's Match | Herman Hoeyeraal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:45 | ITF Women's Match | Giulia Safina Popa | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-07 10:40 | ITF Women's Match | Angela Fita Boluda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-07 10:34 | ITF Men's Match | Vincent Dullinger | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
