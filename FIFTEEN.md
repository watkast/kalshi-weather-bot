# 15-Minute 1¢ Study

*Updated Wed Nov 11, 2:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4220 finished bets | 1% | $175.25 | +37% | +4.15¢ | $85.15 / $90.10 |

*Expect about **95 buys a day** (~$14.19/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3948 | $90.35 | +21% |
| Volatility model ≥ 2%, hold to the close | 7749 | $47.30 | +5% |
| Momentum model ≥ 2%, hold to the close | 6438 | -$26.10 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 53900 | 53879 | 205 (0%) | 1.07% | -$3,701.95 (-56%) | Hold to the close: -$3,701.95 (-56%) |

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
| Volatility model | 32410 | 4.7% | 0.4% (131) | -672% | ❌ Worse |
| Momentum model | 32410 | 4.6% | 0.4% (131) | -697% | ❌ Worse |
| Mean-reversion model | 32410 | 8.1% | 0.4% (131) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32410 | 131 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7749 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4220 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2437 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6438 | 51 | -4% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3948 | 37 | +21% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2589 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13395 | 92 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9367 | 78 | -8% | -80% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6260 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32615 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12903 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8361 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 53879 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 205 | 0% | -$3,701.95 | -56% | — |
| Sell at 2¢ | 2146 | 4% | -$5,733.99 | -87% | 47 sec |
| Sell at 3¢ | 1463 | 3% | -$5,721.38 | -87% | 48 sec |
| Sell at 5¢ | 1013 | 2% | -$5,605.50 | -85% | 63 sec |
| Sell at 10¢ | 612 | 1% | -$5,378.23 | -82% | 65 sec |
| Sell at 25¢ | 325 | 1% | -$4,992.20 | -76% | 82 sec |
| Sell at 50¢ | 212 | 0% | -$4,524.95 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2696 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17425 | 94 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13608 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20138 | 53 | 1% | 0% | -62% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3651 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3647 | 16 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3640 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3632 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3628 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3621 | 15 | 7% | 3% | -49% | -82% | -81% |
| NEAR | 3603 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3602 | 17 | 5% | 2% | -35% | -87% | -88% |
| XRP | 3591 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1942 | 5 | 5% | 2% | -68% | -81% | -83% |
| WTI | 1928 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1894 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1721 | 4 | 2% | 1% | -78% | -96% | -95% |
| EURUSD | 1658 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1610 | 6 | 2% | 1% | -65% | -74% | -74% |
| GBPUSD | 1582 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1579 | 8 | 2% | 1% | -53% | -79% | -78% |
| USDJPY | 1559 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1548 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1115 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1081 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 681 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27314 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26565 | 97 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5176 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5542 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8375 | 30 | 5% | 2% | -55% | -89% | -89% |
| 0.2–0.5% | 9800 | 41 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3714 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 12972 | 57 | 4% | 2% | -49% | -86% | -86% |
| Evening (6pm–12am) | 14588 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,862 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 2:14:45 PM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:45 PM | SOL | UP | 14 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:14:45 PM | BTC | DOWN | 14 sec | +0.059% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:14:29 PM | PALLADIUM | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:29 PM | DOGE | DOWN | 30 sec | +0.023% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:29 PM | WTI | DOWN | 30 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:29 PM | BNB | DOWN | 30 sec | +0.018% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:29 PM | GBPUSD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:14 PM | HYPE | DOWN | 45 sec | +0.135% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:14:14 PM | ETH | UP | 45 sec | -0.065% | 0¢ | ❌ Lost | $0.00 |
| 11/11 2:14:14 PM | SILVER | DOWN | 45 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:13:58 PM | PLATINUM | DOWN | 61 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:13:42 PM | NEAR | DOWN | 77 sec | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:13:42 PM | XRP | DOWN | 77 sec | +0.150% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 2:13:42 PM | ZEC | DOWN | 77 sec | +0.336% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 2:13:10 PM | AUDUSD | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:59:44 PM | INX | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:59:44 PM | GOLD | UP | 16 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/11 1:59:28 PM | AUDUSD | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:59:28 PM | COPPER | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:59:13 PM | WTI | DOWN | 46 sec | — | 2¢ | ❌ Lost | -$0.15 |
| 11/11 1:58:39 PM | PLATINUM | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:58:39 PM | GBPUSD | UP | 81 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:58:08 PM | USDJPY | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:58:08 PM | USDCAD | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:57:52 PM | SILVER | UP | 2.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 1:57:36 PM | NEAR | DOWN | 2.4 min | +0.346% | 4¢ | ❌ Lost | -$0.15 |
| 11/11 1:57:20 PM | EURUSD | UP | 2.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 1:57:20 PM | SOL | DOWN | 2.6 min | +0.269% | 3¢ | ❌ Lost | -$0.15 |
| 11/11 1:56:45 PM | DOGE | DOWN | 3.2 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
