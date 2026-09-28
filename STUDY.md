# 1¢ Study

*Updated Mon Sep 28, 11:15 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 297 finished bets | 2% | -$40.00 | -90% | -13.47¢ | -$19.60 / -$20.40 |

*Expect **301 buys in the first 19 hours** ($45.15 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **4 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 297 | -$40.65 | -91% |
| all leagues, sell at 3¢ | 297 | -$41.04 | -92% |
| all leagues, sell at 25¢ | 297 | -$41.24 | -93% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 301 | 27 | 0 (0%) | 1.1% | -$4.05 (-100%) | Sell at 5¢: -$2.75 (-68%) |

*In play right now: 4. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Unverified | 270 | 4% | 3% | 2% | 1% | 0% | 0% |

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
| TT Elite Series Match | ✘ | 119 | 0 | 1% | 1% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 30 | 0 | 7% | 0% | -100% | -88% | 4 min |
| Counter-Strike 2 Game | ✘ | 22 | 0 | 5% | 0% | -100% | -92% | 13 min |
| ITF Men's Match | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 4 min |
| ITF Women's Match | ✘ | 17 | 0 | 6% | 6% | -100% | -90% | 5 min |
| TT Star Series Match | ✘ | 10 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Men's T20 Cricket Match | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| League of Legends Game | ✘ | 6 | 0 | 17% | 17% | -100% | -71% | 12 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
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
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| KHL Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 5 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |
| Valorant game winner | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 2 min |

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
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 4 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 17:13 | TT Elite Series Match | Andrzej Krezel | ✘ | — | — | In play | — |
| 09-28 17:09 | TT Elite Series Match | Mrugala Bartlomiej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:09 | Counter-Strike 2 Game | struggletony | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:09 | AFCON Game Winner | Zimbabwe | ✘ | — | — | In play | — |
| 09-28 17:05 | TT Elite Series Match | Dariusz Maszczynski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:04 | Challenger ATP  | Dan Added | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:01 | Counter-Strike 2 Game | Zetta Games | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:59 | TT Elite Series Match | Zbigniew Nocun | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:57 | ITF Women's Match | Chrystal Lopez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:57 | TT Elite Series Match | Iwasyszyn Wojciech | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:54 | TT Star Series Match | Seibert Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:52 | Challenger ATP  | James Kent Trotter | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:50 | TT Elite Series Match | Wojciech Tobiasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:49 | Slovakian 2. Liga Game | FK Humenne | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:49 | Slovakian 2. Liga Game | Zilina B | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:49 | ITF Women's Match | Olivia Gram | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:42 | League of Legends Game | UCAM Esports Club | ✘ | — | 49¢ | ❌ Lost | -$0.15 |
| 09-28 16:40 | League of Legends Game | eSuba | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:38 | TT Elite Series Match | Jakub Cyndera | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:37 | Valorant game winner | Fear Never Ends | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:37 | League of Legends Game | Skillcamp Esport | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:37 | Challenger ATP  | Alex Rybakov | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:34 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:30 | TT Elite Series Match | Fomin Yurij | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:27 | League of Legends Game | Frites Esports Club | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:26 | Men's T20 Cricket Match | USN Indians | ✘ | — | — | In play | — |
| 09-28 16:26 | TT Elite Series Match | Michal Skorski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:21 | TT Elite Series Match | Staszczyk Konrad | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:21 | ELH Game | HC Sparta Praha | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 16:21 | TT Elite Series Match | Dariusz Maszczynski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
