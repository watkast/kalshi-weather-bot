# 1¢ Study

*Updated Sun Sep 27, 7:14 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 51 finished bets | 4% | -$6.35 | -83% | -12.45¢ | -$3.10 / -$3.25 |

*Expect **65 buys in the first 3 hours** ($9.75 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 51 | -$6.61 | -86% |
| all leagues, sell at 3¢ | 51 | -$6.87 | -90% |
| all leagues, hold to the end | 51 | -$7.65 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 65 | 8 | 0 (0%) | 1.1% | -$1.20 (-100%) | Sell at 2¢: -$0.94 (-78%) |

*In play right now: 14. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 8 | 12% | 0% | 0% | 0% | 0% | 0% |
| Unverified | 43 | 7% | 5% | 5% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$1.20 | -100% |
| Sell at 2¢ | 1 | 12% | -$0.94 | -78% |
| Sell at 3¢ | 0 | 0% | -$1.20 | -100% |
| Sell at 5¢ | 0 | 0% | -$1.20 | -100% |
| Sell at 10¢ | 0 | 0% | -$1.20 | -100% |
| Sell at 25¢ | 0 | 0% | -$1.20 | -100% |
| Sell at 50¢ | 0 | 0% | -$1.20 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 22 | 0 | 5% | 5% | -100% | -92% | 5 min |
| Counter-Strike 2 Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Professional Football Game | ✔ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Men's T20 Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's College Volleyball Match | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 19 min |
| Liga DIMAYOR Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| NWSL Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| CONCACAF Nations League Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 16 min |
| League of Legends Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 42 min |
| LNBP Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 29 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 3 | 0% | 0% | 0% | -100% |
| 5–15 min | 4 | 25% | 0% | 0% | -57% |
| 15–30 min | 1 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 33 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 2 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 35 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 01:09 | TT Elite Series Match | Andrzej Szurgot | ✘ | — | — | In play | — |
| 09-28 01:05 | NWSL Game | Tie | ✔ | 90'+6' · NC 1 - UTA 2 | — | In play | — |
| 09-28 01:03 | Liga DIMAYOR Game | Tolima | ✘ | — | — | In play | — |
| 09-28 01:01 | TT Elite Series Match | Rafal Ogon | ✘ | — | — | In play | — |
| 09-28 01:00 | TT Elite Series Match | Vincenec Oliver | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:56 | NWSL Game | North Carolina Courage | ✔ | 87' · NC 1 - UTA 2 | — | In play | — |
| 09-28 00:51 | TT Elite Series Match | Lukasz Pietraszko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:49 | Liga DIMAYOR Game | Fortaleza | ✘ | — | — | In play | — |
| 09-28 00:47 | Women's Pro Basketball Game | Washington | ✔ | 7:56 - 4th · WSH 57 - ATL 74 | — | In play | — |
| 09-28 00:44 | CONCACAF Nations League Game | Tie | ✔ | 86' · CRC 0 - HAI 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:44 | TT Elite Series Match | Dawid Kotwica | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:39 | TT Elite Series Match | Wojciech Urban | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:38 | CONCACAF Nations League Game | Dominica | ✔ | 38' · PUR 1 - DMA 0 | — | In play | — |
| 09-28 00:31 | CONCACAF Nations League Game | Costa Rica | ✔ | 72' · CRC 0 - HAI 2 | 1¢ | ❌ Lost | -$0.15 |
| 09-28 00:30 | TT Elite Series Match | Michal Olbrycht | ✘ | — | — | In play | — |
| 09-28 00:27 | CONCACAF Nations League Game | Tie | ✔ | 27' · NCA 0 - CUW 1 | — | In play | — |
| 09-28 00:25 | TT Elite Series Match | Jakub Glanowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:22 | TT Elite Series Match | Andrzej Szurgot | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:20 | CONCACAF Nations League Game | Nicaragua | ✔ | 20' · NCA 0 - CUW 1 | — | In play | — |
| 09-28 00:19 | Counter-Strike 2 Game | Wildcard | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:13 | LNBP Basketball Game | Diablos Rojos Del Mexico | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:10 | TT Elite Series Match | Adam Ruszkiewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:09 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:00 | TT Elite Series Match | Linek Adam | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-27 23:58 | TT Elite Series Match | Andrzej Krezel | ✘ | — | 5¢ | ❌ Lost | -$0.15 |
| 09-27 23:56 | TT Elite Series Match | Maciej Kolek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-27 23:47 | TT Elite Series Match | Pawel Adamus | ✘ | — | — | In play | — |
| 09-27 23:44 | Professional Football Game | Dallas | ✔ | 0:01 - 4th · BAL 31 - DAL 31 | 0¢ | ❌ Lost | -$0.15 |
| 09-27 23:44 | Counter-Strike 2 Game | Galorys | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-27 23:43 | Women's College Volleyball Match | Central Florida | ✘ | — | — | In play | — |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
