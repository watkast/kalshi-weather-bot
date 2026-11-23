# 15-Minute 1¢ Study

*Updated Mon Nov 23, 5:30 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4796 finished bets | 1% | $218.35 | +42% | +4.55¢ | $78.65 / $139.70 |

*Expect about **85 buys a day** (~$12.79/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4550 | $115.40 | +24% |
| Volatility model ≥ 2%, hold to the close | 8936 | $53.65 | +5% |
| Momentum model ≥ 2%, hold to the close | 7450 | -$22.10 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 65557 | 65506 | 252 (0%) | 1.07% | -$4,403.70 (-56%) | Hold to the close: -$4,403.70 (-56%) |

*In play or awaiting result: 23. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 39147 | 4.5% | 0.4% (163) | -642% | ❌ Worse |
| Momentum model | 39147 | 4.4% | 0.4% (163) | -665% | ❌ Worse |
| Mean-reversion model | 39147 | 7.9% | 0.4% (163) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39147 | 163 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8936 | 80 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4796 | 53 | +42% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2775 | 32 | +70% | -64% | -62% | -59% |
| Momentum model ≥ 2% | 7450 | 59 | -3% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 4550 | 43 | +24% | -75% | -74% | -71% |
| Momentum model ≥ 10% | 2963 | 28 | +36% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 15936 | 111 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11085 | 91 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7367 | 66 | +2% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39353 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15491 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10662 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 65506 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 252 | 0% | -$4,403.70 | -56% | — |
| Sell at 2¢ | 2681 | 4% | -$6,940.64 | -88% | 47 sec |
| Sell at 3¢ | 1807 | 3% | -$6,932.97 | -87% | 48 sec |
| Sell at 5¢ | 1235 | 2% | -$6,806.95 | -86% | 61 sec |
| Sell at 10¢ | 757 | 1% | -$6,534.03 | -82% | 65 sec |
| Sell at 25¢ | 407 | 1% | -$6,024.53 | -76% | 79 sec |
| Sell at 50¢ | 260 | 0% | -$5,434.70 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3392 | 17 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 21222 | 113 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16372 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24507 | 65 | 1% | 0% | -62% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4400 | 19 | 5% | 2% | -42% | -88% | -87% |
| HYPE | 4393 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4391 | 20 | 5% | 2% | -41% | -86% | -86% |
| BNB | 4383 | 22 | 5% | 2% | -36% | -86% | -85% |
| DOGE | 4378 | 11 | 4% | 2% | -68% | -89% | -89% |
| ETH | 4374 | 19 | 7% | 3% | -45% | -82% | -82% |
| BTC | 4351 | 24 | 6% | 2% | -24% | -86% | -87% |
| NEAR | 4347 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4336 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2299 | 8 | 5% | 2% | -57% | -82% | -84% |
| WTI | 2280 | 8 | 4% | 2% | -57% | -91% | -92% |
| SILVER | 2243 | 9 | 5% | 2% | -52% | -83% | -83% |
| PLATINUM | 2037 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 1995 | 7 | 3% | 1% | -67% | -91% | -90% |
| GBPUSD | 1930 | 8 | 2% | 1% | -61% | -96% | -96% |
| COPPER | 1924 | 6 | 2% | 1% | -71% | -77% | -77% |
| NATGAS | 1887 | 10 | 2% | 1% | -51% | -77% | -76% |
| USDJPY | 1887 | 6 | 2% | 1% | -70% | -97% | -96% |
| PALLADIUM | 1831 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1441 | 6 | 2% | 1% | -61% | -90% | -90% |
| USDCAD | 1366 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 990 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 511 | 2 | 3% | 1% | -63% | -76% | -75% |
| 2YRRATE | 485 | 4 | 4% | 2% | -23% | -55% | -54% |
| 30YRRATE | 473 | 0 | 3% | 1% | -100% | -96% | -93% |
| 5YRRATE | 462 | 2 | 3% | 2% | -60% | -94% | -95% |
| INX | 108 | 1 | 2% | 1% | -14% | -97% | -98% |
| USDMXN | 4 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33514 | 129 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 31992 | 123 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5763 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6299 | 26 | 3% | 2% | -34% | -91% | -90% |
| 0.1–0.2% | 9793 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12331 | 55 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5158 | 23 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 15924 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 15984 | 71 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18012 | 51 | 4% | 2% | -67% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,143 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/23 5:29:47 AM | BTC | DOWN | 12 sec | +0.020% | 0¢ | In play | — |
| 11/23 5:29:15 AM | SOL | UP | 45 sec | -0.141% | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:29:15 AM | SILVER | UP | 45 sec | — | 2¢ | In play | — |
| 11/23 5:29:15 AM | BNB | DOWN | 45 sec | +0.023% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:29:15 AM | GBPUSD | DOWN | 45 sec | — | 0¢ | In play | — |
| 11/23 5:29:15 AM | AUDUSD | UP | 45 sec | — | 0¢ | In play | — |
| 11/23 5:28:40 AM | BRENT | UP | 80 sec | — | 0¢ | In play | — |
| 11/23 5:28:24 AM | PLATINUM | UP | 1.6 min | — | 0¢ | In play | — |
| 11/23 5:28:09 AM | USDCAD | DOWN | 1.8 min | — | 3¢ | In play | — |
| 11/23 5:28:09 AM | DOGE | UP | 1.8 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:27:52 AM | NEAR | UP | 2.1 min | -0.343% | 0¢ | In play | — |
| 11/23 5:27:52 AM | WTI | UP | 2.1 min | — | 1¢ | In play | — |
| 11/23 5:27:20 AM | HYPE | UP | 2.6 min | -0.326% | 1¢ | In play | — |
| 11/23 5:27:04 AM | 30YRRATE | UP | 2.9 min | — | 0¢ | In play | — |
| 11/23 5:27:04 AM | PALLADIUM | UP | 2.9 min | — | 0¢ | In play | — |
| 11/23 5:26:47 AM | COPPER | UP | 3.2 min | — | 0¢ | In play | — |
| 11/23 5:26:31 AM | USDJPY | UP | 3.5 min | — | 0¢ | In play | — |
| 11/23 5:25:59 AM | 5YRRATE | UP | 4.0 min | — | 0¢ | In play | — |
| 11/23 5:25:59 AM | 10YRRATE | UP | 4.0 min | — | 0¢ | In play | — |
| 11/23 5:25:59 AM | ZEC | UP | 4.0 min | -0.577% | 1¢ | ❌ Lost | -$0.15 |
| 11/23 5:25:42 AM | 2YRRATE | UP | 4.3 min | — | 1¢ | In play | — |
| 11/23 5:14:46 AM | 30YRRATE | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:30 AM | 2YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:30 AM | NEAR | UP | 30 sec | -0.356% | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:14:30 AM | 5YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:30 AM | 10YRRATE | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:14:15 AM | USDJPY | UP | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:13:56 AM | GOLD | UP | 63 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/23 5:13:40 AM | SOL | UP | 79 sec | -0.187% | 0¢ | ❌ Lost | -$0.15 |
| 11/23 5:13:40 AM | DOGE | UP | 79 sec | -0.169% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
