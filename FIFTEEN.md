# 15-Minute 1¢ Study

*Updated Mon Oct 26, 12:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2717 finished bets | 1% | $83.60 | +27% | +3.08¢ | $33.05 / $50.55 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2523 | $57.00 | +20% |
| Volatility model ≥ 2%, hold to the close | 5035 | -$14.80 | -2% |
| Momentum model ≥ 2%, hold to the close | 4198 | -$30.15 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32296 | 32288 | 120 (0%) | 1.07% | -$2,242.50 (-57%) | Hold to the close: -$2,242.50 (-57%) |

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
| Volatility model | 20809 | 4.6% | 0.4% (85) | -657% | ❌ Worse |
| Momentum model | 20809 | 4.5% | 0.4% (85) | -682% | ❌ Worse |
| Mean-reversion model | 20809 | 7.9% | 0.4% (85) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20809 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5035 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2717 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1537 | 18 | +64% | -66% | -65% | -62% |
| Momentum model ≥ 2% | 4198 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2523 | 24 | +20% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1644 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8391 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5878 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3913 | 33 | -5% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 21009 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7507 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3772 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32288 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,242.50 | -57% | — |
| Sell at 2¢ | 1202 | 4% | -$3,441.98 | -88% | 47 sec |
| Sell at 3¢ | 824 | 3% | -$3,433.14 | -88% | 48 sec |
| Sell at 5¢ | 573 | 2% | -$3,382.05 | -86% | 61 sec |
| Sell at 10¢ | 354 | 1% | -$3,248.76 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$3,010.29 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,735.00 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1415 | 7 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 10345 | 55 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 8171 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12353 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2354 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2347 | 8 | 5% | 3% | -58% | -89% | -87% |
| BNB | 2344 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2340 | 6 | 3% | 1% | -68% | -92% | -92% |
| ETH | 2334 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2327 | 4 | 4% | 2% | -79% | -91% | -90% |
| NEAR | 2324 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2324 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2315 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1216 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1181 | 5 | 4% | 2% | -51% | -82% | -82% |
| WTI | 1159 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1029 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1006 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 961 | 3 | 2% | 1% | -71% | -87% | -87% |
| NATGAS | 954 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 917 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 907 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 891 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 450 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 411 | 0 | 1% | 0% | -100% | -97% | -99% |
| BRENT | 45 | 0 | 0% | 0% | -100% | -100% | -100% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16356 | 66 | 4% | 2% | -54% | -87% | -87% |
| DOWN (bought NO) | 15932 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3507 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3612 | 11 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 5427 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6131 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2328 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7926 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8974 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,819 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/26 12:14:59 AM | COPPER | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:27 AM | BRENT | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:11 AM | NATGAS | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:14:11 AM | PALLADIUM | UP | 49 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:38 AM | WTI | DOWN | 82 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:38 AM | USDJPY | DOWN | 82 sec | — | 5¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:38 AM | PLATINUM | UP | 82 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:13:22 AM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:12:47 AM | USDCAD | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:12:47 AM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:12:31 AM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:12:00 AM | GBPUSD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:11:27 AM | HYPE | UP | 3.5 min | -0.572% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:11:11 AM | BTC | UP | 3.8 min | -0.213% | 2¢ | ❌ Lost | -$0.15 |
| 10/26 12:10:55 AM | BNB | UP | 4.1 min | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:10:22 AM | SILVER | UP | 4.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:09:50 AM | XRP | UP | 5.2 min | -0.357% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:09:31 AM | NEAR | UP | 5.5 min | -0.938% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:09:31 AM | SOL | UP | 5.5 min | -0.336% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:09:01 AM | DOGE | UP | 6.0 min | -0.408% | 1¢ | ❌ Lost | -$0.15 |
| 10/26 12:09:01 AM | ZEC | UP | 6.0 min | -0.882% | 0¢ | ❌ Lost | -$0.15 |
| 10/26 12:09:01 AM | ETH | UP | 6.0 min | -0.349% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:50 PM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:50 PM | SILVER | DOWN | 10 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:59:50 PM | SOL | DOWN | 10 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:59:50 PM | EURUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:34 PM | GOLD | DOWN | 26 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:59:34 PM | USDCAD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:59:19 PM | BTC | DOWN | 40 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:59:19 PM | NEAR | UP | 40 sec | -0.113% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
