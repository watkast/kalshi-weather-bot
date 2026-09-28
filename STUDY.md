# 1¢ Study

*Updated Sun Sep 27, 6:21 PM MT. Paper money: each bet buys 5 contracts at 1¢ (5¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (5 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| all leagues, sell at 5¢ | 37 finished bets | 5% | -$1.76 | -79% | -4.76¢ | -$1.08 / -$0.68 |

*Expect **43 buys in the first 2 hours** ($2.58 risked) — daily pace shows after 24 hours; max loss per buy **6¢**; typical wait to sell **2 min**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| all leagues, sell at 2¢ | 37 | -$1.86 | -84% |
| all leagues, sell at 3¢ | 37 | -$1.96 | -88% |
| all leagues, hold to the end | 37 | -$2.22 | -100% |

</details>

*Re-picked automatically from the latest data every refresh. Rules only use what's knowable at the moment of buying (league, price), not hindsight like how the game ended.*

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 43 | 6 | 0 (0%) | 1.2% | -$0.36 (-100%) | Sell at 2¢: -$0.27 (-75%) |

*In play right now: 6. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 6 | 17% | 0% | 0% | 0% | 0% | 0% |
| Unverified | 31 | 10% | 6% | 6% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 5-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$0.36 | -100% |
| Sell at 2¢ | 1 | 17% | -$0.27 | -75% |
| Sell at 3¢ | 0 | 0% | -$0.36 | -100% |
| Sell at 5¢ | 0 | 0% | -$0.36 | -100% |
| Sell at 10¢ | 0 | 0% | -$0.36 | -100% |
| Sell at 25¢ | 0 | 0% | -$0.36 | -100% |
| Sell at 50¢ | 0 | 0% | -$0.36 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 13 | 0 | 8% | 8% | -100% | -88% | 4 min |
| Professional Football Game | ✔ | 4 | 0 | 25% | 0% | -100% | -62% | 6 min |
| Men's T20 Cricket Match | ✘ | 3 | 0 | 0% | 0% | -100% | -100% | 7 min |
| Women's College Volleyball Match | ✘ | 2 | 0 | 50% | 0% | -100% | -25% | 19 min |
| Liga DIMAYOR Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| NWSL Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Counter-Strike 2 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 23 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 50% | 50% | -100% | -25% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| League of Legends Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 42 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 3 | 0% | 0% | 0% | -100% |
| 5–15 min | 3 | 33% | 0% | 0% | -50% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 38 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 2 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 94 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-28 00:09 | TT Elite Series Match | Jakub Pruszkowski | ✘ | — | — | In play | — |
| 09-28 00:00 | TT Elite Series Match | Linek Adam | ✘ | — | — | In play | — |
| 09-27 23:58 | TT Elite Series Match | Andrzej Krezel | ✘ | — | 5¢ | ❌ Lost | -$0.06 |
| 09-27 23:56 | TT Elite Series Match | Maciej Kolek | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:47 | TT Elite Series Match | Pawel Adamus | ✘ | — | — | In play | — |
| 09-27 23:44 | Professional Football Game | Dallas | ✔ | 0:01 - 4th · BAL 31 - DAL 31 | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:44 | Counter-Strike 2 Game | Galorys | ✘ | — | — | In play | — |
| 09-27 23:43 | Women's College Volleyball Match | Central Florida | ✘ | — | — | In play | — |
| 09-27 23:43 | Men's T20 Cricket Match | Seattle Thunderbolts | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:41 | Professional Football Game | New Orleans | ✔ | 1:02 - 4th · LV 35 - NO 27 | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:36 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:32 | Brasileiro Serie B Game | Athletic Club Sjdr | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:32 | Brasileiro Serie B Game | Fortaleza | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:32 | TT Elite Series Match | Filip Mlynarski | ✘ | — | — | In play | — |
| 09-27 23:30 | TT Elite Series Match | Jakub Glanowski | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:28 | Brasileiro Serie C Game | Brusque | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:26 | Counter-Strike 2 Game | ALKA | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:26 | TT Elite Series Match | Pawel Kurek | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:19 | Brasileiro Serie C Game | Ferroviaria | ✘ | — | 6¢ | ❌ Lost | -$0.06 |
| 09-27 23:17 | League of Legends Game | Cloud9 | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:14 | Professional Football Game | Tampa Bay | ✔ | 1:54 - 4th · MIN 20 - TB 16 | 2¢ | ❌ Lost | -$0.06 |
| 09-27 23:08 | TT Elite Series Match | Artur Kubiak | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:07 | Professional Football Game | Arizona | ✔ | 1:37 - 4th · ARI 27 - SF 29 | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:06 | Counter-Strike 2 Game | Yawara Esports | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:06 | TT Elite Series Match | Michal Olbrycht | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:01 | Argentine Nacional B Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 23:01 | NWSL Game | Tie | ✔ | 90'+6' · ORL 2 - BAY 1 | 0¢ | ❌ Lost | -$0.06 |
| 09-27 22:58 | Uruguay Primera Division Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 22:55 | Liga DIMAYOR Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.06 |
| 09-27 22:53 | TT Elite Series Match | Filip Mlynarski | ✘ | — | 0¢ | ❌ Lost | -$0.06 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
