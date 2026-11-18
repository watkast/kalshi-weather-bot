# 15-Minute 1¢ Study

*Updated Wed Nov 18, 1:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4499 finished bets | 1% | $216.90 | +44% | +4.82¢ | $81.90 / $135.00 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4236 | $117.10 | +26% |
| Volatility model ≥ 2%, hold to the close | 8392 | $82.50 | +8% |
| Momentum model ≥ 2%, hold to the close | 6963 | -$0.90 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 60406 | 60372 | 237 (0%) | 1.07% | -$4,029.90 (-55%) | Hold to the close: -$4,029.90 (-55%) |

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
| Volatility model | 36155 | 4.5% | 0.4% (154) | -622% | ❌ Worse |
| Momentum model | 36155 | 4.4% | 0.4% (154) | -647% | ❌ Worse |
| Mean-reversion model | 36155 | 7.9% | 0.4% (154) | -755% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 36155 | 154 | -45% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 8392 | 78 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4499 | 51 | +44% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2582 | 30 | +69% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6963 | 57 | -0% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4236 | 41 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2757 | 26 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14816 | 108 | -20% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10304 | 89 | -4% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6844 | 64 | +6% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 36361 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14369 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9642 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 60372 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 237 | 0% | -$4,029.90 | -55% | — |
| Sell at 2¢ | 2433 | 4% | -$6,421.32 | -87% | 47 sec |
| Sell at 3¢ | 1643 | 3% | -$6,413.13 | -87% | 48 sec |
| Sell at 5¢ | 1123 | 2% | -$6,295.95 | -86% | 63 sec |
| Sell at 10¢ | 685 | 1% | -$6,044.55 | -82% | 65 sec |
| Sell at 25¢ | 366 | 1% | -$5,590.44 | -76% | 80 sec |
| Sell at 50¢ | 243 | 0% | -$5,035.65 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3054 | 17 | 11% | 4% | -47% | -81% | -83% |
| 2–5 min | 19575 | 108 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 15142 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22588 | 61 | 1% | 0% | -61% | -86% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4067 | 19 | 5% | 3% | -39% | -88% | -87% |
| SOL | 4064 | 19 | 4% | 2% | -40% | -86% | -87% |
| HYPE | 4057 | 12 | 5% | 2% | -62% | -89% | -88% |
| DOGE | 4046 | 11 | 4% | 2% | -66% | -90% | -89% |
| BNB | 4045 | 21 | 5% | 2% | -34% | -85% | -85% |
| ETH | 4039 | 19 | 6% | 3% | -41% | -82% | -82% |
| NEAR | 4020 | 18 | 5% | 2% | -42% | -85% | -86% |
| BTC | 4020 | 21 | 5% | 2% | -29% | -86% | -88% |
| XRP | 4003 | 16 | 3% | 2% | -49% | -89% | -88% |
| GOLD | 2148 | 6 | 5% | 2% | -66% | -82% | -84% |
| WTI | 2130 | 7 | 4% | 1% | -60% | -91% | -92% |
| SILVER | 2084 | 9 | 5% | 2% | -49% | -83% | -83% |
| PLATINUM | 1901 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1853 | 7 | 2% | 1% | -65% | -91% | -90% |
| COPPER | 1785 | 6 | 2% | 1% | -69% | -76% | -76% |
| GBPUSD | 1780 | 6 | 2% | 1% | -69% | -96% | -96% |
| NATGAS | 1751 | 10 | 2% | 1% | -47% | -75% | -75% |
| USDJPY | 1740 | 6 | 2% | 1% | -68% | -97% | -96% |
| PALLADIUM | 1709 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1293 | 6 | 2% | 1% | -57% | -89% | -89% |
| USDCAD | 1238 | 1 | 3% | 1% | -92% | -95% | -96% |
| BRENT | 861 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 437 | 2 | 3% | 1% | -57% | -73% | -71% |
| 2YRRATE | 422 | 4 | 4% | 2% | -12% | -50% | -48% |
| 30YRRATE | 405 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 393 | 2 | 4% | 2% | -53% | -93% | -95% |
| INX | 81 | 1 | 2% | 1% | +15% | -96% | -97% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30771 | 121 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 29601 | 116 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5460 | 25 | 2% | 1% | -18% | -78% | -77% |
| 0.05–0.1% | 5920 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9109 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11276 | 50 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 4587 | 23 | 7% | 3% | -48% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14585 | 45 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 14416 | 78 | 5% | 2% | -38% | -85% | -84% |
| Afternoon (12–6pm) | 14813 | 65 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 16558 | 49 | 4% | 2% | -66% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,078 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/18 1:14:36 AM | GBPUSD | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:32 AM | 30YRRATE | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:32 AM | 2YRRATE | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | 5YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | AUDUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | 10YRRATE | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:13:00 AM | USDJPY | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:12:41 AM | XRP | UP | 2.3 min | -0.429% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:12:09 AM | DOGE | UP | 2.8 min | -0.278% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:11:40 AM | GOLD | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:11:40 AM | BRENT | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:11:24 AM | NEAR | UP | 3.6 min | -0.587% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:11:08 AM | WTI | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:11:08 AM | NATGAS | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:10:52 AM | ZEC | UP | 4.1 min | -0.684% | 0¢ | ❌ Lost | $0.00 |
| 11/18 1:10:52 AM | PALLADIUM | UP | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:10:20 AM | SOL | UP | 4.7 min | -0.433% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:10:04 AM | BNB | UP | 4.9 min | -0.312% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:10:04 AM | HYPE | UP | 4.9 min | -0.485% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:09:48 AM | COPPER | UP | 5.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 1:09:33 AM | SILVER | UP | 5.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:09:17 AM | BTC | UP | 5.7 min | -0.333% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:09:17 AM | ETH | UP | 5.7 min | -0.370% | 1¢ | ❌ Lost | -$0.15 |
| 11/18 1:09:01 AM | PLATINUM | UP | 6.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:59:48 AM | BRENT | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:59:16 AM | 30YRRATE | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:59:16 AM | WTI | UP | 43 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/18 12:59:16 AM | NEAR | DOWN | 43 sec | +0.050% | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:59:16 AM | AUDUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/18 12:59:16 AM | PALLADIUM | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
