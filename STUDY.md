# 1¢ Study

*Updated Sun Oct 4, 12:10 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 377 finished bets | 0% | -$42.55 | -75% | -11.29¢ | -$14.20 / -$28.35 |

*Expect about **55 buys a day**, roughly **$8.31/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 377 | -$43.05 | -76% |
| ESPN-verified leagues only, sell at 5¢ | 377 | -$44.20 | -78% |
| ESPN-verified leagues only, sell at 10¢ | 377 | -$44.76 | -79% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 4119 | 377 | 1 (0%) | 1.1% | -$42.55 (-75%) | Hold to the end: -$42.55 (-75%) |

*In play right now: 21. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 76 | 2.2% | 0.0% (0) | -175% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 76 | 0 | -100% | -75% | -79% | -77% |
| ESPN win probability ≥ 2% | 12 | 0 | -100% | -71% | -78% | -100% |
| ESPN win probability ≥ 5% | 4 | 0 | -100% | -57% | -35% | -100% |
| ESPN win probability ≥ 10% | 3 | 0 | -100% | -42% | -13% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 377 | 12% | 7% | 5% | 2% | 1% | 1% |
| Unverified | 3721 | 5% | 3% | 3% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 0% | -$42.55 | -75% |
| Sell at 2¢ | 45 | 12% | -$44.85 | -79% |
| Sell at 3¢ | 27 | 7% | -$46.02 | -81% |
| Sell at 5¢ | 19 | 5% | -$44.20 | -78% |
| Sell at 10¢ | 9 | 2% | -$44.76 | -79% |
| Sell at 25¢ | 3 | 1% | -$46.62 | -82% |
| Sell at 50¢ | 2 | 1% | -$43.05 | -76% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 1304 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Counter-Strike 2 Game | ✘ | 262 | 1 | 4% | 3% | -64% | -93% | 9 min |
| ITF Men's Match | ✘ | 257 | 0 | 9% | 4% | -100% | -84% | 5 min |
| ITF Women's Match | ✘ | 248 | 0 | 11% | 5% | -100% | -80% | 4 min |
| Challenger ATP  | ✘ | 202 | 1 | 8% | 2% | -54% | -85% | 5 min |
| TT Star Series Match | ✘ | 110 | 1 | 3% | 3% | -15% | -95% | 4 min |
| College Football Game | partly | 97 | 2 | 13% | 5% | +92% | -77% | 46 min |
| UEFA Nations League Game | ✔ | 94 | 0 | 9% | 4% | -100% | -85% | 8 min |
| League of Legends Game | ✘ | 88 | 0 | 7% | 2% | -100% | -88% | 12 min |
| CONCACAF Nations League Game | partly | 67 | 1 | 21% | 9% | +39% | -64% | 25 min |
| Women's College Volleyball Match | ✘ | 64 | 0 | 5% | 2% | -100% | -92% | 71 min |
| Darts Match | ✘ | 56 | 0 | 2% | 2% | -100% | -97% | 11 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| English National League Game | ✘ | 46 | 0 | 9% | 7% | -100% | -85% | 9 min |
| Men's T20 Cricket Match | ✘ | 43 | 0 | 16% | 7% | -100% | -72% | 18 min |
| Dota 2 Game | ✘ | 43 | 0 | 2% | 2% | -100% | -96% | 30 min |
| Serie C Game | ✘ | 43 | 1 | 9% | 2% | +117% | -84% | 9 min |
| Challenger WTA | ✘ | 37 | 0 | 22% | 14% | -100% | -63% | 10 min |
| International Friendly Game | partly | 37 | 0 | 5% | 0% | -100% | -91% | 17 min |
| NHL Game | ✔ | 34 | 0 | 12% | 6% | -100% | -80% | 5 min |
| Ettan Game | ✘ | 31 | 0 | 3% | 0% | -100% | -94% | 4 min |
| R6 Game | ✘ | 30 | 0 | 0% | 0% | -100% | -100% | 9 min |
| USL Championship Game | partly | 28 | 0 | 14% | 4% | -100% | -75% | 8 min |
| KHL Game | ✘ | 27 | 0 | 4% | 4% | -100% | -94% | 5 min |
| Brasileiro Serie B Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| KBO Game | ✘ | 23 | 0 | 4% | 4% | -100% | -92% | 5 min |
| National League Game | ✘ | 22 | 1 | 5% | 5% | +324% | -92% | 5 min |
| Japan NPB Game | ✘ | 21 | 0 | 0% | 0% | -100% | -100% | 2 min |
| WTA Tennis Match | ✘ | 20 | 0 | 5% | 0% | -100% | -91% | 3 min |
| Euroleague Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 15 min |
| AHL Game | ✘ | 20 | 0 | 5% | 5% | -100% | -91% | 7 min |
| Japan J2 League Game | ✘ | 20 | 0 | 15% | 5% | -100% | -74% | 113 min |
| ATP Tennis Match | ✘ | 19 | 0 | 11% | 0% | -100% | -82% | 3 min |
| ELH Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Champions League Women's Game | partly | 19 | 1 | 21% | 11% | +391% | -64% | 20 min |
| Liga DIMAYOR Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liiga Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 4 min |
| SHL Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Tweede Divisie Game | ✘ | 17 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Uruguay Primera Division Game | ✘ | 16 | 0 | 6% | 6% | -100% | -89% | 14 min |
| LNBP Basketball Game | ✘ | 16 | 0 | 6% | 0% | -100% | -89% | 12 min |
| Slovakian 2. Liga Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 111 min |
| Overwatch Game | ✘ | 16 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Eerste Divisie Game | ✘ | 16 | 0 | 12% | 12% | -100% | -78% | 7 min |
| Valorant game winner | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 15 min |
| NWSL Game | ✔ | 14 | 0 | 7% | 0% | -100% | -88% | 10 min |
| LaLiga 2 Game | partly | 14 | 0 | 14% | 7% | -100% | -75% | 18 min |
| Liga Expansion Game | ✘ | 14 | 0 | 14% | 14% | -100% | -75% | 17 min |
| England Women's Super League Game | ✘ | 14 | 0 | 7% | 0% | -100% | -88% | 40 min |
| DEL Game | ✘ | 13 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 11 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Rugby French 14 Match | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 42 min |
| Copa Del Rey Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 30 min |
| Argentina Primera Division Game | ✘ | 11 | 0 | 18% | 18% | -100% | -68% | 12 min |
| Brasileiro Serie C Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 4 min |
| Finland Korisliiga Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Czech NBL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| LNB Elite 2 Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Serie A Femminile Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 29 min |
| Eredivisie Vrouwen Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 22 min |
| Professional Baseball Game | partly | 9 | 0 | 22% | 11% | -100% | -61% | 5 min |
| Australia NBL Game | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 20 min |
| Slovakia SBL Game | ✘ | 9 | 0 | 0% | 0% | -100% | -100% | 21 min |
| Bundesliga Basketball Game | ✘ | 9 | 0 | 11% | 11% | -100% | -81% | 13 min |
| Women's Pro Basketball Game | ✔ | 8 | 0 | 25% | 12% | -100% | -57% | 13 min |
| Women's ODI Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 39 min |
| Sweden SBL Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 26 min |
| Austria BSL Game | ✘ | 8 | 0 | 12% | 0% | -100% | -78% | 5 min |
| Canadian Premier League | ✘ | 7 | 1 | 57% | 57% | +1233% | -1% | 29 min |
| Adriatic ABA Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 7 min |
| LNB Elite Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 16 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Major League Soccer Game | partly | 6 | 0 | 0% | 0% | -100% | -100% | 5 min |
| APF Division de Honor Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 3 min |
| EFL League One Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Spain Liga ACB Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 83 min |
| College Hockey Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 24 min |
| Slovenia 1. SKL Game | ✘ | 5 | 0 | 20% | 20% | -100% | -65% | 22 min |
| Russia VTB United Game | ✘ | 5 | 0 | 20% | 0% | -100% | -65% | 38 min |
| Croatia Premijer Liga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Italy Serie A Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Turkey BSL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 15 min |
| England Super League Basketball Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 17 min |
| Brasileiro Serie A Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| CFL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 22 min |
| United Rugby Championship Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| LKL Lithuania Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Women's T20 Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 37 min |
| PREM Rugby Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
| Italy Serie A2 Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| NFL Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 14 min |
| Club Friendlies | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Chile Liga de Primera Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| England Super League Rugby Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| NBA Game | ✔ | 1 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Rugby NRL Match | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 7 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 134 | 4% | 1% | 0% | -92% |
| 5–15 min | 67 | 10% | 3% | 0% | -82% |
| 15–30 min | 71 | 28% | 11% | 1% | -51% |
| 30–60 min | 55 | 11% | 5% | 0% | -81% |
| Over 60 min | 50 | 12% | 10% | 0% | -79% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 39 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-04 18:08 | R6 Game | FaZe Clan | ✘ | — | — | In play | — |
| 10-04 18:07 | ITF Men's Match | Theo Papamalamis | ✘ | — | — | In play | — |
| 10-04 17:59 | Italy Serie A2 Game | Juvi Cremona 1952 | ✘ | — | — | In play | — |
| 10-04 17:58 | Italy Serie A2 Game | Juvecaserta 2021 | ✘ | — | — | In play | — |
| 10-04 17:58 | League of Legends Game | Barça eSports | ✘ | — | — | In play | — |
| 10-04 17:55 | ELH Game | HC Verva Litvinov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:55 | Serie A Femminile Game | Tie | ✘ | — | — | In play | — |
| 10-04 17:55 | Austria BSL Game | BC Vienna | ✘ | — | — | In play | — |
| 10-04 17:54 | Italy Serie A2 Game | AS Pistoia Basket 2000 | ✘ | — | — | In play | — |
| 10-04 17:54 | Adriatic ABA Game | KK Crvena zvezda Belgrade | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:54 | Copa Del Rey Game | Reg Time: UD Maracena | ✘ | — | — | In play | — |
| 10-04 17:54 | Copa Del Rey Game | Reg Time: UE Tavernes | ✘ | — | — | In play | — |
| 10-04 17:53 | Italy Serie A2 Game | Pallacanestro Ruvo di Puglia | ✘ | — | — | In play | — |
| 10-04 17:52 | UEFA Nations League Game | Austria | ✔ | 90'+4' · AUT 1 - KOS 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:52 | Italy Serie A2 Game | Dinamo Sassari | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:52 | UEFA Nations League Game | Kosovo | ✔ | 90'+4' · AUT 1 - KOS 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:51 | Uruguay Primera Division Game | Las Piedras | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:51 | Uruguay Primera Division Game | Boston River | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:49 | Serie A Femminile Game | Como | ✘ | — | — | In play | — |
| 10-04 17:49 | UEFA Nations League Game | Tie | ✔ | 90'+3' · AND 0 - MLT 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:48 | Czech NBL Game | Basket Brno | ✘ | — | — | In play | — |
| 10-04 17:47 | Italy Serie A2 Game | Rinascita Basket Rimini | ✘ | — | — | In play | — |
| 10-04 17:45 | Bundesliga Basketball Game | Riesen Ludwigsburg | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:43 | Men's T20 Cricket Match | Gamblers SC | ✘ | — | — | In play | — |
| 10-04 17:39 | ELH Game | HC Vitkovice | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:38 | Italy Serie A2 Game | Urania Milano | ✘ | — | — | In play | — |
| 10-04 17:36 | UEFA Nations League Game | Andorra | ✔ | 80' · AND 0 - MLT 1 | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:29 | Italy Serie A Game | Pallacanestro Trieste 2004 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:28 | Serie C Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-04 17:23 | Austria BSL Game | BK Dukes Klosterneuburg | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
