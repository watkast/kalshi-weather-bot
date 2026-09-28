# 1¢ Study

*Updated Sun Sep 27, 10:18 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 105 finished bets | 4% | -$13.15 | -83% | -12.52¢ | -$6.50 / -$6.65 |

*Expect **110 buys in the first 6 hours** ($16.50 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **6 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 105 | -$13.93 | -88% |
| all leagues, sell at 3¢ | 105 | -$14.19 | -90% |
| all leagues, hold to the end | 105 | -$15.75 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price, model reading), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 110 | 23 | 0 (0%) | 1.1% | -$3.45 (-100%) | Sell at 5¢: -$2.15 (-62%) |

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
| Verified | 23 | 17% | 9% | 9% | 0% | 0% | 0% |
| Unverified | 82 | 4% | 2% | 2% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 14-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$3.45 | -100% |
| Sell at 2¢ | 4 | 17% | -$2.41 | -70% |
| Sell at 3¢ | 2 | 9% | -$2.67 | -77% |
| Sell at 5¢ | 2 | 9% | -$2.15 | -62% |
| Sell at 10¢ | 0 | 0% | -$3.45 | -100% |
| Sell at 25¢ | 0 | 0% | -$3.45 | -100% |
| Sell at 50¢ | 0 | 0% | -$3.45 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 47 | 0 | 2% | 2% | -100% | -96% | 6 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Counter-Strike 2 Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 20 min |
| Professional Football Game | ✔ | 5 | 0 | 20% | 0% | -100% | -65% | 2 min |
| Women's College Volleyball Match | ✘ | 4 | 0 | 25% | 0% | -100% | -57% | 26 min |
| NWSL Game | ✔ | 4 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Men's T20 Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -13% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| LNBP Basketball Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 82 min |
| Women's Pro Basketball Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 44 min |
| Major League Soccer Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| Liga MX Game | ✔ | 2 | 0 | 50% | 50% | -100% | -13% | 9 min |
| Challenger ATP  | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| ATP Tennis Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 13 min |
| League of Legends Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 42 min |
| Challenger WTA | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 4 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 9 | 0% | 0% | 0% | -100% |
| 5–15 min | 6 | 33% | 0% | 0% | -42% |
| 15–30 min | 3 | 33% | 33% | 0% | -42% |
| 30–60 min | 2 | 50% | 50% | 0% | -13% |
| Over 60 min | 3 | 0% | 0% | 0% | -100% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 40 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 2 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 94 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 04:16 | WTA Tennis Match | Mina Hodzic | ✘ | — | — | In play | — |
| 09-28 04:13 | WTA Tennis Match | Tiphanie Lemaitre | ✘ | — | — | In play | — |
| 09-28 04:10 | TT Elite Series Match | Mariusz Baron | ✘ | — | — | In play | — |
| 09-28 04:09 | Challenger ATP  | Jilong Huang | ✘ | — | — | In play | — |
| 09-28 04:06 | Challenger WTA | Mei Yamaguchi | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 04:02 | TT Elite Series Match | Miroslav Sklensky | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:54 | Professional Football Game | Los Angeles R | ✔ | 0:02 - 4th · LAR 26 - DEN 30 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:47 | TT Elite Series Match | Janus Slawomir | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:43 | TT Elite Series Match | Pawel Kurek | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:41 | TT Elite Series Match | Mateusz Trela | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:39 | TT Elite Series Match | Jakub Kosowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:38 | TT Elite Series Match | Krzysztof Kapik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:37 | Challenger ATP  | Chuan Ding | ✘ | — | — | In play | — |
| 09-28 03:35 | TT Elite Series Match | Piotr Przewlocki | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:33 | Challenger ATP  | Naoya Honda | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 03:20 | TT Elite Series Match | Grzegorz Poliniewicz | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:17 | ATP Tennis Match | Yoshihito Nishioka | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 03:17 | TT Elite Series Match | Vincenec Oliver | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:15 | TT Elite Series Match | Igor Szymanski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:14 | TT Elite Series Match | Tibor Spanik | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:12 | ATP Tennis Match | Camilo Ugo Carabelli | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:08 | Challenger ATP  | Chase Ferguson | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:05 | Liga MX Game | Tie | ✔ | 90'+11' · JUA 1 - LEO 2 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 03:04 | Counter-Strike 2 Game | FarmVille | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:59 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:55 | Liga DIMAYOR Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:53 | CONCACAF Nations League Game | Tie | ✔ | 90'+5' · DOM 2 - TRI 1 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:48 | TT Elite Series Match | Tkaczyk Henryk | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 02:47 | Liga MX Game | Juarez | ✔ | 83' · JUA 0 - LEO 1 | 7¢ | ❌ Lost | -$0.15 |
| 09-28 02:45 | CONCACAF Nations League Game | Trinidad and Tobago | ✔ | 87' · DOM 2 - TRI 1 | 2¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
