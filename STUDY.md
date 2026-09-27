# 1¢ Study

*Updated Sun Sep 27, 5:52 PM MT. Paper money: each bet buys 100 contracts at 1¢ ($1 + 7¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Headline (verified live bets)

| 1¢ moments (all leagues) | Finished (verified) | Came back & won | Break-even win rate | Hold-to-end P&L | Best exit so far |
|---|---|---|---|---|---|
| 39 | 6 | 0 (0%) | 1.07% | -$6.42 (-100%) | Sell at 10¢: $2.95 (+46%) |

*In play right now: 6. Verified = ESPN confirmed the game was still being played when we bought. Unverified leagues are shown separately below.*

![Bounce curve](study/charts/bounce.png)

## How high did the price bounce?

*Share of bets where someone later bid at least this much before the game ended.*

| Group | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Verified | 6 | 50% | 50% | 17% | 17% | 0% | 0% |
| Unverified | 27 | 33% | 22% | 15% | 0% | 0% | 0% |

## Exit strategies

*Sell the first time the bid reaches the target (after Kalshi's selling fee); if it never does, hold to the end. Based on the best bid each minute, assuming a 100-contract sale would fill.*

| Strategy | Hits | Hit rate | P&L | Return |
|---|---|---|---|---|
| Hold to the end | 0 | 0% | -$6.42 | -100% |
| Sell at 2¢ | 3 | 50% | -$0.84 | -13% |
| Sell at 3¢ | 3 | 50% | $1.95 | +30% |
| Sell at 5¢ | 1 | 17% | -$1.76 | -27% |
| Sell at 10¢ | 1 | 17% | $2.95 | +46% |
| Sell at 25¢ | 0 | 0% | -$6.42 | -100% |
| Sell at 50¢ | 0 | 0% | -$6.42 | -100% |

![Exit strategies](study/charts/exits.png)

## By league

| League | Verified | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ return | Typical time left |
|---|---|---|---|---|---|---|---|---|
| TT Elite Series Match | ✘ | 11 | 0 | 36% | 18% | -100% | -37% | 6 min |
| Professional Football Game | ✔ | 4 | 0 | 75% | 25% | -100% | +30% | 6 min |
| Men's T20 Cricket Match | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 12 min |
| Women's College Volleyball Match | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 19 min |
| Liga DIMAYOR Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Uruguay Primera Division Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Argentine Nacional B Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 8 min |
| NWSL Game | ✔ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |
| Counter-Strike 2 Game | ✘ | 2 | 0 | 50% | 0% | -100% | -13% | 23 min |
| Brasileiro Serie C Game | ✘ | 2 | 0 | 100% | 100% | -100% | +74% | 11 min |
| Brasileiro Serie B Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 5 min |

## By time left when it hit 1¢

| Time left in game | Bets | ≥2¢ | ≥5¢ | Won | Sell@2¢ return |
|---|---|---|---|---|---|
| Under 5 min | 3 | 33% | 33% | 0% | -42% |
| 5–15 min | 3 | 67% | 0% | 0% | +16% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 53 sec later |
| Time from 1¢ to its best bounce (bounced bets) | 0 min |
| Contracts traded at 1¢ after our buy (how much you could buy) | 1 |

![Price paths](study/charts/paths.png)

## Latest bets

*Times are UTC. Peak = best bid after our buy.*

| When | League | Pick | Verified | Situation at 1¢ | Peak | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 09-27 23:47 | TT Elite Series Match | Pawel Adamus | ✘ | — | — | In play | — |
| 09-27 23:44 | Professional Football Game | Dallas | ✔ | 0:01 - 4th · BAL 31 - DAL 31 | 24¢ | ❌ Lost | -$1.07 |
| 09-27 23:44 | Counter-Strike 2 Game | Galorys | ✘ | — | — | In play | — |
| 09-27 23:43 | Women's College Volleyball Match | Central Florida | ✘ | — | — | In play | — |
| 09-27 23:43 | Men's T20 Cricket Match | Seattle Thunderbolts | ✘ | — | — | In play | — |
| 09-27 23:41 | Professional Football Game | New Orleans | ✔ | 1:02 - 4th · LV 35 - NO 27 | 1¢ | ❌ Lost | -$1.07 |
| 09-27 23:36 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | 0¢ | ❌ Lost | -$1.07 |
| 09-27 23:32 | Brasileiro Serie B Game | Athletic Club Sjdr | ✘ | — | 0¢ | ❌ Lost | -$1.07 |
| 09-27 23:32 | Brasileiro Serie B Game | Fortaleza | ✘ | — | 0¢ | ❌ Lost | -$1.07 |
| 09-27 23:32 | TT Elite Series Match | Filip Mlynarski | ✘ | — | — | In play | — |
| 09-27 23:30 | TT Elite Series Match | Jakub Glanowski | ✘ | — | 2¢ | ❌ Lost | -$1.07 |
| 09-27 23:28 | Brasileiro Serie C Game | Brusque | ✘ | — | 6¢ | ❌ Lost | -$1.07 |
| 09-27 23:26 | Counter-Strike 2 Game | ALKA | ✘ | — | 1¢ | ❌ Lost | -$1.07 |
| 09-27 23:26 | TT Elite Series Match | Pawel Kurek | ✘ | — | 0¢ | ❌ Lost | -$1.07 |
| 09-27 23:19 | Brasileiro Serie C Game | Ferroviaria | ✘ | — | 6¢ | ❌ Lost | -$1.07 |
| 09-27 23:17 | League of Legends Game | Cloud9 | ✘ | — | — | In play | — |
| 09-27 23:14 | Professional Football Game | Tampa Bay | ✔ | 1:54 - 4th · MIN 20 - TB 16 | 3¢ | ❌ Lost | -$1.07 |
| 09-27 23:08 | TT Elite Series Match | Artur Kubiak | ✘ | — | 1¢ | ❌ Lost | -$1.07 |
| 09-27 23:07 | Professional Football Game | Arizona | ✔ | 1:37 - 4th · ARI 27 - SF 29 | 4¢ | ❌ Lost | -$1.07 |
| 09-27 23:06 | Counter-Strike 2 Game | Yawara Esports | ✘ | — | 3¢ | ❌ Lost | -$1.07 |
| 09-27 23:06 | TT Elite Series Match | Michal Olbrycht | ✘ | — | 2¢ | ❌ Lost | -$1.07 |
| 09-27 23:01 | Argentine Nacional B Game | Tie | ✘ | — | 3¢ | ❌ Lost | -$1.07 |
| 09-27 23:01 | NWSL Game | Tie | ✔ | 90'+6' · ORL 2 - BAY 1 | 1¢ | ❌ Lost | -$1.07 |
| 09-27 22:58 | Uruguay Primera Division Game | Tie | ✘ | — | 0¢ | ❌ Lost | -$1.07 |
| 09-27 22:55 | Liga DIMAYOR Game | Tie | ✘ | — | 1¢ | ❌ Lost | -$1.07 |
| 09-27 22:53 | TT Elite Series Match | Filip Mlynarski | ✘ | — | 1¢ | ❌ Lost | -$1.07 |
| 09-27 22:53 | NWSL Game | Bay FC | ✔ | 88' · ORL 2 - BAY 1 | 0¢ | ❌ Lost | -$1.07 |
| 09-27 22:51 | Argentine Nacional B Game | Rafaela | ✘ | — | 0¢ | ❌ Lost | -$1.07 |
| 09-27 22:50 | TT Elite Series Match | Andrzej Szurgot | ✘ | — | 1¢ | ❌ Lost | -$1.07 |
| 09-27 22:48 | Uruguay Primera Division Game | Danubio | ✘ | — | 0¢ | ❌ Lost | -$1.07 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
