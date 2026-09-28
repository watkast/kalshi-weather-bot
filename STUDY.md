# 1¢ Study

*Updated Mon Sep 28, 8:19 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 224 finished bets | 3% | -$29.70 | -88% | -13.26¢ | -$14.20 / -$15.50 |

*Expect **230 buys in the first 16 hours** ($34.50 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **7 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 224 | -$30.22 | -90% |
| all leagues, sell at 3¢ | 224 | -$30.48 | -91% |
| all leagues, sell at 10¢ | 224 | -$32.29 | -96% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 230 | 27 | 0 (0%) | 1.1% | -$4.05 (-100%) | Sell at 5¢: -$2.75 (-68%) |

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
| Verified | 27 | 15% | 7% | 7% | 0% | 0% | 0% |
| Unverified | 197 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$4.05 | -100% |
| Sell at 2¢ | 4 | 15% | -$3.01 | -74% |
| Sell at 3¢ | 2 | 7% | -$3.27 | -81% |
| Sell at 5¢ | 2 | 7% | -$2.75 | -68% |
| Sell at 10¢ | 0 | 0% | -$4.05 | -100% |
| Sell at 25¢ | 0 | 0% | -$4.05 | -100% |
| Sell at 50¢ | 0 | 0% | -$4.05 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 89 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 17 | 0 | 12% | 0% | -100% | -80% | 5 min |
| ITF Men's Match | ✘ | 16 | 0 | 12% | 6% | -100% | -78% | 4 min |
| Counter-Strike 2 Game | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 14 min |
| ITF Women's Match | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 5 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Men's T20 Cricket Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| TT Star Series Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ATP Tennis Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
| International Friendly Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Japan NPB Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
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
| Dota 2 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 22 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 10 | 0% | 0% | 0% | -100% |
| 5–15 min | 7 | 29% | 0% | 0% | -50% |
| 15–30 min | 4 | 25% | 25% | 0% | -57% |
| 30–60 min | 2 | 50% | 50% | 0% | -13% |
| Over 60 min | 4 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 29 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 4 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 14:17 | ITF Men's Match | Anup Bangargi | ✘ | — | — | In play | — |
| 09-28 14:16 | TT Elite Series Match | Wojciech Tobiasz | ✘ | — | — | In play | — |
| 09-28 14:13 | TT Elite Series Match | Krzysztof Kapik | ✘ | — | — | In play | — |
| 09-28 14:08 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:07 | TT Elite Series Match | Zochniak Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:05 | Counter-Strike 2 Game | Nexus | ✘ | — | — | In play | — |
| 09-28 13:58 | ITF Women's Match | Freya Peet | ✘ | — | — | In play | — |
| 09-28 13:54 | ITF Men's Match | Timofei Derepasko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:53 | ITF Women's Match | Tinatini Mtvarelishvili | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:53 | Counter-Strike 2 Game | FOKUS | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:51 | TT Elite Series Match | Szostok Sebastian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:48 | TT Elite Series Match | Pawel Slosarczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:47 | TT Elite Series Match | Michal Minda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:45 | TT Star Series Match | Saha Sourav | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:41 | ITF Women's Match | Elizabeth Jurna | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 13:38 | TT Elite Series Match | Jakub Kosowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:33 | ITF Men's Match | Zura Tkemaladze | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:31 | ITF Women's Match | Severine Deppner | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:27 | Men's T20 Cricket Match | Rishikesh Falcons | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:27 | TT Elite Series Match | Maciej Kolek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:25 | TT Elite Series Match | Wojciech Tobiasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:24 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:23 | ATP Tennis Match | Roman Safiullin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:20 | Counter-Strike 2 Game | Black Phoenix | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:13 | ITF Women's Match | Lea Fojcik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:10 | Challenger ATP  | Benjamin Bonzi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:06 | Challenger ATP  | Matteo Sciahbasi | ✘ | — | 3¢ | ❌ Lost | -$0.15 |
| 09-28 13:05 | ITF Women's Match | Lilian Poling | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:03 | TT Elite Series Match | Krystian Kolodziej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 13:01 | Counter-Strike 2 Game | OldMix | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
