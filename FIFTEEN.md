# 15-Minute 1¢ Study

*Updated Mon Nov 16, 11:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4455 finished bets | 1% | $221.70 | +45% | +4.98¢ | $84.45 / $137.25 |

*Expect about **89 buys a day** (~$13.38/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4201 | $120.55 | +27% |
| Volatility model ≥ 2%, hold to the close | 8295 | $80.50 | +8% |
| Momentum model ≥ 2%, hold to the close | 6892 | $7.65 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59316 | 59268 | 227 (0%) | 1.07% | -$4,030.25 (-56%) | Hold to the close: -$4,030.25 (-56%) |

*In play or awaiting result: 20. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35650 | 4.6% | 0.4% (148) | -637% | ❌ Worse |
| Momentum model | 35650 | 4.5% | 0.4% (148) | -663% | ❌ Worse |
| Mean-reversion model | 35650 | 7.9% | 0.4% (148) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35650 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8295 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4455 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2564 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6892 | 57 | +1% | -79% | -78% | -74% |
| Momentum model ≥ 5% | 4201 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2738 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14602 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10160 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6746 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35856 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14064 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9348 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59268 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,030.25 | -56% | — |
| Sell at 2¢ | 2380 | 4% | -$6,295.45 | -87% | 47 sec |
| Sell at 3¢ | 1606 | 3% | -$6,287.91 | -87% | 48 sec |
| Sell at 5¢ | 1099 | 2% | -$6,171.90 | -86% | 63 sec |
| Sell at 10¢ | 669 | 1% | -$5,925.86 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,501.20 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,970.75 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2973 | 13 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 19181 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14906 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22195 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4013 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4008 | 18 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 4000 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3990 | 20 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 3989 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3981 | 17 | 7% | 3% | -47% | -82% | -82% |
| BTC | 3964 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3962 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3949 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2103 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2087 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2045 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1865 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1811 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1745 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1740 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1721 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1697 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1677 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1254 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1198 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 821 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30140 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29128 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5431 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5876 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 8993 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 11083 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4464 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16286 | 49 | 4% | 2% | -65% | -89% | -89% |

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
| 11/16 11:13:21 PM | ETH | UP | 1.6 min | -0.194% | — | In play | — |
| 11/16 11:13:05 PM | NEAR | UP | 1.9 min | -0.370% | — | In play | — |
| 11/16 11:12:49 PM | BNB | UP | 2.2 min | -0.172% | — | In play | — |
| 11/16 11:12:34 PM | COPPER | UP | 2.4 min | — | — | In play | — |
| 11/16 11:12:18 PM | EURUSD | UP | 2.7 min | — | — | In play | — |
| 11/16 11:12:18 PM | BTC | UP | 2.7 min | -0.193% | — | In play | — |
| 11/16 11:12:18 PM | AUDUSD | UP | 2.7 min | — | — | In play | — |
| 11/16 11:12:18 PM | DOGE | UP | 2.7 min | -0.191% | — | In play | — |
| 11/16 11:12:18 PM | GBPUSD | UP | 2.7 min | — | — | In play | — |
| 11/16 11:11:46 PM | SILVER | UP | 3.2 min | — | — | In play | — |
| 11/16 11:11:31 PM | USDJPY | DOWN | 3.5 min | — | — | In play | — |
| 11/16 11:11:31 PM | GOLD | UP | 3.5 min | — | — | In play | — |
| 11/16 11:10:59 PM | PLATINUM | UP | 4.0 min | — | — | In play | — |
| 11/16 11:10:25 PM | USDCAD | DOWN | 4.6 min | — | — | In play | — |
| 11/16 10:59:48 PM | DOGE | UP | 12 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:59:48 PM | GBPUSD | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:59:33 PM | XRP | UP | 26 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:59:17 PM | PALLADIUM | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | ZEC | UP | 1.5 min | -0.416% | 0¢ | ❌ Lost | $0.00 |
| 11/16 10:58:28 PM | SILVER | UP | 1.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | HYPE | UP | 1.5 min | -0.253% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | BRENT | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | PLATINUM | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:28 PM | ETH | UP | 1.5 min | -0.147% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:58:12 PM | BNB | UP | 1.8 min | -0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:57:41 PM | BTC | UP | 2.3 min | -0.131% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:57:41 PM | WTI | UP | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:57:41 PM | SOL | UP | 2.3 min | -0.235% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 10:57:33 PM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 10:56:45 PM | NEAR | UP | 3.2 min | -0.608% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
