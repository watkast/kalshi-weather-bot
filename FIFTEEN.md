# 15-Minute 1¢ Study

*Updated Mon Nov 9, 1:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4104 finished bets | 1% | $187.55 | +41% | +4.57¢ | $91.90 / $95.65 |

*Expect about **96 buys a day** (~$14.45/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3811 | $105.20 | +25% |
| Volatility model ≥ 2%, hold to the close | 7511 | $75.65 | +8% |
| Momentum model ≥ 2%, hold to the close | 6209 | $0.60 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51135 | 51118 | 189 (0%) | 1.07% | -$3,576.30 (-57%) | Hold to the close: -$3,576.30 (-57%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 31134 | 4.8% | 0.4% (124) | -685% | ❌ Worse |
| Momentum model | 31134 | 4.6% | 0.4% (124) | -711% | ❌ Worse |
| Mean-reversion model | 31134 | 8.1% | 0.4% (124) | -828% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31134 | 124 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7511 | 70 | +8% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4104 | 46 | +41% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2361 | 28 | +70% | -61% | -60% | -56% |
| Momentum model ≥ 2% | 6209 | 51 | +0% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3811 | 37 | +25% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2498 | 25 | +41% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12870 | 90 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9024 | 77 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6031 | 56 | +6% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31339 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12073 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7706 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51118 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 189 | 0% | -$3,576.30 | -57% | — |
| Sell at 2¢ | 2023 | 4% | -$5,416.32 | -87% | 47 sec |
| Sell at 3¢ | 1376 | 3% | -$5,405.66 | -87% | 48 sec |
| Sell at 5¢ | 961 | 2% | -$5,289.65 | -85% | 62 sec |
| Sell at 10¢ | 580 | 1% | -$5,070.50 | -81% | 65 sec |
| Sell at 25¢ | 301 | 1% | -$4,721.99 | -76% | 83 sec |
| Sell at 50¢ | 194 | 0% | -$4,310.80 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2531 | 12 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 16507 | 88 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12930 | 43 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19138 | 46 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3512 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3505 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3496 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3490 | 19 | 5% | 2% | -31% | -86% | -85% |
| DOGE | 3487 | 7 | 4% | 2% | -75% | -90% | -89% |
| ETH | 3481 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3460 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3459 | 16 | 5% | 2% | -36% | -87% | -89% |
| XRP | 3449 | 13 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1837 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1807 | 6 | 4% | 1% | -60% | -92% | -92% |
| SILVER | 1786 | 8 | 5% | 2% | -47% | -82% | -82% |
| PLATINUM | 1619 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1550 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1516 | 6 | 2% | 1% | -63% | -72% | -72% |
| NATGAS | 1476 | 8 | 2% | 1% | -49% | -77% | -77% |
| GBPUSD | 1471 | 4 | 2% | 1% | -75% | -96% | -96% |
| PALLADIUM | 1455 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1454 | 5 | 2% | 1% | -68% | -97% | -96% |
| AUDUSD | 1013 | 5 | 2% | 1% | -54% | -87% | -87% |
| USDCAD | 979 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 577 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 328 | 1 | 4% | 2% | -72% | -64% | -62% |
| 2YRRATE | 310 | 3 | 4% | 2% | -10% | -33% | -31% |
| 30YRRATE | 305 | 0 | 2% | 1% | -100% | -97% | -95% |
| 5YRRATE | 286 | 1 | 4% | 1% | -67% | -93% | -95% |
| INX | 10 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25912 | 98 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 25206 | 91 | 4% | 2% | -59% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5058 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5353 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8059 | 27 | 5% | 2% | -58% | -89% | -89% |
| 0.2–0.5% | 9347 | 40 | 6% | 3% | -52% | -87% | -86% |
| Over 0.5% | 3514 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12671 | 43 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12220 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13802 | 43 | 4% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,908 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/9 1:44:52 PM | HYPE | UP | 8 sec | -0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:44:37 PM | XRP | DOWN | 23 sec | +0.064% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:37 PM | 5YRRATE | DOWN | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:04 PM | 2YRRATE | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:44:04 PM | NEAR | UP | 55 sec | -0.333% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:48 PM | BTC | UP | 71 sec | -0.099% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:48 PM | SILVER | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:48 PM | DOGE | UP | 71 sec | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:48 PM | INX | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | SOL | UP | 88 sec | -0.350% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:31 PM | PALLADIUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | PLATINUM | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | GOLD | UP | 88 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:31 PM | COPPER | UP | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | WTI | DOWN | 88 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:31 PM | ZEC | UP | 88 sec | -0.835% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:31 PM | BNB | UP | 88 sec | -0.154% | 0¢ | ❌ Lost | -$0.15 |
| 11/9 1:43:31 PM | ETH | UP | 88 sec | -0.209% | 0¢ | ❌ Lost | $0.00 |
| 11/9 1:43:31 PM | BRENT | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:27 AM | XRP | UP | 32 sec | -0.264% | 0¢ | ❌ Lost | $0.00 |
| 11/9 8:14:27 AM | PLATINUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:27 AM | HYPE | UP | 32 sec | -0.200% | 1¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:27 AM | 30YRRATE | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:27 AM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:09 AM | WTI | DOWN | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/9 8:14:09 AM | BRENT | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:09 AM | 2YRRATE | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:09 AM | PALLADIUM | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/9 8:14:09 AM | SOL | DOWN | 50 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
