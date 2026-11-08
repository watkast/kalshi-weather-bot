# 15-Minute 1¢ Study

*Updated Sun Nov 8, 6:24 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3987 finished bets | 1% | $144.90 | +33% | +3.63¢ | $85.10 / $59.80 |

*Expect about **97 buys a day** (~$14.49/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3702 | $75.35 | +19% |
| Volatility model ≥ 2%, hold to the close | 7311 | $30.25 | +3% |
| Momentum model ≥ 2%, hold to the close | 6034 | -$35.00 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49554 | 49537 | 180 (0%) | 1.07% | -$3,503.85 (-58%) | Hold to the close: -$3,503.85 (-58%) |

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
| Volatility model | 30294 | 4.8% | 0.4% (116) | -708% | ❌ Worse |
| Momentum model | 30294 | 4.7% | 0.4% (116) | -733% | ❌ Worse |
| Mean-reversion model | 30294 | 8.1% | 0.4% (116) | -856% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30294 | 116 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7311 | 65 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 3987 | 42 | +33% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2302 | 27 | +68% | -60% | -59% | -55% |
| Momentum model ≥ 2% | 6034 | 47 | -5% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3702 | 34 | +19% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2429 | 23 | +33% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12504 | 84 | -26% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8775 | 73 | -8% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5874 | 53 | +3% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30499 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49537 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,503.85 | -58% | — |
| Sell at 2¢ | 1934 | 4% | -$5,241.01 | -87% | 47 sec |
| Sell at 3¢ | 1313 | 3% | -$5,231.78 | -87% | 48 sec |
| Sell at 5¢ | 911 | 2% | -$5,123.70 | -85% | 63 sec |
| Sell at 10¢ | 550 | 1% | -$4,911.35 | -82% | 65 sec |
| Sell at 25¢ | 288 | 1% | -$4,566.57 | -76% | 82 sec |
| Sell at 50¢ | 184 | 0% | -$4,179.85 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2447 | 11 | 11% | 4% | -57% | -81% | -83% |
| 2–5 min | 15947 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12511 | 40 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18620 | 45 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3420 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3412 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3403 | 11 | 5% | 2% | -59% | -89% | -88% |
| BNB | 3396 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3392 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3387 | 13 | 7% | 3% | -53% | -81% | -81% |
| NEAR | 3368 | 16 | 5% | 2% | -38% | -85% | -85% |
| BTC | 3365 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3356 | 12 | 3% | 1% | -55% | -90% | -89% |
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
| DOWN (bought NO) | 24437 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4992 | 25 | 2% | 1% | -12% | -77% | -76% |
| 0.05–0.1% | 5255 | 19 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7869 | 26 | 4% | 2% | -58% | -90% | -90% |
| 0.2–0.5% | 9007 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3368 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12095 | 54 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 11900 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,892 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 6:12:09 AM | NEAR | DOWN | 2.9 min | +0.340% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:12:09 AM | ZEC | DOWN | 2.9 min | +0.326% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:11:38 AM | ETH | DOWN | 3.4 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:11:38 AM | SOL | DOWN | 3.4 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:10:50 AM | DOGE | DOWN | 4.2 min | +0.134% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:10:50 AM | BTC | DOWN | 4.2 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:10:50 AM | HYPE | DOWN | 4.2 min | +0.307% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:10:50 AM | XRP | DOWN | 4.2 min | +0.172% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:09:45 AM | BNB | DOWN | 5.2 min | +0.161% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:57:59 AM | BTC | DOWN | 2.0 min | +0.039% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:56:55 AM | BNB | DOWN | 3.1 min | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:56:21 AM | XRP | DOWN | 3.6 min | +0.138% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:56:05 AM | ETH | DOWN | 3.9 min | +0.085% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:55:50 AM | ZEC | DOWN | 4.2 min | +0.341% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:54:46 AM | NEAR | DOWN | 5.2 min | +0.427% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:54:46 AM | SOL | DOWN | 5.2 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:54:28 AM | DOGE | DOWN | 5.5 min | +0.197% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 5:52:19 AM | HYPE | DOWN | 7.7 min | +0.490% | 1¢ | ❌ Lost | -$0.15 |
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

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
