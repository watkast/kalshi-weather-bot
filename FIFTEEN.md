# 15-Minute 1¢ Study

*Updated Tue Nov 17, 12:58 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4465 finished bets | 1% | $220.65 | +45% | +4.94¢ | $84.00 / $136.65 |

*Expect about **89 buys a day** (~$13.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4206 | $120.10 | +26% |
| Volatility model ≥ 2%, hold to the close | 8313 | $78.25 | +8% |
| Momentum model ≥ 2%, hold to the close | 6902 | $6.45 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 59438 | 59394 | 227 (0%) | 1.07% | -$4,046.90 (-56%) | Hold to the close: -$4,046.90 (-56%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 35711 | 4.5% | 0.4% (148) | -637% | ❌ Worse |
| Momentum model | 35711 | 4.5% | 0.4% (148) | -663% | ❌ Worse |
| Mean-reversion model | 35711 | 7.9% | 0.4% (148) | -775% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35711 | 148 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8313 | 77 | +8% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4465 | 51 | +45% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2567 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6902 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4206 | 41 | +26% | -74% | -74% | -69% |
| Momentum model ≥ 10% | 2739 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14635 | 103 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10187 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6768 | 61 | +3% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35917 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 14100 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9377 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 59394 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$4,046.90 | -56% | — |
| Sell at 2¢ | 2385 | 4% | -$6,310.80 | -87% | 47 sec |
| Sell at 3¢ | 1608 | 3% | -$6,303.78 | -87% | 48 sec |
| Sell at 5¢ | 1100 | 2% | -$6,187.90 | -86% | 62 sec |
| Sell at 10¢ | 669 | 1% | -$5,942.51 | -82% | 65 sec |
| Sell at 25¢ | 355 | 1% | -$5,517.85 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,987.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2984 | 13 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 19226 | 104 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 14929 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22242 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4019 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 4015 | 18 | 4% | 2% | -43% | -86% | -87% |
| HYPE | 4007 | 12 | 4% | 2% | -62% | -89% | -88% |
| BNB | 3997 | 20 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3996 | 11 | 4% | 2% | -65% | -90% | -89% |
| ETH | 3988 | 17 | 6% | 3% | -47% | -82% | -82% |
| BTC | 3971 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3969 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3955 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2110 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2091 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2050 | 9 | 5% | 2% | -48% | -83% | -83% |
| PLATINUM | 1868 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1817 | 6 | 2% | 1% | -69% | -91% | -90% |
| COPPER | 1750 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1744 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1726 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1704 | 6 | 2% | 1% | -67% | -96% | -96% |
| PALLADIUM | 1681 | 4 | 1% | 0% | -78% | -92% | -93% |
| AUDUSD | 1259 | 6 | 2% | 1% | -56% | -89% | -89% |
| USDCAD | 1205 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 824 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 30212 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 29182 | 114 | 4% | 2% | -55% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5435 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5882 | 24 | 3% | 2% | -37% | -91% | -91% |
| 0.1–0.2% | 9016 | 34 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 11104 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4471 | 19 | 7% | 3% | -56% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14463 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14631 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16360 | 49 | 4% | 2% | -66% | -89% | -89% |

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
| 11/17 12:58:14 AM | XRP | DOWN | 1.8 min | +0.136% | — | In play | — |
| 11/17 12:58:14 AM | USDJPY | DOWN | 1.8 min | — | — | In play | — |
| 11/17 12:57:11 AM | WTI | UP | 2.8 min | — | — | In play | — |
| 11/17 12:57:11 AM | DOGE | DOWN | 2.8 min | +0.178% | — | In play | — |
| 11/17 12:56:55 AM | BRENT | UP | 3.1 min | — | — | In play | — |
| 11/17 12:56:40 AM | NEAR | DOWN | 3.3 min | +0.308% | — | In play | — |
| 11/17 12:56:24 AM | BTC | DOWN | 3.6 min | +0.153% | — | In play | — |
| 11/17 12:56:08 AM | ETH | DOWN | 3.9 min | +0.236% | — | In play | — |
| 11/17 12:56:08 AM | SILVER | DOWN | 3.9 min | — | — | In play | — |
| 11/17 12:55:20 AM | EURUSD | UP | 4.7 min | — | — | In play | — |
| 11/17 12:44:48 AM | USDCAD | DOWN | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:44:33 AM | BNB | UP | 27 sec | -0.132% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:44:33 AM | GBPUSD | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:44:17 AM | DOGE | UP | 43 sec | -0.070% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 12:44:17 AM | NEAR | UP | 43 sec | -0.200% | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:44:01 AM | SOL | UP | 59 sec | -0.144% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 12:44:01 AM | XRP | UP | 59 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 11/17 12:43:44 AM | PLATINUM | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:43:44 AM | GOLD | UP | 75 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/17 12:43:29 AM | AUDUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:43:29 AM | EURUSD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:41:54 AM | ETH | UP | 3.1 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 12:41:38 AM | BTC | UP | 3.4 min | -0.174% | 3¢ | ❌ Lost | -$0.15 |
| 11/17 12:41:23 AM | SILVER | UP | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 12:41:07 AM | WTI | DOWN | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/17 12:40:51 AM | PALLADIUM | UP | 4.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:40:35 AM | HYPE | UP | 4.4 min | -0.424% | 1¢ | ❌ Lost | -$0.15 |
| 11/17 12:40:20 AM | USDJPY | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:39:32 AM | BRENT | DOWN | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/17 12:29:50 AM | USDCAD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
