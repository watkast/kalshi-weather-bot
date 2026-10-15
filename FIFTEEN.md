# 15-Minute 1¢ Study

*Updated Thu Oct 15, 11:12 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1522 finished bets | 1% | $83.55 | +50% | +5.49¢ | $30.10 / $53.45 |

*Expect about **87 buys a day** (~$13.09/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1420 | $56.25 | +37% |
| Momentum model ≥ 2%, hold to the close | 2376 | $5.05 | +2% |
| Volatility model ≥ 2%, hold to the close | 2762 | -$11.60 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19515 | 19500 | 78 (0%) | 1.07% | -$1,275.15 (-54%) | Hold to the close: -$1,275.15 (-54%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12575 | 4.5% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 12575 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 12575 | 7.4% | 0.4% (53) | -758% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12575 | 53 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2762 | 23 | -3% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1522 | 18 | +50% | -73% | -72% | -67% |
| Volatility model ≥ 10% | 898 | 11 | +74% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 2376 | 20 | +2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1420 | 15 | +37% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 952 | 10 | +47% | -71% | -71% | -65% |
| Mean-reversion model ≥ 2% | 4703 | 33 | -23% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3228 | 26 | -11% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2112 | 15 | -18% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12773 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4802 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1925 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19500 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,275.15 | -54% | — |
| Sell at 2¢ | 694 | 4% | -$2,102.71 | -89% | 42 sec |
| Sell at 3¢ | 468 | 2% | -$2,100.63 | -89% | 47 sec |
| Sell at 5¢ | 341 | 2% | -$2,061.50 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$1,976.12 | -83% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,802.71 | -76% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,596.40 | -67% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 628 | 5 | 11% | 3% | -24% | -81% | -86% |
| 2–5 min | 6314 | 36 | 7% | 3% | -44% | -88% | -88% |
| 1–2 min | 5079 | 20 | 3% | 2% | -57% | -92% | -91% |
| Under 1 min | 7475 | 17 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1434 | 11 | 5% | 3% | -4% | -89% | -89% |
| HYPE | 1428 | 5 | 4% | 2% | -57% | -90% | -89% |
| ETH | 1422 | 8 | 5% | 3% | -32% | -88% | -87% |
| DOGE | 1422 | 2 | 4% | 2% | -82% | -91% | -90% |
| BNB | 1422 | 5 | 5% | 2% | -57% | -90% | -89% |
| SOL | 1417 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1411 | 7 | 3% | 1% | -38% | -85% | -86% |
| BTC | 1409 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1408 | 8 | 5% | 3% | -26% | -78% | -78% |
| GOLD | 783 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 761 | 4 | 3% | 1% | -39% | -79% | -78% |
| WTI | 737 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 678 | 2 | 2% | 1% | -72% | -83% | -82% |
| PLATINUM | 645 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 600 | 2 | 1% | 0% | -69% | -82% | -83% |
| NATGAS | 598 | 4 | 3% | 2% | -38% | -96% | -94% |
| EURUSD | 591 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 553 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 513 | 3 | 1% | 1% | -45% | -99% | -98% |
| AUDUSD | 140 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 128 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9853 | 39 | 4% | 2% | -54% | -89% | -88% |
| DOWN (bought NO) | 9647 | 39 | 4% | 2% | -53% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2143 | 11 | 2% | 1% | -14% | -78% | -78% |
| 0.05–0.1% | 2204 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3206 | 10 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 3725 | 21 | 6% | 3% | -38% | -88% | -88% |
| Over 0.5% | 1492 | 6 | 6% | 2% | -58% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4633 | 26 | 4% | 2% | -35% | -86% | -85% |
| Afternoon (12–6pm) | 4482 | 16 | 3% | 1% | -58% | -87% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,477 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 11:12:50 AM | PALLADIUM | DOWN | 2.1 min | — | — | In play | — |
| 10/15 11:12:50 AM | EURUSD | DOWN | 2.1 min | — | — | In play | — |
| 10/15 11:12:19 AM | WTI | UP | 2.7 min | — | — | In play | — |
| 10/15 11:12:03 AM | SOL | DOWN | 2.9 min | +0.248% | — | In play | — |
| 10/15 11:11:47 AM | ETH | DOWN | 3.2 min | +0.260% | — | In play | — |
| 10/15 11:11:31 AM | GBPUSD | DOWN | 3.5 min | — | — | In play | — |
| 10/15 11:09:40 AM | ZEC | DOWN | 5.3 min | +1.345% | — | In play | — |
| 10/15 11:09:25 AM | HYPE | DOWN | 5.6 min | +0.407% | — | In play | — |
| 10/15 10:59:55 AM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:59:55 AM | USDJPY | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:59:39 AM | HYPE | UP | 21 sec | -0.103% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:59:23 AM | DOGE | UP | 37 sec | -0.192% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:59:23 AM | NEAR | UP | 37 sec | -0.301% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:58:52 AM | BTC | DOWN | 68 sec | +0.082% | 1¢ | ❌ Lost | $0.00 |
| 10/15 10:58:52 AM | SOL | DOWN | 68 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:58:52 AM | NATGAS | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:58:36 AM | XRP | DOWN | 84 sec | +0.157% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:58:20 AM | PALLADIUM | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:58:20 AM | AUDUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:48 AM | ETH | DOWN | 2.2 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:32 AM | ZEC | DOWN | 2.5 min | +0.507% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:32 AM | BNB | DOWN | 2.5 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:16 AM | WTI | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:44:45 AM | BTC | UP | 14 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:44:45 AM | USDJPY | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:44:29 AM | GOLD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:44:13 AM | SILVER | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:44:13 AM | COPPER | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:44:13 AM | NATGAS | UP | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:43:57 AM | GBPUSD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
