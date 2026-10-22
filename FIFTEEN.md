# 15-Minute 1¢ Study

*Updated Thu Oct 22, 2:34 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2392 finished bets | 1% | $79.55 | +29% | +3.33¢ | $38.25 / $41.30 |

*Expect about **97 buys a day** (~$14.60/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2209 | $48.90 | +20% |
| Volatility model ≥ 2%, hold to the close | 4404 | $6.30 | +1% |
| Momentum model ≥ 2%, hold to the close | 3692 | -$29.00 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 28628 | 28620 | 109 (0%) | 1.07% | -$1,964.80 (-56%) | Hold to the close: -$1,964.80 (-56%) |

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
| Volatility model | 18288 | 4.7% | 0.4% (79) | -638% | ❌ Worse |
| Momentum model | 18288 | 4.6% | 0.4% (79) | -663% | ❌ Worse |
| Mean-reversion model | 18288 | 7.9% | 0.4% (79) | -768% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 18288 | 79 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4404 | 39 | +1% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2392 | 25 | +29% | -73% | -72% | -69% |
| Volatility model ≥ 10% | 1361 | 16 | +65% | -63% | -61% | -59% |
| Momentum model ≥ 2% | 3692 | 29 | -7% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2209 | 21 | +20% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1452 | 14 | +32% | -69% | -68% | -64% |
| Mean-reversion model ≥ 2% | 7313 | 52 | -22% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 5110 | 43 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 3399 | 30 | +0% | -78% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 18487 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 6883 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 3250 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 28620 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 109 | 0% | -$1,964.80 | -56% | — |
| Sell at 2¢ | 1049 | 4% | -$3,078.06 | -88% | 47 sec |
| Sell at 3¢ | 717 | 3% | -$3,071.17 | -88% | 48 sec |
| Sell at 5¢ | 505 | 2% | -$3,022.55 | -87% | 61 sec |
| Sell at 10¢ | 311 | 1% | -$2,915.39 | -84% | 64 sec |
| Sell at 25¢ | 172 | 1% | -$2,683.48 | -77% | 82 sec |
| Sell at 50¢ | 113 | 0% | -$2,420.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1200 | 7 | 11% | 4% | -44% | -81% | -83% |
| 2–5 min | 9219 | 52 | 7% | 3% | -44% | -87% | -87% |
| 1–2 min | 7271 | 27 | 3% | 1% | -60% | -93% | -93% |
| Under 1 min | 10926 | 23 | 1% | 0% | -70% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2072 | 12 | 5% | 2% | -28% | -89% | -89% |
| BNB | 2067 | 12 | 5% | 3% | -28% | -83% | -82% |
| HYPE | 2064 | 8 | 5% | 3% | -52% | -88% | -87% |
| ETH | 2054 | 10 | 6% | 3% | -41% | -86% | -85% |
| SOL | 2054 | 3 | 3% | 2% | -82% | -92% | -92% |
| DOGE | 2050 | 4 | 4% | 2% | -76% | -90% | -90% |
| XRP | 2045 | 8 | 3% | 1% | -52% | -88% | -88% |
| NEAR | 2041 | 12 | 6% | 3% | -24% | -80% | -80% |
| BTC | 2040 | 12 | 5% | 2% | -21% | -88% | -90% |
| GOLD | 1124 | 3 | 4% | 1% | -68% | -82% | -84% |
| SILVER | 1088 | 4 | 3% | 1% | -57% | -82% | -83% |
| WTI | 1063 | 3 | 3% | 1% | -67% | -94% | -95% |
| PLATINUM | 944 | 0 | 1% | 0% | -100% | -99% | -98% |
| COPPER | 937 | 3 | 1% | 1% | -70% | -78% | -77% |
| EURUSD | 875 | 3 | 2% | 1% | -68% | -85% | -85% |
| NATGAS | 870 | 5 | 2% | 1% | -46% | -86% | -85% |
| PALLADIUM | 846 | 2 | 1% | 0% | -78% | -87% | -87% |
| GBPUSD | 819 | 1 | 2% | 1% | -89% | -97% | -97% |
| USDJPY | 793 | 4 | 1% | 1% | -53% | -99% | -98% |
| AUDUSD | 374 | 0 | 0% | 0% | -100% | -100% | -99% |
| USDCAD | 329 | 0 | 1% | 0% | -100% | -99% | -99% |
| 10YRRATE | 19 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| 30YRRATE | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 11 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 9 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 14458 | 58 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 14162 | 51 | 3% | 1% | -59% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3063 | 15 | 2% | 1% | -18% | -79% | -78% |
| 0.05–0.1% | 3174 | 11 | 3% | 2% | -49% | -92% | -91% |
| 0.1–0.2% | 4731 | 17 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 5420 | 28 | 6% | 3% | -43% | -87% | -87% |
| Over 0.5% | 2095 | 10 | 7% | 3% | -51% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7128 | 30 | 4% | 2% | -52% | -86% | -85% |
| Morning (6am–12pm) | 7002 | 33 | 4% | 2% | -46% | -88% | -87% |
| Afternoon (12–6pm) | 6748 | 21 | 4% | 2% | -63% | -89% | -89% |
| Evening (6pm–12am) | 7742 | 25 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/22 2:29:55 PM | COPPER | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:29:55 PM | GOLD | UP | 5 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:29:39 PM | XRP | UP | 21 sec | -0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:29:39 PM | ZEC | UP | 21 sec | -0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:29:23 PM | SILVER | DOWN | 37 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:29:23 PM | DOGE | UP | 37 sec | -0.055% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:29:23 PM | SOL | UP | 37 sec | -0.100% | 0¢ | ❌ Lost | $0.00 |
| 10/22 2:28:53 PM | AUDUSD | DOWN | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:28:37 PM | EURUSD | DOWN | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:28:37 PM | HYPE | DOWN | 82 sec | +0.207% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:28:21 PM | USDJPY | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:28:21 PM | WTI | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:27:48 PM | NEAR | UP | 2.2 min | -0.444% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:27:48 PM | 30YRRATE | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:27:48 PM | ETH | UP | 2.2 min | -0.123% | 7¢ | ❌ Lost | -$0.15 |
| 10/22 2:27:48 PM | GBPUSD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:27:01 PM | BNB | UP | 3.0 min | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:26:30 PM | 2YRRATE | UP | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:26:30 PM | BTC | UP | 3.5 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:24:54 PM | 10YRRATE | UP | 5.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:24:54 PM | 5YRRATE | UP | 5.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:48 PM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:48 PM | ZEC | UP | 11 sec | -0.066% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:32 PM | HYPE | UP | 27 sec | -0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:32 PM | DOGE | UP | 27 sec | -0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:32 PM | ETH | DOWN | 27 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:10 PM | WTI | UP | 49 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/22 2:14:10 PM | BNB | UP | 49 sec | -0.093% | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:13:54 PM | AUDUSD | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/22 2:13:21 PM | XRP | UP | 1.6 min | -0.238% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
