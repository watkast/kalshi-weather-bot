# 15-Minute 1¢ Study

*Updated Sun Nov 8, 11:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4068 finished bets | 1% | $191.75 | +42% | +4.71¢ | $93.70 / $98.05 |

*Expect about **97 buys a day** (~$14.54/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3774 | $109.55 | +27% |
| Volatility model ≥ 2%, hold to the close | 7447 | $83.75 | +9% |
| Momentum model ≥ 2%, hold to the close | 6146 | $7.95 | +1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 50355 | 50334 | 186 (0%) | 1.07% | -$3,518.40 (-57%) | Hold to the close: -$3,518.40 (-57%) |

*In play or awaiting result: 13. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 30809 | 4.8% | 0.4% (121) | -691% | ❌ Worse |
| Momentum model | 30809 | 4.6% | 0.4% (121) | -717% | ❌ Worse |
| Mean-reversion model | 30809 | 8.1% | 0.4% (121) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30809 | 121 | -50% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7447 | 70 | +9% | -76% | -75% | -71% |
| Volatility model ≥ 5% | 4068 | 46 | +42% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2341 | 28 | +71% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6146 | 51 | +1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3774 | 37 | +27% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2475 | 25 | +42% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 12738 | 89 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8931 | 77 | -4% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5971 | 56 | +7% | -76% | -76% | -73% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31014 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11839 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7481 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 50334 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 186 | 0% | -$3,518.40 | -57% | — |
| Sell at 2¢ | 1977 | 4% | -$5,328.38 | -87% | 47 sec |
| Sell at 3¢ | 1346 | 3% | -$5,317.46 | -87% | 48 sec |
| Sell at 5¢ | 940 | 2% | -$5,203.40 | -85% | 63 sec |
| Sell at 10¢ | 566 | 1% | -$4,988.94 | -81% | 65 sec |
| Sell at 25¢ | 296 | 1% | -$4,638.64 | -76% | 83 sec |
| Sell at 50¢ | 190 | 0% | -$4,237.90 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2491 | 12 | 11% | 4% | -54% | -81% | -82% |
| 2–5 min | 16249 | 87 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 12708 | 41 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 18874 | 46 | 1% | 0% | -65% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3476 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3469 | 15 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3460 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3453 | 18 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3452 | 7 | 4% | 2% | -74% | -90% | -90% |
| ETH | 3445 | 14 | 7% | 3% | -50% | -81% | -81% |
| NEAR | 3425 | 16 | 5% | 2% | -40% | -85% | -85% |
| BTC | 3422 | 16 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3412 | 13 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1804 | 5 | 6% | 2% | -66% | -81% | -83% |
| WTI | 1775 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1757 | 8 | 5% | 2% | -46% | -82% | -82% |
| PLATINUM | 1587 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1525 | 4 | 2% | 1% | -76% | -90% | -89% |
| COPPER | 1490 | 6 | 2% | 1% | -62% | -72% | -72% |
| NATGAS | 1451 | 8 | 2% | 1% | -49% | -77% | -76% |
| GBPUSD | 1445 | 4 | 2% | 1% | -74% | -96% | -96% |
| USDJPY | 1429 | 5 | 2% | 1% | -67% | -97% | -96% |
| PALLADIUM | 1428 | 3 | 1% | 0% | -80% | -92% | -92% |
| AUDUSD | 984 | 5 | 2% | 1% | -53% | -87% | -87% |
| USDCAD | 954 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 547 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25527 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24807 | 91 | 4% | 2% | -58% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5046 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5320 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7985 | 27 | 4% | 2% | -57% | -89% | -89% |
| 0.2–0.5% | 9205 | 38 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3450 | 14 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12200 | 47 | 4% | 2% | -55% | -86% | -86% |
| Evening (6pm–12am) | 13732 | 43 | 3% | 2% | -64% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,947 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/8 11:12:33 PM | BTC | DOWN | 2.5 min | +0.171% | — | In play | — |
| 11/8 11:12:17 PM | GBPUSD | DOWN | 2.7 min | — | — | In play | — |
| 11/8 11:11:44 PM | COPPER | UP | 3.3 min | — | — | In play | — |
| 11/8 11:10:23 PM | EURUSD | DOWN | 4.6 min | — | — | In play | — |
| 11/8 10:59:58 PM | PLATINUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:59:58 PM | EURUSD | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:59:42 PM | GOLD | DOWN | 17 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:59:42 PM | ETH | DOWN | 17 sec | +0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:59:26 PM | USDCAD | DOWN | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:59:26 PM | DOGE | UP | 33 sec | -0.085% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:59:26 PM | SILVER | DOWN | 33 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:59:10 PM | XRP | UP | 50 sec | -0.182% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:58:53 PM | COPPER | UP | 66 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:58:53 PM | BNB | DOWN | 66 sec | -0.009% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:58:37 PM | SOL | UP | 82 sec | -0.216% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:48 PM | HYPE | UP | 2.2 min | -0.302% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:48 PM | ZEC | UP | 2.2 min | -0.397% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:48 PM | AUDUSD | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:48 PM | USDJPY | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:32 PM | BRENT | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:16 PM | WTI | UP | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:57:16 PM | NEAR | UP | 2.7 min | -0.448% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:55:54 PM | BTC | DOWN | 4.1 min | +0.242% | 2¢ | ❌ Lost | -$0.15 |
| 11/8 10:44:48 PM | NEAR | DOWN | 12 sec | -0.028% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:44:48 PM | HYPE | DOWN | 12 sec | -0.007% | 0¢ | ❌ Lost | $0.00 |
| 11/8 10:44:32 PM | PALLADIUM | UP | 28 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:44:17 PM | WTI | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:44:17 PM | GBPUSD | UP | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 10:43:59 PM | BRENT | UP | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 10:43:43 PM | USDCAD | DOWN | 77 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
