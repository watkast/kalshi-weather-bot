# 15-Minute 1¢ Study

*Updated Sun Nov 8, 5:07 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4035 finished bets | 1% | $194.90 | +43% | +4.83¢ | $96.10 / $98.80 |

*Expect about **97 buys a day** (~$14.51/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3745 | $112.10 | +28% |
| Volatility model ≥ 2%, hold to the close | 7390 | $76.05 | +9% |
| Momentum model ≥ 2%, hold to the close | 6102 | $12.60 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49903 | 49884 | 184 (0%) | 1.07% | -$3,488.95 (-58%) | Hold to the close: -$3,488.95 (-58%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30598 | 4.8% | 0.4% (120) | -693% | ❌ Worse |
| Momentum model | 30598 | 4.6% | 0.4% (120) | -717% | ❌ Worse |
| Mean-reversion model | 30598 | 8.1% | 0.4% (120) | -838% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30598 | 120 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7390 | 69 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4035 | 46 | +43% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2325 | 28 | +72% | -61% | -59% | -55% |
| Momentum model ≥ 2% | 6102 | 51 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3745 | 37 | +28% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2454 | 25 | +43% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12639 | 88 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8862 | 76 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5930 | 55 | +6% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30803 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11691 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7390 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49884 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 184 | 0% | -$3,488.95 | -58% | — |
| Sell at 2¢ | 1956 | 4% | -$5,276.39 | -87% | 47 sec |
| Sell at 3¢ | 1330 | 3% | -$5,266.25 | -87% | 48 sec |
| Sell at 5¢ | 925 | 2% | -$5,155.70 | -85% | 63 sec |
| Sell at 10¢ | 559 | 1% | -$4,940.66 | -81% | 65 sec |
| Sell at 25¢ | 293 | 1% | -$4,591.12 | -76% | 83 sec |
| Sell at 50¢ | 188 | 0% | -$4,193.95 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2475 | 11 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 16082 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12595 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18720 | 45 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3454 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3446 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3437 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3430 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3428 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3421 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3402 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3398 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3387 | 12 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 1786 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1753 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1736 | 8 | 5% | 2% | -46% | -82% | -81% |
| PLATINUM | 1569 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1506 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1474 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1436 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1432 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1411 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1411 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 964 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 933 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 526 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25313 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24571 | 89 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5031 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5296 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7944 | 27 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 9096 | 38 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3428 | 13 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12119 | 47 | 4% | 2% | -55% | -86% | -86% |
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
| 11/8 5:07:26 PM | GOLD | DOWN | 7.5 min | — | — | In play | — |
| 11/8 5:06:38 PM | PLATINUM | DOWN | 8.4 min | — | — | In play | — |
| 11/8 4:59:36 PM | USDCAD | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:59:21 PM | NATGAS | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:59:21 PM | EURUSD | UP | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:58:49 PM | PALLADIUM | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:57:46 PM | COPPER | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:57:46 PM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:57:19 PM | USDJPY | UP | 2.7 min | — | 6¢ | ❌ Lost | -$0.15 |
| 11/8 4:56:46 PM | ZEC | UP | 3.2 min | -0.868% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:56:46 PM | NEAR | UP | 3.2 min | -0.886% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:56:13 PM | XRP | UP | 3.8 min | -0.564% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:56:13 PM | PLATINUM | UP | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:55 PM | SOL | UP | 4.1 min | -0.667% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:55 PM | DOGE | UP | 4.1 min | -0.654% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:39 PM | HYPE | UP | 4.3 min | -0.684% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:39 PM | ETH | UP | 4.3 min | -0.625% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:39 PM | BNB | UP | 4.3 min | -0.421% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:39 PM | GOLD | UP | 4.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:08 PM | BTC | UP | 4.9 min | -0.416% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:55:08 PM | SILVER | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:44:30 PM | BRENT | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:44:30 PM | SILVER | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:44:16 PM | PALLADIUM | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:43:59 PM | EURUSD | DOWN | 60 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:43:59 PM | AUDUSD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:43:27 PM | GBPUSD | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:43:27 PM | COPPER | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:42:36 PM | USDJPY | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:42:05 PM | BNB | UP | 2.9 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
