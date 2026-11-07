# 15-Minute 1¢ Study

*Updated Sat Nov 7, 3:48 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3865 finished bets | 1% | $117.30 | +27% | +3.03¢ | $77.70 / $39.60 |

*Expect about **96 buys a day** (~$14.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3600 | $45.35 | +12% |
| Volatility model ≥ 2%, hold to the close | 7124 | $11.20 | +1% |
| Momentum model ≥ 2%, hold to the close | 5882 | -$59.15 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48721 | 48704 | 175 (0%) | 1.07% | -$3,484.60 (-59%) | Hold to the close: -$3,484.60 (-59%) |

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
| Volatility model | 29461 | 4.8% | 0.4% (111) | -714% | ❌ Worse |
| Momentum model | 29461 | 4.6% | 0.4% (111) | -741% | ❌ Worse |
| Mean-reversion model | 29461 | 8.1% | 0.4% (111) | -864% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29461 | 111 | -52% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7124 | 62 | +1% | -79% | -78% | -75% |
| Volatility model ≥ 5% | 3865 | 39 | +27% | -77% | -76% | -72% |
| Volatility model ≥ 10% | 2223 | 24 | +55% | -72% | -71% | -67% |
| Momentum model ≥ 2% | 5882 | 44 | -9% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3600 | 31 | +12% | -80% | -79% | -76% |
| Momentum model ≥ 10% | 2361 | 20 | +19% | -76% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12191 | 80 | -28% | -84% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8548 | 69 | -10% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5714 | 49 | -2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29666 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48704 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,484.60 | -59% | — |
| Sell at 2¢ | 1912 | 4% | -$5,185.48 | -87% | 47 sec |
| Sell at 3¢ | 1299 | 3% | -$5,175.99 | -87% | 48 sec |
| Sell at 5¢ | 901 | 2% | -$5,068.95 | -85% | 63 sec |
| Sell at 10¢ | 542 | 1% | -$4,860.58 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,525.18 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,145.60 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2402 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15664 | 83 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12268 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18358 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3326 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3318 | 12 | 4% | 2% | -54% | -90% | -90% |
| HYPE | 3308 | 10 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3306 | 17 | 5% | 2% | -35% | -85% | -84% |
| DOGE | 3298 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3296 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3275 | 16 | 5% | 2% | -37% | -84% | -85% |
| BTC | 3272 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3267 | 12 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 24694 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 24010 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4782 | 22 | 2% | 1% | -19% | -83% | -83% |
| 0.05–0.1% | 5038 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7630 | 26 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8858 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3350 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11894 | 41 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13167 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,698 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/7 3:44:40 AM | BTC | DOWN | 20 sec | +0.005% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:43:51 AM | NEAR | DOWN | 69 sec | +0.155% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:43:35 AM | BNB | DOWN | 85 sec | -0.017% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:43:35 AM | SOL | DOWN | 85 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 11/7 3:43:35 AM | HYPE | DOWN | 85 sec | +0.110% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:43:19 AM | ZEC | DOWN | 1.7 min | +0.373% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:41:59 AM | XRP | DOWN | 3.0 min | +0.206% | 2¢ | ❌ Lost | -$0.15 |
| 11/7 3:41:40 AM | DOGE | DOWN | 3.3 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:41:24 AM | ETH | DOWN | 3.6 min | +0.110% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:28:41 AM | BNB | UP | 79 sec | -0.167% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:28:25 AM | BTC | UP | 1.6 min | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/7 3:28:09 AM | XRP | UP | 1.9 min | -0.197% | 0¢ | ❌ Lost | $0.00 |
| 11/7 3:28:09 AM | HYPE | UP | 1.9 min | -0.199% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:27:31 AM | DOGE | UP | 2.5 min | -0.153% | 0¢ | ❌ Lost | $0.00 |
| 11/7 3:26:42 AM | NEAR | UP | 3.3 min | -0.664% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:26:42 AM | SOL | UP | 3.3 min | -0.197% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:26:26 AM | ETH | UP | 3.5 min | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:26:10 AM | ZEC | UP | 3.8 min | -0.884% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:14:46 AM | NEAR | DOWN | 14 sec | +0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/7 3:14:46 AM | SOL | DOWN | 14 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:14:30 AM | BTC | UP | 30 sec | -0.024% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:14:15 AM | BNB | DOWN | 45 sec | -0.052% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:12:53 AM | XRP | UP | 2.1 min | -0.205% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 3:12:53 AM | ZEC | UP | 2.1 min | -0.375% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 3:11:48 AM | ETH | DOWN | 3.2 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:59:30 AM | SOL | DOWN | 30 sec | +0.026% | 0¢ | ❌ Lost | -$0.15 |
| 11/7 2:59:30 AM | HYPE | DOWN | 30 sec | +0.030% | 1¢ | ❌ Lost | -$0.15 |
| 11/7 2:58:59 AM | XRP | DOWN | 61 sec | +0.103% | 0¢ | ❌ Lost | $0.00 |
| 11/7 2:57:56 AM | ETH | UP | 2.0 min | -0.050% | 2¢ | ❌ Lost | -$0.15 |
| 11/7 2:57:40 AM | NEAR | UP | 2.3 min | -0.310% | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
