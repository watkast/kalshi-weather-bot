# 15-Minute 1¢ Study

*Updated Sun Oct 25, 5:46 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2698 finished bets | 1% | $85.25 | +28% | +3.16¢ | $34.25 / $51.00 |

*Expect about **97 buys a day** (~$14.61/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2494 | $59.70 | +22% |
| Volatility model ≥ 2%, hold to the close | 4987 | -$9.55 | -2% |
| Momentum model ≥ 2%, hold to the close | 4153 | -$25.50 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 31860 | 31842 | 120 (0%) | 1.07% | -$2,189.10 (-57%) | Hold to the close: -$2,189.10 (-57%) |

*In play or awaiting result: 17. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20582 | 4.6% | 0.4% (85) | -651% | ❌ Worse |
| Momentum model | 20582 | 4.5% | 0.4% (85) | -675% | ❌ Worse |
| Mean-reversion model | 20582 | 7.9% | 0.4% (85) | -789% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20582 | 85 | -48% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 4987 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2698 | 28 | +28% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1527 | 18 | +65% | -66% | -64% | -61% |
| Momentum model ≥ 2% | 4153 | 33 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2494 | 24 | +22% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1626 | 16 | +35% | -70% | -70% | -65% |
| Mean-reversion model ≥ 2% | 8299 | 56 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 5816 | 47 | -11% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3873 | 33 | -4% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20782 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7379 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3681 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 31842 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,189.10 | -57% | — |
| Sell at 2¢ | 1178 | 4% | -$3,394.82 | -88% | 47 sec |
| Sell at 3¢ | 809 | 3% | -$3,385.59 | -88% | 48 sec |
| Sell at 5¢ | 564 | 2% | -$3,334.50 | -86% | 61 sec |
| Sell at 10¢ | 348 | 1% | -$3,203.22 | -83% | 64 sec |
| Sell at 25¢ | 189 | 1% | -$2,963.51 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,681.60 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1403 | 7 | 11% | 4% | -52% | -81% | -83% |
| 2–5 min | 10212 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8061 | 30 | 3% | 1% | -59% | -92% | -91% |
| Under 1 min | 12162 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2329 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2322 | 8 | 5% | 3% | -57% | -89% | -87% |
| BNB | 2318 | 13 | 5% | 3% | -30% | -84% | -83% |
| SOL | 2314 | 6 | 3% | 2% | -68% | -92% | -92% |
| ETH | 2309 | 11 | 6% | 3% | -43% | -86% | -86% |
| DOGE | 2304 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2298 | 12 | 5% | 2% | -32% | -82% | -81% |
| XRP | 2298 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2290 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1194 | 4 | 4% | 2% | -60% | -81% | -83% |
| SILVER | 1160 | 5 | 4% | 1% | -50% | -82% | -82% |
| WTI | 1147 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1013 | 0 | 1% | 1% | -100% | -98% | -98% |
| COPPER | 990 | 4 | 1% | 1% | -62% | -69% | -69% |
| EURUSD | 944 | 3 | 2% | 1% | -70% | -86% | -86% |
| NATGAS | 937 | 5 | 2% | 1% | -50% | -87% | -86% |
| PALLADIUM | 899 | 2 | 1% | 0% | -79% | -88% | -88% |
| GBPUSD | 889 | 1 | 2% | 1% | -90% | -96% | -96% |
| USDJPY | 872 | 5 | 1% | 1% | -46% | -98% | -97% |
| AUDUSD | 433 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 391 | 0 | 2% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16134 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15708 | 54 | 4% | 1% | -60% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3483 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3575 | 11 | 3% | 2% | -55% | -92% | -92% |
| 0.1–0.2% | 5379 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6037 | 28 | 6% | 3% | -49% | -87% | -86% |
| Over 0.5% | 2304 | 10 | 7% | 3% | -55% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7582 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8575 | 29 | 3% | 2% | -61% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,824 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 5:44:58 PM | BTC | DOWN | 1 sec | -0.020% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:58 PM | SOL | UP | 1 sec | -0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:58 PM | ETH | UP | 1 sec | -0.062% | 0¢ | In play | — |
| 10/25 5:44:58 PM | GOLD | UP | 1 sec | — | 0¢ | In play | — |
| 10/25 5:44:58 PM | USDCAD | UP | 1 sec | — | 0¢ | In play | — |
| 10/25 5:44:58 PM | BNB | DOWN | 1 sec | -0.039% | 0¢ | ❌ Lost | $0.00 |
| 10/25 5:44:41 PM | NEAR | DOWN | 18 sec | -0.022% | 1¢ | In play | — |
| 10/25 5:44:41 PM | HYPE | UP | 18 sec | -0.063% | 1¢ | In play | — |
| 10/25 5:44:09 PM | XRP | DOWN | 50 sec | +0.101% | 1¢ | In play | — |
| 10/25 5:43:55 PM | AUDUSD | DOWN | 64 sec | — | 0¢ | In play | — |
| 10/25 5:43:40 PM | EURUSD | DOWN | 79 sec | — | 0¢ | In play | — |
| 10/25 5:43:40 PM | USDJPY | UP | 79 sec | — | 0¢ | In play | — |
| 10/25 5:42:37 PM | ZEC | UP | 2.4 min | -0.755% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:42:21 PM | GBPUSD | DOWN | 2.6 min | — | 0¢ | In play | — |
| 10/25 5:29:45 PM | EURUSD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:29:29 PM | COPPER | UP | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:29:13 PM | USDJPY | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:28:09 PM | SILVER | UP | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:27:38 PM | PLATINUM | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:27:22 PM | AUDUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:27:22 PM | NEAR | UP | 2.6 min | -0.722% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:27:22 PM | PALLADIUM | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:27:06 PM | ZEC | UP | 2.9 min | -0.513% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:26:50 PM | SOL | UP | 3.2 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:26:50 PM | HYPE | UP | 3.2 min | -0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:26:50 PM | XRP | UP | 3.2 min | -0.285% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:26:33 PM | BNB | UP | 3.5 min | -0.186% | 0¢ | ❌ Lost | -$0.15 |
| 10/25 5:26:17 PM | DOGE | UP | 3.7 min | -0.242% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:25:46 PM | ETH | UP | 4.2 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 5:25:22 PM | BTC | UP | 4.6 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
