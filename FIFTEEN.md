# 15-Minute 1¢ Study

*Updated Mon Nov 16, 11:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4457 finished bets | 1% | $221.55 | +45% | +4.97¢ | $84.45 / $137.10 |

*Expect about **89 buys a day** (~$13.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4202 | $120.55 | +27% |
| Volatility model ≥ 2%, hold to the close | 8297 | $80.35 | +8% |
| Momentum model ≥ 2%, hold to the close | 6893 | $7.65 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59323 | 59288 | 227 (0%) | 1.07% | -$4,032.65 (-56%) | Hold to the close: -$4,032.65 (-56%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35659 | 4.6% | 0.4% (148) | -638% | ❌ Worse |
| Momentum model | 35659 | 4.5% | 0.4% (148) | -664% | ❌ Worse |
| Mean-reversion model | 35659 | 7.9% | 0.4% (148) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35659 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8297 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4457 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2565 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6893 | 57 | +1% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4202 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2739 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14605 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10162 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6748 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35865 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14070 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9353 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59288 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,032.65 | -56% | — |
| Sell at 2¢ | 2380 | 4% | -$6,297.85 | -87% | 47 sec |
| Sell at 3¢ | 1606 | 3% | -$6,290.31 | -87% | 48 sec |
| Sell at 5¢ | 1099 | 2% | -$6,174.30 | -86% | 63 sec |
| Sell at 10¢ | 669 | 1% | -$5,928.26 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,503.60 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,973.15 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2973 | 13 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 19193 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14908 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22201 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4014 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4009 | 18 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4001 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3991 | 20 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3990 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3982 | 17 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3965 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3963 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3950 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2104 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2087 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2046 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1866 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1812 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1746 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1741 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1722 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1698 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1678 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1255 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1199 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 821 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30154 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29134 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5433 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5877 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 8997 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11085 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4464 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16306 | 49 | 4% | 2% | -66% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,084 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 11:23:48 PM | BNB | UP | 6.2 min | -0.278% | — | In play | — |
| 11/16 11:14:59 PM | NATGAS | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:14:59 PM | SOL | UP | 1 sec | +0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:14:44 PM | PALLADIUM | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:14:44 PM | ZEC | DOWN | 16 sec | +0.275% | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:14:44 PM | HYPE | DOWN | 16 sec | +0.047% | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:14:44 PM | XRP | DOWN | 16 sec | +0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/16 11:13:21 PM | ETH | UP | 1.6 min | -0.194% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:13:05 PM | NEAR | UP | 1.9 min | -0.370% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:49 PM | BNB | UP | 2.2 min | -0.172% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:34 PM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:18 PM | EURUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:18 PM | BTC | UP | 2.7 min | -0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:18 PM | AUDUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:18 PM | DOGE | UP | 2.7 min | -0.191% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:12:18 PM | GBPUSD | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:11:46 PM | SILVER | UP | 3.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:11:31 PM | USDJPY | DOWN | 3.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:11:31 PM | GOLD | UP | 3.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 11:10:59 PM | PLATINUM | UP | 4.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 11:10:25 PM | USDCAD | DOWN | 4.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:59:48 PM | DOGE | UP | 12 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:59:48 PM | GBPUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:59:33 PM | XRP | UP | 26 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:59:17 PM | PALLADIUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | ZEC | UP | 1.5 min | -0.416% | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:58:28 PM | SILVER | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | HYPE | UP | 1.5 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | BRENT | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | PLATINUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
