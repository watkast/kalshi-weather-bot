# 15-Minute 1¢ Study

*Updated Tue Oct 20, 10:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2152 finished bets | 1% | $79.30 | +33% | +3.68¢ | $22.40 / $56.90 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1980 | $61.15 | +28% |
| Momentum model ≥ 2%, hold to the close | 3306 | -$25.40 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2152 | -$37.70 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25366 | 25358 | 92 (0%) | 1.07% | -$1,798.70 (-58%) | Hold to the close: -$1,798.70 (-58%) |

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
| Volatility model | 16541 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16541 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16541 | 7.8% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16541 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3909 | 31 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2152 | 23 | +33% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1240 | 15 | +69% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 3306 | 26 | -7% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 1980 | 20 | +28% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1308 | 13 | +36% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6494 | 42 | -30% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4520 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2990 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16739 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5990 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2629 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25358 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,798.70 | -58% | — |
| Sell at 2¢ | 918 | 4% | -$2,722.02 | -88% | 46 sec |
| Sell at 3¢ | 623 | 2% | -$2,717.73 | -88% | 47 sec |
| Sell at 5¢ | 442 | 2% | -$2,673.40 | -87% | 51 sec |
| Sell at 10¢ | 270 | 1% | -$2,579.00 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,390.13 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,165.45 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1007 | 5 | 11% | 3% | -53% | -81% | -84% |
| 2–5 min | 8212 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6476 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9659 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1882 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1871 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1870 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1859 | 9 | 6% | 3% | -42% | -87% | -87% |
| DOGE | 1859 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1857 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1850 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1846 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1845 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 982 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 947 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 923 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 823 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 817 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 755 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 753 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 743 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 709 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 662 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 277 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12775 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12583 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2811 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2901 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4236 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4888 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1900 | 6 | 7% | 3% | -67% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6139 | 29 | 4% | 2% | -46% | -87% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,774 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 10:53:03 AM | ETH | DOWN | 7.0 min | +0.479% | — | In play | — |
| 10/20 10:44:48 AM | COPPER | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:44:16 AM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:44:00 AM | HYPE | DOWN | 59 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:43:45 AM | USDJPY | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:43:18 AM | DOGE | DOWN | 1.7 min | +0.183% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:43:02 AM | BTC | DOWN | 1.9 min | +0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:42:46 AM | XRP | DOWN | 2.2 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:41:57 AM | SOL | DOWN | 3.0 min | +0.339% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:41:57 AM | GOLD | DOWN | 3.0 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/20 10:41:42 AM | ETH | DOWN | 3.3 min | +0.252% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:41:27 AM | SILVER | DOWN | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:41:27 AM | PLATINUM | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:40:39 AM | BNB | DOWN | 4.3 min | +0.196% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:38:01 AM | NEAR | DOWN | 7.0 min | +0.947% | 18¢ | ❌ Lost | -$0.15 |
| 10/20 10:37:45 AM | ZEC | DOWN | 7.2 min | +0.942% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:53 AM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:38 AM | SOL | UP | 22 sec | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:22 AM | BTC | UP | 38 sec | -0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:22 AM | NEAR | DOWN | 38 sec | +0.182% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:29:22 AM | ZEC | DOWN | 38 sec | +0.165% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:29:06 AM | GOLD | UP | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:28:50 AM | DOGE | DOWN | 70 sec | +0.154% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:27:31 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:27:15 AM | BNB | UP | 2.8 min | -0.147% | 4¢ | ❌ Lost | -$0.15 |
| 10/20 10:26:59 AM | HYPE | UP | 3.0 min | -0.356% | 11¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:20 AM | SILVER | UP | 39 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:20 AM | USDJPY | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:04 AM | BNB | DOWN | 55 sec | +0.112% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:14:04 AM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
