# 15-Minute 1¢ Study

*Updated Sat Oct 31, 10:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3351 finished bets | 1% | $115.60 | +31% | +3.45¢ | $80.15 / $35.45 |

*Expect about **99 buys a day** (~$14.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3100 | $54.20 | +16% |
| Volatility model ≥ 2%, hold to the close | 6185 | $21.20 | +3% |
| Momentum model ≥ 2%, hold to the close | 5107 | -$44.55 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 41042 | 41032 | 152 (0%) | 1.07% | -$2,868.50 (-57%) | Hold to the close: -$2,868.50 (-57%) |

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
| Volatility model | 25431 | 4.7% | 0.4% (99) | -695% | ❌ Worse |
| Momentum model | 25431 | 4.6% | 0.4% (99) | -718% | ❌ Worse |
| Mean-reversion model | 25431 | 8.1% | 0.4% (99) | -845% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 25431 | 99 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6185 | 55 | +3% | -79% | -77% | -73% |
| Volatility model ≥ 5% | 3351 | 35 | +31% | -76% | -74% | -70% |
| Volatility model ≥ 10% | 1899 | 21 | +58% | -69% | -68% | -64% |
| Momentum model ≥ 2% | 5107 | 39 | -8% | -81% | -80% | -77% |
| Momentum model ≥ 5% | 3100 | 28 | +16% | -78% | -78% | -73% |
| Momentum model ≥ 10% | 2026 | 19 | +31% | -73% | -72% | -68% |
| Mean-reversion model ≥ 2% | 10460 | 70 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 7331 | 60 | -9% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 4902 | 42 | -3% | -79% | -79% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 25633 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 9712 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 5687 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 41032 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 152 | 0% | -$2,868.50 | -57% | — |
| Sell at 2¢ | 1595 | 4% | -$4,357.80 | -87% | 47 sec |
| Sell at 3¢ | 1097 | 3% | -$4,344.67 | -87% | 48 sec |
| Sell at 5¢ | 759 | 2% | -$4,265.15 | -85% | 63 sec |
| Sell at 10¢ | 455 | 1% | -$4,092.45 | -82% | 65 sec |
| Sell at 25¢ | 239 | 1% | -$3,785.41 | -76% | 83 sec |
| Sell at 50¢ | 156 | 0% | -$3,439.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 1925 | 9 | 11% | 4% | -55% | -80% | -81% |
| 2–5 min | 13098 | 71 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 10388 | 35 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 15610 | 37 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2871 | 13 | 5% | 3% | -42% | -88% | -88% |
| SOL | 2859 | 9 | 4% | 2% | -60% | -91% | -91% |
| HYPE | 2859 | 8 | 5% | 2% | -65% | -89% | -87% |
| BNB | 2858 | 17 | 5% | 2% | -25% | -85% | -84% |
| DOGE | 2849 | 6 | 4% | 2% | -74% | -90% | -89% |
| ETH | 2848 | 11 | 6% | 3% | -53% | -85% | -85% |
| NEAR | 2830 | 13 | 5% | 2% | -40% | -83% | -83% |
| BTC | 2830 | 13 | 5% | 2% | -38% | -88% | -89% |
| XRP | 2829 | 11 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1515 | 5 | 5% | 2% | -60% | -82% | -83% |
| SILVER | 1481 | 7 | 4% | 2% | -44% | -82% | -81% |
| WTI | 1476 | 4 | 3% | 1% | -67% | -93% | -93% |
| PLATINUM | 1314 | 3 | 2% | 1% | -79% | -96% | -96% |
| COPPER | 1253 | 5 | 1% | 1% | -63% | -75% | -75% |
| EURUSD | 1249 | 3 | 2% | 1% | -78% | -89% | -88% |
| NATGAS | 1212 | 7 | 2% | 1% | -46% | -81% | -80% |
| GBPUSD | 1185 | 2 | 2% | 1% | -84% | -96% | -96% |
| PALLADIUM | 1178 | 2 | 1% | 0% | -84% | -90% | -91% |
| USDJPY | 1171 | 5 | 2% | 1% | -60% | -97% | -96% |
| AUDUSD | 705 | 4 | 2% | 1% | -47% | -84% | -83% |
| USDCAD | 685 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 283 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 188 | 1 | 5% | 2% | -50% | -41% | -39% |
| 30YRRATE | 177 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 170 | 2 | 5% | 1% | +10% | +18% | +19% |
| 5YRRATE | 157 | 1 | 6% | 3% | -41% | -89% | -92% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 20828 | 83 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 20204 | 69 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4162 | 21 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 4387 | 15 | 3% | 2% | -48% | -92% | -91% |
| 0.1–0.2% | 6609 | 22 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 7584 | 32 | 7% | 3% | -53% | -87% | -86% |
| Over 0.5% | 2886 | 11 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 10116 | 36 | 4% | 2% | -59% | -86% | -86% |
| Morning (6am–12pm) | 10310 | 46 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 9655 | 34 | 4% | 2% | -59% | -87% | -87% |
| Evening (6pm–12am) | 10951 | 36 | 3% | 2% | -62% | -91% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,656 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/31 10:14:48 PM | BNB | DOWN | 11 sec | +0.114% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 10:13:10 PM | HYPE | DOWN | 1.8 min | +0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:12:35 PM | ZEC | UP | 2.4 min | -0.171% | 3¢ | ❌ Lost | -$0.15 |
| 10/31 10:12:19 PM | BNB | UP | 2.7 min | -0.071% | 99¢ | ✅ Won | $13.85 |
| 10/31 10:12:04 PM | BTC | UP | 2.9 min | -0.088% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 10:12:04 PM | DOGE | UP | 2.9 min | -0.202% | 2¢ | ❌ Lost | -$0.15 |
| 10/31 10:11:47 PM | XRP | UP | 3.2 min | -0.120% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:11:14 PM | NEAR | UP | 3.8 min | -0.431% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:09:53 PM | ETH | UP | 5.1 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 10:08:14 PM | SOL | UP | 6.8 min | -0.275% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:59:30 PM | NEAR | UP | 29 sec | -0.231% | 0¢ | ❌ Lost | $0.00 |
| 10/31 9:58:27 PM | BTC | UP | 1.5 min | -0.051% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 9:58:27 PM | ZEC | UP | 1.5 min | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 9:58:11 PM | XRP | UP | 1.8 min | -0.104% | 0¢ | ❌ Lost | $0.00 |
| 10/31 9:58:11 PM | ETH | UP | 1.8 min | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 9:57:52 PM | BNB | UP | 2.1 min | -0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:57:06 PM | DOGE | UP | 2.9 min | -0.161% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 9:56:01 PM | SOL | UP | 4.0 min | -0.163% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:54:36 PM | HYPE | UP | 5.4 min | -0.382% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:43:41 PM | NEAR | UP | 79 sec | -0.352% | 0¢ | ❌ Lost | -$0.15 |
| 10/31 9:42:54 PM | HYPE | UP | 2.1 min | -0.191% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:42:06 PM | BTC | DOWN | 2.9 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:41:19 PM | BNB | DOWN | 3.7 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:41:03 PM | ETH | DOWN | 4.0 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:41:03 PM | ZEC | DOWN | 4.0 min | +0.414% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:40:25 PM | XRP | DOWN | 4.6 min | +0.168% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:40:09 PM | DOGE | DOWN | 4.8 min | +0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:39:36 PM | SOL | DOWN | 5.4 min | +0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/31 9:29:31 PM | HYPE | DOWN | 28 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/31 9:29:16 PM | XRP | UP | 43 sec | -0.032% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
