# 1¢ Study

*Updated Mon Sep 28, 9:41 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 56 finished bets | 4% | -$5.78 | -69% | -10.32¢ | -$4.20 / -$1.58 |

*Expect about **48 buys a day**, roughly **$7.25/day** at risk; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 56 | -$5.80 | -69% |
| ESPN-verified leagues only, sell at 5¢ | 56 | -$5.80 | -69% |
| ESPN-verified leagues only, sell at 3¢ | 56 | -$6.45 | -77% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 545 | 56 | 0 (0%) | 1.1% | -$8.40 (-100%) | Sell at 10¢: -$5.78 (-69%) |

*In play right now: 7. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **ESPN win probability:** ESPN's live in-game win-probability model (NFL, NBA, WNBA, college football & basketball)

*Readings start with the next watch session (about 10:30 PM MT, Sep 27). Leagues ESPN doesn't model show no reading.*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| ESPN win probability | 1 | 0.9% | 0.0% (0) | +13% | ✅ Better |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 1 | 0 | -100% | -100% | -100% | -100% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 56 | 18% | 9% | 7% | 4% | 0% | 0% |
| Unverified | 482 | 4% | 2% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$8.40 | -100% |
| Sell at 2¢ | 10 | 18% | -$5.80 | -69% |
| Sell at 3¢ | 5 | 9% | -$6.45 | -77% |
| Sell at 5¢ | 4 | 7% | -$5.80 | -69% |
| Sell at 10¢ | 2 | 4% | -$5.78 | -69% |
| Sell at 25¢ | 0 | 0% | -$8.40 | -100% |
| Sell at 50¢ | 0 | 0% | -$8.40 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 223 | 0 | 0% | 0% | -100% | -99% | 5 min |
| Counter-Strike 2 Game | ✘ | 37 | 0 | 5% | 3% | -100% | -91% | 13 min |
| Challenger ATP  | ✘ | 37 | 0 | 5% | 0% | -100% | -91% | 4 min |
| ITF Women's Match | ✘ | 34 | 0 | 9% | 6% | -100% | -85% | 4 min |
| League of Legends Game | ✘ | 23 | 0 | 13% | 4% | -100% | -77% | 10 min |
| TT Star Series Match | ✘ | 21 | 1 | 5% | 5% | +344% | -92% | 5 min |
| ITF Men's Match | ✘ | 21 | 0 | 10% | 5% | -100% | -83% | 4 min |
| CONCACAF Nations League Game | partly | 20 | 0 | 20% | 10% | -100% | -65% | 21 min |
| UEFA Nations League Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 3 min |
| Men's T20 Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| AFCON Game Winner | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 25 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 6 min |
| ATP Tennis Match | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| R6 Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie B Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| International Friendly Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 18 min |
| APF Division de Honor Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Japan NPB Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| WTA Tennis Match | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 18 min |
| Dota 2 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Valorant game winner | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 20 | 5% | 0% | 0% | -91% |
| 5–15 min | 14 | 29% | 7% | 0% | -50% |
| 15–30 min | 9 | 22% | 22% | 0% | -61% |
| 30–60 min | 8 | 38% | 12% | 0% | -35% |
| Over 60 min | 5 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 4 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-29 03:40 | TT Elite Series Match | Karol Wisniewski | ✘ | — | — | In play | — |
| 09-29 03:35 | TT Elite Series Match | Schaniel Krzysztof | ✘ | — | — | In play | — |
| 09-29 03:32 | TT Elite Series Match | Kaczmarek Jakub | ✘ | — | — | In play | — |
| 09-29 03:29 | League of Legends Game | United Arab Emirates | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:28 | ITF Women's Match | Chloe Schwarz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:28 | ITF Women's Match | Caitlin Baker | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:21 | TT Elite Series Match | Felkel Grzegorz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:20 | TT Elite Series Match | Blazej Warpas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:19 | Women's ODI Cricket Match | Queensland Fire | ✘ | — | — | In play | — |
| 09-29 03:18 | TT Elite Series Match | Krzysztof Wloczko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:17 | TT Elite Series Match | Oracz Lukasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:14 | CONCACAF Nations League Game | Tie | ✔ | 56' · SLV 0 - GUA 3 | — | In play | — |
| 09-29 03:14 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:14 | ATP Tennis Match | Rinky Hijikata | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 03:09 | League of Legends Game | Malaysia | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 03:04 | TT Elite Series Match | Jerzy Michalik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 02:50 | Professional Football Game | Philadelphia | ✔ | 8:09 - 4th · PHI 7 - CHI 20 | 1¢ | ❌ Lost | -$0.15 |
| 09-29 02:34 | CONCACAF Nations League Game | El Salvador | ✔ | 34' · SLV 0 - GUA 3 | — | In play | — |
| 09-29 02:33 | TT Elite Series Match | Jacek Zelezik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 02:26 | Counter-Strike 2 Game | regain | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 02:22 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 02:12 | TT Elite Series Match | Artur Kubiak | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 02:05 | TT Elite Series Match | Dawid Dytko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 02:02 | TT Elite Series Match | Aleksander Barton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:54 | CONCACAF Nations League Game | Tie | ✔ | 90'+6' · HON 1 - JAM 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:48 | CONCACAF Nations League Game | Jamaica | ✔ | 89' · HON 1 - JAM 0 | 1¢ | ❌ Lost | -$0.15 |
| 09-29 01:48 | League of Legends Game | Malaysia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:41 | TT Elite Series Match | Oracz Lukasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:35 | CONCACAF Nations League Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:30 | TT Elite Series Match | Kacper Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
