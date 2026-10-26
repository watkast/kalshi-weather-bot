# 15-Minute 1¢ Study

*Updated Sun Oct 25, 11:59 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2714 finished bets | 1% | $84.05 | +27% | +3.10¢ | $33.05 / $51.00 |

*Expect about **97 buys a day** (~$14.57/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2521 | $57.30 | +21% |
| Volatility model ≥ 2%, hold to the close | 5031 | -$14.20 | -2% |
| Momentum model ≥ 2%, hold to the close | 4196 | -$29.85 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 32265 | 32245 | 120 (0%) | 1.07% | -$2,236.65 (-57%) | Hold to the close: -$2,236.65 (-57%) |

*In play or awaiting result: 19. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 20791 | 4.6% | 0.4% (85) | -657% | ❌ Worse |
| Momentum model | 20791 | 4.5% | 0.4% (85) | -682% | ❌ Worse |
| Mean-reversion model | 20791 | 7.9% | 0.4% (85) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 20791 | 85 | -49% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 5031 | 43 | -2% | -78% | -77% | -74% |
| Volatility model ≥ 5% | 2714 | 28 | +27% | -75% | -73% | -70% |
| Volatility model ≥ 10% | 1536 | 18 | +64% | -66% | -65% | -61% |
| Momentum model ≥ 2% | 4196 | 33 | -6% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 2521 | 24 | +21% | -77% | -76% | -72% |
| Momentum model ≥ 10% | 1643 | 16 | +33% | -71% | -70% | -66% |
| Mean-reversion model ≥ 2% | 8377 | 56 | -27% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 5869 | 47 | -12% | -81% | -80% | -78% |
| Mean-reversion model ≥ 10% | 3908 | 33 | -5% | -78% | -78% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 20991 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 7492 | 2% | 2% | 1% | 1% | 0% | 0% |
| Financials | 3762 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 32245 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 120 | 0% | -$2,236.65 | -57% | — |
| Sell at 2¢ | 1200 | 4% | -$3,436.65 | -88% | 47 sec |
| Sell at 3¢ | 823 | 3% | -$3,427.68 | -88% | 48 sec |
| Sell at 5¢ | 572 | 2% | -$3,376.85 | -86% | 61 sec |
| Sell at 10¢ | 354 | 1% | -$3,242.91 | -83% | 65 sec |
| Sell at 25¢ | 191 | 1% | -$3,004.44 | -77% | 82 sec |
| Sell at 50¢ | 122 | 0% | -$2,729.15 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1409 | 7 | 11% | 4% | -53% | -81% | -82% |
| 2–5 min | 10331 | 55 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 8161 | 30 | 3% | 1% | -60% | -92% | -91% |
| Under 1 min | 12340 | 28 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 2352 | 12 | 5% | 2% | -35% | -89% | -89% |
| HYPE | 2345 | 8 | 5% | 3% | -58% | -89% | -86% |
| BNB | 2342 | 13 | 5% | 3% | -31% | -84% | -83% |
| SOL | 2338 | 6 | 3% | 1% | -68% | -92% | -92% |
| ETH | 2332 | 11 | 6% | 3% | -43% | -86% | -85% |
| DOGE | 2325 | 4 | 4% | 2% | -78% | -91% | -90% |
| NEAR | 2322 | 12 | 5% | 2% | -33% | -82% | -81% |
| XRP | 2322 | 9 | 3% | 1% | -52% | -89% | -88% |
| BTC | 2313 | 12 | 5% | 2% | -30% | -88% | -89% |
| GOLD | 1214 | 4 | 4% | 1% | -61% | -81% | -83% |
| SILVER | 1179 | 5 | 4% | 2% | -51% | -82% | -82% |
| WTI | 1157 | 3 | 3% | 1% | -69% | -94% | -95% |
| PLATINUM | 1027 | 0 | 1% | 1% | -100% | -98% | -97% |
| COPPER | 1004 | 4 | 1% | 1% | -63% | -70% | -70% |
| EURUSD | 959 | 3 | 2% | 1% | -71% | -86% | -86% |
| NATGAS | 953 | 5 | 2% | 1% | -51% | -87% | -86% |
| PALLADIUM | 915 | 2 | 1% | 0% | -80% | -88% | -88% |
| GBPUSD | 905 | 1 | 2% | 1% | -90% | -96% | -97% |
| USDJPY | 889 | 5 | 1% | 1% | -48% | -98% | -97% |
| AUDUSD | 448 | 0 | 1% | 0% | -100% | -98% | -98% |
| USDCAD | 409 | 0 | 1% | 0% | -100% | -97% | -99% |
| 10YRRATE | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| BRENT | 43 | 0 | 0% | 0% | -100% | -100% | -100% |
| 2YRRATE | 40 | 1 | 2% | 0% | +133% | +138% | +133% |
| 30YRRATE | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| 5YRRATE | 30 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 16330 | 66 | 4% | 2% | -53% | -87% | -87% |
| DOWN (bought NO) | 15915 | 54 | 4% | 1% | -61% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 3505 | 18 | 2% | 1% | -13% | -80% | -80% |
| 0.05–0.1% | 3611 | 11 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 5423 | 20 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 6123 | 28 | 6% | 3% | -50% | -87% | -86% |
| Over 0.5% | 2325 | 10 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 7904 | 32 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 7781 | 35 | 4% | 2% | -49% | -88% | -87% |
| Afternoon (12–6pm) | 7607 | 24 | 4% | 2% | -63% | -87% | -88% |
| Evening (6pm–12am) | 8953 | 29 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,820 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/25 11:58:58 PM | COPPER | UP | 62 sec | — | — | In play | — |
| 10/25 11:58:58 PM | AUDUSD | UP | 62 sec | — | — | In play | — |
| 10/25 11:58:42 PM | DOGE | DOWN | 78 sec | +0.104% | — | In play | — |
| 10/25 11:58:42 PM | PLATINUM | UP | 78 sec | — | — | In play | — |
| 10/25 11:58:26 PM | ETH | DOWN | 1.6 min | +0.091% | — | In play | — |
| 10/25 11:58:11 PM | PALLADIUM | UP | 1.8 min | — | — | In play | — |
| 10/25 11:57:53 PM | WTI | UP | 2.1 min | — | — | In play | — |
| 10/25 11:57:53 PM | XRP | DOWN | 2.1 min | +0.101% | — | In play | — |
| 10/25 11:57:53 PM | BRENT | UP | 2.1 min | — | — | In play | — |
| 10/25 11:57:06 PM | HYPE | DOWN | 2.9 min | +0.224% | — | In play | — |
| 10/25 11:57:06 PM | BNB | UP | 2.9 min | -0.143% | — | In play | — |
| 10/25 11:57:06 PM | ZEC | DOWN | 2.9 min | +0.406% | — | In play | — |
| 10/25 11:44:45 PM | SOL | DOWN | 15 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:44:29 PM | NEAR | UP | 31 sec | -0.261% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:44:29 PM | BNB | UP | 31 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:44:14 PM | SILVER | UP | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:44:14 PM | BTC | DOWN | 45 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:44:14 PM | DOGE | DOWN | 45 sec | +0.144% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:55 PM | AUDUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:55 PM | USDCAD | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:55 PM | XRP | UP | 64 sec | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:55 PM | GOLD | UP | 64 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/25 11:43:39 PM | USDJPY | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:23 PM | GBPUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:43:09 PM | EURUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:42:52 PM | ZEC | DOWN | 2.1 min | +0.288% | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:42:36 PM | COPPER | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:42:03 PM | PALLADIUM | UP | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/25 11:41:44 PM | PLATINUM | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/25 11:39:52 PM | HYPE | DOWN | 5.1 min | +0.296% | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
