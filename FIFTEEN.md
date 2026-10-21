# 15-Minute 1¢ Study

*Updated Wed Oct 21, 12:08 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2197 finished bets | 1% | $73.45 | +30% | +3.34¢ | $20.60 / $52.85 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2037 | $53.65 | +24% |
| Momentum model ≥ 2%, hold to the close | 3399 | -$37.10 | -9% |
| Volatility model ≥ 5%, sell at 50¢ | 2197 | -$43.55 | -18% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 26159 | 26152 | 95 (0%) | 1.07% | -$1,857.65 (-58%) | Hold to the close: -$1,857.65 (-58%) |

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
| Volatility model | 17000 | 4.6% | 0.4% (67) | -670% | ❌ Worse |
| Momentum model | 17000 | 4.5% | 0.4% (67) | -692% | ❌ Worse |
| Mean-reversion model | 17000 | 7.8% | 0.4% (67) | -809% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 17000 | 67 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4028 | 32 | -9% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2197 | 23 | +30% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 1262 | 15 | +66% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3399 | 26 | -9% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2037 | 20 | +24% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 1340 | 13 | +32% | -68% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6692 | 43 | -30% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4661 | 35 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3087 | 23 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17198 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6209 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2745 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 26152 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 95 | 0% | -$1,857.65 | -58% | — |
| Sell at 2¢ | 951 | 4% | -$2,800.39 | -88% | 46 sec |
| Sell at 3¢ | 647 | 2% | -$2,795.32 | -88% | 48 sec |
| Sell at 5¢ | 458 | 2% | -$2,749.95 | -86% | 56 sec |
| Sell at 10¢ | 278 | 1% | -$2,655.47 | -83% | 64 sec |
| Sell at 25¢ | 150 | 1% | -$2,467.15 | -77% | 80 sec |
| Sell at 50¢ | 97 | 0% | -$2,238.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1050 | 5 | 10% | 4% | -55% | -81% | -84% |
| 2–5 min | 8451 | 42 | 7% | 3% | -51% | -87% | -87% |
| 1–2 min | 6672 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9975 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1932 | 11 | 5% | 2% | -29% | -90% | -90% |
| HYPE | 1921 | 6 | 5% | 3% | -62% | -89% | -87% |
| BNB | 1921 | 9 | 5% | 2% | -43% | -83% | -82% |
| ETH | 1911 | 9 | 6% | 3% | -44% | -87% | -86% |
| DOGE | 1910 | 3 | 4% | 2% | -81% | -91% | -90% |
| SOL | 1909 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1902 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1896 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1896 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1019 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 981 | 4 | 3% | 1% | -53% | -82% | -81% |
| WTI | 957 | 3 | 3% | 1% | -63% | -94% | -95% |
| PLATINUM | 852 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 848 | 3 | 2% | 1% | -67% | -75% | -75% |
| NATGAS | 781 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 778 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 771 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 732 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 689 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 299 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 247 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13171 | 48 | 4% | 2% | -58% | -87% | -87% |
| DOWN (bought NO) | 12981 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2883 | 15 | 2% | 1% | -13% | -77% | -77% |
| 0.05–0.1% | 2986 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4361 | 14 | 5% | 2% | -61% | -89% | -89% |
| 0.2–0.5% | 5022 | 24 | 6% | 3% | -48% | -88% | -87% |
| Over 0.5% | 1943 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7332 | 21 | 3% | 2% | -67% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,782 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 11:59:46 PM | BNB | UP | 13 sec | -0.005% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:46 PM | USDCAD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:14 PM | SOL | UP | 45 sec | -0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:59 PM | BTC | UP | 60 sec | -0.047% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:59 PM | XRP | UP | 60 sec | -0.098% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:59 PM | ETH | UP | 60 sec | -0.074% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:43 PM | PLATINUM | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:43 PM | HYPE | UP | 76 sec | -0.181% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:58:43 PM | NATGAS | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:58:43 PM | ZEC | UP | 76 sec | -0.281% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:58:27 PM | USDJPY | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:57:49 PM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:57:33 PM | DOGE | UP | 2.5 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:57:02 PM | EURUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:57:02 PM | NEAR | UP | 3.0 min | -0.526% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:44:29 PM | NEAR | UP | 31 sec | -0.152% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:44:12 PM | WTI | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:33 PM | XRP | UP | 2.5 min | -0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:33 PM | HYPE | UP | 2.5 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:33 PM | ZEC | UP | 2.5 min | -0.527% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:02 PM | BTC | UP | 3.0 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:02 PM | SOL | UP | 3.0 min | -0.290% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:02 PM | DOGE | UP | 3.0 min | -0.261% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:02 PM | GOLD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:42:02 PM | PALLADIUM | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:41:45 PM | ETH | UP | 3.2 min | -0.256% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:40:57 PM | COPPER | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:40:25 PM | PLATINUM | UP | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:39:06 PM | SILVER | UP | 5.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 11:29:57 PM | DOGE | DOWN | 2 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
