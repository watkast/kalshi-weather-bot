# 1¢ Study

*Updated Mon Sep 28, 6:17 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 2¢ | 174 finished bets | 6% | -$23.50 | -90% | -13.51¢ | -$11.23 / -$12.27 |

*Expect **180 buys in the first 14 hours** ($27.00 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 5¢ | 174 | -$23.50 | -90% |
| all leagues, sell at 3¢ | 174 | -$24.15 | -93% |
| all leagues, hold to the end | 174 | -$26.10 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 180 | 23 | 0 (0%) | 1.1% | -$3.45 (-100%) | Sell at 5¢: -$2.15 (-62%) |

*In play right now: 6. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 0 | — | — | — | — |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

*Model scores appear once bets with model readings settle.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 23 | 17% | 9% | 9% | 0% | 0% | 0% |
| Unverified | 151 | 4% | 2% | 1% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$3.45 | -100% |
| Sell at 2¢ | 4 | 17% | -$2.41 | -70% |
| Sell at 3¢ | 2 | 9% | -$2.67 | -77% |
| Sell at 5¢ | 2 | 9% | -$2.15 | -62% |
| Sell at 10¢ | 0 | 0% | -$3.45 | -100% |
| Sell at 25¢ | 0 | 0% | -$3.45 | -100% |
| Sell at 50¢ | 0 | 0% | -$3.45 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 70 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 6 min |
| ITF Men's Match | ✘ | 13 | 0 | 8% | 0% | -100% | -87% | 4 min |
| Counter-Strike 2 Game | ✘ | 11 | 0 | 0% | 0% | -100% | -100% | 14 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's T20 Cricket Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ITF Women's Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 3 min |
| ATP Tennis Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 3 min |
| TT Star Series Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| League of Legends Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| WTA Tennis Match | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 18 min |
| Dota 2 Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 30 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 9 | 0% | 0% | 0% | -100% |
| 5–15 min | 6 | 33% | 0% | 0% | -42% |
| 15–30 min | 3 | 33% | 33% | 0% | -42% |
| 30–60 min | 2 | 50% | 50% | 0% | -13% |
| Over 60 min | 3 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 2 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 12:16 | ITF Men's Match | Iulius Maximus Stoica | ✘ | — | — | In play | — |
| 09-28 12:15 | TT Elite Series Match | Pawel Slosarczyk | ✘ | — | — | In play | — |
| 09-28 12:13 | ITF Men's Match | Aleksander Chayka | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:11 | TT Star Series Match | Buben Vlastimil | ✘ | — | — | In play | — |
| 09-28 12:08 | Challenger ATP  | Alejo Sanchez Quilez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:05 | ITF Men's Match | Francesco Ferrari | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-28 12:02 | ITF Women's Match | Kaat Coppez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:02 | TT Elite Series Match | Kaczmarek Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:01 | TT Elite Series Match | Artur Sobel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:01 | ITF Men's Match | Denis Klok | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:00 | ITF Women's Match | Saumya Vig | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:00 | Challenger ATP  | Ryan Peniston | ✘ | — | 3¢ | ❌ Lost | -$0.15 |
| 09-28 11:59 | TT Elite Series Match | Piotr Chodorski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:58 | League of Legends Game | KT Rolster Challengers | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:56 | ITF Men's Match | Rafael Behr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:56 | ITF Men's Match | Arian Barbic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:56 | Challenger WTA | Noma Noha Akugue | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 11:51 | TT Star Series Match | Vráblík Jiří | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:47 | Challenger ATP  | Christian Langmo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:46 | TT Elite Series Match | Piotr Przewlocki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:45 | International Friendly Game | Korea Republic | ✔ | 44' · URU 2 - KOR 0 | — | In play | — |
| 09-28 11:42 | TT Elite Series Match | Wojciech Tobiasz | ✘ | — | — | In play | — |
| 09-28 11:41 | TT Elite Series Match | Michal Minda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:37 | Japan NPB Game | Chiba Lotte Marines | ✘ | — | — | In play | — |
| 09-28 11:34 | ITF Men's Match | Ethan Terblanche | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:29 | TT Elite Series Match | Tibor Spanik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:28 | ITF Men's Match | Maximilian Todorov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:28 | ITF Men's Match | Trishan Dhawan | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 11:22 | TT Elite Series Match | Fomin Yurij | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 11:22 | Challenger ATP  | Svyatoslav Gulin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
