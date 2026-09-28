# 1¢ Study

*Updated Mon Sep 28, 4:33 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 47 finished bets | 19% | -$4.71 | -67% | -10.02¢ | -$2.41 / -$2.30 |

*Expect **49 buys in the first 24 hours** ($7.35 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **3 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 5¢ | 47 | -$5.10 | -72% |
| ESPN-verified leagues only, sell at 3¢ | 47 | -$5.49 | -78% |
| ESPN-verified leagues only, sell at 10¢ | 47 | -$5.74 | -81% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 462 | 47 | 0 (0%) | 1.1% | -$7.05 (-100%) | Sell at 2¢: -$4.71 (-67%) |

*In play right now: 5. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 47 | 19% | 9% | 6% | 2% | 0% | 0% |
| Unverified | 410 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$7.05 | -100% |
| Sell at 2¢ | 9 | 19% | -$4.71 | -67% |
| Sell at 3¢ | 4 | 9% | -$5.49 | -78% |
| Sell at 5¢ | 3 | 6% | -$5.10 | -72% |
| Sell at 10¢ | 1 | 2% | -$5.74 | -81% |
| Sell at 25¢ | 0 | 0% | -$7.05 | -100% |
| Sell at 50¢ | 0 | 0% | -$7.05 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 178 | 0 | 1% | 1% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 37 | 0 | 5% | 0% | -100% | -91% | 4 min |
| Counter-Strike 2 Game | ✘ | 33 | 0 | 6% | 3% | -100% | -89% | 12 min |
| ITF Women's Match | ✘ | 25 | 0 | 8% | 8% | -100% | -86% | 4 min |
| TT Star Series Match | ✘ | 21 | 1 | 5% | 5% | +344% | -92% | 5 min |
| ITF Men's Match | ✘ | 21 | 0 | 10% | 5% | -100% | -83% | 4 min |
| League of Legends Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| UEFA Nations League Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 3 min |
| CONCACAF Nations League Game | ✔ | 10 | 0 | 30% | 10% | -100% | -48% | 14 min |
| Men's T20 Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| AFCON Game Winner | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 25 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| R6 Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ATP Tennis Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
| International Friendly Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Japan NPB Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| WTA Tennis Match | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 18 min |
| Dota 2 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 22 min |
| Valorant game winner | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| LaLiga 2 Game | ✔ | 2 | 0 | 50% | 0% | -100% | -13% | 26 min |
| APF Division de Honor Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 3 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 19 | 5% | 0% | 0% | -91% |
| 5–15 min | 13 | 31% | 8% | 0% | -47% |
| 15–30 min | 6 | 17% | 17% | 0% | -71% |
| 30–60 min | 4 | 75% | 25% | 0% | +30% |
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
| 09-28 22:31 | TT Elite Series Match | Rudomina Kamil | ✘ | — | — | In play | — |
| 09-28 22:28 | TT Elite Series Match | Kowalczyk Marcin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:25 | League of Legends Game | Golden Lions | ✘ | — | — | In play | — |
| 09-28 22:23 | TT Elite Series Match | Michał Machelski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:14 | TT Elite Series Match | Mrugala Bartlomiej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:07 | CONCACAF Nations League Game | Tie | ✔ | 50' · BOE 0 - CUB 1 | — | In play | — |
| 09-28 22:07 | TT Star Series Match | Zelinka Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:06 | ITF Women's Match | Martina Okalova | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:06 | CONCACAF Nations League Game | Bonaire | ✔ | 49' · BOE 0 - CUB 1 | — | In play | — |
| 09-28 22:06 | TT Elite Series Match | Oliwier Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:02 | TT Elite Series Match | Andrzej Krezel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 22:02 | TT Elite Series Match | Jakub Cyndera | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:58 | APF Division de Honor Game | San Lorenzo | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:57 | APF Division de Honor Game | CD Recoleta | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:56 | ITF Women's Match | Allura Zamarripa | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:49 | TT Elite Series Match | Mariusz Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:46 | TT Elite Series Match | Michal Skorski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:44 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:41 | TT Elite Series Match | Jakub Glanowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:37 | R6 Game | Fnatic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:35 | Counter-Strike 2 Game | BESTIA Academy | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:25 | TT Elite Series Match | Iwasyszyn Wojciech | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:16 | TT Elite Series Match | Dawid Dytko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:13 | TT Elite Series Match | Aleksander Barton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:11 | TT Elite Series Match | Gesiarz Piotr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:10 | TT Elite Series Match | Bartosz Kwodawski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:07 | TT Star Series Match | Tormos Kilian | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:07 | TT Elite Series Match | Adam Staniczek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:03 | AFCON Game Winner | Tunisia | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 21:01 | ITF Women's Match | Ana Grubor | ✘ | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
