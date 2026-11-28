# 15-Minute 1¢ Study

*Updated Sat Nov 28, 5:55 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 5082 finished bets | 1% | $191.05 | +35% | +3.76¢ | $90.00 / $101.05 |

*Expect about **83 buys a day** (~$12.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4812 | $92.15 | +18% |
| Volatility model ≥ 2%, hold to the close | 9470 | $9.90 | +1% |
| Momentum model ≥ 2%, hold to the close | 7871 | -$49.20 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 69941 | 69905 | 259 (0%) | 1.07% | -$4,826.35 (-57%) | Hold to the close: -$4,826.35 (-57%) |

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
| Volatility model | 41341 | 4.6% | 0.4% (167) | -661% | ❌ Worse |
| Momentum model | 41341 | 4.5% | 0.4% (167) | -684% | ❌ Worse |
| Mean-reversion model | 41341 | 7.9% | 0.4% (167) | -803% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 41341 | 167 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9470 | 81 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 5082 | 53 | +35% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 2958 | 32 | +61% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 7871 | 60 | -6% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4812 | 43 | +18% | -76% | -75% | -72% |
| Momentum model ≥ 10% | 3144 | 28 | +30% | -69% | -69% | -65% |
| Mean-reversion model ≥ 2% | 16890 | 113 | -26% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11769 | 93 | -12% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 7816 | 66 | -3% | -78% | -78% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 41553 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16665 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11687 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 69905 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 259 | 0% | -$4,826.35 | -57% | — |
| Sell at 2¢ | 2858 | 4% | -$7,401.27 | -88% | 47 sec |
| Sell at 3¢ | 1918 | 3% | -$7,396.33 | -88% | 48 sec |
| Sell at 5¢ | 1298 | 2% | -$7,272.65 | -86% | 62 sec |
| Sell at 10¢ | 797 | 1% | -$6,988.28 | -83% | 65 sec |
| Sell at 25¢ | 430 | 1% | -$6,455.05 | -76% | 80 sec |
| Sell at 50¢ | 273 | 0% | -$5,853.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3626 | 17 | 10% | 4% | -56% | -82% | -83% |
| 2–5 min | 22657 | 117 | 7% | 3% | -49% | -86% | -86% |
| 1–2 min | 17368 | 59 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 26241 | 66 | 1% | 0% | -63% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4652 | 21 | 5% | 2% | -40% | -88% | -87% |
| HYPE | 4638 | 16 | 4% | 2% | -55% | -89% | -88% |
| SOL | 4630 | 20 | 4% | 2% | -44% | -86% | -86% |
| BNB | 4625 | 22 | 5% | 2% | -39% | -86% | -85% |
| DOGE | 4623 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4619 | 19 | 6% | 3% | -48% | -82% | -82% |
| BTC | 4595 | 25 | 5% | 2% | -25% | -86% | -88% |
| NEAR | 4587 | 18 | 5% | 2% | -48% | -85% | -86% |
| XRP | 4584 | 16 | 4% | 2% | -55% | -89% | -88% |
| GOLD | 2456 | 8 | 5% | 2% | -60% | -83% | -84% |
| WTI | 2451 | 9 | 4% | 2% | -55% | -86% | -87% |
| SILVER | 2406 | 9 | 5% | 2% | -55% | -83% | -84% |
| PLATINUM | 2173 | 5 | 3% | 1% | -79% | -95% | -95% |
| EURUSD | 2134 | 7 | 3% | 1% | -69% | -91% | -90% |
| GBPUSD | 2078 | 8 | 2% | 1% | -64% | -96% | -95% |
| COPPER | 2061 | 6 | 2% | 1% | -73% | -79% | -79% |
| USDJPY | 2028 | 6 | 2% | 1% | -72% | -97% | -96% |
| NATGAS | 2023 | 10 | 2% | 1% | -54% | -77% | -77% |
| PALLADIUM | 1963 | 4 | 1% | 1% | -81% | -93% | -93% |
| AUDUSD | 1604 | 7 | 2% | 1% | -59% | -90% | -90% |
| USDCAD | 1504 | 1 | 3% | 1% | -94% | -96% | -96% |
| BRENT | 1132 | 1 | 2% | 1% | -92% | -96% | -96% |
| 10YRRATE | 564 | 2 | 3% | 1% | -67% | -78% | -76% |
| 30YRRATE | 526 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 523 | 4 | 4% | 2% | -29% | -58% | -57% |
| 5YRRATE | 514 | 2 | 4% | 2% | -64% | -94% | -95% |
| INX | 142 | 1 | 2% | 1% | -34% | -96% | -96% |
| USDMXN | 70 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 35581 | 135 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 34324 | 124 | 4% | 2% | -58% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 6025 | 25 | 2% | 1% | -23% | -79% | -79% |
| 0.05–0.1% | 6612 | 26 | 3% | 1% | -36% | -91% | -91% |
| 0.1–0.2% | 10302 | 37 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 13085 | 57 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5514 | 24 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16777 | 51 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16558 | 82 | 4% | 2% | -43% | -86% | -85% |
| Afternoon (12–6pm) | 17081 | 74 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 19489 | 52 | 4% | 2% | -69% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,109 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/28 5:44:30 AM | BNB | UP | 30 sec | -0.033% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 5:44:14 AM | HYPE | UP | 46 sec | -0.178% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:44:14 AM | SOL | UP | 46 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:43:58 AM | XRP | UP | 62 sec | -0.096% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:43:58 AM | DOGE | UP | 62 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:43:44 AM | ETH | UP | 76 sec | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:43:28 AM | BTC | UP | 1.5 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:43:28 AM | ZEC | UP | 1.5 min | -0.384% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:41:54 AM | NEAR | UP | 3.1 min | -0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:29:21 AM | BNB | UP | 38 sec | -0.036% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 5:29:21 AM | NEAR | UP | 38 sec | -0.150% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 5:29:21 AM | XRP | DOWN | 38 sec | +0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:29:21 AM | BTC | UP | 38 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:29:07 AM | ETH | UP | 52 sec | -0.087% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 5:28:35 AM | DOGE | UP | 84 sec | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:28:35 AM | ZEC | UP | 84 sec | -0.267% | 4¢ | ❌ Lost | -$0.15 |
| 11/28 5:28:05 AM | SOL | UP | 1.9 min | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:27:35 AM | HYPE | DOWN | 2.4 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:14:54 AM | DOGE | UP | 6 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:14:38 AM | SOL | DOWN | 22 sec | +0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 5:14:38 AM | NEAR | DOWN | 22 sec | +0.191% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:13:52 AM | BNB | DOWN | 68 sec | +0.066% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 5:13:52 AM | BTC | DOWN | 68 sec | +0.102% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:13:52 AM | ZEC | DOWN | 68 sec | +0.226% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:13:36 AM | XRP | DOWN | 84 sec | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 5:13:36 AM | HYPE | DOWN | 84 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/28 5:13:04 AM | ETH | DOWN | 1.9 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/28 4:59:35 AM | BNB | UP | 24 sec | -0.022% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 4:59:35 AM | DOGE | DOWN | 24 sec | -0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/28 4:59:35 AM | HYPE | UP | 24 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
