# 15-Minute 1¢ Study

*Updated Thu Nov 5, 7:53 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 3745 finished bets | 1% | $130.05 | +31% | +3.47¢ | $85.80 / $44.25 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3486 | $57.50 | +15% |
| Volatility model ≥ 2%, hold to the close | 6925 | $34.15 | +4% |
| Momentum model ≥ 2%, hold to the close | 5719 | -$41.00 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 47285 | 47268 | 173 (0%) | 1.07% | -$3,340.70 (-58%) | Hold to the close: -$3,340.70 (-58%) |

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
| Volatility model | 28616 | 4.7% | 0.4% (111) | -686% | ❌ Worse |
| Momentum model | 28616 | 4.6% | 0.4% (111) | -713% | ❌ Worse |
| Mean-reversion model | 28616 | 8.1% | 0.4% (111) | -835% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 28616 | 111 | -51% | -88% | -87% | -85% |
| Volatility model ≥ 2% | 6925 | 62 | +4% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 3745 | 39 | +31% | -77% | -75% | -71% |
| Volatility model ≥ 10% | 2141 | 24 | +61% | -71% | -70% | -66% |
| Momentum model ≥ 2% | 5719 | 44 | -6% | -82% | -81% | -78% |
| Momentum model ≥ 5% | 3486 | 31 | +15% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 2282 | 20 | +23% | -75% | -74% | -70% |
| Mean-reversion model ≥ 2% | 11835 | 80 | -26% | -83% | -83% | -81% |
| Mean-reversion model ≥ 5% | 8295 | 69 | -8% | -82% | -81% | -78% |
| Mean-reversion model ≥ 10% | 5553 | 49 | +0% | -80% | -79% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 28821 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 11351 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7096 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 47268 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 173 | 0% | -$3,340.70 | -58% | — |
| Sell at 2¢ | 1853 | 4% | -$5,028.92 | -87% | 47 sec |
| Sell at 3¢ | 1263 | 3% | -$5,018.13 | -87% | 49 sec |
| Sell at 5¢ | 874 | 2% | -$4,914.60 | -85% | 63 sec |
| Sell at 10¢ | 528 | 1% | -$4,707.02 | -82% | 65 sec |
| Sell at 25¢ | 276 | 1% | -$4,373.14 | -76% | 82 sec |
| Sell at 50¢ | 178 | 0% | -$3,987.20 | -69% | 1.8 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2336 | 10 | 10% | 4% | -59% | -82% | -83% |
| 2–5 min | 15218 | 81 | 7% | 3% | -47% | -87% | -86% |
| 1–2 min | 11884 | 40 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 17818 | 42 | 1% | 0% | -66% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3229 | 13 | 5% | 2% | -48% | -88% | -88% |
| SOL | 3223 | 12 | 4% | 2% | -53% | -90% | -90% |
| BNB | 3218 | 17 | 5% | 2% | -34% | -85% | -84% |
| HYPE | 3215 | 10 | 5% | 2% | -61% | -89% | -87% |
| DOGE | 3203 | 6 | 4% | 2% | -76% | -90% | -90% |
| ETH | 3200 | 12 | 7% | 3% | -54% | -85% | -85% |
| NEAR | 3181 | 16 | 5% | 2% | -35% | -84% | -84% |
| BTC | 3180 | 15 | 5% | 2% | -36% | -88% | -89% |
| XRP | 3172 | 12 | 3% | 1% | -53% | -89% | -89% |
| GOLD | 1749 | 5 | 5% | 2% | -65% | -81% | -83% |
| WTI | 1698 | 5 | 4% | 1% | -65% | -92% | -92% |
| SILVER | 1694 | 8 | 5% | 2% | -44% | -82% | -81% |
| PLATINUM | 1527 | 4 | 2% | 1% | -76% | -96% | -96% |
| EURUSD | 1466 | 3 | 2% | 1% | -81% | -89% | -89% |
| COPPER | 1443 | 6 | 2% | 1% | -61% | -71% | -71% |
| GBPUSD | 1394 | 4 | 2% | 1% | -73% | -96% | -96% |
| NATGAS | 1386 | 8 | 2% | 1% | -46% | -76% | -75% |
| PALLADIUM | 1373 | 3 | 1% | 1% | -80% | -91% | -91% |
| USDJPY | 1372 | 5 | 2% | 1% | -66% | -97% | -97% |
| AUDUSD | 920 | 4 | 2% | 1% | -59% | -87% | -87% |
| USDCAD | 897 | 0 | 2% | 1% | -100% | -97% | -98% |
| BRENT | 481 | 0 | 1% | 1% | -100% | -97% | -97% |
| 10YRRATE | 280 | 1 | 4% | 1% | -67% | -59% | -57% |
| 30YRRATE | 265 | 0 | 2% | 1% | -100% | -97% | -95% |
| 2YRRATE | 261 | 3 | 4% | 1% | +7% | -22% | -21% |
| 5YRRATE | 240 | 1 | 5% | 2% | -61% | -92% | -95% |
| INX | 1 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 23974 | 92 | 4% | 2% | -56% | -88% | -87% |
| DOWN (bought NO) | 23294 | 81 | 4% | 2% | -60% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 4618 | 22 | 2% | 1% | -16% | -83% | -82% |
| 0.05–0.1% | 4883 | 18 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 7413 | 26 | 4% | 2% | -56% | -90% | -89% |
| 0.2–0.5% | 8620 | 34 | 6% | 3% | -56% | -87% | -86% |
| Over 0.5% | 3279 | 13 | 7% | 3% | -59% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 11506 | 40 | 4% | 2% | -60% | -87% | -87% |
| Morning (6am–12pm) | 11661 | 51 | 4% | 2% | -50% | -86% | -85% |
| Afternoon (12–6pm) | 11352 | 41 | 4% | 2% | -58% | -86% | -86% |
| Evening (6pm–12am) | 12749 | 41 | 3% | 2% | -63% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,650 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/5 7:44:58 PM | WTI | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:58 PM | DOGE | UP | 1 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:44:58 PM | BRENT | DOWN | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:58 PM | BNB | DOWN | 1 sec | -0.045% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:42 PM | ETH | UP | 17 sec | -0.068% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:44:42 PM | USDJPY | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:42 PM | USDCAD | DOWN | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:42 PM | PLATINUM | UP | 17 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:26 PM | ZEC | UP | 33 sec | -0.244% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:44:26 PM | PALLADIUM | UP | 33 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:26 PM | SOL | DOWN | 33 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:44:11 PM | BTC | UP | 48 sec | -0.086% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:44:11 PM | HYPE | DOWN | 48 sec | +0.044% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:43:37 PM | SILVER | UP | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:43:21 PM | GOLD | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:43:06 PM | AUDUSD | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:43:06 PM | COPPER | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:42:16 PM | NATGAS | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:41:43 PM | XRP | UP | 3.3 min | -0.386% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:54 PM | XRP | UP | 6 sec | -0.041% | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:54 PM | GBPUSD | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:54 PM | USDCAD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:38 PM | BTC | DOWN | 22 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:38 PM | ETH | DOWN | 22 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:29:38 PM | BNB | DOWN | 22 sec | +0.014% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:29:38 PM | ZEC | DOWN | 22 sec | +0.151% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:29:38 PM | SOL | DOWN | 22 sec | +0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/5 7:29:38 PM | GOLD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:22 PM | DOGE | DOWN | 38 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 11/5 7:29:22 PM | HYPE | DOWN | 38 sec | +0.091% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
