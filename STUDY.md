# 1¢ Study

*Updated Wed Sep 30, 1:37 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, hold to the end | 108 finished bets | 1% | -$2.20 | -14% | -2.04¢ | -$8.10 / $5.90 |

*Expect about **38 buys a day**, roughly **$5.66/day** at risk; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 50¢ | 108 | -$9.45 | -58% |
| ESPN-verified leagues only, sell at 10¢ | 108 | -$12.27 | -76% |
| ESPN-verified leagues only, sell at 5¢ | 108 | -$12.30 | -76% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 1748 | 108 | 1 (1%) | 1.1% | -$2.20 (-14%) | Hold to the end: -$2.20 (-14%) |

*In play right now: 8. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 7 | 1.2% | 0.0% (0) | -23% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 7 | 0 | -100% | -100% | -100% | -100% |
| ESPN win probability ≥ 2% | 2 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 108 | 13% | 8% | 6% | 3% | 1% | 1% |
| Unverified | 1632 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 1 | 1% | -$2.20 | -14% |
| Sell at 2¢ | 14 | 13% | -$12.56 | -78% |
| Sell at 3¢ | 9 | 8% | -$12.69 | -78% |
| Sell at 5¢ | 6 | 6% | -$12.30 | -76% |
| Sell at 10¢ | 3 | 3% | -$12.27 | -76% |
| Sell at 25¢ | 1 | 1% | -$12.89 | -80% |
| Sell at 50¢ | 1 | 1% | -$9.45 | -58% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 700 | 0 | 0% | 0% | -100% | -99% | 5 min |
| ITF Women's Match | ✘ | 155 | 0 | 11% | 6% | -100% | -81% | 5 min |
| ITF Men's Match | ✘ | 154 | 0 | 9% | 4% | -100% | -84% | 6 min |
| Challenger ATP  | ✘ | 104 | 0 | 10% | 2% | -100% | -83% | 5 min |
| Counter-Strike 2 Game | ✘ | 87 | 1 | 5% | 3% | +7% | -92% | 11 min |
| TT Star Series Match | ✘ | 61 | 1 | 3% | 3% | +53% | -94% | 4 min |
| League of Legends Game | ✘ | 56 | 0 | 9% | 2% | -100% | -85% | 11 min |
| AFCON Game Winner | ✘ | 45 | 1 | 16% | 4% | +107% | -73% | 12 min |
| UEFA Nations League Game | ✔ | 36 | 0 | 8% | 0% | -100% | -86% | 8 min |
| CONCACAF Nations League Game | partly | 32 | 0 | 22% | 6% | -100% | -62% | 21 min |
| Men's T20 Cricket Match | ✘ | 20 | 0 | 15% | 10% | -100% | -74% | 17 min |
| English National League Game | ✘ | 20 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Challenger WTA | ✘ | 19 | 0 | 16% | 11% | -100% | -73% | 10 min |
| Dota 2 Game | ✘ | 18 | 0 | 0% | 0% | -100% | -100% | 28 min |
| International Friendly Game | ✔ | 14 | 0 | 0% | 0% | -100% | -100% | 12 min |
| R6 Game | ✘ | 14 | 0 | 0% | 0% | -100% | -100% | 9 min |
| Liga DIMAYOR Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ATP Tennis Match | ✘ | 10 | 0 | 10% | 0% | -100% | -83% | 2 min |
| KHL Game | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KBO Game | ✘ | 10 | 0 | 10% | 10% | -100% | -83% | 20 min |
| WTA Tennis Match | ✘ | 9 | 0 | 11% | 0% | -100% | -81% | 3 min |
| Japan NPB Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Euroleague Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 68 min |
| EuroCup Basketball Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ELH Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| National League Game | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 3 min |
| Champions League Women's Game | partly | 7 | 1 | 43% | 29% | +1233% | -26% | 27 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| Brasileiro Serie B Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Czech NBL Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Valorant game winner | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Liiga Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 3 min |
| NHL Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 4 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Women's Pro Basketball Game | ✔ | 4 | 0 | 25% | 25% | -100% | -57% | 22 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Women's ODI Cricket Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 38 min |
| Finland Korisliiga Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 63 min |
| Sweden SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 36 min |
| Professional Baseball Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 19 min |
| Slovakia SBL Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 25 min |
| SHL Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| China League 1 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 11 min |
| Slovakian Cup Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovenia 1. SKL Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 105 min |
| Australia NBL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Men's ODI Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 45 min |
| Russia VTB United Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 37 min |
| Overwatch Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 40 | 5% | 0% | 0% | -91% |
| 5–15 min | 22 | 23% | 5% | 0% | -61% |
| 15–30 min | 18 | 17% | 17% | 6% | -71% |
| 30–60 min | 17 | 24% | 12% | 0% | -59% |
| Over 60 min | 11 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 29 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 6 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-30 19:36 | Dota 2 Game | Level UP | ✘ | — | — | In play | — |
| 09-30 19:36 | TT Star Series Match | Tormos Kilian | ✘ | — | — | In play | — |
| 09-30 19:34 | TT Elite Series Match | Zbigniew Nocun | ✘ | — | — | In play | — |
| 09-30 19:33 | ITF Men's Match | Ben Weintraub | ✘ | — | — | In play | — |
| 09-30 19:29 | TT Elite Series Match | Rudomina Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:28 | ITF Men's Match | Iiro Vasa | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-30 19:27 | Euroleague Game | ASVEL Lyon-Villeurbanne | ✘ | — | — | In play | — |
| 09-30 19:25 | TT Elite Series Match | Kaczynski Piotr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:22 | TT Elite Series Match | Andriej Fomin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:18 | Men's ODI Cricket Match | South Africa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:17 | TT Elite Series Match | Piotr Strus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:12 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:11 | TT Elite Series Match | Adam Ruszkiewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:11 | TT Star Series Match | Albuquerque Raegan | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:10 | ITF Women's Match | Sol Ailin Larraya Guidi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:10 | League of Legends Game | Gamespace Mediterranean College Esports | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:08 | TT Elite Series Match | Zochniak Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:05 | TT Elite Series Match | Janus Slawomir | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:05 | Counter-Strike 2 Game | Esport BERG | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-30 19:05 | ITF Men's Match | Nicholas Heng | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:05 | EuroCup Basketball Game | Basquet Manresa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 19:00 | Challenger ATP  | Daniel Milavsky | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:52 | TT Elite Series Match | Przemyslaw Blocho | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:51 | KHL Game | Spartak Moscow | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:49 | ITF Men's Match | Jerry Roddick | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:49 | TT Elite Series Match | Sebastian Krupa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:49 | Counter-Strike 2 Game | Semente do Mal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:46 | TT Star Series Match | Mousavi Taher Mohammad | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:45 | TT Elite Series Match | Dawid Kotwica | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-30 18:45 | EuroCup Basketball Game | Slask Wroclaw | ✘ | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
