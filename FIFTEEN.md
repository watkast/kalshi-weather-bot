# 15-Minute 1¢ Study

*Updated Sat Nov 7, 5:00 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3872 finished bets | 1% | $116.25 | +27% | +3.00¢ | $77.40 / $38.85 |

*Expect about **96 buys a day** (~$14.44/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3606 | $44.45 | +11% |
| Volatility model ≥ 2%, hold to the close | 7134 | $9.70 | +1% |
| Momentum model ≥ 2%, hold to the close | 5891 | -$60.50 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48765 | 48743 | 175 (0%) | 1.07% | -$3,488.50 (-59%) | Hold to the close: -$3,488.50 (-59%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 29500 | 4.8% | 0.4% (111) | -714% | ❌ Worse |
| Momentum model | 29500 | 4.6% | 0.4% (111) | -741% | ❌ Worse |
| Mean-reversion model | 29500 | 8.1% | 0.4% (111) | -865% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29500 | 111 | -52% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7134 | 62 | +1% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 3872 | 39 | +27% | -77% | -76% | -72% |
| Volatility model ≥ 10% | 2227 | 24 | +55% | -72% | -71% | -67% |
| Momentum model ≥ 2% | 5891 | 44 | -9% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3606 | 31 | +11% | -80% | -79% | -76% |
| Momentum model ≥ 10% | 2364 | 20 | +19% | -76% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12208 | 80 | -28% | -84% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8558 | 69 | -10% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5721 | 49 | -2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29705 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48743 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,488.50 | -59% | — |
| Sell at 2¢ | 1913 | 4% | -$5,189.12 | -87% | 47 sec |
| Sell at 3¢ | 1299 | 3% | -$5,179.89 | -87% | 48 sec |
| Sell at 5¢ | 901 | 2% | -$5,072.85 | -85% | 63 sec |
| Sell at 10¢ | 542 | 1% | -$4,864.48 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,529.08 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,149.50 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2402 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15673 | 83 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12284 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18372 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3330 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3323 | 12 | 4% | 2% | -54% | -90% | -90% |
| HYPE | 3312 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3311 | 17 | 5% | 2% | -35% | -85% | -84% |
| DOGE | 3302 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3301 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3279 | 16 | 5% | 2% | -37% | -84% | -85% |
| BTC | 3276 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3271 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24714 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24029 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4795 | 22 | 2% | 1% | -19% | -83% | -83% |
| 0.05–0.1% | 5047 | 18 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7642 | 26 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8862 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3351 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11933 | 41 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13167 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,707 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/7 4:59:16 AM | SOL | UP | 43 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:58:58 AM | BTC | UP | 62 sec | -0.043% | 1¢ | In play | — |
| 11/7 4:58:58 AM | XRP | DOWN | 62 sec | +0.060% | 0¢ | In play | — |
| 11/7 4:58:26 AM | BNB | DOWN | 1.6 min | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 4:58:26 AM | ETH | UP | 1.6 min | -0.041% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:57:21 AM | DOGE | UP | 2.6 min | -0.117% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 4:56:32 AM | NEAR | UP | 3.5 min | -0.385% | 1¢ | In play | — |
| 11/7 4:56:01 AM | ZEC | UP | 4.0 min | -0.564% | 1¢ | In play | — |
| 11/7 4:55:27 AM | HYPE | UP | 4.5 min | -0.378% | 1¢ | In play | — |
| 11/7 4:44:43 AM | BNB | UP | 17 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:44:27 AM | HYPE | DOWN | 33 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 4:44:12 AM | ZEC | DOWN | 48 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:43:54 AM | ETH | DOWN | 66 sec | +0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:43:38 AM | XRP | UP | 82 sec | -0.102% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:42:02 AM | BTC | DOWN | 3.0 min | +0.078% | 3¢ | ❌ Lost | -$0.15 |
| 11/7 4:41:13 AM | DOGE | DOWN | 3.8 min | +0.145% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:41:13 AM | SOL | DOWN | 3.8 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:40:57 AM | NEAR | DOWN | 4.0 min | +0.357% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:29:47 AM | SOL | UP | 12 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:29:21 AM | BTC | UP | 39 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:29:21 AM | NEAR | DOWN | 39 sec | +0.008% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 4:29:21 AM | ZEC | UP | 39 sec | -0.106% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 4:28:47 AM | HYPE | DOWN | 73 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:28:00 AM | ETH | UP | 2.0 min | -0.055% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:28:00 AM | XRP | DOWN | 2.0 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:26:55 AM | BNB | UP | 3.1 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 4:14:45 AM | BTC | UP | 14 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:14:29 AM | ETH | UP | 30 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:14:29 AM | XRP | UP | 30 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/7 4:13:58 AM | NEAR | UP | 62 sec | -0.211% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
