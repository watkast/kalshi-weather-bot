# 1¢ Study

*Updated Sat Oct 3, 4:18 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 284 finished bets | 0% | -$28.60 | -67% | -10.07¢ | -$7.30 / -$21.30 |

*Expect about **49 buys a day**, roughly **$7.40/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 284 | -$33.43 | -78% |
| ESPN-verified leagues only, sell at 5¢ | 284 | -$33.50 | -79% |
| ESPN-verified leagues only, sell at 2¢ | 284 | -$33.76 | -79% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 3706 | 284 | 1 (0%) | 1.1% | -$28.60 (-67%) | Hold to the end: -$28.60 (-67%) |

*In play right now: 31. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 33 | 2.8% | 0.0% (0) | -285% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33 | 0 | -100% | -74% | -84% | -74% |
| ESPN win probability ≥ 2% | 5 | 0 | -100% | -65% | -100% | -100% |
| ESPN win probability ≥ 5% | 1 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 10% | 1 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 284 | 12% | 7% | 5% | 2% | 1% | 0% |
| Unverified | 3391 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$28.60 | -67% |
| Sell at 2¢ | 34 | 12% | -$33.76 | -79% |
| Sell at 3¢ | 19 | 7% | -$35.19 | -83% |
| Sell at 5¢ | 14 | 5% | -$33.50 | -79% |
| Sell at 10¢ | 7 | 2% | -$33.43 | -78% |
| Sell at 25¢ | 2 | 1% | -$35.98 | -84% |
| Sell at 50¢ | 1 | 0% | -$35.85 | -84% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| ITF Men's Match | ✘ | 250 | 0 | 8% | 4% | -100% | -85% | 4 min |
| Counter-Strike 2 Game | ✘ | 246 | 1 | 3% | 2% | -62% | -94% | 9 min |
| ITF Women's Match | ✘ | 233 | 0 | 12% | 6% | -100% | -79% | 4 min |
| Challenger ATP  | ✘ | 157 | 0 | 8% | 1% | -100% | -87% | 4 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| UEFA Nations League Game | ✔ | 88 | 0 | 9% | 5% | -100% | -84% | 9 min |
| League of Legends Game | ✘ | 85 | 0 | 7% | 2% | -100% | -88% | 11 min |
| CONCACAF Nations League Game | partly | 63 | 1 | 21% | 8% | +48% | -64% | 25 min |
| Darts Match | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 11 min |
| Women's College Volleyball Match | ✘ | 51 | 0 | 6% | 2% | -100% | -90% | 63 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Dota 2 Game | ✘ | 41 | 0 | 2% | 2% | -100% | -96% | 31 min |
| Men's T20 Cricket Match | ✘ | 38 | 0 | 18% | 8% | -100% | -68% | 18 min |
| College Football Game | partly | 34 | 0 | 12% | 6% | -100% | -80% | 56 min |
| International Friendly Game | partly | 32 | 0 | 3% | 0% | -100% | -95% | 14 min |
| R6 Game | ✘ | 29 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Challenger WTA | ✘ | 28 | 0 | 14% | 11% | -100% | -75% | 10 min |
| Serie C Game | ✘ | 26 | 0 | 8% | 0% | -100% | -87% | 5 min |
| Ettan Game | ✘ | 25 | 0 | 4% | 0% | -100% | -93% | 4 min |
| Brasileiro Serie B Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 14 min |
| KHL Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 5 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| NHL Game | ✔ | 21 | 0 | 14% | 5% | -100% | -75% | 5 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| National League Game | ✘ | 20 | 1 | 5% | 5% | +367% | -91% | 5 min |
| KBO Game | ✘ | 19 | 0 | 5% | 5% | -100% | -91% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Japan NPB Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| WTA Tennis Match | ✘ | 17 | 0 | 6% | 0% | -100% | -90% | 3 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Liga DIMAYOR Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 12 min |
| LNBP Basketball Game | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 12 min |
| ATP Tennis Match | ✘ | 15 | 0 | 13% | 0% | -100% | -77% | 2 min |
| ELH Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Slovakian 2. Liga Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 111 min |
| Eerste Divisie Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 3 min |
| Valorant game winner | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 13 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Rugby French 14 Match | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 42 min |
| Argentina Primera Division Game | ✘ | 11 | 0 | 18% | 18% | -100% | -68% | 12 min |
| Uruguay Primera Division Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 12 min |
| Argentine Nacional B Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 8 min |
| NWSL Game | ✔ | 10 | 0 | 0% | 0% | -100% | -100% | 6 min |
| LaLiga 2 Game | ✔ | 10 | 0 | 10% | 0% | -100% | -83% | 11 min |
| Overwatch Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| AHL Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 8 min |
| Japan J2 League Game | ✘ | 10 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Czech NBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Slovakia SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Australia NBL Game | ✘ | 7 | 0 | 14% | 0% | -100% | -75% | 8 min |
| DEL Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie C Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 4 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Baseball Game | partly | 6 | 0 | 17% | 0% | -100% | -71% | 7 min |
| Adriatic ABA Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 9 min |
| LNB Elite Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Liga Expansion Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 7 min |
| Serie A Femminile Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Copa Del Rey Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 69 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Bundesliga Basketball Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 13 min |
| Canadian Premier League | ✘ | 4 | 0 | 50% | 50% | -100% | -13% | 119 min |
| Austria BSL Game | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 12 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Russia VTB United Game | ✘ | 3 | 0 | 33% | 0% | -100% | -42% | 5 min |
| England Super League Basketball Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 26 min |
| CFL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 35 min |
| LKL Lithuania Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Brasileiro Serie A Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| England Women's Super League Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| PREM Rugby Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Spain Liga ACB Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Italy Serie A2 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Italy Serie A Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |
| NFL Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 1 min |
| Women's T20 Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 52 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 102 | 5% | 1% | 0% | -92% |
| 5–15 min | 52 | 12% | 2% | 0% | -80% |
| 15–30 min | 51 | 24% | 8% | 2% | -59% |
| 30–60 min | 44 | 14% | 7% | 0% | -76% |
| Over 60 min | 35 | 14% | 14% | 0% | -75% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 33 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-03 22:17 | CONCACAF Nations League Game | Tie | ✘ | — | — | In play | — |
| 10-03 22:14 | College Football Game | Florida | ✔ | 0:49 - 3rd · FLA 10 - MIZ 30 | — | In play | — |
| 10-03 22:13 | Canadian Premier League | Hamilton | ✘ | — | — | In play | — |
| 10-03 22:13 | College Football Game | Samford | ✔ | 9:51 - 4th · SAM 14 - UAB 23 | — | In play | — |
| 10-03 22:05 | College Football Game | UMass | ✔ | 14:13 - 4th · EMU 34 - MASS 7 | — | In play | — |
| 10-03 22:04 | College Football Game | Texas Southern | ✔ | 15:00 - 1st · TXSO 0 - FAU 0 | — | In play | — |
| 10-03 22:03 | NWSL Game | Racing Louisville | ✔ | 90'+8' · UTA 1 - LOU 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 22:00 | College Football Game | Virginia | ✔ | 3:16 - 3rd · UVA 7 - FSU 30 | — | In play | — |
| 10-03 21:59 | College Football Game | Iowa | ✔ | 6:11 - 3rd · OSU 23 - IOWA 6 | — | In play | — |
| 10-03 21:59 | College Football Game | Hampton | ✘ | — | — | In play | — |
| 10-03 21:56 | Valorant game winner | Eternal Fire | ✘ | — | — | In play | — |
| 10-03 21:55 | Brasileiro Serie C Game | Santa Cruz FC PE | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:55 | Brasileiro Serie C Game | Floresta | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:55 | Brasileiro Serie C Game | Maringa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:54 | APF Division de Honor Game | Club Guarani | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:54 | APF Division de Honor Game | San Lorenzo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:53 | NWSL Game | Utah Royals | ✔ | 89' · UTA 0 - LOU 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:52 | Argentina Primera Division Game | Lanus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:52 | Argentina Primera Division Game | Newell's Old Boys | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:52 | College Football Game | Northern Colorado | ✘ | — | — | In play | — |
| 10-03 21:46 | Canadian Premier League | Tie | ✘ | — | — | In play | — |
| 10-03 21:45 | Brasileiro Serie C Game | Botafogo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:45 | College Football Game | Akron | ✔ | 3:29 - 3rd · AKR 10 - CMU 35 | — | In play | — |
| 10-03 21:44 | Canadian Premier League | HFX | ✘ | — | — | In play | — |
| 10-03 21:44 | Argentina Primera Division Game | Tucuman | ✘ | — | 8¢ | ❌ Lost | -$0.15 |
| 10-03 21:42 | AHL Game | Chicago Wolves | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:41 | CFL Game | Toronto Argonauts | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:36 | College Football Game | Wyoming | ✔ | 14:00 - 3rd · WYO 0 - NDSU 17 | — | In play | — |
| 10-03 21:35 | Brasileiro Serie B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-03 21:35 | Women's College Volleyball Match | North Carolina Greensboro | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
