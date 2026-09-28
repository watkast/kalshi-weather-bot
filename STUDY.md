# 1¢ Study

*Updated Mon Sep 28, 1:47 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 33 finished bets | 15% | -$3.65 | -74% | -11.06¢ | -$1.88 / -$1.77 |

*Expect **35 buys in the first 21 hours** ($5.25 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **3 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| ESPN-verified leagues only, sell at 5¢ | 33 | -$3.65 | -74% |
| ESPN-verified leagues only, sell at 3¢ | 33 | -$3.78 | -76% |
| ESPN-verified leagues only, hold to the end | 33 | -$4.95 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 394 | 33 | 0 (0%) | 1.1% | -$4.95 (-100%) | Sell at 2¢: -$3.65 (-74%) |

*In play right now: 7. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

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
| Verified | 33 | 15% | 9% | 6% | 0% | 0% | 0% |
| Unverified | 354 | 4% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$4.95 | -100% |
| Sell at 2¢ | 5 | 15% | -$3.65 | -74% |
| Sell at 3¢ | 3 | 9% | -$3.78 | -76% |
| Sell at 5¢ | 2 | 6% | -$3.65 | -74% |
| Sell at 10¢ | 0 | 0% | -$4.95 | -100% |
| Sell at 25¢ | 0 | 0% | -$4.95 | -100% |
| Sell at 50¢ | 0 | 0% | -$4.95 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 148 | 0 | 1% | 1% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 35 | 0 | 6% | 0% | -100% | -90% | 4 min |
| Counter-Strike 2 Game | ✘ | 29 | 0 | 7% | 3% | -100% | -88% | 13 min |
| ITF Men's Match | ✘ | 20 | 0 | 10% | 5% | -100% | -83% | 4 min |
| ITF Women's Match | ✘ | 20 | 0 | 10% | 10% | -100% | -83% | 4 min |
| League of Legends Game | ✘ | 18 | 0 | 11% | 6% | -100% | -81% | 10 min |
| TT Star Series Match | ✘ | 15 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Liga Leumit Game | ✘ | 8 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Men's T20 Cricket Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| AFCON Game Winner | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| UEFA Nations League Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 1 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| KHL Game | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 6 min |
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
| R6 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 15 | 0% | 0% | 0% | -100% |
| 5–15 min | 8 | 38% | 0% | 0% | -35% |
| 15–30 min | 4 | 25% | 25% | 0% | -57% |
| 30–60 min | 2 | 50% | 50% | 0% | -13% |
| Over 60 min | 4 | 0% | 0% | 0% | -100% |

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
| 09-28 19:46 | LaLiga 2 Game | Leganes | ✔ | 57' · CAS 2 - LEG 0 | — | In play | — |
| 09-28 19:43 | TT Elite Series Match | Dawid Dytko | ✘ | — | — | In play | — |
| 09-28 19:42 | ITF Men's Match | Yeray Andres Pastor | ✘ | — | — | In play | — |
| 09-28 19:40 | TT Elite Series Match | Mateusz Trela | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:37 | R6 Game | Virtus.pro | ✘ | — | — | In play | — |
| 09-28 19:37 | TT Elite Series Match | Bartosz Kwodawski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:36 | TT Elite Series Match | Zbigniew Nocun | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:35 | TT Star Series Match | Seibert Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:35 | TT Elite Series Match | Kowalczyk Marcin | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:35 | TT Star Series Match | Gavlas Antonín | ✘ | — | — | In play | — |
| 09-28 19:31 | League of Legends Game | The Secret Club Esport | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:28 | Counter-Strike 2 Game | MASQ | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:27 | TT Elite Series Match | Oliwier Sokolowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:24 | TT Elite Series Match | Dariusz Maszczynski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:21 | League of Legends Game | Forsaken | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:21 | League of Legends Game | Bushido Wildcats | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:19 | ITF Women's Match | Anna Burchak | ✘ | — | 9¢ | ❌ Lost | -$0.15 |
| 09-28 19:19 | Challenger ATP  | Alafia Ayeni | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 19:18 | Counter-Strike 2 Game | struggletony | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:13 | ITF Women's Match | Charlotte Maurey | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:13 | UEFA Nations League Game | Turkiye | ✔ | 27' · ITA 2 - TUR 0 | — | In play | — |
| 09-28 19:12 | TT Star Series Match | Beneš Michal | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:10 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:08 | Challenger ATP  | Pierre-Hugues Herbert | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:07 | TT Elite Series Match | Mateusz Trela | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 19:07 | ITF Men's Match | Mario Martinez Serrano | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:58 | Valorant game winner | Trigon Titans | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:58 | League of Legends Game | HMBLE | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:57 | TT Elite Series Match | Oracz Lukasz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:50 | Challenger ATP  | Quinn Vandecasteele | ✘ | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
