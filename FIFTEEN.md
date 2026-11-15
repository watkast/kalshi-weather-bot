# 15-Minute 1¢ Study

*Updated Sun Nov 15, 3:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4405 finished bets | 1% | $225.30 | +46% | +5.11¢ | $87.15 / $138.15 |

*Expect about **91 buys a day** (~$13.58/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4153 | $123.85 | +28% |
| Volatility model ≥ 2%, hold to the close | 8191 | $91.30 | +9% |
| Momentum model ≥ 2%, hold to the close | 6808 | $15.30 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57860 | 57839 | 226 (0%) | 1.07% | -$3,867.85 (-55%) | Hold to the close: -$3,867.85 (-55%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 34969 | 4.6% | 0.4% (147) | -630% | ❌ Worse |
| Momentum model | 34969 | 4.5% | 0.4% (147) | -656% | ❌ Worse |
| Mean-reversion model | 34969 | 7.9% | 0.4% (147) | -766% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34969 | 147 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8191 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4405 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2529 | 30 | +71% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6808 | 57 | +2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4153 | 41 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2702 | 26 | +36% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14336 | 102 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9980 | 85 | -6% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6625 | 61 | +5% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35175 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9013 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57839 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 226 | 0% | -$3,867.85 | -55% | — |
| Sell at 2¢ | 2330 | 4% | -$6,132.05 | -87% | 47 sec |
| Sell at 3¢ | 1573 | 3% | -$6,124.38 | -87% | 48 sec |
| Sell at 5¢ | 1080 | 2% | -$6,007.85 | -85% | 62 sec |
| Sell at 10¢ | 659 | 1% | -$5,762.56 | -82% | 65 sec |
| Sell at 25¢ | 347 | 1% | -$5,351.28 | -76% | 80 sec |
| Sell at 50¢ | 232 | 0% | -$4,807.85 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2894 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18685 | 103 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14590 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21657 | 59 | 1% | 0% | -61% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3937 | 19 | 5% | 2% | -37% | -88% | -87% |
| SOL | 3932 | 17 | 4% | 2% | -45% | -86% | -86% |
| HYPE | 3927 | 12 | 4% | 2% | -61% | -89% | -88% |
| DOGE | 3916 | 11 | 4% | 2% | -64% | -90% | -89% |
| BNB | 3912 | 20 | 5% | 2% | -35% | -86% | -85% |
| ETH | 3906 | 17 | 7% | 3% | -46% | -82% | -82% |
| BTC | 3886 | 21 | 5% | 2% | -27% | -86% | -88% |
| NEAR | 3885 | 17 | 5% | 2% | -43% | -85% | -86% |
| XRP | 3874 | 15 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1755 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1647 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1200 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1162 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 777 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 401 | 2 | 4% | 1% | -53% | -70% | -68% |
| 2YRRATE | 384 | 4 | 4% | 2% | -3% | -45% | -43% |
| 30YRRATE | 376 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 355 | 2 | 4% | 2% | -47% | -93% | -95% |
| INX | 54 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29435 | 113 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28404 | 113 | 4% | 2% | -54% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5373 | 25 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 5809 | 24 | 3% | 2% | -36% | -91% | -91% |
| 0.1–0.2% | 8855 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 10800 | 47 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4329 | 19 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14049 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13903 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14115 | 63 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 15772 | 49 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,099 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/15 3:29:59 PM | AUDUSD | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:29:43 PM | HYPE | DOWN | 16 sec | +0.042% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:29:27 PM | ZEC | UP | 32 sec | -0.111% | 0¢ | ❌ Lost | $0.00 |
| 11/15 3:29:27 PM | BTC | DOWN | 32 sec | +0.036% | 0¢ | ❌ Lost | $0.00 |
| 11/15 3:28:55 PM | SOL | DOWN | 64 sec | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:28:23 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:28:07 PM | BNB | DOWN | 1.9 min | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:27:51 PM | NEAR | DOWN | 2.1 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:27:51 PM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:27:35 PM | ETH | DOWN | 2.4 min | +0.285% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:26:50 PM | XRP | DOWN | 3.1 min | +0.393% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:26:26 PM | DOGE | DOWN | 3.5 min | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:13:17 PM | HYPE | DOWN | 1.7 min | +0.099% | 1¢ | ❌ Lost | $0.00 |
| 11/15 3:12:55 PM | XRP | DOWN | 2.1 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:39 PM | ZEC | DOWN | 2.4 min | +0.355% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:39 PM | ETH | DOWN | 2.4 min | +0.245% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:39 PM | BTC | DOWN | 2.4 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:39 PM | DOGE | DOWN | 2.4 min | +0.231% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:39 PM | BNB | DOWN | 2.4 min | +0.187% | 0¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:23 PM | NEAR | DOWN | 2.6 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 3:12:23 PM | SOL | DOWN | 2.6 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:59:46 PM | BTC | DOWN | 13 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:59:30 PM | DOGE | DOWN | 29 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:59:30 PM | SOL | DOWN | 29 sec | +0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:59:02 PM | NEAR | UP | 57 sec | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:58:00 PM | ETH | DOWN | 2.0 min | +0.195% | 3¢ | ❌ Lost | -$0.15 |
| 11/15 2:56:48 PM | ZEC | DOWN | 3.2 min | +0.561% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:44:46 PM | BTC | DOWN | 14 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/15 2:44:30 PM | ETH | DOWN | 30 sec | +0.062% | 1¢ | ❌ Lost | -$0.15 |
| 11/15 2:43:59 PM | ZEC | DOWN | 61 sec | +0.175% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
