# 15-Minute 1¢ Study

*Updated Sat Oct 24, 3:09 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2555 finished bets | 1% | $102.50 | +35% | +4.01¢ | $42.35 / $60.15 |

*Expect about **98 buys a day** (~$14.68/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2361 | $74.85 | +29% |
| Volatility model ≥ 2%, hold to the close | 4724 | $23.60 | +4% |
| Momentum model ≥ 2%, hold to the close | 3933 | -$0.15 | -0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 30753 | 30745 | 119 (0%) | 1.07% | -$2,080.10 (-56%) | Hold to the close: -$2,080.10 (-56%) |

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
| Volatility model | 19538 | 4.7% | 0.4% (84) | -630% | ❌ Worse |
| Momentum model | 19538 | 4.6% | 0.4% (84) | -657% | ❌ Worse |
| Mean-reversion model | 19538 | 7.9% | 0.4% (84) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 19538 | 84 | -46% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4724 | 43 | +4% | -78% | -76% | -73% |
| Volatility model ≥ 5% | 2555 | 28 | +35% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 1457 | 18 | +73% | -64% | -63% | -60% |
| Momentum model ≥ 2% | 3933 | 33 | -0% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 2361 | 24 | +29% | -76% | -75% | -71% |
| Momentum model ≥ 10% | 1547 | 16 | +42% | -69% | -68% | -63% |
| Mean-reversion model ≥ 2% | 7851 | 55 | -24% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5489 | 46 | -8% | -81% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3652 | 33 | +2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 19738 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 7352 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3655 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 30745 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 119 | 0% | -$2,080.10 | -56% | — |
| Sell at 2¢ | 1146 | 4% | -$3,280.14 | -88% | 47 sec |
| Sell at 3¢ | 787 | 3% | -$3,271.17 | -87% | 48 sec |
| Sell at 5¢ | 552 | 2% | -$3,219.30 | -86% | 61 sec |
| Sell at 10¢ | 340 | 1% | -$3,090.70 | -83% | 64 sec |
| Sell at 25¢ | 187 | 1% | -$2,847.13 | -76% | 82 sec |
| Sell at 50¢ | 121 | 0% | -$2,565.35 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1313 | 7 | 11% | 4% | -49% | -80% | -82% |
| 2–5 min | 9811 | 54 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 7814 | 30 | 3% | 1% | -58% | -92% | -91% |
| Under 1 min | 11803 | 28 | 1% | 0% | -66% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2212 | 12 | 5% | 2% | -32% | -89% | -89% |
| HYPE | 2204 | 8 | 5% | 3% | -55% | -88% | -86% |
| BNB | 2202 | 12 | 5% | 2% | -32% | -83% | -82% |
| SOL | 2197 | 6 | 4% | 2% | -66% | -92% | -92% |
| ETH | 2194 | 11 | 6% | 3% | -40% | -86% | -85% |
| DOGE | 2188 | 4 | 4% | 2% | -77% | -90% | -90% |
| XRP | 2184 | 9 | 3% | 1% | -49% | -88% | -88% |
| NEAR | 2180 | 12 | 5% | 3% | -28% | -81% | -81% |
| BTC | 2177 | 12 | 5% | 2% | -26% | -88% | -89% |
| GOLD | 1190 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1156 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1143 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1010 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 987 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 938 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 933 | 5 | 2% | 1% | -50% | -86% | -86% |
| PALLADIUM | 897 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 884 | 1 | 2% | 1% | -89% | -96% | -96% |
| USDJPY | 866 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 428 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 387 | 0 | 1% | 0% | -100% | -98% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 36 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 15538 | 65 | 4% | 2% | -52% | -87% | -86% |
| DOWN (bought NO) | 15207 | 54 | 4% | 2% | -59% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3286 | 18 | 2% | 1% | -8% | -79% | -79% |
| 0.05–0.1% | 3400 | 11 | 3% | 2% | -52% | -92% | -92% |
| 0.1–0.2% | 5083 | 19 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 5761 | 28 | 6% | 3% | -47% | -87% | -86% |
| Over 0.5% | 2204 | 10 | 7% | 3% | -53% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7637 | 32 | 4% | 2% | -52% | -85% | -84% |
| Morning (6am–12pm) | 7425 | 34 | 4% | 2% | -48% | -88% | -87% |
| Afternoon (12–6pm) | 7298 | 24 | 4% | 2% | -61% | -87% | -88% |
| Evening (6pm–12am) | 8385 | 29 | 3% | 2% | -60% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,647 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/24 2:59:29 AM | BNB | DOWN | 30 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:59:29 AM | ZEC | UP | 30 sec | -0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:59:29 AM | SOL | DOWN | 30 sec | -0.001% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:58:49 AM | ETH | DOWN | 70 sec | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:58:33 AM | NEAR | UP | 86 sec | -0.364% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:58:33 AM | DOGE | UP | 86 sec | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:58:01 AM | BTC | DOWN | 2.0 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:57:12 AM | HYPE | UP | 2.8 min | -0.381% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:44:06 AM | NEAR | UP | 54 sec | -0.312% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:43:32 AM | DOGE | UP | 88 sec | -0.148% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:43:32 AM | XRP | UP | 88 sec | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:43:01 AM | ZEC | UP | 2.0 min | -0.271% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:43:01 AM | SOL | UP | 2.0 min | -0.145% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:42:45 AM | BTC | UP | 2.2 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:42:13 AM | ETH | UP | 2.8 min | -0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:41:24 AM | BNB | UP | 3.6 min | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:41:24 AM | HYPE | UP | 3.6 min | -0.587% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:29:59 AM | XRP | DOWN | 0 sec | -0.008% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:29:43 AM | HYPE | DOWN | 16 sec | +0.000% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:29:27 AM | BNB | UP | 32 sec | -0.046% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 2:29:27 AM | ETH | UP | 32 sec | -0.057% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 2:29:11 AM | NEAR | UP | 49 sec | -0.320% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:29:11 AM | ZEC | UP | 49 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:29:11 AM | BTC | DOWN | 49 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:29:11 AM | DOGE | DOWN | 49 sec | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/24 2:28:39 AM | SOL | DOWN | 81 sec | +0.128% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:14:54 AM | ETH | DOWN | 5 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 2:14:54 AM | HYPE | UP | 5 sec | -0.011% | 0¢ | ❌ Lost | -$0.15 |
| 10/24 2:14:38 AM | BNB | UP | 21 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 10/24 2:14:38 AM | NEAR | DOWN | 21 sec | +0.046% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
