# 1¢ Study

*Updated Sun Sep 27, 8:53 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 77 finished bets | 4% | -$9.60 | -83% | -12.47¢ | -$5.05 / -$4.55 |

*Expect **83 buys in the first 4 hours** ($12.45 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 77 | -$10.25 | -89% |
| all leagues, sell at 3¢ | 77 | -$10.38 | -90% |
| all leagues, hold to the end | 77 | -$11.55 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 83 | 17 | 0 (0%) | 1.1% | -$2.55 (-100%) | Sell at 5¢: -$1.90 (-75%) |

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
| Verified | 17 | 12% | 6% | 6% | 0% | 0% | 0% |
| Unverified | 60 | 5% | 3% | 3% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$2.55 | -100% |
| Sell at 2¢ | 2 | 12% | -$2.03 | -80% |
| Sell at 3¢ | 1 | 6% | -$2.16 | -85% |
| Sell at 5¢ | 1 | 6% | -$1.90 | -75% |
| Sell at 10¢ | 0 | 0% | -$2.55 | -100% |
| Sell at 25¢ | 0 | 0% | -$2.55 | -100% |
| Sell at 50¢ | 0 | 0% | -$2.55 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 35 | 0 | 3% | 3% | -100% | -95% | 6 min |
| CONCACAF Nations League Game | ✔ | 6 | 0 | 0% | 0% | -100% | -100% | 48 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Liga DIMAYOR Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Counter-Strike 2 Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 27 min |
| Professional Football Game | ✔ | 4 | 0 | 25% | 0% | -100% | -57% | 6 min |
| Men's T20 Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| League of Legends Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 42 min |
| LNBP Basketball Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 29 min |
| Women's Pro Basketball Game | ✔ | 1 | 0 | 100% | 100% | -100% | +73% | 30 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 6 | 0% | 0% | 0% | -100% |
| 5–15 min | 5 | 20% | 0% | 0% | -65% |
| 15–30 min | 2 | 0% | 0% | 0% | -100% |
| 30–60 min | 1 | 100% | 100% | 0% | +73% |
| Over 60 min | 3 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 42 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 2 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 35 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 02:48 | TT Elite Series Match | Tkaczyk Henryk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:47 | Liga MX Game | Juarez | ✔ | 83' · JUA 0 - LEO 1 | — | In play | — |
| 09-28 02:45 | CONCACAF Nations League Game | Trinidad and Tobago | ✔ | 87' · DOM 2 - TRI 1 | — | In play | — |
| 09-28 02:40 | Counter-Strike 2 Game | regain | ✘ | — | — | In play | — |
| 09-28 02:31 | Liga DIMAYOR Game | Aguilas Doradas Rionegro | ✘ | — | — | In play | — |
| 09-28 02:31 | TT Elite Series Match | Wojciech Urban | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:27 | TT Elite Series Match | Artur Kubiak | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:14 | TT Elite Series Match | Vincenec Oliver | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:08 | Women's Pro Basketball Game | Dallas | ✔ | Halftime · DAL 31 - GS 58 | — | In play | — |
| 09-28 01:59 | TT Elite Series Match | Andrzej Szurgot | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:58 | Women's College Volleyball Match | Stanford | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:45 | LNBP Basketball Game | Lobos de Puebla | ✘ | — | — | In play | — |
| 09-28 01:41 | TT Elite Series Match | Tkaczyk Henryk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:33 | CONCACAF Nations League Game | Tie | ✔ | 76' · PUR 2 - DMA 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:28 | TT Elite Series Match | Adam Ruszkiewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:21 | TT Elite Series Match | Mariusz Baron | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:19 | Major League Soccer Game | Tie | ✔ | 90'+10' · MIA 1 - CLB 2 | 1¢ | ❌ Lost | -$0.15 |
| 09-28 01:16 | Major League Soccer Game | Miami | ✔ | 90'+7' · MIA 1 - CLB 1 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:09 | TT Elite Series Match | Andrzej Szurgot | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:05 | NWSL Game | Tie | ✔ | 90'+6' · NC 1 - UTA 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:03 | Liga DIMAYOR Game | Tolima | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:01 | TT Elite Series Match | Rafal Ogon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 01:00 | TT Elite Series Match | Vincenec Oliver | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:56 | NWSL Game | North Carolina Courage | ✔ | 87' · NC 1 - UTA 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:51 | TT Elite Series Match | Lukasz Pietraszko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:49 | Liga DIMAYOR Game | Fortaleza | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:47 | Women's Pro Basketball Game | Washington | ✔ | 7:56 - 4th · WSH 57 - ATL 74 | 8¢ | ❌ Lost | -$0.15 |
| 09-28 00:44 | CONCACAF Nations League Game | Tie | ✔ | 86' · CRC 0 - HAI 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:44 | TT Elite Series Match | Dawid Kotwica | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 00:39 | TT Elite Series Match | Wojciech Urban | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
