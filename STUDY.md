# 1¢ Study

*Updated Thu Oct 1, 2:39 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 131 finished bets | 1% | -$5.65 | -29% | -4.31¢ | -$9.75 / $4.10 |

*Expect about **37 buys a day**, roughly **$5.53/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 131 | -$12.90 | -66% |
| ESPN-verified leagues only, sell at 2¢ | 131 | -$14.97 | -76% |
| ESPN-verified leagues only, sell at 3¢ | 131 | -$15.36 | -78% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 2382 | 131 | 1 (1%) | 1.1% | -$5.65 (-29%) | Hold to the end: -$5.65 (-29%) |

*In play right now: 17. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 9 | 1.1% | 0.0% (0) | -13% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 9 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 2% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 131 | 14% | 8% | 5% | 2% | 1% | 1% |
| Unverified | 2234 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 1% | -$5.65 | -29% |
| Sell at 2¢ | 18 | 14% | -$14.97 | -76% |
| Sell at 3¢ | 11 | 8% | -$15.36 | -78% |
| Sell at 5¢ | 6 | 5% | -$15.75 | -80% |
| Sell at 10¢ | 3 | 2% | -$15.72 | -80% |
| Sell at 25¢ | 1 | 1% | -$16.34 | -83% |
| Sell at 50¢ | 1 | 1% | -$12.90 | -66% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 966 | 0 | 1% | 0% | -100% | -99% | 5 min |
| ITF Men's Match | ✘ | 212 | 0 | 8% | 4% | -100% | -85% | 5 min |
| ITF Women's Match | ✘ | 201 | 0 | 11% | 6% | -100% | -80% | 4 min |
| Counter-Strike 2 Game | ✘ | 129 | 1 | 3% | 2% | -28% | -95% | 10 min |
| Challenger ATP  | ✘ | 129 | 0 | 8% | 2% | -100% | -87% | 5 min |
| TT Star Series Match | ✘ | 89 | 1 | 2% | 2% | +5% | -96% | 4 min |
| League of Legends Game | ✘ | 70 | 0 | 9% | 3% | -100% | -85% | 11 min |
| AFCON Game Winner | ✘ | 47 | 1 | 15% | 4% | +99% | -74% | 12 min |
| UEFA Nations League Game | ✔ | 38 | 0 | 8% | 0% | -100% | -86% | 6 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| Men's T20 Cricket Match | ✘ | 26 | 0 | 15% | 8% | -100% | -73% | 18 min |
| Dota 2 Game | ✘ | 26 | 0 | 0% | 0% | -100% | -100% | 28 min |
| Liga Leumit Game | ✘ | 24 | 0 | 0% | 0% | -100% | -100% | 7 min |
| English National League Game | ✘ | 24 | 0 | 4% | 4% | -100% | -93% | 6 min |
| Challenger WTA | ✘ | 22 | 0 | 14% | 9% | -100% | -76% | 10 min |
| R6 Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 8 min |
| International Friendly Game | partly | 18 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Champions League Women's Game | partly | 15 | 1 | 27% | 13% | +522% | -54% | 20 min |
| KBO Game | ✘ | 14 | 0 | 7% | 7% | -100% | -88% | 4 min |
| Darts Match | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 41 min |
| KHL Game | ✘ | 13 | 0 | 8% | 8% | -100% | -87% | 5 min |
| Euroleague Game | ✘ | 13 | 0 | 23% | 8% | -100% | -60% | 38 min |
| Liga DIMAYOR Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ATP Tennis Match | ✘ | 12 | 0 | 8% | 0% | -100% | -86% | 2 min |
| EuroCup Basketball Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Japan NPB Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 12 min |
| SHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| National League Game | ✘ | 10 | 1 | 10% | 10% | +833% | -83% | 6 min |
| USL Championship Game | ✔ | 10 | 0 | 30% | 0% | -100% | -48% | 11 min |
| Women's College Volleyball Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 86 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| ELH Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 3 min |
| NHL Game | ✔ | 8 | 0 | 25% | 0% | -100% | -57% | 4 min |
| Valorant game winner | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Uruguay Primera Division Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 10 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie B Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Women's Pro Basketball Game | ✔ | 6 | 0 | 17% | 17% | -100% | -71% | 15 min |
| Women's ODI Cricket Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Liiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Professional Baseball Game | partly | 5 | 0 | 20% | 0% | -100% | -65% | 9 min |
| Slovakia SBL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 35 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Major League Soccer Game | partly | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Finland Korisliiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 63 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Australia NBL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovenia 1. SKL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 105 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Russia VTB United Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 37 min |
| Peru Liga 1 Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 17 min |
| Canadian Premier League | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 18 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Croatia Premijer Liga Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 98 min |
| Austria BSL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 86 min |
| DEL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 44 min |
| Bundesliga Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 13 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 49 | 4% | 0% | 0% | -93% |
| 5–15 min | 26 | 19% | 4% | 0% | -67% |
| 15–30 min | 25 | 28% | 12% | 4% | -51% |
| 30–60 min | 17 | 24% | 12% | 0% | -59% |
| Over 60 min | 14 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 5 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10-01 20:38 | UEFA Nations League Game | Israel | ✔ | 90'+4' · KOS 0 - ISR 0 | — | In play | — |
| 10-01 20:38 | UEFA Nations League Game | Kosovo | ✔ | 90'+3' · KOS 0 - ISR 0 | — | In play | — |
| 10-01 20:36 | UEFA Nations League Game | Malta | ✔ | 90'+3' · GIB 1 - MLT 1 | — | In play | — |
| 10-01 20:35 | UEFA Nations League Game | Tie | ✔ | 90'+3' · NOR 1 - WAL 2 | — | In play | — |
| 10-01 20:34 | ITF Women's Match | Francesca Pace | ✘ | — | — | In play | — |
| 10-01 20:33 | UEFA Nations League Game | Tie | ✔ | 87' · POR 3 - DEN 2 | — | In play | — |
| 10-01 20:31 | R6 Game | Wildcard Gaming | ✘ | — | — | In play | — |
| 10-01 20:30 | UEFA Nations League Game | Denmark | ✔ | 84' · POR 3 - DEN 2 | — | In play | — |
| 10-01 20:28 | UEFA Nations League Game | Norway | ✔ | 86' · NOR 1 - WAL 2 | — | In play | — |
| 10-01 20:28 | TT Elite Series Match | Zbigniew Nocun | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:28 | TT Elite Series Match | Arkadiusz Mugowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:27 | Challenger ATP  | Stefan Kozlov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:26 | ITF Men's Match | Dragos Nicolae Cazacu | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:26 | Counter-Strike 2 Game | SINQU | ✘ | — | — | In play | — |
| 10-01 20:23 | Euroleague Game | BC Olympiakos Piraeus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:22 | TT Elite Series Match | Adrian Myszewski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:21 | TT Elite Series Match | Grzegorz Jurowicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:20 | League of Legends Game | Team Phantasma | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:18 | ITF Men's Match | Alejandro Melero Kretzer | ✘ | — | — | In play | — |
| 10-01 20:15 | Champions League Women's Game | Tie | ✔ | 59' · OHL 0 - PSG 2 | — | In play | — |
| 10-01 20:15 | UEFA Nations League Game | Austria | ✔ | 67' · AUT 0 - IRL 2 | — | In play | — |
| 10-01 20:08 | TT Elite Series Match | Michal Wolny | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:07 | National League Game | HC Ambri-Piotta | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:05 | UEFA Nations League Game | Tie | ✔ | 61' · SRB 0 - GER 1 | — | In play | — |
| 10-01 20:02 | Darts Match | Stephen Bunting | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:01 | TT Star Series Match | Tormos Kilian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 20:01 | Euroleague Game | Anadolu Efes SK | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 10-01 19:57 | UEFA Nations League Game | Gibraltar | ✔ | 54' · GIB 0 - MLT 1 | — | In play | — |
| 10-01 19:55 | TT Elite Series Match | Krzysztof Juszczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 10-01 19:54 | TT Elite Series Match | Linek Adam | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
