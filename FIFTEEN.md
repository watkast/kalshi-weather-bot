# 15-Minute 1¢ Study

*Updated Tue Nov 24, 1:54 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4833 finished bets | 1% | $214.45 | +41% | +4.44¢ | $76.70 / $137.75 |

*Expect about **85 buys a day** (~$12.70/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4578 | $113.00 | +23% |
| Volatility model ≥ 2%, hold to the close | 8996 | $46.90 | +4% |
| Momentum model ≥ 2%, hold to the close | 7494 | -$26.45 | -3% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 66318 | 66284 | 254 (0%) | 1.07% | -$4,470.20 (-56%) | Hold to the close: -$4,470.20 (-56%) |

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
| Volatility model | 39504 | 4.5% | 0.4% (164) | -642% | ❌ Worse |
| Momentum model | 39504 | 4.4% | 0.4% (164) | -664% | ❌ Worse |
| Mean-reversion model | 39504 | 7.9% | 0.4% (164) | -779% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 39504 | 164 | -46% | -87% | -86% | -84% |
| Volatility model ≥ 2% | 8996 | 80 | +4% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4833 | 53 | +41% | -73% | -71% | -68% |
| Volatility model ≥ 10% | 2799 | 32 | +69% | -64% | -63% | -59% |
| Momentum model ≥ 2% | 7494 | 59 | -3% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 4578 | 43 | +23% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 2985 | 28 | +35% | -68% | -67% | -63% |
| Mean-reversion model ≥ 2% | 16068 | 112 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 11182 | 92 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7429 | 66 | +2% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 39710 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 15719 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 10855 | 3% | 2% | 1% | 1% | 0% | 0% |
| **All** | 66284 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 254 | 0% | -$4,470.20 | -56% | — |
| Sell at 2¢ | 2716 | 4% | -$7,026.04 | -88% | 47 sec |
| Sell at 3¢ | 1828 | 3% | -$7,019.28 | -87% | 48 sec |
| Sell at 5¢ | 1247 | 2% | -$6,893.65 | -86% | 62 sec |
| Sell at 10¢ | 764 | 1% | -$6,619.36 | -82% | 65 sec |
| Sell at 25¢ | 410 | 1% | -$6,109.10 | -76% | 79 sec |
| Sell at 50¢ | 263 | 0% | -$5,508.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3425 | 17 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 21493 | 115 | 7% | 3% | -47% | -86% | -86% |
| 1–2 min | 16564 | 57 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 24789 | 65 | 1% | 0% | -62% | -87% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4439 | 19 | 5% | 2% | -43% | -88% | -87% |
| HYPE | 4433 | 16 | 5% | 2% | -53% | -89% | -88% |
| SOL | 4431 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4422 | 22 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 4418 | 12 | 5% | 2% | -65% | -89% | -89% |
| ETH | 4413 | 19 | 7% | 3% | -46% | -82% | -82% |
| BTC | 4392 | 24 | 5% | 2% | -25% | -86% | -87% |
| NEAR | 4387 | 18 | 5% | 2% | -46% | -85% | -86% |
| XRP | 4375 | 16 | 4% | 2% | -53% | -89% | -88% |
| GOLD | 2329 | 8 | 5% | 2% | -58% | -82% | -84% |
| WTI | 2315 | 8 | 4% | 2% | -58% | -91% | -92% |
| SILVER | 2272 | 9 | 5% | 2% | -52% | -83% | -84% |
| PLATINUM | 2064 | 5 | 3% | 1% | -77% | -95% | -95% |
| EURUSD | 2025 | 7 | 3% | 1% | -68% | -91% | -90% |
| COPPER | 1954 | 6 | 2% | 1% | -71% | -78% | -78% |
| GBPUSD | 1954 | 8 | 2% | 1% | -62% | -96% | -96% |
| USDJPY | 1919 | 6 | 2% | 1% | -71% | -96% | -96% |
| NATGAS | 1915 | 10 | 2% | 1% | -51% | -77% | -76% |
| PALLADIUM | 1854 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1472 | 6 | 2% | 1% | -62% | -90% | -90% |
| USDCAD | 1390 | 1 | 3% | 1% | -93% | -96% | -96% |
| BRENT | 1016 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 523 | 2 | 3% | 1% | -64% | -77% | -75% |
| 2YRRATE | 495 | 4 | 4% | 2% | -25% | -56% | -55% |
| 30YRRATE | 482 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 474 | 2 | 4% | 1% | -61% | -94% | -96% |
| INX | 112 | 1 | 2% | 1% | -17% | -97% | -98% |
| USDMXN | 9 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 33907 | 130 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 32377 | 124 | 4% | 2% | -56% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5799 | 25 | 2% | 1% | -21% | -78% | -78% |
| 0.05–0.1% | 6334 | 26 | 3% | 2% | -35% | -91% | -90% |
| 0.1–0.2% | 9871 | 36 | 5% | 2% | -52% | -89% | -89% |
| 0.2–0.5% | 12497 | 56 | 7% | 3% | -49% | -86% | -86% |
| Over 0.5% | 5200 | 23 | 7% | 3% | -54% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16137 | 49 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 15586 | 81 | 4% | 2% | -41% | -85% | -85% |
| Afternoon (12–6pm) | 16344 | 73 | 4% | 2% | -47% | -87% | -87% |
| Evening (6pm–12am) | 18217 | 51 | 4% | 2% | -68% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,134 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/24 1:44:00 AM | BRENT | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:44 AM | WTI | UP | 75 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:43:44 AM | XRP | DOWN | 75 sec | +0.212% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:43:44 AM | SOL | DOWN | 75 sec | +0.211% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:43:44 AM | 30YRRATE | UP | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:28 AM | USDMXN | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:28 AM | BTC | DOWN | 1.5 min | +0.249% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:43:12 AM | HYPE | DOWN | 1.8 min | +0.299% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:42:56 AM | ETH | DOWN | 2.1 min | +0.293% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:42:40 AM | DOGE | DOWN | 2.3 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:42:40 AM | USDCAD | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:42:24 AM | AUDUSD | DOWN | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:41:50 AM | BNB | DOWN | 3.2 min | +0.146% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:41:50 AM | NEAR | DOWN | 3.2 min | +0.372% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:41:34 AM | COPPER | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:41:18 AM | SILVER | DOWN | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:41:18 AM | ZEC | DOWN | 3.7 min | +0.710% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:40:47 AM | 2YRRATE | UP | 4.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/24 1:40:47 AM | EURUSD | DOWN | 4.2 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/24 1:40:31 AM | 5YRRATE | UP | 4.5 min | — | 2¢ | ❌ Lost | -$0.15 |
| 11/24 1:40:15 AM | GBPUSD | DOWN | 4.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:38:54 AM | GOLD | DOWN | 6.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:37:33 AM | 10YRRATE | UP | 7.4 min | — | 3¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:35 AM | GBPUSD | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:19 AM | AUDUSD | UP | 41 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:19 AM | XRP | UP | 41 sec | -0.201% | 0¢ | ❌ Lost | $0.00 |
| 11/24 1:29:04 AM | DOGE | UP | 55 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:29:04 AM | HYPE | UP | 55 sec | -0.222% | 0¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:46 AM | BRENT | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/24 1:28:46 AM | USDJPY | UP | 74 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
