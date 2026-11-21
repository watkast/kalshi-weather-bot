# 15-Minute 1¢ Study

*Updated Sat Nov 21, 5:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4640 finished bets | 1% | $204.30 | +40% | +4.40¢ | $74.25 / $130.05 |

*Expect about **86 buys a day** (~$12.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4397 | $101.95 | +22% |
| Volatility model ≥ 2%, hold to the close | 8677 | $52.20 | +5% |
| Momentum model ≥ 2%, hold to the close | 7215 | -$27.45 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63812 | 63778 | 245 (0%) | 1.07% | -$4,316.60 (-56%) | Hold to the close: -$4,316.60 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 37834 | 4.5% | 0.4% (157) | -637% | ❌ Worse |
| Momentum model | 37834 | 4.4% | 0.4% (157) | -662% | ❌ Worse |
| Mean-reversion model | 37834 | 7.8% | 0.4% (157) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37834 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8677 | 78 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4640 | 51 | +40% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2671 | 30 | +65% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7215 | 57 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4397 | 41 | +22% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2862 | 26 | +30% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15429 | 109 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10721 | 89 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7121 | 64 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38040 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63778 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,316.60 | -56% | — |
| Sell at 2¢ | 2575 | 4% | -$6,783.10 | -88% | 47 sec |
| Sell at 3¢ | 1734 | 3% | -$6,776.34 | -87% | 48 sec |
| Sell at 5¢ | 1182 | 2% | -$6,656.30 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,394.78 | -83% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,905.63 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,338.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3292 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20681 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 15929 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23863 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4253 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4246 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4245 | 14 | 4% | 2% | -58% | -89% | -88% |
| DOGE | 4234 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4234 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4228 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4207 | 22 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4205 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4188 | 16 | 3% | 2% | -51% | -89% | -88% |
| GOLD | 2265 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2257 | 7 | 4% | 1% | -62% | -91% | -92% |
| SILVER | 2209 | 9 | 5% | 2% | -51% | -83% | -83% |
| PLATINUM | 2012 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1968 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1900 | 8 | 2% | 1% | -61% | -96% | -95% |
| COPPER | 1895 | 6 | 2% | 1% | -70% | -77% | -77% |
| NATGAS | 1858 | 10 | 2% | 1% | -50% | -76% | -76% |
| USDJPY | 1855 | 6 | 2% | 1% | -70% | -96% | -96% |
| PALLADIUM | 1808 | 4 | 1% | 1% | -79% | -93% | -93% |
| AUDUSD | 1406 | 6 | 2% | 1% | -60% | -90% | -90% |
| USDCAD | 1340 | 1 | 3% | 1% | -93% | -95% | -96% |
| BRENT | 969 | 0 | 2% | 1% | -100% | -97% | -98% |
| 10YRRATE | 499 | 2 | 3% | 1% | -63% | -76% | -74% |
| 2YRRATE | 476 | 4 | 4% | 2% | -22% | -54% | -53% |
| 30YRRATE | 462 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 451 | 2 | 4% | 2% | -59% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 32605 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31173 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5604 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6110 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9477 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11841 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 4999 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15392 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15289 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17521 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,031 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 5:43:22 AM | XRP | DOWN | 1.6 min | +0.420% | 0¢ | ❌ Lost | $0.00 |
| 11/21 5:42:36 AM | DOGE | DOWN | 2.4 min | +0.388% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 5:42:36 AM | HYPE | DOWN | 2.4 min | +0.459% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 5:42:36 AM | SOL | DOWN | 2.4 min | +0.435% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 5:42:36 AM | ZEC | DOWN | 2.4 min | +0.821% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 5:42:20 AM | ETH | DOWN | 2.6 min | +0.433% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 5:41:35 AM | BTC | DOWN | 3.4 min | +0.478% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 5:41:19 AM | NEAR | DOWN | 3.7 min | +1.000% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 5:41:19 AM | BNB | DOWN | 3.7 min | +0.440% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 1:44:57 AM | XRP | DOWN | 3 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:44:41 AM | DOGE | DOWN | 19 sec | +0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:44:41 AM | SOL | DOWN | 19 sec | +0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:44:25 AM | ETH | DOWN | 35 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:44:25 AM | BNB | DOWN | 35 sec | +0.104% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:44:25 AM | ZEC | DOWN | 35 sec | +0.450% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:44:25 AM | BTC | DOWN | 35 sec | +0.183% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:43:36 AM | HYPE | DOWN | 84 sec | +0.398% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 1:41:26 AM | NEAR | UP | 3.6 min | -0.893% | 9¢ | ❌ Lost | -$0.15 |
| 11/21 1:29:30 AM | ETH | UP | 30 sec | -0.177% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 1:29:30 AM | HYPE | UP | 30 sec | -0.202% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:29:13 AM | BTC | UP | 46 sec | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:28:09 AM | DOGE | UP | 1.9 min | -0.352% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 1:28:09 AM | SOL | UP | 1.9 min | -0.367% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 1:27:35 AM | ZEC | UP | 2.4 min | -0.783% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:26:46 AM | NEAR | UP | 3.2 min | -0.893% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 1:26:14 AM | XRP | UP | 3.8 min | -0.685% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 1:25:49 AM | BNB | UP | 4.2 min | -0.524% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 1:14:31 AM | DOGE | UP | 28 sec | -0.119% | 0¢ | ❌ Lost | $0.00 |
| 11/21 1:14:13 AM | NEAR | DOWN | 47 sec | +0.186% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 1:13:57 AM | HYPE | UP | 63 sec | -0.305% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
