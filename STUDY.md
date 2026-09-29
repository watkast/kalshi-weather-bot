# 1¢ Study

*Updated Mon Sep 28, 7:14 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 10¢ | 51 finished bets | 4% | -$5.03 | -66% | -9.86¢ | -$3.75 / -$1.28 |

*Expect about **47 buys a day**, roughly **$7.10/day** at risk; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 51 | -$5.05 | -66% |
| ESPN-verified leagues only, sell at 5¢ | 51 | -$5.05 | -66% |
| ESPN-verified leagues only, sell at 3¢ | 51 | -$5.70 | -75% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 509 | 51 | 0 (0%) | 1.1% | -$7.65 (-100%) | Sell at 10¢: -$5.03 (-66%) |

*In play right now: 3. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 51 | 20% | 10% | 8% | 4% | 0% | 0% |
| Unverified | 455 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$7.65 | -100% |
| Sell at 2¢ | 10 | 20% | -$5.05 | -66% |
| Sell at 3¢ | 5 | 10% | -$5.70 | -75% |
| Sell at 5¢ | 4 | 8% | -$5.05 | -66% |
| Sell at 10¢ | 2 | 4% | -$5.03 | -66% |
| Sell at 25¢ | 0 | 0% | -$7.65 | -100% |
| Sell at 50¢ | 0 | 0% | -$7.65 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 207 | 0 | 0% | 0% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 37 | 0 | 5% | 0% | -100% | -91% | 4 min |
| Counter-Strike 2 Game | ✘ | 36 | 0 | 6% | 3% | -100% | -90% | 12 min |
| ITF Women's Match | ✘ | 31 | 0 | 10% | 6% | -100% | -83% | 4 min |
| TT Star Series Match | ✘ | 21 | 1 | 5% | 5% | +344% | -92% | 5 min |
| ITF Men's Match | ✘ | 21 | 0 | 10% | 5% | -100% | -83% | 4 min |
| League of Legends Game | ✘ | 19 | 0 | 16% | 5% | -100% | -73% | 11 min |
| UEFA Nations League Game | ✔ | 16 | 0 | 12% | 0% | -100% | -78% | 3 min |
| CONCACAF Nations League Game | ✔ | 14 | 0 | 29% | 14% | -100% | -50% | 21 min |
| Men's T20 Cricket Match | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 11 min |
| AFCON Game Winner | ✘ | 8 | 0 | 12% | 12% | -100% | -78% | 25 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| R6 Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| Uruguay Primera Division Game | ✘ | 4 | 0 | 25% | 25% | -100% | -57% | 15 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Brasileiro Serie B Game | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ATP Tennis Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
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
| Under 5 min | 19 | 5% | 0% | 0% | -91% |
| 5–15 min | 13 | 31% | 8% | 0% | -47% |
| 15–30 min | 8 | 25% | 25% | 0% | -57% |
| 30–60 min | 6 | 50% | 17% | 0% | -13% |
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
| 09-29 01:12 | CONCACAF Nations League Game | Bermuda | ✔ | 54' · BER 1 - LCA 3 | — | In play | — |
| 09-29 01:11 | TT Elite Series Match | Kacper Kwiatkowski | ✘ | — | — | In play | — |
| 09-29 01:09 | ITF Women's Match | Dalayna Hewitt | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:05 | TT Elite Series Match | Michał Machelski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 01:04 | TT Elite Series Match | Oliwier Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:50 | ITF Women's Match | Valeriya Strakhova | ✘ | — | 2¢ | ❌ Lost | -$0.15 |
| 09-29 00:49 | TT Elite Series Match | Mrugala Bartlomiej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:48 | TT Elite Series Match | Aleksander Barton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:45 | TT Elite Series Match | Mariusz Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:43 | TT Elite Series Match | Artur Kubiak | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:39 | Uruguay Primera Division Game | Tie | ✘ | — | 17¢ | ❌ Lost | -$0.15 |
| 09-29 00:29 | TT Elite Series Match | Bartosz Kwodawski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:27 | Brasileiro Serie B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:24 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:24 | TT Elite Series Match | Iwasyszyn Wojciech | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:18 | Uruguay Primera Division Game | Albion | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:18 | Brasileiro Serie B Game | America FC | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-29 00:13 | TT Elite Series Match | Kacper Kwiatkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:12 | APF Division de Honor Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:12 | TT Elite Series Match | Michał Machelski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:11 | TT Elite Series Match | Kacper Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:08 | ITF Women's Match | Sofia Elena Cabezas Dominguez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-29 00:02 | TT Elite Series Match | Mrugala Bartlomiej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 23:58 | APF Division de Honor Game | Libertad | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 23:56 | Counter-Strike 2 Game | MIBR fe | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 23:50 | TT Elite Series Match | Aleksander Barton | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 23:42 | TT Elite Series Match | Jacek Mitas | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 23:40 | TT Elite Series Match | Mariusz Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 23:37 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 23:34 | CONCACAF Nations League Game | Tie | ✔ | 77' · MTQ 0 - SUR 2 | 14¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
