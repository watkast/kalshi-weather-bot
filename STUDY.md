# 1¢ Study

*Updated Thu Oct 8, 4:50 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 569 finished bets | 1% | -$43.35 | -51% | -7.62¢ | -$28.60 / -$14.75 |

*Expect about **52 buys a day**, roughly **$7.76/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 569 | -$51.60 | -60% |
| ESPN-verified leagues only, sell at 5¢ | 569 | -$63.90 | -75% |
| ESPN-verified leagues only, sell at 2¢ | 569 | -$64.29 | -75% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 5614 | 569 | 3 (1%) | 1.1% | -$43.35 (-51%) | Hold to the end: -$43.35 (-51%) |

*In play right now: 16. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 116 | 2.9% | 0.0% (0) | -238% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 116 | 0 | -100% | -75% | -75% | -78% |
| ESPN win probability ≥ 2% | 28 | 0 | -100% | -69% | -72% | -100% |
| ESPN win probability ≥ 5% | 11 | 0 | -100% | -84% | -76% | -100% |
| ESPN win probability ≥ 10% | 6 | 0 | -100% | -71% | -57% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 569 | 14% | 9% | 6% | 3% | 1% | 1% |
| Unverified | 5029 | 6% | 4% | 3% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 3 | 1% | -$43.35 | -51% |
| Sell at 2¢ | 81 | 14% | -$64.29 | -75% |
| Sell at 3¢ | 54 | 9% | -$64.29 | -75% |
| Sell at 5¢ | 33 | 6% | -$63.90 | -75% |
| Sell at 10¢ | 16 | 3% | -$64.39 | -75% |
| Sell at 25¢ | 6 | 1% | -$65.49 | -77% |
| Sell at 50¢ | 5 | 1% | -$51.60 | -60% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Women's Match | ✘ | 479 | 0 | 12% | 6% | -100% | -79% | 4 min |
| ITF Men's Match | ✘ | 416 | 1 | 10% | 6% | -78% | -83% | 5 min |
| Counter-Strike 2 Game | ✘ | 406 | 1 | 3% | 2% | -77% | -94% | 10 min |
| Challenger ATP  | ✘ | 279 | 2 | 9% | 3% | -33% | -85% | 5 min |
| TT Star Series Match | ✘ | 177 | 1 | 2% | 2% | -47% | -96% | 4 min |
| UEFA Nations League Game | ✔ | 140 | 0 | 9% | 5% | -100% | -84% | 7 min |
| eSoccer Game | ✘ | 138 | 0 | 1% | 1% | -100% | -99% | 2 min |
| League of Legends Game | ✘ | 111 | 0 | 6% | 3% | -100% | -89% | 11 min |
| CONCACAF Nations League Game | partly | 108 | 2 | 20% | 7% | +73% | -65% | 19 min |
| Darts Match | ✘ | 100 | 0 | 1% | 1% | -100% | -98% | 8 min |
| College Football Game | partly | 100 | 2 | 14% | 6% | +87% | -76% | 46 min |
| Women's College Volleyball Match | ✘ | 94 | 1 | 6% | 2% | -1% | -89% | 63 min |
| Men's T20 Cricket Match | ✘ | 72 | 0 | 15% | 6% | -100% | -74% | 21 min |
| Dota 2 Game | ✘ | 62 | 0 | 3% | 3% | -100% | -94% | 29 min |
| Challenger WTA | ✘ | 61 | 0 | 16% | 10% | -100% | -72% | 8 min |
| International Friendly Game | partly | 59 | 1 | 15% | 7% | +58% | -74% | 17 min |
| NHL Game | ✔ | 55 | 0 | 13% | 5% | -100% | -78% | 4 min |
| Serie C Game | ✘ | 53 | 1 | 8% | 2% | +76% | -87% | 6 min |
| AFCON Game Winner | ✘ | 49 | 1 | 16% | 4% | +90% | -72% | 14 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Brasileiro Serie B Game | ✘ | 42 | 0 | 2% | 0% | -100% | -96% | 11 min |
| R6 Game | ✘ | 40 | 0 | 0% | 0% | -100% | -100% | 9 min |
| KBO Game | ✘ | 38 | 0 | 5% | 5% | -100% | -91% | 7 min |
| KHL Game | ✘ | 36 | 0 | 3% | 3% | -100% | -95% | 5 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| LNBP Basketball Game | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 12 min |
| ATP Tennis Match | ✘ | 30 | 0 | 10% | 3% | -100% | -83% | 3 min |
| USL Championship Game | partly | 30 | 0 | 13% | 3% | -100% | -77% | 8 min |
| EFL Trophy Game | ✘ | 29 | 0 | 7% | 7% | -100% | -88% | 47 min |
| eBasketball Game | ✘ | 29 | 1 | 0% | 0% | +222% | +222% | 1 min |
| Liga DIMAYOR Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| EuroCup Basketball Game | ✘ | 28 | 0 | 4% | 0% | -100% | -94% | 8 min |
| AHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 6 min |
| Euroleague Game | ✘ | 26 | 0 | 23% | 4% | -100% | -60% | 15 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| SHL Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 24 | 1 | 4% | 4% | +289% | -93% | 5 min |
| Japan NPB Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liiga Game | ✘ | 23 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Argentina Primera Division Game | ✘ | 23 | 0 | 22% | 13% | -100% | -62% | 9 min |
| Uruguay Primera Division Game | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 12 min |
| ELH Game | ✘ | 22 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LaLiga 2 Game | partly | 22 | 0 | 18% | 9% | -100% | -68% | 9 min |
| WTA Tennis Match | ✘ | 21 | 0 | 10% | 0% | -100% | -83% | 3 min |
| Valorant game winner | ✘ | 21 | 0 | 5% | 0% | -100% | -92% | 15 min |
| NWSL Game | ✔ | 20 | 0 | 15% | 0% | -100% | -74% | 10 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| Overwatch Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Slovakian 2. Liga Game | ✘ | 18 | 0 | 11% | 11% | -100% | -81% | 111 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| NBA Game | ✔ | 17 | 0 | 12% | 0% | -100% | -80% | 4 min |
| Argentine Nacional B Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 13 min |
| Professional Baseball Game | partly | 16 | 0 | 12% | 6% | -100% | -78% | 2 min |
| NFL Game | ✔ | 16 | 0 | 25% | 6% | -100% | -57% | 3 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Brasileiro Serie A Game | partly | 16 | 0 | 19% | 12% | -100% | -68% | 4 min |
| Liga Expansion Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 24 min |
| Finland Korisliiga Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 8 min |
| DEL Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Rugby French 14 Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 40 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| Copa Del Rey Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 33 min |
| APF Division de Honor Game | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 5 min |
| Serie A Femminile Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Women's Pro Basketball Game | ✔ | 11 | 0 | 27% | 9% | -100% | -53% | 7 min |
| Australia NBL Game | ✘ | 11 | 0 | 9% | 0% | -100% | -84% | 8 min |
| Czech NBL Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Canadian Premier League | ✘ | 11 | 1 | 36% | 36% | +748% | -37% | 32 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Slovakia SBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Bundesliga Basketball Game | ✘ | 10 | 0 | 20% | 10% | -100% | -65% | 13 min |
| Adriatic ABA Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Italy Serie A2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| China League 1 Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 14 min |
| Austria BSL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 5 min |
| Major League Soccer Game | partly | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Men's ODI Cricket Match | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 15 min |
| LNB Elite Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Spain Liga ACB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Italy Serie A Game | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 6 min |
| Russia VTB United Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 16 min |
| College Hockey Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Slovenia 1. SKL Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 18 min |
| Peru Liga 1 Game | ✘ | 6 | 0 | 33% | 17% | -100% | -42% | 12 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Turkey BSL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 14 min |
| LKL Lithuania Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Women's T20 Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| USL Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Vietnam V-League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 228 | 7% | 1% | 0% | -88% |
| 5–15 min | 108 | 15% | 5% | 1% | -74% |
| 15–30 min | 93 | 28% | 12% | 2% | -52% |
| 30–60 min | 72 | 12% | 6% | 0% | -78% |
| Over 60 min | 67 | 21% | 15% | 0% | -64% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 43 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-08 22:48 | Darts Match | Dan Lauby Jr. | ✘ | — | — | In play | — |
| 10-08 22:46 | eSoccer Game | FC Barcelona (Homie) | ✘ | — | — | In play | — |
| 10-08 22:46 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-08 22:43 | eBasketball Game | New Orleans Pelicans (Zion) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:42 | eSoccer Game | Boca Juniors (Frost) | ✘ | — | — | In play | — |
| 10-08 22:42 | eSoccer Game | Tie | ✘ | — | — | In play | — |
| 10-08 22:42 | eSoccer Game | Spurs (Lucy) | ✘ | — | — | In play | — |
| 10-08 22:41 | eSoccer Game | Manchester City (Quinnie) | ✘ | — | — | In play | — |
| 10-08 22:41 | ITF Men's Match | Miles Clark | ✘ | — | — | In play | — |
| 10-08 22:40 | eSoccer Game | Palmeiras (Declan) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:40 | eSoccer Game | Universitario (Aron) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:40 | Counter-Strike 2 Game | Turma do Pagode | ✘ | — | — | In play | — |
| 10-08 22:39 | eSoccer Game | Chelsea (Ellie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:39 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:32 | eSoccer Game | CA Osasuna (Homie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:32 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:30 | Peru Liga 1 Game | Atletico Grau | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:28 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:28 | eSoccer Game | River Plate (Frenkie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:27 | Peru Liga 1 Game | Los Chankas CYC | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 10-08 22:27 | eSoccer Game | Spurs (Lucy) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:27 | eSoccer Game | Manchester City (Quinnie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:26 | Darts Match | William Borland | ✘ | — | — | In play | — |
| 10-08 22:25 | eSoccer Game | Boca Juniors (Frost) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:25 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:25 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:25 | eSoccer Game | Chelsea (Ellie) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:18 | eSoccer Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:17 | eSoccer Game | Girona (Mordor) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-08 22:16 | eSoccer Game | Palmeiras (Declan) | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
