# 1¢ Study

*Updated Mon Sep 28, 10:14 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 265 finished bets | 2% | -$35.85 | -90% | -13.53¢ | -$17.20 / -$18.65 |

*Expect **270 buys in the first 18 hours** ($40.50 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **7 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 265 | -$36.37 | -91% |
| all leagues, sell at 3¢ | 265 | -$36.63 | -92% |
| all leagues, sell at 10¢ | 265 | -$38.44 | -97% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 270 | 27 | 0 (0%) | 1.1% | -$4.05 (-100%) | Sell at 5¢: -$2.75 (-68%) |

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
| Verified | 27 | 15% | 7% | 7% | 0% | 0% | 0% |
| Unverified | 238 | 4% | 3% | 2% | 0% | 0% | 0% |

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
| TT Elite Series Match | ✘ | 105 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 27 | 0 | 7% | 0% | -100% | -87% | 4 min |
| Counter-Strike 2 Game | ✘ | 19 | 0 | 0% | 0% | -100% | -100% | 13 min |
| ITF Men's Match | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 4 min |
| ITF Women's Match | ✘ | 15 | 0 | 7% | 7% | -100% | -88% | 5 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| TT Star Series Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Men's T20 Cricket Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
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
| KHL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |

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
| Our buy vs Kalshi's first 1¢ trade | 30 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 4 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 16:10 | TT Star Series Match | Zelinka Jakub | ✘ | — | — | In play | — |
| 09-28 16:10 | Challenger ATP  | Jack Pinnington Jones | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:10 | TT Elite Series Match | Piotr Strus | ✘ | — | — | In play | — |
| 09-28 16:10 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | — | In play | — |
| 09-28 15:53 | Counter-Strike 2 Game | BIG Academy | ✘ | — | — | In play | — |
| 09-28 15:49 | Challenger ATP  | Michael Mmoh | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:45 | KHL Game | HK Avangard Omsk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:44 | TT Elite Series Match | Kacper Kwiatkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:39 | Challenger ATP  | Bruno Fernandez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:37 | ITF Women's Match | Valentina Khrebtova | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:37 | Counter-Strike 2 Game | The Huns Esports | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:35 | TT Elite Series Match | Jakub Glanowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:30 | TT Star Series Match | Beneš Michal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:27 | TT Elite Series Match | Mateusz Trela | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:24 | TT Elite Series Match | Artur Kubiak | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:23 | TT Elite Series Match | Wichowski Grzegorz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:18 | TT Elite Series Match | Bartosz Kwodawski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:18 | Challenger ATP  | Shunsuke Mitsui | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:10 | ITF Women's Match | Savine ERLER | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:07 | Counter-Strike 2 Game | Leo Team | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:04 | TT Elite Series Match | Artur Sobel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 15:00 | TT Elite Series Match | Kaczmarek Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:53 | TT Star Series Match | Abedinian Milad | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:50 | TT Elite Series Match | Piotr Chodorski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:50 | ITF Men's Match | Aleksandre Shvangiradze | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 14:46 | Challenger ATP  | Wilson Leite | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:45 | TT Elite Series Match | Michal Minda | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:45 | Challenger ATP  | Mika Petkovic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:38 | TT Elite Series Match | Waldemar Jozala | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 14:38 | Challenger ATP  | Mathys Erhard | ✘ | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
