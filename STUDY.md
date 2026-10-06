# 1¢ Study

*Updated Mon Oct 5, 7:47 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 467 finished bets | 0% | -$42.05 | -60% | -9.00¢ | -$20.95 / -$21.10 |

*Expect about **58 buys a day**, roughly **$8.77/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 467 | -$49.80 | -71% |
| ESPN-verified leagues only, sell at 2¢ | 467 | -$53.41 | -76% |
| ESPN-verified leagues only, sell at 5¢ | 467 | -$54.45 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4493 | 467 | 2 (0%) | 1.1% | -$42.05 (-60%) | Hold to the end: -$42.05 (-60%) |

*In play right now: 10. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 92 | 2.7% | 0.0% (0) | -225% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 92 | 0 | -100% | -72% | -72% | -76% |
| ESPN win probability ≥ 2% | 18 | 0 | -100% | -61% | -57% | -100% |
| ESPN win probability ≥ 5% | 7 | 0 | -100% | -75% | -63% | -100% |
| ESPN win probability ≥ 10% | 4 | 0 | -100% | -57% | -35% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 467 | 14% | 8% | 5% | 2% | 1% | 1% |
| Unverified | 4016 | 5% | 4% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 2 | 0% | -$42.05 | -60% |
| Sell at 2¢ | 64 | 14% | -$53.41 | -76% |
| Sell at 3¢ | 39 | 8% | -$54.84 | -78% |
| Sell at 5¢ | 24 | 5% | -$54.45 | -78% |
| Sell at 10¢ | 11 | 2% | -$55.64 | -79% |
| Sell at 25¢ | 4 | 1% | -$56.81 | -81% |
| Sell at 50¢ | 3 | 1% | -$49.80 | -71% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 287 | 1 | 4% | 3% | -67% | -93% | 9 min |
| ITF Women's Match | ✘ | 283 | 0 | 11% | 5% | -100% | -81% | 4 min |
| ITF Men's Match | ✘ | 273 | 1 | 10% | 5% | -66% | -83% | 4 min |
| Challenger ATP  | ✘ | 230 | 1 | 8% | 2% | -59% | -86% | 5 min |
| TT Star Series Match | ✘ | 127 | 1 | 2% | 2% | -27% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 120 | 0 | 8% | 4% | -100% | -86% | 6 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| League of Legends Game | ✘ | 95 | 0 | 6% | 2% | -100% | -89% | 12 min |
| CONCACAF Nations League Game | partly | 90 | 2 | 21% | 9% | +107% | -63% | 20 min |
| Women's College Volleyball Match | ✘ | 89 | 1 | 7% | 2% | +5% | -88% | 55 min |
| Darts Match | ✘ | 65 | 0 | 2% | 2% | -100% | -97% | 9 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| Men's T20 Cricket Match | ✘ | 50 | 0 | 16% | 6% | -100% | -72% | 17 min |
| Challenger WTA | ✘ | 48 | 0 | 19% | 10% | -100% | -68% | 9 min |
| Dota 2 Game | ✘ | 47 | 0 | 2% | 2% | -100% | -96% | 28 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| International Friendly Game | partly | 45 | 0 | 11% | 2% | -100% | -81% | 17 min |
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
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| Japan NPB Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Argentina Primera Division Game | ✘ | 21 | 0 | 24% | 14% | -100% | -59% | 12 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| WTA Tennis Match | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 3 min |
| ELH Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Overwatch Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
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
| Professional Baseball Game | partly | 10 | 0 | 20% | 10% | -100% | -65% | 4 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Canadian Premier League | ✘ | 9 | 1 | 44% | 44% | +937% | -23% | 32 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| APF Division de Honor Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| College Hockey Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
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
| Men's ODI Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| NBA Game | ✔ | 3 | 0 | 33% | 0% | -100% | -42% | 15 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
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
| Under 5 min | 183 | 8% | 1% | 0% | -87% |
| 5–15 min | 89 | 13% | 4% | 1% | -77% |
| 15–30 min | 81 | 28% | 11% | 1% | -51% |
| 30–60 min | 58 | 12% | 5% | 0% | -79% |
| Over 60 min | 55 | 15% | 11% | 0% | -75% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 43 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-06 01:44 | NHL Game | Philadelphia | ✔ | 4:02 - 3rd · PHI 1 - TB 2 | — | In play | — |
| 10-06 01:40 | CONCACAF Nations League Game | Tie | ✔ | 82' · BOE 3 - GRN 1 | — | In play | — |
| 10-06 01:40 | CONCACAF Nations League Game | Bermuda | ✔ | 84' · BRB 1 - BER 1 | — | In play | — |
| 10-06 01:35 | CONCACAF Nations League Game | Grenada | ✔ | 77' · BOE 3 - GRN 1 | — | In play | — |
| 10-06 01:29 | NBA Game | Atlanta | ✔ | 57.2 - 4th · MEM 128 - ATL 121 | — | In play | — |
| 10-06 01:29 | NHL Game | San Jose | ✔ | 3:30 - 2nd · SJ 0 - DAL 4 | — | In play | — |
| 10-06 01:16 | NHL Game | Boston | ✔ | 4:24 - 2nd · OTT 4 - BOS 0 | — | In play | — |
| 10-06 01:10 | NBA Game | New York | ✔ | 6:46 - 4th · NY 82 - PHI 101 | — | In play | — |
| 10-06 00:49 | Uruguay Primera Division Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-06 00:16 | League of Legends Game | Zeu5 Esports | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 00:14 | Uruguay Primera Division Game | Montevideo City | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-06 00:11 | Professional Baseball Game | Cleveland | ✔ | Bot 9th · CHW 4 - CLE 3 | 0¢ | ❌ Lost | -$0.15 |
| 10-06 00:04 | APF Division de Honor Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:58 | Argentina Primera Division Game | Velez Sarsfield | ✘ | — | 3¢ | ❌ Lost | -$0.15 |
| 10-05 23:54 | CONCACAF Nations League Game | Martinique | ✔ | 90'+4' · SLV 1 - MTQ 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:52 | CONCACAF Nations League Game | El Salvador | ✔ | 90'+2' · SLV 1 - MTQ 1 | 4¢ | ❌ Lost | -$0.15 |
| 10-05 23:52 | APF Division de Honor Game | Cerro Porteno | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:48 | Argentina Primera Division Game | Platense | ✘ | — | 12¢ | ❌ Lost | -$0.15 |
| 10-05 23:46 | Argentina Primera Division Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:43 | League of Legends Game | 9z Globant | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:39 | Argentina Primera Division Game | Mendoza | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:17 | Men's ODI Cricket Match | United Arab Emirates | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 23:00 | ITF Women's Match | Kate Sharabura | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-05 22:55 | CONCACAF Nations League Game | Cuba | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 22:55 | CONCACAF Nations League Game | Saint Kitts and Nevis | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 22:55 | ITF Women's Match | Amaliia Elizarova | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 21:02 | ITF Women's Match | Diae El Jardi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 21:02 | ITF Men's Match | Jose Luis Claro | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 20:57 | Challenger ATP  | Valerio Aboian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-05 20:55 | CONCACAF Nations League Game | Tie | ✔ | 90'+4' · LCA 1 - GDL 0 | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
