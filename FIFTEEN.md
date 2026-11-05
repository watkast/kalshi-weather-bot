# 15-Minute 1¢ Study

*Updated Wed Nov 4, 9:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3681 finished bets | 1% | $136.05 | +33% | +3.70¢ | $89.70 / $46.35 |

*Expect about **97 buys a day** (~$14.56/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3415 | $63.80 | +17% |
| Volatility model ≥ 2%, hold to the close | 6816 | $45.40 | +6% |
| Momentum model ≥ 2%, hold to the close | 5624 | -$31.70 | -5% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 46156 | 46128 | 170 (0%) | 1.07% | -$3,244.25 (-58%) | Hold to the close: -$3,244.25 (-58%) |

*In play or awaiting result: 26. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 28097 | 4.7% | 0.4% (110) | -678% | ❌ Worse |
| Momentum model | 28097 | 4.6% | 0.4% (110) | -705% | ❌ Worse |
| Mean-reversion model | 28097 | 8.1% | 0.4% (110) | -826% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28097 | 110 | -50% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6816 | 62 | +6% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3681 | 39 | +33% | -76% | -75% | -71% |
| Volatility model ≥ 10% | 2096 | 24 | +64% | -71% | -69% | -66% |
| Momentum model ≥ 2% | 5624 | 44 | -5% | -81% | -81% | -78% |
| Momentum model ≥ 5% | 3415 | 31 | +17% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2231 | 20 | +26% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11634 | 80 | -25% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8164 | 69 | -6% | -81% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5468 | 49 | +2% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28302 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11007 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 6819 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 46128 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 170 | 0% | -$3,244.25 | -58% | — |
| Sell at 2¢ | 1813 | 4% | -$4,900.87 | -87% | 47 sec |
| Sell at 3¢ | 1238 | 3% | -$4,889.43 | -87% | 48 sec |
| Sell at 5¢ | 857 | 2% | -$4,787.20 | -85% | 63 sec |
| Sell at 10¢ | 518 | 1% | -$4,581.67 | -81% | 65 sec |
| Sell at 25¢ | 269 | 1% | -$4,257.86 | -76% | 83 sec |
| Sell at 50¢ | 173 | 0% | -$3,882.50 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 11 | 0 | 27% | 18% | -100% | -53% | -29% |
| 5–10 min | 2289 | 10 | 10% | 4% | -58% | -81% | -83% |
| 2–5 min | 14855 | 79 | 7% | 3% | -48% | -87% | -86% |
| 1–2 min | 11606 | 39 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17367 | 42 | 1% | 0% | -66% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3171 | 13 | 5% | 2% | -47% | -88% | -88% |
| SOL | 3166 | 12 | 4% | 2% | -52% | -90% | -90% |
| HYPE | 3158 | 9 | 5% | 2% | -64% | -89% | -87% |
| BNB | 3158 | 17 | 5% | 2% | -32% | -85% | -84% |
| DOGE | 3146 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3139 | 12 | 7% | 3% | -53% | -85% | -85% |
| BTC | 3125 | 15 | 5% | 2% | -35% | -88% | -89% |
| NEAR | 3123 | 16 | 5% | 2% | -34% | -84% | -84% |
| XRP | 3116 | 12 | 3% | 1% | -52% | -89% | -89% |
| GOLD | 1701 | 5 | 5% | 2% | -64% | -81% | -83% |
| SILVER | 1655 | 8 | 5% | 2% | -43% | -82% | -82% |
| WTI | 1654 | 5 | 4% | 1% | -64% | -92% | -92% |
| PLATINUM | 1484 | 4 | 2% | 1% | -75% | -96% | -96% |
| EURUSD | 1426 | 3 | 2% | 1% | -80% | -89% | -89% |
| COPPER | 1398 | 6 | 2% | 1% | -60% | -70% | -70% |
| GBPUSD | 1353 | 3 | 2% | 1% | -79% | -96% | -96% |
| NATGAS | 1342 | 8 | 2% | 1% | -44% | -76% | -75% |
| USDJPY | 1332 | 5 | 2% | 1% | -65% | -97% | -96% |
| PALLADIUM | 1330 | 3 | 1% | 1% | -79% | -91% | -91% |
| AUDUSD | 881 | 4 | 2% | 1% | -58% | -86% | -86% |
| USDCAD | 855 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 443 | 0 | 1% | 1% | -100% | -98% | -96% |
| 10YRRATE | 260 | 1 | 5% | 2% | -64% | -56% | -54% |
| 30YRRATE | 244 | 0 | 2% | 1% | -100% | -96% | -95% |
| 2YRRATE | 243 | 2 | 3% | 0% | -23% | -17% | -17% |
| 5YRRATE | 225 | 1 | 4% | 2% | -59% | -92% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23391 | 90 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 22737 | 80 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4550 | 22 | 2% | 1% | -15% | -83% | -82% |
| 0.05–0.1% | 4813 | 18 | 3% | 2% | -43% | -91% | -90% |
| 0.1–0.2% | 7292 | 26 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 8444 | 33 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3195 | 13 | 7% | 3% | -58% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11276 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11422 | 50 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 10960 | 39 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12470 | 41 | 3% | 2% | -62% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,683 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/4 9:44:21 PM | USDCAD | DOWN | 39 sec | — | — | In play | — |
| 11/4 9:42:57 PM | SOL | DOWN | 2.0 min | +0.286% | — | In play | — |
| 11/4 9:42:57 PM | GBPUSD | UP | 2.0 min | — | — | In play | — |
| 11/4 9:42:57 PM | PLATINUM | DOWN | 2.0 min | — | — | In play | — |
| 11/4 9:42:57 PM | COPPER | DOWN | 2.0 min | — | — | In play | — |
| 11/4 9:42:25 PM | BNB | DOWN | 2.6 min | +0.099% | — | In play | — |
| 11/4 9:42:25 PM | DOGE | DOWN | 2.6 min | +0.248% | — | In play | — |
| 11/4 9:42:25 PM | NEAR | DOWN | 2.6 min | +0.507% | — | In play | — |
| 11/4 9:42:25 PM | HYPE | DOWN | 2.6 min | +0.237% | — | In play | — |
| 11/4 9:42:10 PM | PALLADIUM | DOWN | 2.8 min | — | — | In play | — |
| 11/4 9:42:10 PM | USDJPY | DOWN | 2.8 min | — | — | In play | — |
| 11/4 9:41:52 PM | XRP | DOWN | 3.1 min | +0.184% | — | In play | — |
| 11/4 9:41:52 PM | ETH | DOWN | 3.1 min | +0.193% | — | In play | — |
| 11/4 9:41:52 PM | BTC | DOWN | 3.1 min | +0.183% | — | In play | — |
| 11/4 9:41:52 PM | ZEC | DOWN | 3.1 min | +0.460% | — | In play | — |
| 11/4 9:41:05 PM | SILVER | DOWN | 3.9 min | — | — | In play | — |
| 11/4 9:41:05 PM | GOLD | DOWN | 3.9 min | — | — | In play | — |
| 11/4 9:29:59 PM | DOGE | DOWN | 1 sec | +0.001% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:59 PM | NEAR | DOWN | 1 sec | +0.075% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:59 PM | ZEC | UP | 1 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:59 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:59 PM | BRENT | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:29:27 PM | SOL | DOWN | 33 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:27 PM | XRP | DOWN | 33 sec | +0.077% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:27 PM | BTC | DOWN | 33 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:29:12 PM | BNB | DOWN | 47 sec | +0.038% | 0¢ | ❌ Lost | $0.00 |
| 11/4 9:28:53 PM | ETH | DOWN | 67 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:28:37 PM | PALLADIUM | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:28:37 PM | USDCAD | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/4 9:28:21 PM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
