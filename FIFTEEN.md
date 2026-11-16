# 15-Minute 1¢ Study

*Updated Mon Nov 16, 3:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4440 finished bets | 1% | $223.35 | +46% | +5.03¢ | $85.20 / $138.15 |

*Expect about **89 buys a day** (~$13.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4193 | $121.30 | +27% |
| Volatility model ≥ 2%, hold to the close | 8261 | $85.00 | +9% |
| Momentum model ≥ 2%, hold to the close | 6872 | $9.75 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 58985 | 58951 | 227 (0%) | 1.07% | -$3,991.55 (-56%) | Hold to the close: -$3,991.55 (-56%) |

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
| Volatility model | 35480 | 4.6% | 0.4% (148) | -636% | ❌ Worse |
| Momentum model | 35480 | 4.5% | 0.4% (148) | -661% | ❌ Worse |
| Mean-reversion model | 35480 | 7.9% | 0.4% (148) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 35480 | 148 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 8261 | 77 | +9% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4440 | 51 | +46% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2556 | 30 | +70% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 6872 | 57 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 4193 | 41 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 2731 | 26 | +35% | -66% | -66% | -62% |
| Mean-reversion model ≥ 2% | 14521 | 103 | -22% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 10103 | 85 | -7% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6705 | 61 | +4% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 35686 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 13969 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 9296 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 58951 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 227 | 0% | -$3,991.55 | -56% | — |
| Sell at 2¢ | 2368 | 4% | -$6,259.87 | -87% | 47 sec |
| Sell at 3¢ | 1596 | 3% | -$6,253.11 | -87% | 48 sec |
| Sell at 5¢ | 1093 | 2% | -$6,137.10 | -86% | 62 sec |
| Sell at 10¢ | 667 | 1% | -$5,889.78 | -82% | 65 sec |
| Sell at 25¢ | 353 | 1% | -$5,469.12 | -76% | 80 sec |
| Sell at 50¢ | 234 | 0% | -$4,932.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 2944 | 13 | 11% | 4% | -58% | -81% | -83% |
| 2–5 min | 19070 | 104 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 14846 | 51 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 22078 | 59 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3994 | 19 | 5% | 3% | -38% | -88% | -87% |
| SOL | 3989 | 18 | 4% | 2% | -42% | -86% | -87% |
| HYPE | 3981 | 12 | 4% | 2% | -62% | -89% | -88% |
| DOGE | 3971 | 11 | 4% | 2% | -65% | -90% | -89% |
| BNB | 3971 | 20 | 5% | 2% | -36% | -86% | -85% |
| ETH | 3962 | 17 | 6% | 3% | -47% | -82% | -82% |
| BTC | 3945 | 21 | 5% | 2% | -28% | -86% | -88% |
| NEAR | 3943 | 17 | 5% | 2% | -44% | -85% | -86% |
| XRP | 3930 | 15 | 3% | 2% | -52% | -89% | -88% |
| GOLD | 2089 | 5 | 5% | 2% | -71% | -82% | -84% |
| WTI | 2071 | 7 | 4% | 1% | -59% | -91% | -92% |
| SILVER | 2033 | 9 | 5% | 2% | -47% | -83% | -83% |
| PLATINUM | 1855 | 4 | 3% | 1% | -80% | -95% | -95% |
| EURUSD | 1801 | 6 | 2% | 1% | -69% | -90% | -90% |
| COPPER | 1733 | 6 | 2% | 1% | -68% | -75% | -75% |
| GBPUSD | 1726 | 6 | 2% | 1% | -68% | -96% | -96% |
| NATGAS | 1709 | 9 | 2% | 1% | -51% | -75% | -74% |
| USDJPY | 1686 | 6 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1665 | 4 | 1% | 0% | -78% | -93% | -93% |
| AUDUSD | 1245 | 6 | 2% | 1% | -55% | -89% | -89% |
| USDCAD | 1190 | 1 | 3% | 1% | -92% | -96% | -96% |
| BRENT | 814 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 418 | 2 | 4% | 1% | -55% | -71% | -70% |
| 2YRRATE | 403 | 4 | 4% | 2% | -7% | -47% | -46% |
| 30YRRATE | 388 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 375 | 2 | 4% | 2% | -50% | -94% | -95% |
| INX | 64 | 0 | 2% | 0% | -100% | -97% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 29987 | 113 | 4% | 2% | -57% | -88% | -88% |
| DOWN (bought NO) | 28964 | 114 | 4% | 2% | -55% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5416 | 25 | 2% | 1% | -17% | -78% | -77% |
| 0.05–0.1% | 5856 | 24 | 3% | 2% | -36% | -91% | -90% |
| 0.1–0.2% | 8959 | 34 | 5% | 2% | -51% | -89% | -89% |
| 0.2–0.5% | 11012 | 48 | 7% | 3% | -51% | -86% | -86% |
| Over 0.5% | 4434 | 19 | 7% | 3% | -55% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 14411 | 45 | 4% | 2% | -64% | -88% | -88% |
| Morning (6am–12pm) | 13940 | 70 | 4% | 2% | -43% | -85% | -84% |
| Afternoon (12–6pm) | 14543 | 63 | 4% | 2% | -49% | -87% | -87% |
| Evening (6pm–12am) | 16057 | 49 | 4% | 2% | -65% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,075 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/16 3:28:20 PM | XRP | UP | 1.6 min | -0.208% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:28:20 PM | ETH | UP | 1.6 min | -0.183% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:28:20 PM | DOGE | UP | 1.6 min | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:28:20 PM | BNB | UP | 1.6 min | -0.162% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:28:04 PM | SOL | UP | 1.9 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:28:04 PM | BTC | UP | 1.9 min | -0.168% | 0¢ | ❌ Lost | $0.00 |
| 11/16 3:26:59 PM | NEAR | UP | 3.0 min | -0.617% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:26:59 PM | ZEC | UP | 3.0 min | -0.585% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:26:25 PM | HYPE | UP | 3.6 min | -1.012% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:44 PM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:14:44 PM | NATGAS | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:12:50 PM | BTC | DOWN | 2.1 min | +0.266% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:12:34 PM | HYPE | DOWN | 2.4 min | +0.786% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 3:12:34 PM | DOGE | DOWN | 2.4 min | +0.303% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:12:02 PM | SOL | DOWN | 3.0 min | +0.281% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:12:02 PM | NEAR | DOWN | 3.0 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:11:45 PM | BNB | DOWN | 3.2 min | +0.206% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:11:29 PM | XRP | DOWN | 3.5 min | +0.376% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:10:56 PM | ZEC | DOWN | 4.0 min | +0.868% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 3:10:56 PM | ETH | DOWN | 4.0 min | +0.310% | 1¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:49 PM | 2YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:49 PM | SOL | DOWN | 10 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:59:49 PM | ZEC | UP | 10 sec | -0.146% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:59:49 PM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:49 PM | BTC | DOWN | 10 sec | +0.005% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:59:33 PM | NATGAS | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:33 PM | NEAR | UP | 26 sec | -0.185% | 0¢ | ❌ Lost | -$0.15 |
| 11/16 2:59:33 PM | DOGE | UP | 26 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:59:33 PM | BNB | UP | 26 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/16 2:59:17 PM | XRP | DOWN | 43 sec | +0.073% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
