# 1¢ Study

*Updated Mon Sep 28, 12:46 PM MT. Paper money: each bet buys 14 contracts at 1¢ (14¢ + 1¢ fee). Prices come from Kalshi's own trade records and minute-by-minute bid/ask.*

[← Back to all bots](README.md)

## Current strategy

🔴 **Sit out.** No rule has made money yet, so if we turned it on now it would not buy anything.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| ESPN-verified leagues only, sell at 2¢ | 33 finished bets | 15% | -$3.65 | -74% | -11.06¢ | -$1.88 / -$1.77 |

*Expect **33 buys in the first 20 hours** ($4.95 risked) — daily pace shows after 24 hours; max loss per buy **15¢**; typical wait to sell **3 min**.*

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
| 362 | 33 | 0 (0%) | 1.1% | -$4.95 (-100%) | Sell at 2¢: -$3.65 (-74%) |

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
| Verified | 33 | 15% | 9% | 6% | 0% | 0% | 0% |
| Unverified | 319 | 4% | 3% | 2% | 1% | 0% | 0% |

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
| TT Elite Series Match | ✘ | 137 | 0 | 1% | 1% | -100% | -99% | 5 min |
| Challenger ATP  | ✘ | 32 | 0 | 6% | 0% | -100% | -89% | 4 min |
| Counter-Strike 2 Game | ✘ | 26 | 0 | 8% | 4% | -100% | -87% | 13 min |
| ITF Men's Match | ✘ | 19 | 0 | 11% | 5% | -100% | -82% | 4 min |
| ITF Women's Match | ✘ | 18 | 0 | 6% | 6% | -100% | -90% | 4 min |
| League of Legends Game | ✘ | 12 | 0 | 8% | 8% | -100% | -86% | 12 min |
| TT Star Series Match | ✘ | 12 | 0 | 0% | 0% | -100% | -100% | 6 min |
| CONCACAF Nations League Game | ✔ | 8 | 0 | 12% | 0% | -100% | -78% | 21 min |
| Men's T20 Cricket Match | ✘ | 7 | 0 | 0% | 0% | -100% | -100% | 8 min |
| Liga DIMAYOR Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 12 min |
| AFCON Game Winner | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 15 min |
| Liga Leumit Game | ✘ | 6 | 0 | 0% | 0% | -100% | -100% | 10 min |
| UEFA Nations League Game | ✔ | 6 | 0 | 17% | 0% | -100% | -71% | 1 min |
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
| KHL Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| Slovakian 2. Liga Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 2 min |
| R6 Game | ✘ | 2 | 0 | 0% | 0% | -100% | -100% | 14 min |
| ELH Game | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | -1 min |
| Valorant game winner | ✘ | 1 | 0 | 0% | 0% | -100% | -100% | 2 min |

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
| 09-28 18:44 | KHL Game | HC Sochi | ✘ | — | — | In play | — |
| 09-28 18:44 | TT Elite Series Match | Miroslaw Lewczuk | ✘ | — | — | In play | — |
| 09-28 18:43 | TT Elite Series Match | Rudomina Kamil | ✘ | — | — | In play | — |
| 09-28 18:41 | League of Legends Game | White Dragons | ✘ | — | — | In play | — |
| 09-28 18:39 | TT Elite Series Match | Mrugala Bartlomiej | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:38 | Liga Leumit Game | Tie | ✘ | — | — | In play | — |
| 09-28 18:38 | Counter-Strike 2 Game | MASQ | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:38 | TT Elite Series Match | Mariusz Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:37 | TT Elite Series Match | Dariusz Maszczynski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:35 | Counter-Strike 2 Game | megoshort | ✘ | — | — | In play | — |
| 09-28 18:34 | League of Legends Game | Valerion | ✘ | — | — | In play | — |
| 09-28 18:33 | KHL Game | Torpedo Nizhny Novgorod | ✘ | — | — | In play | — |
| 09-28 18:32 | Liga Leumit Game | Maccabi Bney Reine | ✘ | — | — | In play | — |
| 09-28 18:31 | TT Elite Series Match | Arkadiusz Skupinski | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:30 | League of Legends Game | NightBirds | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:30 | TT Elite Series Match | Piotr Strus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:21 | R6 Game | Team Secret | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:16 | KHL Game | Lada Togliatti | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:15 | TT Elite Series Match | Gesiarz Piotr | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:11 | Counter-Strike 2 Game | EAC Extra | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:10 | TT Star Series Match | Zelinka Jakub | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:05 | TT Elite Series Match | Kacper Adamus | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:02 | League of Legends Game | MAGAZA | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 18:00 | TT Elite Series Match | Andrzej Krezel | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:58 | Challenger ATP  | Tiago Torres | ✘ | — | 1¢ | ❌ Lost | -$0.15 |
| 09-28 17:57 | TT Elite Series Match | Rudomina Kamil | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:55 | AFCON Game Winner | Tie | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:55 | UEFA Nations League Game | Georgia | ✔ | 90'+3' · UKR 0 - GEO 0 | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:55 | ITF Women's Match | Julie Myatovic | ✘ | — | 0¢ | ❌ Lost | -$0.15 |
| 09-28 17:54 | UEFA Nations League Game | Ukraine | ✔ | 90'+3' · UKR 0 - GEO 0 | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [study/bets.csv](study/bets.csv) — one row per bet with every metric
- `study/ticks/` — every Kalshi trade from the first 1¢ trade to the end, per bet
- `study/candles/` — minute-by-minute bid / ask / volume, per bet
