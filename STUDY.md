# 1¢ Study

*Updated Mon Sep 28, 2:47 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 44 finished bets | 16% | -$4.78 | -72% | -10.86¢ | -$2.26 / -$2.52 |

*Expect **46 buys in the first 22 hours** ($6.90 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 5¢ | 44 | -$5.30 | -80% |
| ESPN-verified leagues only, sell at 3¢ | 44 | -$5.43 | -82% |
| ESPN-verified leagues only, hold to the end | 44 | -$6.60 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 429 | 44 | 0 (0%) | 1.1% | -$6.60 (-100%) | Sell at 2¢: -$4.78 (-72%) |

*In play right now: 10. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 44 | 16% | 7% | 5% | 0% | 0% | 0% |
| Unverified | 375 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$6.60 | -100% |
| Sell at 2¢ | 7 | 16% | -$4.78 | -72% |
| Sell at 3¢ | 3 | 7% | -$5.43 | -82% |
| Sell at 5¢ | 2 | 5% | -$5.30 | -80% |
| Sell at 10¢ | 0 | 0% | -$6.60 | -100% |
| Sell at 25¢ | 0 | 0% | -$6.60 | -100% |
| Sell at 50¢ | 0 | 0% | -$6.60 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 158 | 0 | 1% | 1% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 36 | 0 | 6% | 0% | -100% | -90% | 4 min |
| Counter-Strike 2 Game | ✘ | 31 | 0 | 6% | 3% | -100% | -89% | 13 min |
| ITF Women's Match | ✘ | 22 | 0 | 9% | 9% | -100% | -84% | 4 min |
| ITF Men's Match | ✘ | 21 | 0 | 10% | 5% | -100% | -83% | 4 min |
| TT Star Series Match | ✘ | 19 | 1 | 5% | 5% | +391% | -91% | 6 min |
| League of Legends Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| UEFA Nations League Game | ✔ | 15 | 0 | 13% | 0% | -100% | -77% | 5 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Men's T20 Cricket Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| AFCON Game Winner | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ATP Tennis Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 2 min |
| International Friendly Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 18 min |
| Japan NPB Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 4 min |
| R6 Game | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 13 min |
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
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 17 | 0% | 0% | 0% | -100% |
| 5–15 min | 12 | 25% | 0% | 0% | -57% |
| 15–30 min | 6 | 17% | 17% | 0% | -71% |
| 30–60 min | 4 | 75% | 25% | 0% | +30% |
| Over 60 min | 5 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 27 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 4 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 20:45 | TT Elite Series Match | Tkaczyk Henryk | ✘ | — | — | In play | — |
| 09-28 20:44 | CONCACAF Nations League Game | Guadeloupe | ✔ | 87' · BRB 2 - GDL 1 | — | In play | — |
| 09-28 20:44 | TT Elite Series Match | Jakub Glanowski | ✘ | — | — | In play | — |
| 09-28 20:44 | Counter-Strike 2 Game | DFX Peek | ✘ | — | — | In play | — |
| 09-28 20:43 | TT Elite Series Match | Kowalczyk Marcin | ✘ | — | — | In play | — |
| 09-28 20:42 | UEFA Nations League Game | Tie | ✔ | 90'+3' · FRA 1 - BEL 0 | — | In play | — |
| 09-28 20:41 | R6 Game | Twisted Minds | ✘ | — | — | In play | — |
| 09-28 20:40 | TT Star Series Match | Seibert Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:40 | UEFA Nations League Game | Northern Ireland | ✔ | 90'+4' · HUN 0 - NIR 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:39 | UEFA Nations League Game | Hungary | ✔ | 90'+4' · HUN 0 - NIR 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:39 | TT Elite Series Match | Dawid Dytko | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:39 | Challenger ATP  | Blaise Bicknell | ✘ | — | — | In play | — |
| 09-28 20:38 | Challenger ATP  | Tyler Zink | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:37 | UEFA Nations League Game | Belgium | ✔ | 88' · FRA 0 - BEL 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:30 | UEFA Nations League Game | Tie | ✔ | 85' · POL 1 - SWE 3 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:29 | UEFA Nations League Game | Tie | ✔ | 87' · BIH 4 - ROU 2 | 1¢ | ❌ Lost | -$0.15 |
| 09-28 20:28 | ITF Women's Match | Kelly Keller | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:25 | TT Elite Series Match | Bartosz Kwodawski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:23 | TT Elite Series Match | Zbigniew Nocun | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:20 | TT Star Series Match | Zelinka Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:16 | TT Elite Series Match | Dariusz Maszczynski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:16 | LaLiga 2 Game | Tie | ✔ | 87' · CAS 2 - LEG 0 | 1¢ | ❌ Lost | -$0.15 |
| 09-28 20:16 | AFCON Game Winner | Botswana | ✘ | — | — | In play | — |
| 09-28 20:16 | UEFA Nations League Game | Poland | ✔ | 72' · POL 1 - SWE 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:15 | TT Elite Series Match | Iwasyszyn Wojciech | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:13 | UEFA Nations League Game | Tie | ✔ | 70' · ITA 4 - TUR 1 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:09 | TT Elite Series Match | Oracz Lukasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:08 | ITF Women's Match | Krisha Mahendran | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:04 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 20:03 | TT Star Series Match | Abedinian Milad | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
