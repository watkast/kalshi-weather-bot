# 15-Minute 1¢ Study

*Updated Sat Oct 24, 12:35 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2544 finished bets | 1% | $103.70 | +36% | +4.08¢ | $42.65 / $61.05 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2351 | $75.90 | +29% |
| Volatility model ≥ 2%, hold to the close | 4711 | $24.95 | +4% |
| Momentum model ≥ 2%, hold to the close | 3919 | $1.35 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30667 | 30659 | 119 (0%) | 1.07% | -$2,071.85 (-55%) | Hold to the close: -$2,071.85 (-55%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 19452 | 4.7% | 0.4% (84) | -629% | ❌ Worse |
| Momentum model | 19452 | 4.6% | 0.4% (84) | -656% | ❌ Worse |
| Mean-reversion model | 19452 | 7.9% | 0.4% (84) | -759% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19452 | 84 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4711 | 43 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2544 | 28 | +36% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1450 | 18 | +74% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 3919 | 33 | +0% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2351 | 24 | +29% | -75% | -75% | -70% |
| Momentum model ≥ 10% | 1542 | 16 | +43% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7826 | 55 | -23% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5472 | 46 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3641 | 33 | +3% | -78% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19652 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30659 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,071.85 | -55% | — |
| Sell at 2¢ | 1145 | 4% | -$3,272.15 | -88% | 47 sec |
| Sell at 3¢ | 787 | 3% | -$3,262.92 | -87% | 48 sec |
| Sell at 5¢ | 552 | 2% | -$3,211.05 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,082.45 | -82% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,838.88 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,557.10 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1313 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9794 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7794 | 30 | 3% | 2% | -58% | -91% | -91% |
| Under 1 min | 11754 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2202 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2194 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2192 | 12 | 5% | 2% | -32% | -83% | -82% |
| SOL | 2187 | 6 | 4% | 2% | -66% | -92% | -91% |
| ETH | 2184 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2180 | 4 | 4% | 2% | -77% | -90% | -89% |
| XRP | 2175 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2170 | 12 | 5% | 3% | -28% | -81% | -81% |
| BTC | 2168 | 12 | 5% | 2% | -26% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15485 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15174 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3257 | 18 | 2% | 1% | -7% | -79% | -78% |
| 0.05–0.1% | 3384 | 11 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5059 | 19 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 5746 | 28 | 6% | 3% | -46% | -87% | -86% |
| Over 0.5% | 2202 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7551 | 32 | 4% | 2% | -52% | -84% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,637 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 12:29:58 AM | BTC | DOWN | 1 sec | +0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:29:58 AM | DOGE | UP | 1 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:29:58 AM | ETH | DOWN | 1 sec | -0.003% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:29:42 AM | XRP | DOWN | 17 sec | -0.008% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:29:42 AM | ZEC | DOWN | 17 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:29:26 AM | SOL | UP | 33 sec | -0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 12:28:54 AM | SOL | DOWN | 65 sec | -0.032% | 100¢ | ✅ Won | $13.85 |
| 10/24 12:28:54 AM | NEAR | DOWN | 65 sec | +0.143% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:28:38 AM | BNB | DOWN | 81 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 12:28:38 AM | HYPE | DOWN | 81 sec | +0.055% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 12:14:40 AM | DOGE | UP | 20 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:14:40 AM | BNB | UP | 20 sec | -0.056% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:14:22 AM | SOL | UP | 38 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:14:22 AM | BTC | DOWN | 38 sec | +0.012% | 2¢ | ❌ Lost | -$0.15 |
| 10/24 12:14:22 AM | XRP | DOWN | 38 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:14:22 AM | NEAR | UP | 38 sec | -0.236% | 0¢ | ❌ Lost | $0.00 |
| 10/24 12:14:22 AM | HYPE | UP | 38 sec | -0.070% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 12:14:06 AM | ETH | DOWN | 54 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 12:12:47 AM | ZEC | DOWN | 2.2 min | +0.372% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:59:56 PM | BNB | UP | 3 sec | -0.037% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:59:56 PM | SOL | UP | 3 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:59:56 PM | DOGE | UP | 3 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:59:40 PM | ETH | DOWN | 19 sec | +0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:59:40 PM | BTC | DOWN | 19 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:59:24 PM | HYPE | UP | 35 sec | -0.026% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:59:08 PM | NEAR | UP | 52 sec | -0.177% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:57:47 PM | XRP | UP | 2.2 min | -0.140% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:57:47 PM | ZEC | UP | 2.2 min | -0.247% | 0¢ | ❌ Lost | -$0.15 |
| 10/23 11:44:52 PM | BTC | DOWN | 8 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/23 11:44:36 PM | ETH | DOWN | 24 sec | +0.027% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
