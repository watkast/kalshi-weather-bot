# 15-Minute 1¢ Study

*Updated Sun Nov 8, 5:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4039 finished bets | 1% | $194.60 | +43% | +4.82¢ | $95.80 / $98.80 |

*Expect about **97 buys a day** (~$14.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3747 | $112.10 | +28% |
| Volatility model ≥ 2%, hold to the close | 7395 | $75.60 | +8% |
| Momentum model ≥ 2%, hold to the close | 6104 | $12.60 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49942 | 49924 | 184 (0%) | 1.07% | -$3,493.75 (-58%) | Hold to the close: -$3,493.75 (-58%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30616 | 4.8% | 0.4% (120) | -693% | ❌ Worse |
| Momentum model | 30616 | 4.6% | 0.4% (120) | -718% | ❌ Worse |
| Mean-reversion model | 30616 | 8.1% | 0.4% (120) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30616 | 120 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7395 | 69 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4039 | 46 | +43% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2327 | 28 | +72% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6104 | 51 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3747 | 37 | +28% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2456 | 25 | +43% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12652 | 88 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8874 | 76 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5938 | 55 | +6% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30821 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11705 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7398 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49924 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 184 | 0% | -$3,493.75 | -58% | — |
| Sell at 2¢ | 1957 | 4% | -$5,280.93 | -87% | 47 sec |
| Sell at 3¢ | 1331 | 3% | -$5,270.66 | -87% | 48 sec |
| Sell at 5¢ | 926 | 2% | -$5,159.85 | -85% | 63 sec |
| Sell at 10¢ | 559 | 1% | -$4,945.46 | -81% | 65 sec |
| Sell at 25¢ | 293 | 1% | -$4,595.92 | -76% | 83 sec |
| Sell at 50¢ | 188 | 0% | -$4,198.75 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2478 | 11 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 16088 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12610 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18736 | 45 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3456 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3448 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3439 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3432 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3430 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3423 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3404 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3400 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3389 | 12 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 1788 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1755 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1738 | 8 | 5% | 2% | -46% | -82% | -81% |
| PLATINUM | 1571 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1508 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1476 | 6 | 2% | 1% | -62% | -72% | -72% |
| NATGAS | 1437 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1433 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1413 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1412 | 3 | 1% | 0% | -80% | -91% | -92% |
| AUDUSD | 966 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 934 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 528 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25327 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24597 | 89 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5032 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5297 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7949 | 27 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 9102 | 38 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3433 | 13 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12159 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,943 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 5:38:12 PM | GOLD | DOWN | 6.8 min | — | — | In play | — |
| 11/8 5:29:59 PM | PLATINUM | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:29:59 PM | NATGAS | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:29:59 PM | GOLD | UP | 0 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:29:59 PM | COPPER | UP | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:29:43 PM | USDJPY | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:29:43 PM | EURUSD | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:29:27 PM | SOL | DOWN | 32 sec | +0.190% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:29:12 PM | DOGE | DOWN | 47 sec | +0.164% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:29:12 PM | WTI | DOWN | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:29:12 PM | XRP | DOWN | 47 sec | +0.189% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:29:12 PM | BRENT | DOWN | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:56 PM | BNB | DOWN | 63 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:28:56 PM | ZEC | UP | 63 sec | -0.408% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:40 PM | AUDUSD | DOWN | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:40 PM | ETH | DOWN | 79 sec | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:17 PM | HYPE | UP | 1.7 min | -0.516% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:17 PM | BTC | DOWN | 1.7 min | +0.221% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:27:59 PM | SILVER | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:27:43 PM | NEAR | UP | 2.3 min | -0.841% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:14:46 PM | BTC | UP | 14 sec | +0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:14:30 PM | XRP | DOWN | 30 sec | +0.144% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:14:30 PM | USDCAD | DOWN | 30 sec | — | 9¢ | ❌ Lost | -$0.15 |
| 11/8 5:14:30 PM | AUDUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:14:15 PM | USDJPY | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:13:57 PM | BRENT | UP | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:13:57 PM | EURUSD | DOWN | 63 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:13:41 PM | WTI | UP | 79 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:13:25 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:13:25 PM | DOGE | DOWN | 1.6 min | +0.340% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
