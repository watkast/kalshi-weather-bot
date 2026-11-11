# 15-Minute 1¢ Study

*Updated Tue Nov 10, 11:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4196 finished bets | 1% | $177.95 | +38% | +4.24¢ | $86.95 / $91.00 |

*Expect about **95 buys a day** (~$14.31/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3917 | $93.80 | +22% |
| Volatility model ≥ 2%, hold to the close | 7691 | $54.20 | +6% |
| Momentum model ≥ 2%, hold to the close | 6379 | -$18.90 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53137 | 53115 | 203 (0%) | 1.07% | -$3,634.55 (-56%) | Hold to the close: -$3,634.55 (-56%) |

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
| Volatility model | 32039 | 4.7% | 0.4% (130) | -675% | ❌ Worse |
| Momentum model | 32039 | 4.6% | 0.4% (130) | -700% | ❌ Worse |
| Mean-reversion model | 32039 | 8.1% | 0.4% (130) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32039 | 130 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7691 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4196 | 46 | +38% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2420 | 28 | +66% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6379 | 51 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3917 | 37 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2571 | 25 | +37% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13264 | 92 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9291 | 78 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6210 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32244 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12660 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8211 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53115 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 203 | 0% | -$3,634.55 | -56% | — |
| Sell at 2¢ | 2119 | 4% | -$5,645.61 | -87% | 47 sec |
| Sell at 3¢ | 1442 | 3% | -$5,634.17 | -87% | 48 sec |
| Sell at 5¢ | 1002 | 2% | -$5,517.25 | -85% | 63 sec |
| Sell at 10¢ | 605 | 1% | -$5,292.00 | -82% | 65 sec |
| Sell at 25¢ | 320 | 1% | -$4,913.35 | -76% | 83 sec |
| Sell at 50¢ | 211 | 0% | -$4,450.30 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2655 | 13 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 17202 | 94 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 13380 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19866 | 52 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3610 | 16 | 5% | 2% | -42% | -88% | -88% |
| SOL | 3605 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3598 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3591 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3587 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3580 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3562 | 17 | 5% | 2% | -35% | -87% | -88% |
| NEAR | 3561 | 17 | 5% | 2% | -38% | -85% | -85% |
| XRP | 3550 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1911 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1891 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1864 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1691 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1629 | 5 | 3% | 1% | -71% | -90% | -89% |
| COPPER | 1584 | 6 | 2% | 1% | -65% | -73% | -73% |
| NATGAS | 1551 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1547 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1529 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1519 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1092 | 6 | 2% | 1% | -49% | -88% | -88% |
| USDCAD | 1057 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 649 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26896 | 107 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26219 | 96 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5145 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5483 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8281 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9657 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3670 | 17 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14514 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,876 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 11:11:49 PM | DOGE | UP | 3.2 min | -0.252% | — | In play | — |
| 11/10 11:11:01 PM | SOL | UP | 4.0 min | -0.304% | — | In play | — |
| 11/10 11:10:30 PM | NEAR | UP | 4.5 min | -0.698% | — | In play | — |
| 11/10 11:09:42 PM | HYPE | UP | 5.3 min | -0.470% | — | In play | — |
| 11/10 11:09:27 PM | ZEC | UP | 5.5 min | -0.990% | — | In play | — |
| 11/10 10:59:53 PM | PALLADIUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:53 PM | GOLD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:53 PM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:21 PM | AUDUSD | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:21 PM | SILVER | DOWN | 38 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:05 PM | ZEC | DOWN | 55 sec | +0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:59:05 PM | HYPE | DOWN | 55 sec | +0.118% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:58:48 PM | COPPER | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:32 PM | USDCAD | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:32 PM | USDJPY | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:01 PM | BTC | DOWN | 2.0 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:58:01 PM | NEAR | DOWN | 2.0 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:57:46 PM | DOGE | DOWN | 2.2 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:57:14 PM | ETH | DOWN | 2.8 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:57:14 PM | BNB | DOWN | 2.8 min | +0.092% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 10:57:14 PM | SOL | DOWN | 2.8 min | +0.214% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:56:11 PM | XRP | DOWN | 3.8 min | +0.245% | 2¢ | ❌ Lost | -$0.15 |
| 11/10 10:44:54 PM | BNB | UP | 6 sec | -0.049% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:44:54 PM | COPPER | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:44:39 PM | NATGAS | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:44:23 PM | GOLD | DOWN | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:44:23 PM | USDJPY | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 10:44:07 PM | ETH | DOWN | 53 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:44:07 PM | BTC | DOWN | 53 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/10 10:44:07 PM | WTI | DOWN | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
