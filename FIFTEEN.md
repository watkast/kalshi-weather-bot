# 15-Minute 1¢ Study

*Updated Sun Nov 8, 7:11 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4047 finished bets | 1% | $193.55 | +43% | +4.78¢ | $95.20 / $98.35 |

*Expect about **97 buys a day** (~$14.52/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3755 | $111.20 | +27% |
| Volatility model ≥ 2%, hold to the close | 7411 | $87.65 | +10% |
| Momentum model ≥ 2%, hold to the close | 6115 | $11.25 | +2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50056 | 50037 | 186 (0%) | 1.07% | -$3,479.10 (-57%) | Hold to the close: -$3,479.10 (-57%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30670 | 4.8% | 0.4% (121) | -689% | ❌ Worse |
| Momentum model | 30670 | 4.6% | 0.4% (121) | -715% | ❌ Worse |
| Mean-reversion model | 30670 | 8.1% | 0.4% (121) | -833% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30670 | 121 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7411 | 70 | +10% | -77% | -75% | -71% |
| Volatility model ≥ 5% | 4047 | 46 | +43% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2331 | 28 | +72% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6115 | 51 | +2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3755 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2461 | 25 | +43% | -64% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12675 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8888 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5944 | 56 | +7% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30875 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11739 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7423 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50037 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,479.10 | -57% | — |
| Sell at 2¢ | 1960 | 4% | -$5,293.50 | -87% | 47 sec |
| Sell at 3¢ | 1334 | 3% | -$5,282.84 | -87% | 48 sec |
| Sell at 5¢ | 929 | 2% | -$5,171.25 | -85% | 63 sec |
| Sell at 10¢ | 562 | 1% | -$4,954.88 | -81% | 66 sec |
| Sell at 25¢ | 295 | 1% | -$4,602.65 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,198.60 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2482 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16131 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12632 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18780 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3461 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3454 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3445 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3438 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3436 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3429 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3410 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3406 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3396 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1791 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1760 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1743 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1575 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1514 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1480 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1441 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1436 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1418 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1416 | 3 | 1% | 0% | -80% | -91% | -92% |
| AUDUSD | 971 | 5 | 2% | 1% | -52% | -87% | -87% |
| USDCAD | 940 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 533 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25375 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24662 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5035 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5300 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7960 | 27 | 4% | 2% | -57% | -90% | -90% |
| 0.2–0.5% | 9131 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3441 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13435 | 43 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,943 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 7:11:13 PM | WTI | DOWN | 3.8 min | — | — | In play | — |
| 11/8 7:07:10 PM | NATGAS | DOWN | 7.8 min | — | — | In play | — |
| 11/8 6:59:45 PM | ETH | DOWN | 14 sec | +0.011% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:45 PM | DOGE | UP | 14 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:45 PM | BNB | UP | 14 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:29 PM | HYPE | DOWN | 30 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:14 PM | XRP | UP | 45 sec | -0.242% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:14 PM | SOL | UP | 45 sec | -0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:14 PM | BTC | DOWN | 45 sec | +0.054% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:59:14 PM | NEAR | UP | 45 sec | -0.366% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:59:14 PM | USDCAD | UP | 45 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:58:56 PM | AUDUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:58:40 PM | EURUSD | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:57:52 PM | BRENT | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:57:52 PM | NATGAS | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:57:36 PM | WTI | UP | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:44:46 PM | USDCAD | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:44:30 PM | GBPUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:44:15 PM | NATGAS | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:43:27 PM | USDJPY | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:42:08 PM | BTC | DOWN | 2.9 min | +0.411% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:42:08 PM | EURUSD | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:42:08 PM | COPPER | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:42:08 PM | ZEC | DOWN | 2.9 min | +0.779% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:53 PM | XRP | DOWN | 3.1 min | +0.496% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:53 PM | BNB | DOWN | 3.1 min | +0.269% | 0¢ | ❌ Lost | $0.00 |
| 11/8 6:41:53 PM | AUDUSD | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:37 PM | NEAR | DOWN | 3.4 min | +0.671% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:37 PM | HYPE | DOWN | 3.4 min | +0.572% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 6:41:21 PM | GOLD | DOWN | 3.6 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
