# 15-Minute 1¢ Study

*Updated Wed Nov 25, 9:11 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4882 finished bets | 1% | $210.10 | +39% | +4.30¢ | $88.00 / $122.10 |

*Expect about **84 buys a day** (~$12.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4625 | $109.25 | +22% |
| Volatility model ≥ 2%, hold to the close | 9094 | $36.55 | +3% |
| Momentum model ≥ 2%, hold to the close | 7565 | -$33.05 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 67425 | 67391 | 255 (0%) | 1.07% | -$4,588.80 (-56%) | Hold to the close: -$4,588.80 (-56%) |

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
| Volatility model | 40003 | 4.5% | 0.4% (164) | -649% | ❌ Worse |
| Momentum model | 40003 | 4.4% | 0.4% (164) | -671% | ❌ Worse |
| Mean-reversion model | 40003 | 7.9% | 0.4% (164) | -788% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40003 | 164 | -47% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 9094 | 80 | +3% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4882 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2826 | 32 | +67% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7565 | 59 | -4% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4625 | 43 | +22% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3017 | 28 | +34% | -68% | -68% | -63% |
| Mean-reversion model ≥ 2% | 16277 | 112 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11331 | 92 | -10% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7530 | 66 | +0% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40209 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16028 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11154 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 67391 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 255 | 0% | -$4,588.80 | -56% | — |
| Sell at 2¢ | 2762 | 4% | -$7,146.68 | -88% | 47 sec |
| Sell at 3¢ | 1857 | 3% | -$7,140.57 | -88% | 48 sec |
| Sell at 5¢ | 1257 | 2% | -$7,019.75 | -86% | 62 sec |
| Sell at 10¢ | 768 | 1% | -$6,746.72 | -83% | 65 sec |
| Sell at 25¢ | 414 | 1% | -$6,228.46 | -76% | 80 sec |
| Sell at 50¢ | 265 | 0% | -$5,628.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3475 | 17 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 21850 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16827 | 57 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25226 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4496 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4490 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4484 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4477 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4474 | 12 | 4% | 2% | -65% | -89% | -89% |
| ETH | 4468 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4447 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4442 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4431 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2372 | 8 | 5% | 2% | -59% | -82% | -84% |
| WTI | 2359 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2313 | 9 | 5% | 2% | -53% | -83% | -84% |
| PLATINUM | 2100 | 5 | 3% | 1% | -78% | -95% | -95% |
| EURUSD | 2056 | 7 | 3% | 1% | -68% | -91% | -90% |
| GBPUSD | 1994 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 1993 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1956 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1949 | 10 | 2% | 1% | -52% | -77% | -77% |
| PALLADIUM | 1887 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1514 | 7 | 2% | 1% | -57% | -90% | -90% |
| USDCAD | 1427 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1055 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 545 | 2 | 3% | 1% | -66% | -77% | -76% |
| 30YRRATE | 506 | 0 | 3% | 1% | -100% | -96% | -93% |
| 2YRRATE | 505 | 4 | 4% | 2% | -26% | -57% | -56% |
| 5YRRATE | 495 | 2 | 4% | 2% | -62% | -94% | -95% |
| INX | 128 | 1 | 2% | 1% | -27% | -97% | -98% |
| USDMXN | 28 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34495 | 131 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32896 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5842 | 25 | 2% | 1% | -21% | -79% | -78% |
| 0.05–0.1% | 6388 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 9990 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12679 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5301 | 23 | 7% | 3% | -54% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15862 | 81 | 4% | 2% | -42% | -85% | -85% |
| Afternoon (12–6pm) | 16634 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18565 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,110 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 8:59:35 AM | GBPUSD | UP | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:59:16 AM | SILVER | DOWN | 44 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:59:16 AM | 5YRRATE | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:59:00 AM | USDCAD | DOWN | 60 sec | — | 4¢ | ❌ Lost | -$0.15 |
| 11/25 8:59:00 AM | EURUSD | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:58:44 AM | USDMXN | UP | 76 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:58:09 AM | BTC | DOWN | 1.9 min | +0.377% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:58:09 AM | HYPE | DOWN | 1.9 min | +0.470% | 2¢ | ❌ Lost | -$0.15 |
| 11/25 8:58:09 AM | BNB | DOWN | 1.9 min | +0.316% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:58:09 AM | ETH | DOWN | 1.9 min | +0.438% | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:57:37 AM | AUDUSD | UP | 2.4 min | — | 5¢ | ❌ Lost | -$0.15 |
| 11/25 8:56:48 AM | PALLADIUM | DOWN | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:56:48 AM | 10YRRATE | UP | 3.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:56:16 AM | ZEC | DOWN | 3.7 min | +1.138% | 2¢ | ❌ Lost | -$0.15 |
| 11/25 8:56:16 AM | BRENT | DOWN | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:56:16 AM | NATGAS | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:55:56 AM | SOL | DOWN | 4.1 min | +1.125% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:55:56 AM | WTI | DOWN | 4.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:55:40 AM | DOGE | DOWN | 4.3 min | +0.764% | 1¢ | ❌ Lost | $0.00 |
| 11/25 8:55:40 AM | NEAR | DOWN | 4.3 min | +0.968% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:54:32 AM | 30YRRATE | UP | 5.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:54:16 AM | XRP | DOWN | 5.7 min | +0.936% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:52 AM | USDJPY | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:52 AM | INX | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:52 AM | SILVER | DOWN | 7 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 8:44:52 AM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:52 AM | 30YRRATE | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:36 AM | WTI | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:36 AM | PALLADIUM | UP | 24 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 8:44:36 AM | USDMXN | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
