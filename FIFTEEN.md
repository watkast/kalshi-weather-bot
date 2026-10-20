# 15-Minute 1¢ Study

*Updated Tue Oct 20, 6:22 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2116 finished bets | 1% | $84.25 | +35% | +3.98¢ | $23.90 / $60.35 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1948 | $65.50 | +31% |
| Momentum model ≥ 2%, hold to the close | 3245 | -$17.00 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 2116 | -$32.75 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25057 | 25050 | 92 (0%) | 1.07% | -$1,757.15 (-58%) | Hold to the close: -$1,757.15 (-58%) |

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
| Volatility model | 16384 | 4.6% | 0.4% (65) | -673% | ❌ Worse |
| Momentum model | 16384 | 4.6% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16384 | 7.7% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16384 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3834 | 31 | -7% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2116 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1231 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3245 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1948 | 20 | +31% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1291 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6397 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4450 | 34 | -16% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2942 | 22 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16582 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5898 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2570 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25050 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,757.15 | -58% | — |
| Sell at 2¢ | 902 | 4% | -$2,684.63 | -88% | 46 sec |
| Sell at 3¢ | 613 | 2% | -$2,680.08 | -88% | 47 sec |
| Sell at 5¢ | 435 | 2% | -$2,636.40 | -87% | 51 sec |
| Sell at 10¢ | 265 | 1% | -$2,544.00 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,351.89 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,123.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 974 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8125 | 41 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6397 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9550 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1864 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1853 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1852 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1843 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1842 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1839 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1833 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1828 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1828 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 968 | 1 | 3% | 1% | -88% | -93% | -95% |
| SILVER | 934 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 910 | 3 | 3% | 1% | -61% | -94% | -95% |
| COPPER | 810 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 802 | 0 | 0% | 0% | -100% | -99% | -99% |
| NATGAS | 744 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 739 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 730 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 697 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 647 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 269 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 218 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12651 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12399 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2803 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2886 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4196 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4831 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1863 | 6 | 6% | 3% | -67% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 5831 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,790 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:14:55 AM | DOGE | UP | 4 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:55 AM | ETH | UP | 4 sec | -0.050% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:55 AM | WTI | DOWN | 4 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:23 AM | XRP | UP | 36 sec | -0.131% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:06 AM | HYPE | UP | 53 sec | -0.083% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:06 AM | USDJPY | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:06 AM | NEAR | DOWN | 53 sec | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:13:50 AM | SOL | DOWN | 69 sec | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:13:34 AM | BNB | DOWN | 85 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:13:02 AM | ZEC | DOWN | 2.0 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:12:45 AM | GBPUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:12:29 AM | NATGAS | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:12:13 AM | PLATINUM | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:12:13 AM | EURUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:11:08 AM | BTC | UP | 3.9 min | -0.203% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 6:09:47 AM | GOLD | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:09:47 AM | SILVER | UP | 5.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:59:51 AM | NATGAS | UP | 9 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:30 AM | USDCAD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:30 AM | GOLD | DOWN | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | XRP | UP | 1.8 min | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:14 AM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:40 AM | WTI | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:24 AM | SOL | UP | 2.6 min | -0.208% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:09 AM | HYPE | UP | 2.8 min | -0.174% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 5:56:52 AM | ETH | UP | 3.1 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:56:52 AM | BTC | UP | 3.1 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:56:04 AM | DOGE | UP | 3.9 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
