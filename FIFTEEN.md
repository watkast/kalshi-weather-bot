# 15-Minute 1¢ Study

*Updated Fri Nov 6, 5:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3811 finished bets | 1% | $123.00 | +29% | +3.23¢ | $81.30 / $41.70 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3543 | $51.65 | +14% |
| Volatility model ≥ 2%, hold to the close | 7038 | $21.10 | +2% |
| Momentum model ≥ 2%, hold to the close | 5806 | -$50.30 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48346 | 48329 | 175 (0%) | 1.07% | -$3,443.65 (-58%) | Hold to the close: -$3,443.65 (-58%) |

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
| Volatility model | 29109 | 4.7% | 0.4% (111) | -694% | ❌ Worse |
| Momentum model | 29109 | 4.6% | 0.4% (111) | -721% | ❌ Worse |
| Mean-reversion model | 29109 | 8.1% | 0.4% (111) | -844% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29109 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7038 | 62 | +2% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3811 | 39 | +29% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2178 | 24 | +59% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5806 | 44 | -8% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3543 | 31 | +14% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2314 | 20 | +22% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12043 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8439 | 69 | -9% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5644 | 49 | -1% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29314 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11647 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48329 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,443.65 | -58% | — |
| Sell at 2¢ | 1900 | 4% | -$5,147.65 | -87% | 47 sec |
| Sell at 3¢ | 1295 | 3% | -$5,136.60 | -87% | 48 sec |
| Sell at 5¢ | 898 | 2% | -$5,029.95 | -85% | 63 sec |
| Sell at 10¢ | 540 | 1% | -$4,822.25 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,484.23 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,104.65 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2390 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15529 | 83 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12178 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18220 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3286 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3279 | 12 | 4% | 2% | -53% | -90% | -90% |
| HYPE | 3268 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3268 | 17 | 5% | 2% | -34% | -85% | -84% |
| DOGE | 3259 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3256 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3236 | 16 | 5% | 2% | -36% | -84% | -84% |
| BTC | 3234 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3228 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1741 | 6 | 4% | 1% | -58% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| GBPUSD | 1426 | 4 | 2% | 1% | -74% | -96% | -96% |
| NATGAS | 1425 | 8 | 2% | 1% | -48% | -76% | -76% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1406 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 960 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 929 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 519 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 24511 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23818 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4678 | 22 | 2% | 1% | -17% | -83% | -82% |
| 0.05–0.1% | 4965 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7544 | 26 | 5% | 2% | -56% | -89% | -89% |
| 0.2–0.5% | 8784 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3335 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11665 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12947 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,630 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 5:14:27 PM | HYPE | DOWN | 33 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 5:13:41 PM | ZEC | DOWN | 78 sec | +0.280% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:13:41 PM | DOGE | DOWN | 78 sec | +0.012% | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:13:25 PM | WTI | DOWN | 1.6 min | — | 0¢ | ❌ Lost | $0.00 |
| 11/6 5:13:25 PM | SOL | DOWN | 1.6 min | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:11:33 PM | BTC | DOWN | 3.4 min | +0.111% | 2¢ | ❌ Lost | -$0.15 |
| 11/6 5:11:17 PM | BNB | DOWN | 3.7 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:10:29 PM | ETH | DOWN | 4.5 min | +0.123% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 5:10:13 PM | XRP | DOWN | 4.8 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:59:29 PM | BRENT | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 4:59:13 PM | NEAR | DOWN | 47 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 4:58:57 PM | WTI | DOWN | 62 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:58:41 PM | BNB | UP | 78 sec | -0.095% | 0¢ | ❌ Lost | $0.00 |
| 11/6 4:58:41 PM | HYPE | UP | 78 sec | -0.093% | 0¢ | ❌ Lost | $0.00 |
| 11/6 4:58:41 PM | ZEC | UP | 78 sec | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 11/6 4:58:41 PM | DOGE | UP | 78 sec | -0.058% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:58:09 PM | BTC | UP | 1.9 min | -0.138% | 0¢ | ❌ Lost | $0.00 |
| 11/6 4:57:52 PM | SOL | UP | 2.1 min | -0.167% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:57:20 PM | XRP | UP | 2.7 min | -0.136% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 4:57:20 PM | ETH | UP | 2.7 min | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:44:41 PM | NATGAS | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 4:44:09 PM | BTC | DOWN | 50 sec | +0.041% | 0¢ | ❌ Lost | $0.00 |
| 11/6 4:43:53 PM | XRP | DOWN | 67 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/6 4:43:53 PM | NEAR | DOWN | 67 sec | +0.051% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:43:36 PM | HYPE | DOWN | 84 sec | +0.059% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:42:49 PM | DOGE | DOWN | 2.2 min | +0.108% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:41:45 PM | ZEC | DOWN | 3.2 min | +0.460% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:40:41 PM | SOL | DOWN | 4.3 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:40:41 PM | ETH | DOWN | 4.3 min | +0.195% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 4:40:08 PM | BNB | DOWN | 4.9 min | +0.107% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
