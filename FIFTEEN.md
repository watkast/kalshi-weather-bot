# 15-Minute 1¢ Study

*Updated Wed Nov 4, 12:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3623 finished bets | 1% | $113.60 | +28% | +3.14¢ | $78.85 / $34.75 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3357 | $41.35 | +11% |
| Volatility model ≥ 2%, hold to the close | 6710 | $28.65 | +4% |
| Momentum model ≥ 2%, hold to the close | 5530 | -$50.40 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 44948 | 44921 | 167 (0%) | 1.07% | -$3,132.95 (-57%) | Hold to the close: -$3,132.95 (-57%) |

*In play or awaiting result: 26. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 27557 | 4.7% | 0.4% (108) | -677% | ❌ Worse |
| Momentum model | 27557 | 4.6% | 0.4% (108) | -703% | ❌ Worse |
| Mean-reversion model | 27557 | 8.1% | 0.4% (108) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 27557 | 108 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6710 | 60 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3623 | 37 | +28% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2056 | 22 | +53% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5530 | 42 | -8% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3357 | 29 | +11% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2189 | 19 | +22% | -74% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11408 | 78 | -25% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 8013 | 67 | -7% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 5363 | 47 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 27762 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 10662 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6497 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 44921 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 167 | 0% | -$3,132.95 | -57% | — |
| Sell at 2¢ | 1766 | 4% | -$4,759.79 | -87% | 47 sec |
| Sell at 3¢ | 1211 | 3% | -$4,746.66 | -87% | 49 sec |
| Sell at 5¢ | 838 | 2% | -$4,646.25 | -85% | 63 sec |
| Sell at 10¢ | 506 | 1% | -$4,444.09 | -81% | 66 sec |
| Sell at 25¢ | 266 | 1% | -$4,114.49 | -75% | 83 sec |
| Sell at 50¢ | 170 | 0% | -$3,749.45 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2200 | 10 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 14444 | 79 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 11340 | 39 | 3% | 1% | -62% | -92% | -92% |
| Under 1 min | 16926 | 39 | 1% | 0% | -67% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3110 | 13 | 5% | 3% | -46% | -88% | -88% |
| SOL | 3104 | 12 | 4% | 2% | -51% | -90% | -90% |
| BNB | 3097 | 17 | 5% | 2% | -31% | -85% | -84% |
| HYPE | 3096 | 9 | 5% | 2% | -64% | -89% | -87% |
| DOGE | 3084 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3079 | 12 | 7% | 3% | -52% | -85% | -85% |
| NEAR | 3067 | 15 | 5% | 2% | -37% | -84% | -84% |
| BTC | 3067 | 14 | 5% | 2% | -38% | -88% | -89% |
| XRP | 3058 | 12 | 3% | 1% | -51% | -89% | -89% |
| GOLD | 1652 | 5 | 5% | 2% | -63% | -81% | -83% |
| WTI | 1608 | 5 | 3% | 1% | -62% | -92% | -93% |
| SILVER | 1608 | 7 | 5% | 2% | -48% | -82% | -82% |
| PLATINUM | 1439 | 4 | 2% | 1% | -74% | -96% | -96% |
| EURUSD | 1380 | 3 | 3% | 1% | -80% | -89% | -89% |
| COPPER | 1360 | 6 | 2% | 1% | -59% | -70% | -69% |
| NATGAS | 1308 | 8 | 2% | 1% | -43% | -75% | -74% |
| GBPUSD | 1307 | 3 | 2% | 1% | -79% | -96% | -96% |
| USDJPY | 1290 | 5 | 2% | 1% | -64% | -97% | -97% |
| PALLADIUM | 1288 | 3 | 1% | 1% | -78% | -91% | -91% |
| AUDUSD | 838 | 4 | 2% | 1% | -55% | -86% | -85% |
| USDCAD | 805 | 0 | 2% | 0% | -100% | -97% | -98% |
| BRENT | 399 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 240 | 1 | 5% | 2% | -61% | -52% | -50% |
| 30YRRATE | 223 | 0 | 1% | 0% | -100% | -98% | -97% |
| 2YRRATE | 215 | 2 | 4% | 0% | -13% | -7% | -6% |
| 5YRRATE | 199 | 1 | 5% | 2% | -53% | -91% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 22811 | 89 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 22110 | 78 | 4% | 2% | -60% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4489 | 21 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4732 | 18 | 3% | 2% | -42% | -91% | -90% |
| 0.1–0.2% | 7187 | 25 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8243 | 33 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3103 | 13 | 7% | 3% | -57% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11066 | 40 | 4% | 2% | -59% | -87% | -87% |
| Morning (6am–12pm) | 11054 | 48 | 4% | 2% | -51% | -85% | -85% |
| Afternoon (12–6pm) | 10598 | 39 | 4% | 2% | -57% | -86% | -86% |
| Evening (6pm–12am) | 12203 | 40 | 3% | 2% | -62% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,723 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 12:29:04 AM | ZEC | DOWN | 55 sec | +0.245% | — | In play | — |
| 11/4 12:28:48 AM | ETH | DOWN | 71 sec | +0.100% | — | In play | — |
| 11/4 12:28:32 AM | PALLADIUM | DOWN | 87 sec | — | — | In play | — |
| 11/4 12:28:16 AM | BRENT | DOWN | 1.7 min | — | — | In play | — |
| 11/4 12:28:00 AM | USDJPY | UP | 2.0 min | — | — | In play | — |
| 11/4 12:27:26 AM | DOGE | DOWN | 2.6 min | +0.177% | — | In play | — |
| 11/4 12:27:26 AM | WTI | DOWN | 2.6 min | — | — | In play | — |
| 11/4 12:27:26 AM | AUDUSD | DOWN | 2.6 min | — | — | In play | — |
| 11/4 12:27:10 AM | SOL | DOWN | 2.8 min | +0.259% | — | In play | — |
| 11/4 12:27:10 AM | BTC | DOWN | 2.8 min | +0.215% | — | In play | — |
| 11/4 12:27:10 AM | XRP | DOWN | 2.8 min | +0.220% | — | In play | — |
| 11/4 12:26:23 AM | HYPE | DOWN | 3.6 min | +0.313% | — | In play | — |
| 11/4 12:26:23 AM | BNB | DOWN | 3.6 min | +0.341% | — | In play | — |
| 11/4 12:26:23 AM | NEAR | DOWN | 3.6 min | +1.058% | — | In play | — |
| 11/4 12:26:07 AM | EURUSD | DOWN | 3.9 min | — | — | In play | — |
| 11/4 12:25:32 AM | GBPUSD | DOWN | 4.5 min | — | — | In play | — |
| 11/4 12:23:42 AM | USDCAD | UP | 6.3 min | — | — | In play | — |
| 11/4 12:14:44 AM | XRP | UP | 16 sec | -0.133% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:14:44 AM | DOGE | DOWN | 16 sec | -0.032% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:14:28 AM | COPPER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:14:13 AM | AUDUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:57 AM | SOL | DOWN | 62 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:13:57 AM | HYPE | DOWN | 62 sec | +0.178% | 0¢ | ❌ Lost | $0.00 |
| 11/4 12:13:57 AM | BNB | DOWN | 62 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:41 AM | BTC | DOWN | 78 sec | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:41 AM | ZEC | DOWN | 78 sec | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:41 AM | WTI | UP | 78 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:25 AM | BRENT | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:25 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 12:13:25 AM | ETH | DOWN | 1.6 min | +0.157% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
