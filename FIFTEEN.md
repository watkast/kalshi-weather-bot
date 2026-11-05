# 15-Minute 1¢ Study

*Updated Thu Nov 5, 4:10 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3692 finished bets | 1% | $135.00 | +33% | +3.66¢ | $88.80 / $46.20 |

*Expect about **97 buys a day** (~$14.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3432 | $62.45 | +17% |
| Volatility model ≥ 2%, hold to the close | 6836 | $43.45 | +5% |
| Momentum model ≥ 2%, hold to the close | 5643 | -$33.35 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46369 | 46358 | 170 (0%) | 1.07% | -$3,272.15 (-58%) | Hold to the close: -$3,272.15 (-58%) |

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
| Volatility model | 28206 | 4.7% | 0.4% (110) | -683% | ❌ Worse |
| Momentum model | 28206 | 4.6% | 0.4% (110) | -710% | ❌ Worse |
| Mean-reversion model | 28206 | 8.1% | 0.4% (110) | -831% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28206 | 110 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6836 | 62 | +5% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3692 | 39 | +33% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2107 | 24 | +64% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5643 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3432 | 31 | +17% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2242 | 20 | +25% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11670 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8189 | 69 | -7% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5487 | 49 | +1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28411 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11081 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6866 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46358 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,272.15 | -58% | — |
| Sell at 2¢ | 1817 | 4% | -$4,927.73 | -87% | 47 sec |
| Sell at 3¢ | 1241 | 3% | -$4,916.16 | -87% | 48 sec |
| Sell at 5¢ | 858 | 2% | -$4,814.45 | -85% | 63 sec |
| Sell at 10¢ | 519 | 1% | -$4,608.26 | -82% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,285.76 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,910.40 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2291 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 14931 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11663 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17462 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3182 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3177 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3171 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3171 | 17 | 5% | 2% | -33% | -85% | -85% |
| DOGE | 3158 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3152 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3136 | 16 | 5% | 2% | -34% | -84% | -84% |
| BTC | 3136 | 15 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3128 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1713 | 5 | 5% | 2% | -64% | -81% | -83% |
| SILVER | 1664 | 8 | 5% | 2% | -43% | -82% | -82% |
| WTI | 1663 | 5 | 4% | 1% | -64% | -92% | -93% |
| PLATINUM | 1492 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1433 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1410 | 6 | 2% | 1% | -60% | -71% | -70% |
| GBPUSD | 1361 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1350 | 8 | 2% | 1% | -45% | -76% | -75% |
| USDJPY | 1342 | 5 | 2% | 1% | -65% | -97% | -97% |
| PALLADIUM | 1340 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 888 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 865 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 449 | 0 | 1% | 1% | -100% | -98% | -97% |
| 10YRRATE | 262 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 246 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 244 | 2 | 3% | 0% | -23% | -18% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23515 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22843 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4567 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4839 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7324 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8471 | 33 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3202 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11350 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12626 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,679 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 3:59:46 AM | USDCAD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:59:46 AM | WTI | UP | 14 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:59:14 AM | GBPUSD | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:59:14 AM | PALLADIUM | DOWN | 46 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:59:14 AM | ETH | UP | 46 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:59:14 AM | SOL | UP | 46 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:59:14 AM | BNB | DOWN | 46 sec | -0.022% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:58:57 AM | USDJPY | UP | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:58:42 AM | COPPER | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:58:26 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:58:26 AM | HYPE | UP | 1.6 min | -0.301% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:58:10 AM | BTC | UP | 1.8 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:58:10 AM | DOGE | UP | 1.8 min | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:57:54 AM | XRP | UP | 2.1 min | -0.174% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:57:54 AM | ZEC | UP | 2.1 min | -0.399% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:57:54 AM | NEAR | UP | 2.1 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:49 AM | USDJPY | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:49 AM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:33 AM | GBPUSD | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:33 AM | ETH | UP | 26 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:44:33 AM | 2YRRATE | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:33 AM | 10YRRATE | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:17 AM | XRP | UP | 42 sec | -0.106% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:44:17 AM | BNB | UP | 42 sec | -0.094% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:44:01 AM | HYPE | UP | 58 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:43:30 AM | ZEC | UP | 1.5 min | -0.334% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:43:30 AM | SOL | UP | 1.5 min | -0.186% | 0¢ | ❌ Lost | $0.00 |
| 11/5 3:43:30 AM | DOGE | UP | 1.5 min | -0.139% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 3:42:58 AM | PALLADIUM | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 3:42:58 AM | EURUSD | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
