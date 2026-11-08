# 15-Minute 1¢ Study

*Updated Sun Nov 8, 5:53 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3985 finished bets | 1% | $145.20 | +33% | +3.64¢ | $85.25 / $59.95 |

*Expect about **97 buys a day** (~$14.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3702 | $75.35 | +19% |
| Volatility model ≥ 2%, hold to the close | 7305 | $31.15 | +4% |
| Momentum model ≥ 2%, hold to the close | 6033 | -$34.85 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49537 | 49519 | 180 (0%) | 1.07% | -$3,501.15 (-58%) | Hold to the close: -$3,501.15 (-58%) |

*In play or awaiting result: 10. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30276 | 4.8% | 0.4% (116) | -708% | ❌ Worse |
| Momentum model | 30276 | 4.7% | 0.4% (116) | -733% | ❌ Worse |
| Mean-reversion model | 30276 | 8.1% | 0.4% (116) | -856% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30276 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7305 | 65 | +4% | -76% | -76% | -72% |
| Volatility model ≥ 5% | 3985 | 42 | +33% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2301 | 27 | +68% | -60% | -59% | -55% |
| Momentum model ≥ 2% | 6033 | 47 | -5% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3702 | 34 | +19% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2429 | 23 | +33% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12490 | 84 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8764 | 73 | -7% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5867 | 53 | +3% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30481 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49519 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,501.15 | -58% | — |
| Sell at 2¢ | 1934 | 4% | -$5,238.31 | -87% | 47 sec |
| Sell at 3¢ | 1313 | 3% | -$5,229.08 | -87% | 48 sec |
| Sell at 5¢ | 911 | 2% | -$5,121.00 | -85% | 63 sec |
| Sell at 10¢ | 550 | 1% | -$4,908.65 | -82% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,563.87 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,177.15 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2442 | 11 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 15934 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12511 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18620 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3418 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3410 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3401 | 11 | 5% | 2% | -59% | -89% | -88% |
| BNB | 3394 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3390 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3385 | 13 | 7% | 3% | -53% | -81% | -81% |
| NEAR | 3366 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3363 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3354 | 12 | 3% | 1% | -55% | -90% | -89% |
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
| UP (bought YES) | 25100 | 95 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24419 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4990 | 25 | 2% | 1% | -12% | -76% | -76% |
| 0.05–0.1% | 5253 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7861 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 9001 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3368 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12170 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12086 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,888 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 5:52:19 AM | HYPE | DOWN | 7.7 min | +0.490% | — | In play | — |
| 11/8 5:44:54 AM | BNB | DOWN | 6 sec | -0.003% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:42:44 AM | NEAR | UP | 2.3 min | -0.340% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:42:44 AM | BTC | UP | 2.3 min | -0.067% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:42:44 AM | SOL | UP | 2.3 min | -0.179% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:41:57 AM | ZEC | UP | 3.0 min | -0.478% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:41:07 AM | XRP | UP | 3.9 min | -0.224% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:41:07 AM | DOGE | UP | 3.9 min | -0.155% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:40:52 AM | ETH | UP | 4.1 min | -0.123% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:40:52 AM | HYPE | UP | 4.1 min | -0.281% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:29:45 AM | ETH | UP | 14 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:29:29 AM | NEAR | UP | 30 sec | -0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:55 AM | BTC | DOWN | 65 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:28:55 AM | SOL | UP | 65 sec | -0.073% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:28:23 AM | XRP | UP | 1.6 min | -0.129% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:27:52 AM | HYPE | DOWN | 2.1 min | +0.156% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:27:36 AM | DOGE | UP | 2.4 min | -0.117% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:27:20 AM | ZEC | DOWN | 2.6 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:26:46 AM | BNB | UP | 3.2 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:14:58 AM | ETH | UP | 1 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:14:42 AM | XRP | UP | 17 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:14:42 AM | BTC | UP | 17 sec | -0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:14:42 AM | BNB | UP | 17 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:14:42 AM | SOL | UP | 17 sec | -0.078% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 5:13:54 AM | HYPE | UP | 66 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 11/8 5:13:38 AM | NEAR | UP | 82 sec | -0.223% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:12:35 AM | DOGE | DOWN | 2.4 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:11:55 AM | ZEC | UP | 3.1 min | -0.565% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:59:44 AM | BNB | DOWN | 15 sec | -0.006% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:59:13 AM | XRP | DOWN | 46 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
