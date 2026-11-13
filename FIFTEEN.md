# 15-Minute 1¢ Study

*Updated Fri Nov 13, 5:16 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4280 finished bets | 1% | $168.80 | +36% | +3.94¢ | $80.95 / $87.85 |

*Expect about **93 buys a day** (~$13.89/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4021 | $95.80 | +22% |
| Volatility model ≥ 2%, hold to the close | 7900 | $28.85 | +3% |
| Momentum model ≥ 2%, hold to the close | 6557 | -$25.75 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 55861 | 55840 | 212 (0%) | 1.07% | -$3,846.65 (-56%) | Hold to the close: -$3,846.65 (-56%) |

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
| Volatility model | 33335 | 4.7% | 0.4% (133) | -670% | ❌ Worse |
| Momentum model | 33335 | 4.6% | 0.4% (133) | -697% | ❌ Worse |
| Mean-reversion model | 33335 | 8.0% | 0.4% (133) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33335 | 133 | -49% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7900 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4280 | 46 | +36% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2479 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6557 | 52 | -3% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4021 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2636 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13728 | 93 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9575 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6386 | 56 | -0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33540 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13467 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8833 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 55840 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,846.65 | -56% | — |
| Sell at 2¢ | 2227 | 4% | -$5,941.63 | -87% | 47 sec |
| Sell at 3¢ | 1512 | 3% | -$5,930.97 | -87% | 48 sec |
| Sell at 5¢ | 1040 | 2% | -$5,816.65 | -85% | 63 sec |
| Sell at 10¢ | 632 | 1% | -$5,580.73 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,190.35 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,705.90 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2781 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18009 | 97 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14080 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20957 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3755 | 17 | 5% | 3% | -41% | -88% | -87% |
| SOL | 3750 | 16 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3745 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3731 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3731 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3725 | 16 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3706 | 17 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3706 | 18 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3691 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2023 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2001 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1965 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1791 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1738 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1678 | 6 | 2% | 1% | -67% | -74% | -74% |
| GBPUSD | 1662 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1653 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1628 | 6 | 2% | 1% | -66% | -96% | -96% |
| PALLADIUM | 1605 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1179 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1147 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 751 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 380 | 2 | 4% | 2% | -51% | -69% | -67% |
| 2YRRATE | 364 | 4 | 4% | 2% | +3% | -42% | -41% |
| 30YRRATE | 360 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 334 | 2 | 4% | 2% | -44% | -93% | -95% |
| INX | 41 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28368 | 110 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 27472 | 102 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5261 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5669 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8567 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10157 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3878 | 18 | 7% | 3% | -52% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13680 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13343 | 62 | 4% | 2% | -47% | -85% | -84% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,822 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 5:14:55 AM | AUDUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:14:55 AM | 5YRRATE | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:14:55 AM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:14:07 AM | GOLD | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:14:07 AM | SILVER | DOWN | 52 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:51 AM | PLATINUM | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:35 AM | USDCAD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:35 AM | EURUSD | UP | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:35 AM | 30YRRATE | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:16 AM | 10YRRATE | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:16 AM | BNB | DOWN | 1.7 min | +0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:13:16 AM | NEAR | UP | 1.7 min | -0.703% | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:12:44 AM | BTC | DOWN | 2.3 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:12:29 AM | GBPUSD | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:12:10 AM | SOL | DOWN | 2.8 min | +0.213% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:12:10 AM | USDJPY | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:12:10 AM | HYPE | DOWN | 2.8 min | +0.462% | 2¢ | ❌ Lost | -$0.15 |
| 11/13 5:11:54 AM | ETH | DOWN | 3.1 min | +0.225% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:11:23 AM | XRP | DOWN | 3.6 min | +0.284% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:11:06 AM | DOGE | DOWN | 3.9 min | +0.271% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 5:10:18 AM | NATGAS | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 5:08:08 AM | ZEC | DOWN | 6.9 min | +1.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:48 AM | USDJPY | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:48 AM | NATGAS | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:32 AM | XRP | DOWN | 27 sec | +0.010% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:32 AM | DOGE | UP | 27 sec | -0.069% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:32 AM | HYPE | DOWN | 27 sec | +0.087% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:15 AM | SOL | UP | 44 sec | -0.112% | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:15 AM | WTI | DOWN | 44 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/13 4:59:15 AM | ETH | UP | 44 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
