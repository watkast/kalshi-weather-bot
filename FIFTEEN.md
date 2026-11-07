# 15-Minute 1¢ Study

*Updated Fri Nov 6, 10:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3838 finished bets | 1% | $120.30 | +28% | +3.13¢ | $79.50 / $40.80 |

*Expect about **96 buys a day** (~$14.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3568 | $49.10 | +13% |
| Volatility model ≥ 2%, hold to the close | 7081 | $16.45 | +2% |
| Momentum model ≥ 2%, hold to the close | 5843 | -$54.50 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48533 | 48516 | 175 (0%) | 1.07% | -$3,464.80 (-59%) | Hold to the close: -$3,464.80 (-59%) |

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
| Volatility model | 29273 | 4.7% | 0.4% (111) | -704% | ❌ Worse |
| Momentum model | 29273 | 4.6% | 0.4% (111) | -730% | ❌ Worse |
| Mean-reversion model | 29273 | 8.1% | 0.4% (111) | -854% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29273 | 111 | -52% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7081 | 62 | +2% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3838 | 39 | +28% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2199 | 24 | +57% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5843 | 44 | -8% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3568 | 31 | +13% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2334 | 20 | +21% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12120 | 80 | -28% | -84% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8497 | 69 | -10% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5679 | 49 | -2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29478 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48516 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,464.80 | -59% | — |
| Sell at 2¢ | 1905 | 4% | -$5,167.50 | -87% | 47 sec |
| Sell at 3¢ | 1297 | 3% | -$5,156.97 | -87% | 48 sec |
| Sell at 5¢ | 900 | 2% | -$5,049.80 | -85% | 63 sec |
| Sell at 10¢ | 541 | 1% | -$4,842.09 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,505.38 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,125.80 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2400 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15596 | 83 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12220 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18288 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3304 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3298 | 12 | 4% | 2% | -54% | -90% | -90% |
| HYPE | 3287 | 10 | 5% | 2% | -62% | -89% | -87% |
| BNB | 3286 | 17 | 5% | 2% | -35% | -85% | -84% |
| DOGE | 3277 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3274 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3253 | 16 | 5% | 2% | -36% | -84% | -85% |
| BTC | 3252 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3247 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1751 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1433 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 524 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24604 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23912 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4719 | 22 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 5005 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7575 | 26 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8824 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3347 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13105 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,667 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 10:14:59 PM | DOGE | DOWN | 0 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:59 PM | XRP | DOWN | 0 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:27 PM | BTC | DOWN | 32 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:27 PM | HYPE | UP | 32 sec | -0.063% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:27 PM | NEAR | DOWN | 32 sec | +0.003% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:11 PM | SOL | UP | 49 sec | -0.071% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:13:52 PM | BNB | DOWN | 68 sec | +0.000% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:12:48 PM | ETH | DOWN | 2.2 min | +0.082% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:12:00 PM | ZEC | UP | 3.0 min | -0.414% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:42 PM | WTI | UP | 18 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:27 PM | ZEC | UP | 32 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:09 PM | DOGE | DOWN | 51 sec | +0.029% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:09 PM | SOL | DOWN | 51 sec | +0.020% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:59:09 PM | NEAR | DOWN | 51 sec | +0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:59:09 PM | BTC | DOWN | 51 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:58:37 PM | HYPE | UP | 83 sec | -0.134% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:58:37 PM | ETH | DOWN | 83 sec | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:58:05 PM | BNB | UP | 1.9 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:56:12 PM | XRP | DOWN | 3.8 min | +0.261% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:44:29 PM | SOL | UP | 30 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:44:29 PM | ETH | UP | 30 sec | -0.028% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:44:14 PM | BTC | DOWN | 45 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:43:09 PM | ZEC | UP | 1.8 min | -0.421% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:43:09 PM | HYPE | UP | 1.8 min | -0.196% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:43:09 PM | DOGE | UP | 1.8 min | -0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:42:35 PM | XRP | UP | 2.4 min | -0.269% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:41:30 PM | NEAR | DOWN | 3.5 min | +0.460% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:29:45 PM | WTI | UP | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:29:29 PM | BTC | UP | 31 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:29:14 PM | DOGE | DOWN | 45 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
