# 15-Minute 1¢ Study

*Updated Fri Nov 6, 11:09 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3843 finished bets | 1% | $119.70 | +28% | +3.11¢ | $79.20 / $40.50 |

*Expect about **96 buys a day** (~$14.42/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3574 | $48.35 | +13% |
| Volatility model ≥ 2%, hold to the close | 7088 | $15.55 | +2% |
| Momentum model ≥ 2%, hold to the close | 5849 | -$55.25 | -8% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 48560 | 48543 | 175 (0%) | 1.07% | -$3,467.35 (-59%) | Hold to the close: -$3,467.35 (-59%) |

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
| Volatility model | 29300 | 4.7% | 0.4% (111) | -706% | ❌ Worse |
| Momentum model | 29300 | 4.6% | 0.4% (111) | -732% | ❌ Worse |
| Mean-reversion model | 29300 | 8.1% | 0.4% (111) | -856% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 29300 | 111 | -52% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 7088 | 62 | +2% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3843 | 39 | +28% | -77% | -76% | -72% |
| Volatility model ≥ 10% | 2204 | 24 | +57% | -72% | -70% | -67% |
| Momentum model ≥ 2% | 5849 | 44 | -8% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3574 | 31 | +13% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 2339 | 20 | +21% | -75% | -75% | -71% |
| Mean-reversion model ≥ 2% | 12132 | 80 | -28% | -84% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8507 | 69 | -10% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5688 | 49 | -2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 29505 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11670 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7368 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 48543 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 175 | 0% | -$3,467.35 | -59% | — |
| Sell at 2¢ | 1905 | 4% | -$5,170.05 | -87% | 47 sec |
| Sell at 3¢ | 1297 | 3% | -$5,159.52 | -87% | 48 sec |
| Sell at 5¢ | 900 | 2% | -$5,052.35 | -85% | 63 sec |
| Sell at 10¢ | 541 | 1% | -$4,844.64 | -82% | 66 sec |
| Sell at 25¢ | 282 | 1% | -$4,507.93 | -76% | 83 sec |
| Sell at 50¢ | 180 | 0% | -$4,128.35 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2402 | 10 | 11% | 4% | -60% | -81% | -82% |
| 2–5 min | 15605 | 83 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 12225 | 40 | 3% | 1% | -64% | -92% | -92% |
| Under 1 min | 18299 | 42 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3307 | 13 | 5% | 2% | -49% | -88% | -88% |
| SOL | 3301 | 12 | 4% | 2% | -54% | -90% | -90% |
| HYPE | 3290 | 10 | 5% | 2% | -62% | -89% | -87% |
| BNB | 3289 | 17 | 5% | 2% | -35% | -85% | -84% |
| DOGE | 3280 | 6 | 4% | 2% | -77% | -90% | -90% |
| ETH | 3277 | 12 | 7% | 3% | -55% | -85% | -85% |
| NEAR | 3256 | 16 | 5% | 2% | -36% | -84% | -85% |
| BTC | 3255 | 15 | 5% | 2% | -37% | -88% | -89% |
| XRP | 3250 | 12 | 3% | 1% | -54% | -89% | -89% |
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
| UP (bought YES) | 24613 | 94 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23930 | 81 | 4% | 2% | -61% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4728 | 22 | 2% | 1% | -18% | -83% | -82% |
| 0.05–0.1% | 5009 | 18 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 7585 | 26 | 5% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 8828 | 34 | 6% | 3% | -57% | -87% | -86% |
| Over 0.5% | 3347 | 13 | 7% | 3% | -60% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11768 | 41 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11949 | 51 | 4% | 2% | -51% | -86% | -85% |
| Afternoon (12–6pm) | 11694 | 42 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13132 | 41 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,671 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/6 10:59:53 PM | ZEC | DOWN | 7 sec | -0.017% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:59:37 PM | NEAR | UP | 23 sec | -0.120% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:59:37 PM | BNB | UP | 23 sec | -0.037% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:59:37 PM | XRP | UP | 23 sec | -0.060% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:59:21 PM | HYPE | DOWN | 39 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:58:37 PM | BTC | DOWN | 83 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:58:37 PM | ETH | DOWN | 83 sec | +0.054% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:56:11 PM | SOL | DOWN | 3.8 min | +0.124% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:55:56 PM | DOGE | DOWN | 4.0 min | +0.114% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:44:30 PM | SOL | UP | 30 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:44:30 PM | BNB | DOWN | 30 sec | -0.050% | 0¢ | ❌ Lost | -$0.15 |
| 11/6 10:44:15 PM | BTC | UP | 45 sec | -0.017% | 1¢ | ❌ Lost | $0.00 |
| 11/6 10:44:15 PM | DOGE | DOWN | 45 sec | +0.001% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:43:57 PM | ETH | UP | 63 sec | -0.052% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:43:41 PM | ZEC | UP | 79 sec | -0.230% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:42:53 PM | XRP | DOWN | 2.1 min | +0.190% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:42:37 PM | HYPE | DOWN | 2.4 min | +0.149% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:41:46 PM | NEAR | UP | 3.2 min | -0.394% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:29:53 PM | NEAR | UP | 6 sec | -0.112% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:29:37 PM | HYPE | DOWN | 22 sec | +0.029% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:28:46 PM | ZEC | DOWN | 74 sec | +0.233% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:27:19 PM | BNB | DOWN | 2.7 min | +0.035% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:26:31 PM | XRP | DOWN | 3.5 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:26:15 PM | DOGE | DOWN | 3.7 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:25:59 PM | BTC | DOWN | 4.0 min | +0.148% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:24:54 PM | ETH | DOWN | 5.1 min | +0.178% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:24:35 PM | SOL | DOWN | 5.4 min | +0.191% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:59 PM | DOGE | DOWN | 0 sec | -0.042% | 0¢ | ❌ Lost | $0.00 |
| 11/6 10:14:59 PM | XRP | DOWN | 0 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/6 10:14:27 PM | BTC | DOWN | 32 sec | +0.018% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
