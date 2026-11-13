# 15-Minute 1¢ Study

*Updated Fri Nov 13, 3:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4274 finished bets | 1% | $169.40 | +36% | +3.96¢ | $81.40 / $88.00 |

*Expect about **93 buys a day** (~$13.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4014 | $96.55 | +22% |
| Volatility model ≥ 2%, hold to the close | 7889 | $30.20 | +3% |
| Momentum model ≥ 2%, hold to the close | 6548 | -$24.70 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55738 | 55711 | 212 (0%) | 1.07% | -$3,830.00 (-56%) | Hold to the close: -$3,830.00 (-56%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 33277 | 4.7% | 0.4% (133) | -670% | ❌ Worse |
| Momentum model | 33277 | 4.6% | 0.4% (133) | -696% | ❌ Worse |
| Mean-reversion model | 33277 | 8.0% | 0.4% (133) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33277 | 133 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7889 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4274 | 46 | +36% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2473 | 28 | +62% | -62% | -61% | -58% |
| Momentum model ≥ 2% | 6548 | 52 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4014 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2632 | 25 | +33% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13705 | 93 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9561 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6374 | 56 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33482 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13431 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8798 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55711 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,830.00 | -56% | — |
| Sell at 2¢ | 2223 | 4% | -$5,926.02 | -87% | 47 sec |
| Sell at 3¢ | 1510 | 3% | -$5,915.10 | -87% | 49 sec |
| Sell at 5¢ | 1038 | 2% | -$5,801.30 | -85% | 63 sec |
| Sell at 10¢ | 630 | 1% | -$5,566.70 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,173.70 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,689.25 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2772 | 13 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 17974 | 97 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 14044 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20908 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3748 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3743 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3738 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3725 | 19 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3724 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3719 | 16 | 7% | 3% | -47% | -82% | -81% |
| BTC | 3701 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3699 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3685 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2018 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 1998 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1958 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1786 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1732 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1674 | 6 | 2% | 1% | -67% | -74% | -74% |
| GBPUSD | 1657 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1648 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1623 | 6 | 2% | 1% | -65% | -96% | -96% |
| PALLADIUM | 1601 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1176 | 6 | 2% | 1% | -52% | -89% | -89% |
| USDCAD | 1141 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 748 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 377 | 2 | 4% | 2% | -50% | -68% | -66% |
| 2YRRATE | 361 | 4 | 4% | 2% | +3% | -42% | -40% |
| 30YRRATE | 358 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 332 | 2 | 4% | 2% | -44% | -93% | -95% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28326 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27385 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5255 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5658 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8555 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10133 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3873 | 18 | 7% | 3% | -52% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13551 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,830 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 3:43:03 AM | PLATINUM | UP | 1.9 min | — | — | In play | — |
| 11/13 3:43:03 AM | USDCAD | DOWN | 1.9 min | — | — | In play | — |
| 11/13 3:42:45 AM | AUDUSD | UP | 2.2 min | — | — | In play | — |
| 11/13 3:42:45 AM | GOLD | UP | 2.2 min | — | — | In play | — |
| 11/13 3:42:13 AM | HYPE | DOWN | 2.8 min | +0.329% | — | In play | — |
| 11/13 3:39:50 AM | XRP | UP | 5.2 min | -0.409% | — | In play | — |
| 11/13 3:29:52 AM | BRENT | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:52 AM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:52 AM | WTI | UP | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:52 AM | USDJPY | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:21 AM | BNB | UP | 39 sec | -0.116% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:21 AM | PLATINUM | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:21 AM | SILVER | UP | 39 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:29:21 AM | DOGE | DOWN | 39 sec | +0.055% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:29:02 AM | ETH | UP | 58 sec | -0.142% | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:28:46 AM | NEAR | UP | 74 sec | -0.312% | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:28:46 AM | ZEC | UP | 74 sec | -0.363% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:28:30 AM | GOLD | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:28:15 AM | PALLADIUM | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:28:15 AM | SOL | DOWN | 1.8 min | +0.208% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:28:15 AM | XRP | DOWN | 1.8 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:28:15 AM | GBPUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:28:15 AM | HYPE | DOWN | 1.8 min | +0.200% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:26:53 AM | BTC | UP | 3.1 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 3:14:45 AM | 5YRRATE | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:14:45 AM | SILVER | UP | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 3:14:29 AM | NATGAS | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:13:58 AM | EURUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:13:58 AM | AUDUSD | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 3:13:42 AM | USDCAD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
