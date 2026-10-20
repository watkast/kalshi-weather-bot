# 15-Minute 1¢ Study

*Updated Tue Oct 20, 9:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2126 finished bets | 1% | $83.05 | +35% | +3.91¢ | $23.45 / $59.60 |

*Expect about **95 buys a day** (~$14.27/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1955 | $64.75 | +30% |
| Momentum model ≥ 2%, hold to the close | 3265 | -$19.55 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 2126 | -$33.95 | -14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25250 | 25227 | 92 (0%) | 1.07% | -$1,780.55 (-58%) | Hold to the close: -$1,780.55 (-58%) |

*In play or awaiting result: 22. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16477 | 4.6% | 0.4% (65) | -672% | ❌ Worse |
| Momentum model | 16477 | 4.5% | 0.4% (65) | -695% | ❌ Worse |
| Mean-reversion model | 16477 | 7.8% | 0.4% (65) | -811% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16477 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3863 | 31 | -8% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2126 | 23 | +35% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1233 | 15 | +71% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3265 | 26 | -5% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 1955 | 20 | +30% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 1293 | 13 | +38% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6450 | 42 | -29% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4490 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2969 | 22 | -16% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16675 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5948 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2604 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25227 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,780.55 | -58% | — |
| Sell at 2¢ | 911 | 4% | -$2,705.69 | -88% | 46 sec |
| Sell at 3¢ | 618 | 2% | -$2,701.53 | -88% | 48 sec |
| Sell at 5¢ | 439 | 2% | -$2,657.20 | -87% | 51 sec |
| Sell at 10¢ | 267 | 1% | -$2,564.78 | -84% | 64 sec |
| Sell at 25¢ | 146 | 1% | -$2,375.29 | -77% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,147.30 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1002 | 5 | 10% | 3% | -52% | -81% | -84% |
| 2–5 min | 8171 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6438 | 24 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9612 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1875 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1863 | 6 | 5% | 3% | -60% | -89% | -88% |
| BNB | 1862 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1853 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1853 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1850 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1843 | 7 | 3% | 1% | -53% | -87% | -88% |
| NEAR | 1839 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1837 | 10 | 5% | 2% | -27% | -88% | -90% |
| GOLD | 976 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 941 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 919 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 816 | 3 | 2% | 1% | -66% | -74% | -74% |
| PLATINUM | 811 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 748 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 747 | 3 | 2% | 1% | -63% | -83% | -83% |
| PALLADIUM | 737 | 2 | 1% | 0% | -75% | -85% | -86% |
| GBPUSD | 704 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 655 | 3 | 1% | 1% | -57% | -99% | -98% |
| AUDUSD | 273 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 225 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12710 | 45 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12517 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2808 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2896 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4220 | 13 | 5% | 2% | -62% | -90% | -89% |
| 0.2–0.5% | 4861 | 23 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1887 | 6 | 7% | 3% | -67% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6008 | 29 | 4% | 2% | -45% | -87% | -87% |
| Afternoon (12–6pm) | 5807 | 19 | 3% | 1% | -61% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,787 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 8:59:56 AM | DOGE | DOWN | 3 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:59:56 AM | PALLADIUM | UP | 3 sec | — | 0¢ | In play | — |
| 10/20 8:59:41 AM | WTI | DOWN | 19 sec | — | 0¢ | In play | — |
| 10/20 8:59:41 AM | COPPER | UP | 19 sec | — | 0¢ | In play | — |
| 10/20 8:59:25 AM | USDJPY | DOWN | 35 sec | — | 0¢ | In play | — |
| 10/20 8:59:25 AM | ZEC | DOWN | 35 sec | +0.163% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:59:25 AM | BTC | DOWN | 35 sec | +0.135% | 0¢ | In play | — |
| 10/20 8:59:25 AM | BNB | DOWN | 35 sec | +0.081% | 0¢ | In play | — |
| 10/20 8:59:09 AM | NEAR | UP | 51 sec | -0.527% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:59:09 AM | EURUSD | UP | 51 sec | — | 0¢ | In play | — |
| 10/20 8:59:09 AM | USDCAD | DOWN | 51 sec | — | 0¢ | In play | — |
| 10/20 8:58:53 AM | PLATINUM | DOWN | 67 sec | — | 0¢ | In play | — |
| 10/20 8:58:38 AM | AUDUSD | UP | 82 sec | — | 0¢ | In play | — |
| 10/20 8:58:22 AM | HYPE | UP | 1.6 min | -0.271% | 1¢ | In play | — |
| 10/20 8:57:50 AM | NATGAS | UP | 2.2 min | — | 0¢ | In play | — |
| 10/20 8:57:50 AM | SOL | DOWN | 2.2 min | +0.363% | 4¢ | ❌ Lost | -$0.15 |
| 10/20 8:57:19 AM | ETH | DOWN | 2.7 min | +0.362% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:57:03 AM | XRP | DOWN | 3.0 min | +0.494% | 1¢ | In play | — |
| 10/20 8:57:03 AM | SILVER | UP | 3.0 min | — | 1¢ | In play | — |
| 10/20 8:56:47 AM | GBPUSD | UP | 3.2 min | — | 0¢ | In play | — |
| 10/20 8:55:12 AM | GOLD | UP | 4.8 min | — | 1¢ | In play | — |
| 10/20 8:44:39 AM | COPPER | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:44:39 AM | SOL | UP | 21 sec | -0.141% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:44:23 AM | ZEC | DOWN | 37 sec | +0.336% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:44:23 AM | USDCAD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:43:51 AM | BNB | DOWN | 69 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/20 8:43:36 AM | GBPUSD | UP | 84 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:43:20 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 8:42:48 AM | ETH | DOWN | 2.2 min | +0.306% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 8:42:48 AM | XRP | DOWN | 2.2 min | +0.338% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
