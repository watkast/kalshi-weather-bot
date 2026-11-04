# 15-Minute 1¢ Study

*Updated Tue Nov 3, 6:37 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3601 finished bets | 1% | $115.70 | +29% | +3.21¢ | $80.05 / $35.65 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3338 | $42.85 | +12% |
| Volatility model ≥ 2%, hold to the close | 6659 | $34.65 | +4% |
| Momentum model ≥ 2%, hold to the close | 5495 | -$46.80 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44494 | 44484 | 165 (0%) | 1.07% | -$3,106.80 (-57%) | Hold to the close: -$3,106.80 (-57%) |

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
| Volatility model | 27351 | 4.7% | 0.4% (107) | -681% | ❌ Worse |
| Momentum model | 27351 | 4.6% | 0.4% (107) | -705% | ❌ Worse |
| Mean-reversion model | 27351 | 8.1% | 0.4% (107) | -829% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27351 | 107 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6659 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3601 | 37 | +29% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2045 | 22 | +54% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5495 | 42 | -7% | -81% | -81% | -77% |
| Momentum model ≥ 5% | 3338 | 29 | +12% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2179 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11305 | 77 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7935 | 66 | -8% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5313 | 47 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27556 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10520 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6408 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44484 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 165 | 0% | -$3,106.80 | -57% | — |
| Sell at 2¢ | 1754 | 4% | -$4,722.76 | -87% | 47 sec |
| Sell at 3¢ | 1200 | 3% | -$4,710.80 | -87% | 49 sec |
| Sell at 5¢ | 831 | 2% | -$4,610.65 | -85% | 63 sec |
| Sell at 10¢ | 501 | 1% | -$4,410.49 | -81% | 66 sec |
| Sell at 25¢ | 262 | 1% | -$4,087.58 | -75% | 83 sec |
| Sell at 50¢ | 169 | 0% | -$3,716.05 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2153 | 9 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 14302 | 79 | 7% | 4% | -45% | -86% | -86% |
| 1–2 min | 11221 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16797 | 38 | 1% | 0% | -68% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3087 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3080 | 11 | 4% | 2% | -55% | -90% | -90% |
| BNB | 3074 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3073 | 9 | 5% | 2% | -63% | -89% | -87% |
| DOGE | 3061 | 6 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3058 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3044 | 15 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3044 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3035 | 12 | 3% | 1% | -51% | -89% | -88% |
| GOLD | 1632 | 5 | 5% | 2% | -63% | -81% | -83% |
| SILVER | 1590 | 7 | 5% | 2% | -48% | -82% | -81% |
| WTI | 1588 | 5 | 3% | 1% | -62% | -92% | -93% |
| PLATINUM | 1421 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1362 | 3 | 2% | 1% | -79% | -89% | -89% |
| COPPER | 1343 | 6 | 2% | 1% | -58% | -69% | -69% |
| NATGAS | 1293 | 7 | 2% | 1% | -49% | -82% | -81% |
| GBPUSD | 1292 | 3 | 2% | 1% | -78% | -96% | -96% |
| PALLADIUM | 1272 | 3 | 1% | 1% | -78% | -90% | -91% |
| USDJPY | 1269 | 5 | 2% | 1% | -63% | -97% | -97% |
| AUDUSD | 822 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 786 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 381 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22608 | 88 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 21876 | 77 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4478 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4713 | 18 | 3% | 2% | -42% | -91% | -91% |
| 0.1–0.2% | 7137 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8167 | 33 | 7% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3053 | 12 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11048 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 11784 | 38 | 3% | 2% | -63% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,721 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/3 6:29:21 PM | ETH | DOWN | 38 sec | +0.057% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:29:21 PM | DOGE | DOWN | 38 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:29:21 PM | ZEC | DOWN | 38 sec | +0.167% | 0¢ | ❌ Lost | $0.00 |
| 11/3 6:29:06 PM | XRP | UP | 53 sec | -0.192% | 0¢ | ❌ Lost | $0.00 |
| 11/3 6:29:06 PM | HYPE | DOWN | 53 sec | +0.258% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:29:06 PM | NEAR | DOWN | 53 sec | +0.289% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:29:06 PM | PALLADIUM | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:29:06 PM | USDCAD | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:29:06 PM | SOL | DOWN | 53 sec | +0.177% | 0¢ | ❌ Lost | $0.00 |
| 11/3 6:28:34 PM | USDJPY | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:28:18 PM | EURUSD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:28:18 PM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:27:41 PM | GBPUSD | DOWN | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:27:25 PM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:27:25 PM | BTC | DOWN | 2.6 min | +0.309% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:27:25 PM | BRENT | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:26:57 PM | WTI | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:26:07 PM | BNB | DOWN | 3.9 min | +0.504% | 2¢ | ❌ Lost | -$0.15 |
| 11/3 6:25:34 PM | GOLD | DOWN | 4.4 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/3 6:25:18 PM | SILVER | DOWN | 4.7 min | — | 9¢ | ❌ Lost | -$0.15 |
| 11/3 6:24:29 PM | PLATINUM | DOWN | 5.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:14:35 PM | PALLADIUM | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:14:19 PM | SILVER | DOWN | 41 sec | — | 2¢ | ❌ Lost | $0.00 |
| 11/3 6:13:48 PM | AUDUSD | DOWN | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/3 6:13:48 PM | GOLD | DOWN | 71 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/3 6:13:32 PM | NATGAS | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:12:28 PM | ETH | UP | 2.5 min | -0.460% | 0¢ | ❌ Lost | $0.00 |
| 11/3 6:12:28 PM | BNB | UP | 2.5 min | -0.181% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:12:12 PM | XRP | UP | 2.8 min | -0.484% | 1¢ | ❌ Lost | -$0.15 |
| 11/3 6:11:58 PM | BTC | UP | 3.0 min | -0.391% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
