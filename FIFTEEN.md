# 15-Minute 1¢ Study

*Updated Thu Nov 12, 10:42 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4269 finished bets | 1% | $170.15 | +36% | +3.99¢ | $81.85 / $88.30 |

*Expect about **93 buys a day** (~$13.93/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4008 | $97.45 | +22% |
| Volatility model ≥ 2%, hold to the close | 7874 | $32.30 | +3% |
| Momentum model ≥ 2%, hold to the close | 6538 | -$23.20 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55589 | 55564 | 212 (0%) | 1.07% | -$3,811.70 (-56%) | Hold to the close: -$3,811.70 (-56%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 33207 | 4.7% | 0.4% (133) | -670% | ❌ Worse |
| Momentum model | 33207 | 4.6% | 0.4% (133) | -697% | ❌ Worse |
| Mean-reversion model | 33207 | 8.0% | 0.4% (133) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33207 | 133 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7874 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4269 | 46 | +36% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2470 | 28 | +63% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6538 | 52 | -3% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 4008 | 38 | +22% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2628 | 25 | +34% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13677 | 93 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9546 | 79 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6364 | 56 | +0% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33412 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13385 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8767 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55564 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,811.70 | -56% | — |
| Sell at 2¢ | 2215 | 4% | -$5,909.80 | -87% | 47 sec |
| Sell at 3¢ | 1506 | 3% | -$5,898.36 | -87% | 49 sec |
| Sell at 5¢ | 1037 | 2% | -$5,783.65 | -85% | 63 sec |
| Sell at 10¢ | 629 | 1% | -$5,549.71 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,155.40 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,670.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2762 | 13 | 11% | 4% | -55% | -81% | -82% |
| 2–5 min | 17928 | 97 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 14002 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20859 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3740 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3735 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3730 | 11 | 5% | 2% | -63% | -89% | -88% |
| BNB | 3718 | 19 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3716 | 8 | 4% | 2% | -73% | -90% | -90% |
| ETH | 3711 | 16 | 7% | 3% | -46% | -82% | -81% |
| BTC | 3693 | 18 | 5% | 2% | -33% | -87% | -88% |
| NEAR | 3691 | 17 | 5% | 2% | -40% | -85% | -85% |
| XRP | 3678 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2012 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 1992 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1952 | 9 | 5% | 2% | -45% | -83% | -83% |
| PLATINUM | 1779 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1726 | 6 | 3% | 1% | -68% | -90% | -89% |
| COPPER | 1670 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1652 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1643 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1621 | 6 | 2% | 1% | -65% | -96% | -96% |
| PALLADIUM | 1594 | 4 | 1% | 1% | -77% | -92% | -92% |
| AUDUSD | 1172 | 6 | 2% | 1% | -52% | -89% | -89% |
| USDCAD | 1134 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 743 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 375 | 2 | 4% | 2% | -50% | -68% | -66% |
| 2YRRATE | 360 | 4 | 4% | 2% | +4% | -41% | -40% |
| 30YRRATE | 356 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 330 | 2 | 4% | 2% | -43% | -93% | -94% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28254 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27310 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5252 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5651 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8543 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10105 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3853 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13478 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15290 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,830 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 10:41:52 PM | HYPE | DOWN | 3.1 min | +0.737% | — | In play | — |
| 11/12 10:41:52 PM | NEAR | DOWN | 3.1 min | +0.737% | — | In play | — |
| 11/12 10:41:04 PM | USDCAD | DOWN | 3.9 min | — | — | In play | — |
| 11/12 10:40:17 PM | COPPER | UP | 4.7 min | — | — | In play | — |
| 11/12 10:29:56 PM | DOGE | UP | 4 sec | -0.064% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:56 PM | USDJPY | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:56 PM | SOL | DOWN | 4 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:29:56 PM | COPPER | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:56 PM | USDCAD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:40 PM | HYPE | UP | 19 sec | -0.200% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:29:40 PM | PALLADIUM | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:40 PM | EURUSD | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:24 PM | SILVER | DOWN | 35 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:29:24 PM | AUDUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:29:24 PM | ZEC | DOWN | 35 sec | +0.139% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:29:08 PM | NEAR | DOWN | 51 sec | +0.379% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:28:52 PM | BTC | UP | 67 sec | -0.159% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:28:52 PM | BNB | UP | 67 sec | -0.177% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:28:36 PM | GOLD | DOWN | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:28:36 PM | XRP | DOWN | 83 sec | +0.248% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:27:33 PM | ETH | UP | 2.5 min | -0.355% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:14:52 PM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:14:52 PM | WTI | UP | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:14:52 PM | BRENT | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:14:36 PM | ETH | DOWN | 24 sec | +0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:14:20 PM | GOLD | DOWN | 40 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/12 10:14:04 PM | SOL | DOWN | 56 sec | +0.150% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:14:04 PM | ZEC | DOWN | 56 sec | +0.596% | 0¢ | ❌ Lost | $0.00 |
| 11/12 10:13:48 PM | AUDUSD | UP | 71 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 10:13:48 PM | BNB | DOWN | 71 sec | +0.135% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
