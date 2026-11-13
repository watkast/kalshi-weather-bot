# 15-Minute 1¢ Study

*Updated Fri Nov 13, 11:15 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4284 finished bets | 1% | $168.50 | +35% | +3.93¢ | $80.65 / $87.85 |

*Expect about **92 buys a day** (~$13.82/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4027 | $95.50 | +22% |
| Volatility model ≥ 2%, hold to the close | 7912 | $27.50 | +3% |
| Momentum model ≥ 2%, hold to the close | 6570 | -$26.95 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 56143 | 56102 | 212 (0%) | 1.07% | -$3,878.45 (-57%) | Hold to the close: -$3,878.45 (-57%) |

*In play or awaiting result: 29. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 33449 | 4.7% | 0.4% (133) | -671% | ❌ Worse |
| Momentum model | 33449 | 4.6% | 0.4% (133) | -697% | ❌ Worse |
| Mean-reversion model | 33449 | 8.0% | 0.4% (133) | -813% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 33449 | 133 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7912 | 70 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4284 | 46 | +35% | -72% | -71% | -67% |
| Volatility model ≥ 10% | 2482 | 28 | +62% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6570 | 52 | -4% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4027 | 38 | +22% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2641 | 25 | +33% | -66% | -66% | -61% |
| Mean-reversion model ≥ 2% | 13769 | 93 | -26% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9602 | 79 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6400 | 56 | -1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 33654 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13532 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8916 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 56102 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 212 | 0% | -$3,878.45 | -57% | — |
| Sell at 2¢ | 2233 | 4% | -$5,971.87 | -87% | 47 sec |
| Sell at 3¢ | 1513 | 3% | -$5,962.38 | -87% | 48 sec |
| Sell at 5¢ | 1041 | 2% | -$5,847.80 | -85% | 63 sec |
| Sell at 10¢ | 632 | 1% | -$5,612.53 | -82% | 65 sec |
| Sell at 25¢ | 330 | 1% | -$5,222.15 | -76% | 82 sec |
| Sell at 50¢ | 217 | 0% | -$4,737.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2800 | 13 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 18075 | 97 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14152 | 46 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 21062 | 56 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3768 | 17 | 5% | 2% | -41% | -88% | -87% |
| SOL | 3763 | 16 | 4% | 2% | -46% | -87% | -87% |
| HYPE | 3758 | 11 | 5% | 2% | -63% | -89% | -88% |
| DOGE | 3743 | 8 | 4% | 2% | -73% | -90% | -90% |
| BNB | 3743 | 19 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3739 | 16 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3718 | 17 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3718 | 18 | 5% | 2% | -34% | -87% | -88% |
| XRP | 3704 | 13 | 3% | 1% | -56% | -89% | -89% |
| GOLD | 2034 | 5 | 5% | 2% | -70% | -82% | -84% |
| WTI | 2007 | 7 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 1975 | 9 | 5% | 2% | -46% | -83% | -83% |
| PLATINUM | 1801 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1746 | 6 | 3% | 1% | -68% | -90% | -90% |
| COPPER | 1686 | 6 | 2% | 1% | -67% | -75% | -74% |
| GBPUSD | 1671 | 6 | 2% | 1% | -66% | -96% | -96% |
| NATGAS | 1659 | 9 | 2% | 1% | -49% | -74% | -73% |
| USDJPY | 1634 | 6 | 2% | 1% | -66% | -96% | -96% |
| PALLADIUM | 1615 | 4 | 1% | 0% | -77% | -92% | -92% |
| AUDUSD | 1189 | 6 | 2% | 1% | -53% | -89% | -89% |
| USDCAD | 1155 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 755 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 390 | 2 | 4% | 2% | -52% | -69% | -67% |
| 2YRRATE | 373 | 4 | 4% | 2% | +0% | -43% | -42% |
| 30YRRATE | 370 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 345 | 2 | 4% | 2% | -46% | -93% | -95% |
| INX | 43 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 28506 | 110 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 27596 | 102 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5277 | 25 | 2% | 1% | -16% | -77% | -77% |
| 0.05–0.1% | 5674 | 20 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 8582 | 31 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 10197 | 41 | 6% | 3% | -55% | -87% | -86% |
| Over 0.5% | 3916 | 18 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13733 | 44 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13552 | 62 | 4% | 2% | -48% | -85% | -85% |
| Afternoon (12–6pm) | 13453 | 59 | 4% | 2% | -49% | -86% | -87% |
| Evening (6pm–12am) | 15364 | 47 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,812 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/13 11:14:55 AM | AUDUSD | DOWN | 5 sec | — | 0¢ | In play | — |
| 11/13 11:14:55 AM | GOLD | UP | 5 sec | — | 0¢ | In play | — |
| 11/13 11:14:55 AM | SILVER | UP | 5 sec | — | 1¢ | In play | — |
| 11/13 11:14:55 AM | ETH | DOWN | 5 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:14:39 AM | SOL | DOWN | 21 sec | +0.070% | 0¢ | In play | — |
| 11/13 11:14:39 AM | 10YRRATE | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/13 11:14:39 AM | BRENT | DOWN | 21 sec | — | 0¢ | In play | — |
| 11/13 11:14:24 AM | WTI | DOWN | 36 sec | — | 0¢ | In play | — |
| 11/13 11:14:09 AM | ZEC | UP | 51 sec | -0.253% | 1¢ | In play | — |
| 11/13 11:13:53 AM | NEAR | UP | 67 sec | -0.326% | 0¢ | In play | — |
| 11/13 11:13:53 AM | INX | UP | 67 sec | — | 0¢ | In play | — |
| 11/13 11:13:53 AM | HYPE | UP | 67 sec | -0.271% | 0¢ | ❌ Lost | $0.00 |
| 11/13 11:13:37 AM | DOGE | DOWN | 83 sec | +0.198% | 0¢ | In play | — |
| 11/13 11:13:21 AM | XRP | DOWN | 1.6 min | +0.265% | 1¢ | In play | — |
| 11/13 11:13:21 AM | BNB | DOWN | 1.6 min | +0.126% | 0¢ | In play | — |
| 11/13 11:13:21 AM | USDCAD | UP | 1.6 min | — | 2¢ | In play | — |
| 11/13 11:13:04 AM | COPPER | UP | 1.9 min | — | 0¢ | In play | — |
| 11/13 11:12:46 AM | EURUSD | DOWN | 2.2 min | — | 0¢ | In play | — |
| 11/13 11:12:46 AM | GBPUSD | DOWN | 2.2 min | — | 0¢ | In play | — |
| 11/13 11:12:46 AM | BTC | UP | 2.2 min | -0.172% | 1¢ | In play | — |
| 11/13 11:11:38 AM | NATGAS | DOWN | 3.4 min | — | 0¢ | In play | — |
| 11/13 11:09:28 AM | USDJPY | UP | 5.5 min | — | 0¢ | In play | — |
| 11/13 10:59:53 AM | WTI | DOWN | 6 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/13 10:59:53 AM | INX | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 10:59:37 AM | EURUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 10:59:37 AM | 5YRRATE | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 10:59:37 AM | GBPUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 10:59:21 AM | GOLD | UP | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 10:59:03 AM | 10YRRATE | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/13 10:59:03 AM | 30YRRATE | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
