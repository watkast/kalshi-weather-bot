# 15-Minute 1¢ Study

*Updated Fri Nov 6, 9:36 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3830 finished bets | 1% | $121.35 | +29% | +3.17¢ | $80.10 / $41.25 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3561 | $50.00 | +13% |
| Volatility model ≥ 2%, hold to the close | 7071 | $17.65 | +2% |
| Momentum model ≥ 2%, hold to the close | 5835 | -$53.45 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48506 | 48489 | 175 (0%) | 1.07% | -$3,461.65 (-59%) | Hold to the close: -$3,461.65 (-59%) |

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
| Volatility model | 29247 | 4.7% | 0.4% (111) | -701% | ❌ Worse |
| Momentum model | 29247 | 4.6% | 0.4% (111) | -728% | ❌ Worse |
| Mean-reversion model | 29247 | 8.1% | 0.4% (111) | -851% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29247 | 111 | -52% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7071 | 62 | +2% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3830 | 39 | +29% | -77% | -75% | -72% |
| Volatility model ≥ 10% | 2194 | 24 | +58% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5835 | 44 | -8% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3561 | 31 | +13% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2329 | 20 | +21% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12106 | 80 | -27% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8486 | 69 | -10% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5673 | 49 | -2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29452 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11669 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48489 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,461.65 | -59% | — |
| Sell at 2¢ | 1905 | 4% | -$5,164.35 | -87% | 47 sec |
| Sell at 3¢ | 1297 | 3% | -$5,153.82 | -87% | 48 sec |
| Sell at 5¢ | 900 | 2% | -$5,046.65 | -85% | 63 sec |
| Sell at 10¢ | 541 | 1% | -$4,838.94 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,502.23 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,122.65 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2400 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15591 | 83 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 12213 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18273 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3301 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3295 | 12 | 4% | 2% | -53% | -90% | -90% |
| HYPE | 3284 | 10 | 5% | 2% | -62% | -89% | -87% |
| BNB | 3284 | 17 | 5% | 2% | -35% | -85% | -84% |
| DOGE | 3274 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3271 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3250 | 16 | 5% | 2% | -36% | -84% | -85% |
| BTC | 3249 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3244 | 12 | 3% | 1% | -54% | -89% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1750 | 6 | 4% | 1% | -59% | -92% | -92% |
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
| UP (bought YES) | 24591 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23898 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4708 | 22 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 4997 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7573 | 26 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8819 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3347 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13078 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,660 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 9:29:45 PM | WTI | UP | 15 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:29:29 PM | BTC | UP | 31 sec | -0.018% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:29:14 PM | DOGE | DOWN | 45 sec | +0.019% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:28:56 PM | SOL | DOWN | 64 sec | +0.053% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:28:40 PM | HYPE | UP | 80 sec | -0.158% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:28:40 PM | ETH | DOWN | 80 sec | +0.050% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:26:48 PM | ZEC | UP | 3.2 min | -0.654% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:25:58 PM | BNB | DOWN | 4.0 min | +0.088% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:24:34 PM | XRP | DOWN | 5.4 min | +0.478% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:14:51 PM | BNB | DOWN | 8 sec | -0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:14:19 PM | HYPE | DOWN | 41 sec | +0.098% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:13:45 PM | ZEC | DOWN | 75 sec | +0.225% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:13:45 PM | SOL | UP | 75 sec | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 11/6 9:13:45 PM | BTC | UP | 75 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:13:29 PM | BRENT | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:57 PM | DOGE | UP | 2.0 min | -0.153% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:57 PM | ETH | UP | 2.0 min | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 9:12:25 PM | NEAR | UP | 2.6 min | -0.350% | 3¢ | ❌ Lost | -$0.15 |
| 11/6 9:10:29 PM | XRP | UP | 4.5 min | -0.457% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:59:25 PM | WTI | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:59:10 PM | NATGAS | UP | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:55 PM | BRENT | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:58:55 PM | ZEC | DOWN | 64 sec | +0.234% | 0¢ | ❌ Lost | $0.00 |
| 11/6 8:56:48 PM | ETH | DOWN | 3.2 min | +0.141% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:56:48 PM | BTC | DOWN | 3.2 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:55:45 PM | HYPE | DOWN | 4.2 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:55:29 PM | SOL | DOWN | 4.5 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 8:55:13 PM | NEAR | DOWN | 4.8 min | +0.752% | 0¢ | ❌ Lost | $0.00 |
| 11/6 8:55:13 PM | DOGE | DOWN | 4.8 min | +0.236% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 8:53:28 PM | BNB | DOWN | 6.5 min | +0.032% | 5¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
