# 15-Minute 1¢ Study

*Updated Sun Nov 8, 4:26 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4025 finished bets | 1% | $140.40 | +31% | +3.49¢ | $96.55 / $43.85 |

*Expect about **97 buys a day** (~$14.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3738 | $71.15 | +18% |
| Volatility model ≥ 2%, hold to the close | 7369 | $23.20 | +3% |
| Momentum model ≥ 2%, hold to the close | 6088 | -$41.30 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 49842 | 49821 | 180 (0%) | 1.07% | -$3,536.10 (-58%) | Hold to the close: -$3,536.10 (-58%) |

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
| Volatility model | 30567 | 4.8% | 0.4% (116) | -709% | ❌ Worse |
| Momentum model | 30567 | 4.6% | 0.4% (116) | -734% | ❌ Worse |
| Mean-reversion model | 30567 | 8.1% | 0.4% (116) | -857% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 30567 | 116 | -52% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 7369 | 65 | +3% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4025 | 42 | +31% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2324 | 27 | +66% | -61% | -59% | -56% |
| Momentum model ≥ 2% | 6088 | 47 | -6% | -78% | -78% | -75% |
| Momentum model ≥ 5% | 3738 | 34 | +18% | -73% | -73% | -69% |
| Momentum model ≥ 10% | 2451 | 23 | +32% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 12615 | 84 | -27% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 8845 | 73 | -8% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 5919 | 53 | +2% | -76% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 30772 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11673 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7376 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 49821 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 180 | 0% | -$3,536.10 | -58% | — |
| Sell at 2¢ | 1949 | 4% | -$5,269.36 | -87% | 47 sec |
| Sell at 3¢ | 1324 | 3% | -$5,259.74 | -87% | 48 sec |
| Sell at 5¢ | 920 | 2% | -$5,150.10 | -85% | 63 sec |
| Sell at 10¢ | 555 | 1% | -$4,937.05 | -82% | 65 sec |
| Sell at 25¢ | 289 | 1% | -$4,595.51 | -76% | 83 sec |
| Sell at 50¢ | 184 | 0% | -$4,212.10 | -70% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2475 | 11 | 11% | 4% | -58% | -81% | -82% |
| 2–5 min | 16046 | 84 | 7% | 3% | -48% | -87% | -87% |
| 1–2 min | 12587 | 40 | 3% | 2% | -65% | -92% | -92% |
| Under 1 min | 18701 | 45 | 1% | 0% | -66% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3451 | 13 | 5% | 2% | -51% | -88% | -88% |
| SOL | 3442 | 14 | 4% | 2% | -48% | -87% | -87% |
| HYPE | 3434 | 11 | 5% | 2% | -60% | -89% | -88% |
| BNB | 3426 | 17 | 5% | 2% | -37% | -86% | -85% |
| DOGE | 3424 | 6 | 4% | 2% | -78% | -91% | -90% |
| ETH | 3417 | 13 | 7% | 3% | -53% | -81% | -82% |
| NEAR | 3399 | 16 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3395 | 16 | 5% | 2% | -35% | -88% | -89% |
| XRP | 3384 | 12 | 3% | 1% | -56% | -90% | -89% |
| GOLD | 1783 | 5 | 5% | 2% | -66% | -81% | -83% |
| WTI | 1752 | 6 | 4% | 1% | -59% | -92% | -92% |
| SILVER | 1733 | 8 | 5% | 2% | -45% | -82% | -81% |
| PLATINUM | 1567 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1503 | 4 | 2% | 1% | -75% | -90% | -89% |
| COPPER | 1471 | 6 | 2% | 1% | -62% | -72% | -71% |
| NATGAS | 1434 | 8 | 2% | 1% | -48% | -77% | -76% |
| GBPUSD | 1430 | 4 | 2% | 1% | -74% | -96% | -96% |
| PALLADIUM | 1408 | 3 | 1% | 0% | -80% | -91% | -92% |
| USDJPY | 1408 | 5 | 2% | 1% | -67% | -97% | -96% |
| AUDUSD | 961 | 4 | 2% | 1% | -61% | -87% | -87% |
| USDCAD | 930 | 0 | 2% | 1% | -100% | -97% | -97% |
| BRENT | 525 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 303 | 1 | 4% | 1% | -69% | -62% | -60% |
| 2YRRATE | 287 | 3 | 4% | 1% | -2% | -28% | -27% |
| 30YRRATE | 285 | 0 | 2% | 1% | -100% | -96% | -95% |
| 5YRRATE | 262 | 1 | 4% | 2% | -64% | -93% | -95% |
| INX | 7 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 25272 | 95 | 4% | 2% | -57% | -88% | -87% |
| DOWN (bought NO) | 24549 | 85 | 4% | 2% | -60% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5031 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5295 | 19 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 7941 | 26 | 4% | 2% | -59% | -90% | -90% |
| 0.2–0.5% | 9085 | 35 | 6% | 3% | -57% | -87% | -87% |
| Over 0.5% | 3412 | 13 | 7% | 3% | -61% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12179 | 42 | 4% | 2% | -61% | -87% | -87% |
| Morning (6am–12pm) | 12223 | 54 | 4% | 2% | -50% | -84% | -84% |
| Afternoon (12–6pm) | 12056 | 43 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 13363 | 41 | 3% | 2% | -65% | -90% | -90% |

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
| 11/8 4:26:11 PM | BTC | DOWN | 3.8 min | +0.446% | — | In play | — |
| 11/8 4:25:54 PM | HYPE | DOWN | 4.1 min | +0.692% | — | In play | — |
| 11/8 4:25:38 PM | ZEC | DOWN | 4.3 min | +1.290% | — | In play | — |
| 11/8 4:25:38 PM | NEAR | DOWN | 4.3 min | +1.350% | — | In play | — |
| 11/8 4:14:29 PM | USDJPY | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:13:55 PM | USDCAD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:13:39 PM | GBPUSD | DOWN | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:13:23 PM | NATGAS | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:12:18 PM | AUDUSD | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:12:18 PM | BRENT | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:12:03 PM | WTI | UP | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:12:03 PM | HYPE | DOWN | 2.9 min | +0.632% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:11:46 PM | ZEC | DOWN | 3.2 min | +1.314% | 0¢ | ❌ Lost | $0.00 |
| 11/8 4:11:14 PM | DOGE | DOWN | 3.8 min | +1.076% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 4:10:58 PM | BTC | DOWN | 4.0 min | +0.479% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:10:39 PM | ETH | DOWN | 4.3 min | +0.666% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:10:23 PM | SOL | DOWN | 4.6 min | +0.791% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:10:23 PM | XRP | DOWN | 4.6 min | +0.784% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:10:23 PM | BNB | DOWN | 4.6 min | +0.398% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 4:10:07 PM | NEAR | DOWN | 4.9 min | +1.248% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:59:46 PM | GBPUSD | UP | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:59:30 PM | ZEC | DOWN | 29 sec | +0.070% | 2¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:55 PM | NEAR | DOWN | 65 sec | +0.217% | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:55 PM | DOGE | DOWN | 65 sec | +0.245% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:58:55 PM | BTC | DOWN | 65 sec | +0.119% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:55 PM | BNB | DOWN | 65 sec | +0.113% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:58:23 PM | ETH | DOWN | 1.6 min | +0.260% | 1¢ | ❌ Lost | -$0.15 |
| 11/8 3:58:08 PM | SOL | DOWN | 1.9 min | +0.485% | 0¢ | ❌ Lost | $0.00 |
| 11/8 3:44:45 PM | GBPUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/8 3:44:29 PM | HYPE | DOWN | 31 sec | +0.170% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
