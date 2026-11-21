# 15-Minute 1¢ Study

*Updated Sat Nov 21, 7:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4644 finished bets | 1% | $203.85 | +40% | +4.39¢ | $73.95 / $129.90 |

*Expect about **86 buys a day** (~$12.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4402 | $101.20 | +21% |
| Volatility model ≥ 2%, hold to the close | 8690 | $50.40 | +5% |
| Momentum model ≥ 2%, hold to the close | 7228 | -$29.10 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 63858 | 63823 | 245 (0%) | 1.07% | -$4,321.85 (-56%) | Hold to the close: -$4,321.85 (-56%) |

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
| Volatility model | 37879 | 4.5% | 0.4% (157) | -637% | ❌ Worse |
| Momentum model | 37879 | 4.4% | 0.4% (157) | -662% | ❌ Worse |
| Mean-reversion model | 37879 | 7.8% | 0.4% (157) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 37879 | 157 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8690 | 78 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4644 | 51 | +40% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 2672 | 30 | +65% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7228 | 57 | -4% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4402 | 41 | +21% | -75% | -74% | -70% |
| Momentum model ≥ 10% | 2863 | 26 | +30% | -67% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15450 | 109 | -23% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10737 | 89 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7132 | 64 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 38085 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15273 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10465 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 63823 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 245 | 0% | -$4,321.85 | -56% | — |
| Sell at 2¢ | 2579 | 4% | -$6,787.31 | -88% | 47 sec |
| Sell at 3¢ | 1736 | 3% | -$6,780.81 | -87% | 48 sec |
| Sell at 5¢ | 1183 | 2% | -$6,660.90 | -86% | 63 sec |
| Sell at 10¢ | 722 | 1% | -$6,400.03 | -83% | 65 sec |
| Sell at 25¢ | 387 | 1% | -$5,910.88 | -76% | 80 sec |
| Sell at 50¢ | 251 | 0% | -$5,343.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3303 | 17 | 10% | 4% | -51% | -82% | -83% |
| 2–5 min | 20699 | 110 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 15936 | 55 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 23872 | 63 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4258 | 19 | 5% | 2% | -41% | -88% | -87% |
| SOL | 4251 | 19 | 4% | 2% | -42% | -86% | -86% |
| HYPE | 4250 | 14 | 4% | 2% | -58% | -89% | -88% |
| DOGE | 4239 | 11 | 4% | 2% | -67% | -90% | -89% |
| BNB | 4239 | 21 | 5% | 2% | -37% | -86% | -85% |
| ETH | 4233 | 19 | 7% | 3% | -44% | -82% | -82% |
| BTC | 4212 | 22 | 5% | 2% | -29% | -86% | -88% |
| NEAR | 4210 | 18 | 5% | 2% | -44% | -85% | -86% |
| XRP | 4193 | 16 | 3% | 2% | -51% | -89% | -88% |
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
| UP (bought YES) | 32616 | 126 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 31207 | 119 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5604 | 25 | 2% | 1% | -19% | -78% | -78% |
| 0.05–0.1% | 6110 | 24 | 3% | 2% | -38% | -91% | -91% |
| 0.1–0.2% | 9479 | 34 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 11863 | 53 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5020 | 23 | 7% | 3% | -52% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15401 | 48 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 15325 | 81 | 4% | 2% | -40% | -85% | -85% |
| Afternoon (12–6pm) | 15576 | 66 | 4% | 2% | -50% | -87% | -87% |
| Evening (6pm–12am) | 17521 | 50 | 4% | 2% | -67% | -90% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,038 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/21 7:10:02 AM | ZEC | UP | 5.0 min | -2.055% | — | In play | — |
| 11/21 6:59:19 AM | ETH | DOWN | 41 sec | +0.250% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:59:19 AM | DOGE | DOWN | 41 sec | +0.308% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:59:03 AM | ZEC | DOWN | 57 sec | +0.452% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 6:59:03 AM | BNB | DOWN | 57 sec | +0.181% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:59:03 AM | BTC | DOWN | 57 sec | +0.240% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:58:34 AM | NEAR | DOWN | 86 sec | +0.431% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:58:34 AM | HYPE | DOWN | 86 sec | +0.469% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:57:48 AM | SOL | DOWN | 2.2 min | +0.396% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:57:48 AM | XRP | DOWN | 2.2 min | +0.400% | 0¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:42 AM | NEAR | DOWN | 5.3 min | +2.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:33 AM | ZEC | DOWN | 5.4 min | +3.240% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:33 AM | DOGE | DOWN | 5.4 min | +1.874% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:33 AM | SOL | DOWN | 5.4 min | +1.550% | 2¢ | ❌ Lost | -$0.15 |
| 11/21 6:39:33 AM | HYPE | DOWN | 5.4 min | +1.912% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:38:39 AM | ETH | DOWN | 6.3 min | +1.647% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:38:39 AM | XRP | DOWN | 6.3 min | +1.128% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:38:24 AM | BTC | DOWN | 6.6 min | +2.024% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:38:10 AM | BNB | DOWN | 6.8 min | +1.333% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:29:26 AM | NEAR | DOWN | 33 sec | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:29:26 AM | ZEC | UP | 33 sec | -0.353% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:29:10 AM | HYPE | UP | 49 sec | -0.225% | 0¢ | ❌ Lost | $0.00 |
| 11/21 6:28:40 AM | ETH | DOWN | 80 sec | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:27:41 AM | DOGE | DOWN | 2.3 min | +0.280% | 5¢ | ❌ Lost | -$0.15 |
| 11/21 6:27:07 AM | SOL | DOWN | 2.9 min | +0.455% | 3¢ | ❌ Lost | -$0.15 |
| 11/21 6:27:07 AM | BNB | DOWN | 2.9 min | +0.406% | 1¢ | ❌ Lost | $0.00 |
| 11/21 6:26:38 AM | BTC | DOWN | 3.4 min | +0.601% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:26:38 AM | XRP | DOWN | 3.4 min | +0.551% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:12:03 AM | XRP | DOWN | 3.0 min | +0.420% | 1¢ | ❌ Lost | -$0.15 |
| 11/21 6:11:31 AM | ETH | DOWN | 3.5 min | +0.611% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
