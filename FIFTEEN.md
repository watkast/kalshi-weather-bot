# 15-Minute 1¢ Study

*Updated Sat Nov 14, 3:06 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4354 finished bets | 1% | $230.25 | +48% | +5.29¢ | $76.00 / $154.25 |

*Expect about **91 buys a day** (~$13.71/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4095 | $129.25 | +29% |
| Volatility model ≥ 2%, hold to the close | 8060 | $78.60 | +8% |
| Momentum model ≥ 2%, hold to the close | 6695 | $13.45 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 57141 | 57120 | 220 (0%) | 1.07% | -$3,880.15 (-56%) | Hold to the close: -$3,880.15 (-56%) |

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
| Volatility model | 34253 | 4.6% | 0.4% (141) | -643% | ❌ Worse |
| Momentum model | 34253 | 4.5% | 0.4% (141) | -669% | ❌ Worse |
| Mean-reversion model | 34253 | 7.9% | 0.4% (141) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 34253 | 141 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8060 | 75 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4354 | 51 | +48% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2506 | 30 | +72% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6695 | 56 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4095 | 41 | +29% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2673 | 26 | +37% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 14073 | 100 | -22% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9806 | 84 | -5% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6530 | 60 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 34459 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13651 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9010 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 57120 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 220 | 0% | -$3,880.15 | -56% | — |
| Sell at 2¢ | 2291 | 4% | -$6,070.49 | -87% | 47 sec |
| Sell at 3¢ | 1549 | 3% | -$6,062.04 | -87% | 48 sec |
| Sell at 5¢ | 1061 | 2% | -$5,948.50 | -85% | 62 sec |
| Sell at 10¢ | 646 | 1% | -$5,707.89 | -82% | 65 sec |
| Sell at 25¢ | 340 | 1% | -$5,302.75 | -76% | 80 sec |
| Sell at 50¢ | 225 | 0% | -$4,783.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2851 | 13 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 18415 | 99 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14417 | 51 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 21424 | 57 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3856 | 18 | 5% | 3% | -39% | -88% | -87% |
| SOL | 3851 | 17 | 4% | 2% | -43% | -86% | -86% |
| HYPE | 3849 | 12 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 3835 | 9 | 4% | 2% | -70% | -90% | -90% |
| BNB | 3833 | 20 | 5% | 2% | -34% | -85% | -85% |
| ETH | 3829 | 16 | 7% | 3% | -48% | -82% | -82% |
| BTC | 3807 | 20 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3805 | 17 | 5% | 2% | -42% | -85% | -86% |
| XRP | 3794 | 14 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 2047 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2031 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1988 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1809 | 4 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 1754 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1699 | 6 | 2% | 1% | -67% | -75% | -75% |
| GBPUSD | 1679 | 6 | 2% | 1% | -67% | -96% | -96% |
| NATGAS | 1674 | 9 | 2% | 1% | -50% | -74% | -74% |
| USDJPY | 1646 | 6 | 2% | 1% | -66% | -97% | -96% |
| PALLADIUM | 1626 | 4 | 1% | 0% | -77% | -92% | -93% |
| AUDUSD | 1199 | 6 | 2% | 1% | -53% | -89% | -89% |
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
| UP (bought YES) | 29070 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 28050 | 110 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5328 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5750 | 22 | 3% | 2% | -41% | -91% | -91% |
| 0.1–0.2% | 8732 | 34 | 5% | 2% | -50% | -89% | -89% |
| 0.2–0.5% | 10534 | 44 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 4106 | 18 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13892 | 44 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13774 | 67 | 4% | 2% | -45% | -85% | -84% |
| Afternoon (12–6pm) | 13890 | 61 | 4% | 2% | -48% | -86% | -87% |
| Evening (6pm–12am) | 15564 | 48 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,956 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/14 2:59:26 PM | NEAR | UP | 33 sec | -0.333% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:59:10 PM | HYPE | UP | 49 sec | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:58:55 PM | XRP | UP | 64 sec | -0.514% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:58:39 PM | ZEC | UP | 80 sec | -0.717% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:57:35 PM | DOGE | UP | 2.4 min | -0.717% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:57:19 PM | BNB | UP | 2.7 min | -0.651% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 2:56:47 PM | SOL | UP | 3.2 min | -0.880% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:56:31 PM | BTC | UP | 3.5 min | -0.592% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:55:20 PM | ETH | UP | 4.7 min | -0.812% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:42:46 PM | SOL | DOWN | 2.2 min | +0.864% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:42:14 PM | XRP | DOWN | 2.8 min | +0.768% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:42:14 PM | BNB | DOWN | 2.8 min | +0.461% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:42:14 PM | BTC | DOWN | 2.8 min | +0.544% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:41:59 PM | NEAR | DOWN | 3.0 min | +1.216% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:41:59 PM | DOGE | DOWN | 3.0 min | +0.929% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:41:59 PM | ZEC | DOWN | 3.0 min | +2.012% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:41:25 PM | ETH | DOWN | 3.6 min | +0.583% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:41:25 PM | HYPE | DOWN | 3.6 min | +1.402% | 1¢ | ❌ Lost | $0.00 |
| 11/14 2:29:52 PM | SOL | DOWN | 7 sec | +0.154% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:29:36 PM | BNB | DOWN | 23 sec | +0.048% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:29:21 PM | HYPE | DOWN | 38 sec | +0.521% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:29:21 PM | DOGE | UP | 38 sec | -0.481% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:29:21 PM | ZEC | DOWN | 38 sec | +1.069% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 2:28:49 PM | XRP | UP | 70 sec | -0.762% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 2:28:00 PM | BTC | DOWN | 2.0 min | +0.495% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:27:44 PM | ETH | DOWN | 2.2 min | +0.801% | 1¢ | ❌ Lost | -$0.15 |
| 11/14 2:27:12 PM | NEAR | DOWN | 2.8 min | +1.216% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:14:10 PM | SOL | UP | 49 sec | -0.529% | 0¢ | ❌ Lost | $0.00 |
| 11/14 2:13:38 PM | XRP | UP | 81 sec | -0.604% | 0¢ | ❌ Lost | -$0.15 |
| 11/14 2:13:38 PM | BNB | UP | 81 sec | -0.609% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
