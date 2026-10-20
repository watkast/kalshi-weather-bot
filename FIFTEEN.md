# 15-Minute 1¢ Study

*Updated Tue Oct 20, 11:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2155 finished bets | 1% | $78.85 | +32% | +3.66¢ | $22.25 / $56.60 |

*Expect about **96 buys a day** (~$14.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1989 | $59.95 | +27% |
| Momentum model ≥ 2%, hold to the close | 3315 | -$26.60 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2155 | -$38.15 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25396 | 25389 | 92 (0%) | 1.07% | -$1,802.75 (-58%) | Hold to the close: -$1,802.75 (-58%) |

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
| Volatility model | 16558 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16558 | 4.6% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16558 | 7.8% | 0.4% (65) | -814% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16558 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3916 | 31 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2155 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1241 | 15 | +69% | -60% | -58% | -55% |
| Momentum model ≥ 2% | 3315 | 26 | -7% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 1989 | 20 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1312 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6500 | 42 | -30% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4523 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2993 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16756 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6002 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2631 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25389 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,802.75 | -58% | — |
| Sell at 2¢ | 919 | 4% | -$2,725.81 | -88% | 46 sec |
| Sell at 3¢ | 624 | 2% | -$2,721.39 | -88% | 47 sec |
| Sell at 5¢ | 443 | 2% | -$2,676.80 | -87% | 51 sec |
| Sell at 10¢ | 270 | 1% | -$2,583.05 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,394.18 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,169.50 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1009 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8223 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6481 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9672 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1884 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1873 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1872 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1861 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1861 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1859 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1852 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1848 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1846 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 984 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 949 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 924 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 824 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 819 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 757 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 753 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 745 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 711 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 662 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 277 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 228 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12787 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12602 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2813 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2904 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4237 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4896 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1903 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6170 | 29 | 4% | 2% | -46% | -87% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,768 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 11:14:52 AM | SILVER | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:52 AM | PLATINUM | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:52 AM | XRP | DOWN | 7 sec | -0.023% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:36 AM | DOGE | UP | 23 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:14:36 AM | HYPE | DOWN | 23 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:36 AM | NATGAS | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:36 AM | GOLD | UP | 23 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:36 AM | PALLADIUM | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:36 AM | ETH | UP | 23 sec | -0.048% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:14:13 AM | SOL | UP | 46 sec | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:14:13 AM | BNB | UP | 46 sec | -0.075% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:13:57 AM | GBPUSD | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:12:54 AM | ZEC | DOWN | 2.1 min | +0.330% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:12:21 AM | NEAR | UP | 2.6 min | -0.905% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:59:45 AM | GBPUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:59:45 AM | PLATINUM | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:58:57 AM | NATGAS | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:58:42 AM | WTI | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:58:42 AM | PALLADIUM | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:58:42 AM | COPPER | UP | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:57:54 AM | GOLD | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:57:38 AM | SILVER | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:57:08 AM | SOL | DOWN | 2.9 min | +0.345% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:57:08 AM | ZEC | DOWN | 2.9 min | +0.566% | 0¢ | ❌ Lost | $0.00 |
| 10/20 10:56:52 AM | DOGE | DOWN | 3.1 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:55:43 AM | HYPE | DOWN | 4.3 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:55:43 AM | BNB | DOWN | 4.3 min | +0.200% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:55:43 AM | XRP | DOWN | 4.3 min | +0.423% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 10:55:26 AM | BTC | DOWN | 4.6 min | +0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 10:54:38 AM | NEAR | DOWN | 5.4 min | +1.247% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
