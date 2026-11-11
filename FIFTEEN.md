# 15-Minute 1¢ Study

*Updated Tue Nov 10, 7:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4187 finished bets | 1% | $179.00 | +38% | +4.28¢ | $87.40 / $91.60 |

*Expect about **96 buys a day** (~$14.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3907 | $95.15 | +23% |
| Volatility model ≥ 2%, hold to the close | 7670 | $56.90 | +6% |
| Momentum model ≥ 2%, hold to the close | 6362 | -$16.65 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52858 | 52841 | 202 (0%) | 1.07% | -$3,613.15 (-56%) | Hold to the close: -$3,613.15 (-56%) |

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
| Volatility model | 31912 | 4.7% | 0.4% (129) | -677% | ❌ Worse |
| Momentum model | 31912 | 4.6% | 0.4% (129) | -701% | ❌ Worse |
| Mean-reversion model | 31912 | 8.1% | 0.4% (129) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31912 | 129 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7670 | 70 | +6% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4187 | 46 | +38% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2412 | 28 | +67% | -62% | -60% | -57% |
| Momentum model ≥ 2% | 6362 | 51 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3907 | 37 | +23% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2564 | 25 | +37% | -65% | -65% | -60% |
| Mean-reversion model ≥ 2% | 13210 | 91 | -24% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9255 | 78 | -6% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6184 | 56 | +3% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32117 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12573 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8151 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52841 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 202 | 0% | -$3,613.15 | -56% | — |
| Sell at 2¢ | 2108 | 4% | -$5,613.07 | -87% | 47 sec |
| Sell at 3¢ | 1433 | 3% | -$5,602.28 | -87% | 48 sec |
| Sell at 5¢ | 997 | 2% | -$5,485.10 | -85% | 63 sec |
| Sell at 10¢ | 602 | 1% | -$5,260.53 | -82% | 65 sec |
| Sell at 25¢ | 319 | 1% | -$4,881.26 | -76% | 83 sec |
| Sell at 50¢ | 210 | 0% | -$4,421.65 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2644 | 12 | 11% | 4% | -57% | -81% | -82% |
| 2–5 min | 17091 | 94 | 7% | 3% | -46% | -87% | -86% |
| 1–2 min | 13324 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19770 | 52 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3596 | 16 | 5% | 2% | -42% | -88% | -88% |
| SOL | 3591 | 16 | 4% | 2% | -43% | -87% | -86% |
| HYPE | 3584 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3577 | 19 | 5% | 2% | -33% | -86% | -85% |
| DOGE | 3573 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3566 | 15 | 7% | 3% | -48% | -81% | -81% |
| BTC | 3548 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3546 | 16 | 5% | 2% | -42% | -85% | -85% |
| XRP | 3536 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1899 | 5 | 6% | 2% | -68% | -81% | -83% |
| WTI | 1881 | 6 | 4% | 2% | -62% | -91% | -92% |
| SILVER | 1851 | 8 | 5% | 2% | -49% | -83% | -82% |
| PLATINUM | 1680 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1618 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1572 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1542 | 8 | 2% | 1% | -52% | -78% | -78% |
| GBPUSD | 1534 | 5 | 2% | 1% | -70% | -96% | -96% |
| USDJPY | 1517 | 6 | 2% | 1% | -63% | -97% | -96% |
| PALLADIUM | 1510 | 4 | 1% | 1% | -75% | -92% | -92% |
| AUDUSD | 1079 | 6 | 2% | 1% | -48% | -88% | -88% |
| USDCAD | 1046 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 638 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 23 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26771 | 106 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 26070 | 96 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5130 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5467 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8249 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9612 | 40 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3651 | 16 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12871 | 58 | 4% | 2% | -49% | -85% | -84% |
| Afternoon (12–6pm) | 12822 | 57 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14240 | 44 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,875 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 7:29:56 PM | NATGAS | UP | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:56 PM | PALLADIUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:56 PM | PLATINUM | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:56 PM | SILVER | DOWN | 3 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:56 PM | DOGE | UP | 3 sec | -0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/10 7:29:56 PM | SOL | UP | 3 sec | -0.018% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:40 PM | BNB | UP | 20 sec | -0.081% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:25 PM | GOLD | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/10 7:29:25 PM | AUDUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:25 PM | BTC | UP | 35 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 11/10 7:29:25 PM | WTI | DOWN | 35 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:29:09 PM | GBPUSD | UP | 51 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:28:53 PM | BRENT | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:28:19 PM | USDCAD | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:27:47 PM | XRP | DOWN | 2.2 min | +0.238% | 10¢ | ❌ Lost | -$0.15 |
| 11/10 7:27:47 PM | NEAR | DOWN | 2.2 min | +0.461% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:27:33 PM | HYPE | DOWN | 2.5 min | +0.378% | 0¢ | ❌ Lost | $0.00 |
| 11/10 7:27:16 PM | USDJPY | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:27:00 PM | EURUSD | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:26:44 PM | ETH | DOWN | 3.3 min | +0.226% | 2¢ | ❌ Lost | -$0.15 |
| 11/10 7:25:57 PM | ZEC | DOWN | 4.0 min | +1.009% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:58 PM | USDCAD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:58 PM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:58 PM | AUDUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:42 PM | EURUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:42 PM | SILVER | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:14:11 PM | DOGE | UP | 49 sec | -0.123% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:13:52 PM | USDJPY | DOWN | 67 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 7:13:52 PM | SOL | UP | 67 sec | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 7:13:36 PM | GBPUSD | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
