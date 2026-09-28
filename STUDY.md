# 1¢ Study

*Updated Mon Sep 28, 7:07 AM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 197 finished bets | 3% | -$25.65 | -87% | -13.02¢ | -$12.10 / -$13.55 |

*Expect **204 buys in the first 15 hours** ($30.60 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **7 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 197 | -$26.43 | -89% |
| all leagues, sell at 3¢ | 197 | -$26.82 | -91% |
| all leagues, sell at 10¢ | 197 | -$28.24 | -96% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 204 | 25 | 0 (0%) | 1.1% | -$3.75 (-100%) | Sell at 5¢: -$2.45 (-65%) |

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
| Verified | 25 | 16% | 8% | 8% | 0% | 0% | 0% |
| Unverified | 172 | 5% | 3% | 2% | 1% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$3.75 | -100% |
| Sell at 2¢ | 4 | 16% | -$2.71 | -72% |
| Sell at 3¢ | 2 | 8% | -$2.97 | -79% |
| Sell at 5¢ | 2 | 8% | -$2.45 | -65% |
| Sell at 10¢ | 0 | 0% | -$3.75 | -100% |
| Sell at 25¢ | 0 | 0% | -$3.75 | -100% |
| Sell at 50¢ | 0 | 0% | -$3.75 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 79 | 0 | 1% | 1% | -100% | -98% | 5 min |
| Challenger ATP  | ✘ | 15 | 0 | 7% | 0% | -100% | -88% | 4 min |
| ITF Men's Match | ✘ | 14 | 0 | 14% | 7% | -100% | -75% | 4 min |
| Counter-Strike 2 Game | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 15 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| ITF Women's Match | ✘ | 7 | 0 | 14% | 14% | -100% | -75% | 3 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Challenger WTA | ✘ | 5 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's T20 Cricket Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 10 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| TT Star Series Match | ✘ | 4 | 0 | 0% | 0% | -100% | -100% | 8 min |
| ATP Tennis Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 3 min |
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
| International Friendly Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 4 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 10 | 0% | 0% | 0% | -100% |
| 5–15 min | 7 | 29% | 0% | 0% | -50% |
| 15–30 min | 3 | 33% | 33% | 0% | -42% |
| 30–60 min | 2 | 50% | 50% | 0% | -13% |
| Over 60 min | 3 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 28 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 3 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 0 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 13:06 | Challenger ATP  | Matteo Sciahbasi | ✘ | — | — | In play | — |
| 09-28 13:05 | ITF Women's Match | Lilian Poling | ✘ | — | — | In play | — |
| 09-28 13:03 | TT Elite Series Match | Krystian Kolodziej | ✘ | — | — | In play | — |
| 09-28 13:01 | Counter-Strike 2 Game | OldMix | ✘ | — | — | In play | — |
| 09-28 12:57 | TT Elite Series Match | Oskar Jadach | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:55 | TT Elite Series Match | Bartosz Czerwinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:54 | TT Elite Series Match | Waldemar Jozala | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:53 | TT Elite Series Match | Felkel Grzegorz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:46 | Challenger ATP  | Lui Maxted | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:45 | Japan NPB Game | Saitama Seibu Lions | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:44 | Counter-Strike 2 Game | magic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:42 | ITF Women's Match | Carolina Gomez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:40 | TT Elite Series Match | Krzysztof Kapik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:39 | Japan NPB Game | Yokohama DeNA BayStars | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:39 | TT Elite Series Match | Maciej Kolek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:38 | ITF Women's Match | Victoria Gomez O'Hayon | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:35 | Dota 2 Game | IaChIo123 | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:33 | Challenger ATP  | Manas Dhamne | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:30 | TT Elite Series Match | Buczynski Witold | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:29 | TT Elite Series Match | Fomin Yurij | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:28 | ITF Women's Match | Vanja Gudelj | ✘ | — | 11¢ | ❌ Lost | -$0.15 |
| 09-28 12:27 | International Friendly Game | Tie | ✔ | 64' · URU 4 - KOR 0 | — | In play | — |
| 09-28 12:24 | International Friendly Game | Tie | ✔ | 90'+9' · VEN 1 - JPN 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:20 | International Friendly Game | Venezuela | ✔ | 90'+4' · VEN 1 - JPN 1 | 1¢ | ❌ Lost | -$0.15 |
| 09-28 12:16 | ITF Men's Match | Iulius Maximus Stoica | ✘ | — | 9¢ | ❌ Lost | -$0.15 |
| 09-28 12:15 | TT Elite Series Match | Pawel Slosarczyk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:13 | ITF Men's Match | Aleksander Chayka | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:11 | TT Star Series Match | Buben Vlastimil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:08 | Challenger ATP  | Alejo Sanchez Quilez | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 12:05 | ITF Men's Match | Francesco Ferrari | ✘ | — | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
