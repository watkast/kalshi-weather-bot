# 15-Minute 1¢ Study

*Updated Tue Nov 17, 1:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4467 finished bets | 1% | $220.35 | +45% | +4.93¢ | $83.85 / $136.50 |

*Expect about **89 buys a day** (~$13.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4208 | $119.80 | +26% |
| Volatility model ≥ 2%, hold to the close | 8317 | $77.80 | +8% |
| Momentum model ≥ 2%, hold to the close | 6904 | $6.15 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59470 | 59436 | 227 (0%) | 1.07% | -$4,052.15 (-56%) | Hold to the close: -$4,052.15 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35729 | 4.5% | 0.4% (148) | -637% | ❌ Worse |
| Momentum model | 35729 | 4.5% | 0.4% (148) | -663% | ❌ Worse |
| Mean-reversion model | 35729 | 7.9% | 0.4% (148) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35729 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8317 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4467 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2568 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6904 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4208 | 41 | +26% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 2740 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14643 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10193 | 85 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6772 | 61 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35935 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14112 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9389 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59436 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,052.15 | -56% | — |
| Sell at 2¢ | 2388 | 4% | -$6,315.27 | -87% | 47 sec |
| Sell at 3¢ | 1609 | 3% | -$6,308.64 | -87% | 48 sec |
| Sell at 5¢ | 1101 | 2% | -$6,192.50 | -86% | 62 sec |
| Sell at 10¢ | 670 | 1% | -$5,946.45 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,523.10 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,992.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2985 | 13 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 19244 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14939 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22255 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4021 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4017 | 18 | 4% | 2% | -43% | -87% | -87% |
| HYPE | 4009 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3999 | 20 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3998 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3990 | 17 | 6% | 3% | -47% | -82% | -82% |
| BTC | 3973 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3971 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3957 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2112 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2093 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2052 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1870 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1819 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1751 | 6 | 2% | 1% | -68% | -76% | -75% |
| GBPUSD | 1745 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1726 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1706 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1682 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1260 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1207 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 826 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 419 | 2 | 4% | 1% | -55% | -72% | -70% |
| 2YRRATE | 404 | 4 | 4% | 2% | -8% | -47% | -46% |
| 30YRRATE | 390 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30239 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29197 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5437 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5882 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9025 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11110 | 48 | 6% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4472 | 19 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14505 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,082 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/17 1:14:45 AM | BRENT | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:14:45 AM | WTI | DOWN | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 1:14:45 AM | SILVER | UP | 15 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 1:14:13 AM | ZEC | UP | 47 sec | -0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:13:57 AM | HYPE | UP | 63 sec | -0.222% | 0¢ | ❌ Lost | $0.00 |
| 11/17 1:13:57 AM | ETH | UP | 63 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 11/17 1:13:42 AM | XRP | UP | 78 sec | -0.177% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:13:42 AM | 30YRRATE | UP | 78 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:13:26 AM | 10YRRATE | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:13:26 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:12:39 AM | PALLADIUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:12:23 AM | AUDUSD | UP | 2.6 min | — | 10¢ | ❌ Lost | -$0.15 |
| 11/17 1:12:07 AM | USDJPY | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:11:51 AM | BNB | UP | 3.1 min | -0.196% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:11:35 AM | SOL | UP | 3.4 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 1:11:35 AM | BTC | UP | 3.4 min | -0.211% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 1:11:35 AM | NEAR | UP | 3.4 min | -0.515% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 1:11:03 AM | GOLD | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 1:10:47 AM | USDCAD | UP | 4.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 1:10:47 AM | DOGE | UP | 4.2 min | -0.322% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 1:08:47 AM | PLATINUM | UP | 6.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:52 AM | SOL | DOWN | 8 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 11/17 12:59:52 AM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 12:59:36 AM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:20 AM | ZEC | DOWN | 40 sec | +0.116% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:20 AM | 30YRRATE | UP | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:20 AM | 2YRRATE | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:04 AM | USDCAD | DOWN | 56 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:04 AM | HYPE | UP | 56 sec | -0.146% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:59:04 AM | BNB | DOWN | 56 sec | +0.022% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
