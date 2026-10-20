# 15-Minute 1¢ Study

*Updated Tue Oct 20, 3:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2100 finished bets | 1% | $86.65 | +37% | +4.13¢ | $24.80 / $61.85 |

*Expect about **95 buys a day** (~$14.24/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1934 | $67.60 | +32% |
| Momentum model ≥ 2%, hold to the close | 3223 | -$13.70 | -4% |
| Volatility model ≥ 2%, hold to the close | 3806 | -$29.80 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24882 | 24875 | 92 (0%) | 1.07% | -$1,734.35 (-57%) | Hold to the close: -$1,734.35 (-57%) |

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
| Volatility model | 16288 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16288 | 4.6% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16288 | 7.7% | 0.4% (65) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16288 | 65 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3806 | 31 | -6% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2100 | 23 | +37% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1223 | 15 | +72% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3223 | 26 | -4% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 1934 | 20 | +32% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 1281 | 13 | +40% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6351 | 42 | -28% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4419 | 34 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2921 | 22 | -14% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16486 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5853 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2536 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24875 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,734.35 | -57% | — |
| Sell at 2¢ | 893 | 4% | -$2,664.17 | -88% | 45 sec |
| Sell at 3¢ | 604 | 2% | -$2,660.79 | -88% | 47 sec |
| Sell at 5¢ | 430 | 2% | -$2,616.85 | -87% | 50 sec |
| Sell at 10¢ | 261 | 1% | -$2,526.44 | -84% | 64 sec |
| Sell at 25¢ | 144 | 1% | -$2,335.71 | -77% | 80 sec |
| Sell at 50¢ | 94 | 0% | -$2,107.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 966 | 5 | 10% | 3% | -51% | -82% | -84% |
| 2–5 min | 8072 | 41 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 6345 | 24 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 9488 | 22 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1853 | 11 | 4% | 2% | -26% | -90% | -90% |
| HYPE | 1842 | 6 | 5% | 2% | -60% | -89% | -88% |
| BNB | 1842 | 9 | 5% | 2% | -40% | -82% | -82% |
| ETH | 1832 | 9 | 6% | 3% | -41% | -87% | -86% |
| DOGE | 1831 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1828 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1822 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1818 | 10 | 6% | 3% | -29% | -79% | -79% |
| BTC | 1818 | 10 | 5% | 2% | -26% | -88% | -90% |
| GOLD | 959 | 1 | 3% | 1% | -88% | -93% | -94% |
| SILVER | 928 | 4 | 3% | 1% | -50% | -81% | -81% |
| WTI | 902 | 3 | 3% | 1% | -61% | -94% | -96% |
| COPPER | 805 | 3 | 2% | 1% | -65% | -74% | -74% |
| PLATINUM | 795 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 738 | 5 | 2% | 1% | -37% | -84% | -83% |
| EURUSD | 733 | 3 | 2% | 1% | -62% | -83% | -83% |
| PALLADIUM | 726 | 2 | 1% | 0% | -74% | -85% | -85% |
| GBPUSD | 688 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 639 | 3 | 1% | 1% | -56% | -99% | -98% |
| AUDUSD | 265 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 211 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12562 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12313 | 47 | 3% | 1% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2793 | 15 | 2% | 1% | -10% | -77% | -76% |
| 0.05–0.1% | 2865 | 10 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4160 | 13 | 5% | 2% | -61% | -90% | -89% |
| 0.2–0.5% | 4807 | 23 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1858 | 6 | 6% | 3% | -67% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6292 | 26 | 4% | 2% | -53% | -85% | -85% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,802 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 3:29:44 AM | BTC | DOWN | 15 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:29:28 AM | PLATINUM | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:29:28 AM | NATGAS | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:55 AM | PALLADIUM | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:55 AM | USDCAD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:55 AM | GBPUSD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:23 AM | EURUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:28:07 AM | AUDUSD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:27:50 AM | SOL | DOWN | 2.1 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:25:24 AM | BNB | DOWN | 4.6 min | +0.078% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:24:52 AM | ZEC | DOWN | 5.1 min | +0.452% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:24:35 AM | XRP | DOWN | 5.4 min | +0.263% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:23:14 AM | DOGE | DOWN | 6.8 min | +0.278% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:21:53 AM | ETH | DOWN | 8.1 min | +0.298% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:52 AM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:21 AM | HYPE | DOWN | 38 sec | +0.042% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:14:21 AM | AUDUSD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:04 AM | BNB | UP | 55 sec | -0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:14:04 AM | SOL | UP | 55 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:14:04 AM | EURUSD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:48 AM | BTC | UP | 71 sec | -0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/20 3:13:48 AM | PALLADIUM | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:48 AM | XRP | UP | 71 sec | -0.155% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:48 AM | WTI | DOWN | 71 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:48 AM | DOGE | UP | 71 sec | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:48 AM | ZEC | UP | 71 sec | -0.217% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:48 AM | NATGAS | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:13:32 AM | GBPUSD | UP | 87 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 3:12:11 AM | ETH | UP | 2.8 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 3:12:11 AM | SILVER | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
