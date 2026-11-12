# 15-Minute 1¢ Study

*Updated Wed Nov 11, 8:13 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4225 finished bets | 1% | $174.80 | +37% | +4.14¢ | $84.85 / $89.95 |

*Expect about **94 buys a day** (~$14.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3955 | $103.60 | +24% |
| Volatility model ≥ 2%, hold to the close | 7767 | $45.05 | +5% |
| Momentum model ≥ 2%, hold to the close | 6447 | -$13.15 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54226 | 54195 | 207 (0%) | 1.07% | -$3,712.95 (-56%) | Hold to the close: -$3,712.95 (-56%) |

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
| Volatility model | 32569 | 4.7% | 0.4% (132) | -668% | ❌ Worse |
| Momentum model | 32569 | 4.6% | 0.4% (132) | -693% | ❌ Worse |
| Mean-reversion model | 32569 | 8.1% | 0.4% (132) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32569 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7767 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4225 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2441 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6447 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3955 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2593 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13454 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9406 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6281 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32774 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12997 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8424 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54195 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 207 | 0% | -$3,712.95 | -56% | — |
| Sell at 2¢ | 2155 | 4% | -$5,756.65 | -87% | 47 sec |
| Sell at 3¢ | 1467 | 3% | -$5,744.82 | -87% | 48 sec |
| Sell at 5¢ | 1015 | 2% | -$5,629.20 | -85% | 63 sec |
| Sell at 10¢ | 613 | 1% | -$5,401.92 | -82% | 65 sec |
| Sell at 25¢ | 326 | 1% | -$5,013.89 | -76% | 82 sec |
| Sell at 50¢ | 213 | 0% | -$4,543.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2706 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17546 | 95 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13681 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20250 | 54 | 1% | 0% | -62% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3668 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3665 | 16 | 4% | 2% | -44% | -86% | -86% |
| HYPE | 3657 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3649 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3645 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3640 | 16 | 7% | 3% | -45% | -82% | -81% |
| NEAR | 3621 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3620 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3609 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1953 | 5 | 5% | 2% | -69% | -82% | -83% |
| WTI | 1944 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1905 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1734 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1670 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1619 | 6 | 2% | 1% | -65% | -74% | -74% |
| GBPUSD | 1597 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1593 | 9 | 2% | 1% | -47% | -73% | -73% |
| USDJPY | 1572 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1557 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1127 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1092 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 692 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27500 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26695 | 99 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5188 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5562 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8409 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9865 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3742 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14744 | 46 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,869 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 8:13:44 PM | HYPE | UP | 76 sec | -0.224% | — | In play | — |
| 11/11 8:13:44 PM | BTC | UP | 76 sec | -0.069% | — | In play | — |
| 11/11 8:12:37 PM | AUDUSD | DOWN | 2.4 min | — | — | In play | — |
| 11/11 8:12:37 PM | SILVER | DOWN | 2.4 min | — | — | In play | — |
| 11/11 8:12:37 PM | ZEC | UP | 2.4 min | -0.506% | — | In play | — |
| 11/11 8:12:02 PM | BNB | UP | 3.0 min | -0.262% | — | In play | — |
| 11/11 8:12:02 PM | SOL | UP | 3.0 min | -0.283% | — | In play | — |
| 11/11 8:12:02 PM | ETH | UP | 3.0 min | -0.203% | — | In play | — |
| 11/11 8:12:02 PM | DOGE | UP | 3.0 min | -0.366% | — | In play | — |
| 11/11 8:11:31 PM | XRP | UP | 3.5 min | -0.371% | — | In play | — |
| 11/11 7:59:55 PM | COPPER | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:55 PM | PLATINUM | DOWN | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:55 PM | USDCAD | UP | 4 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:39 PM | XRP | UP | 20 sec | -0.067% | 0¢ | ❌ Lost | $0.00 |
| 11/11 7:59:39 PM | SOL | UP | 20 sec | -0.015% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:39 PM | NATGAS | DOWN | 20 sec | — | 0¢ | ✅ Won | $13.85 |
| 11/11 7:59:23 PM | GBPUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:23 PM | EURUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:23 PM | ZEC | UP | 37 sec | -0.164% | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:04 PM | BNB | UP | 56 sec | -0.132% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:59:04 PM | ETH | UP | 56 sec | -0.084% | 0¢ | ❌ Lost | $0.00 |
| 11/11 7:58:48 PM | USDJPY | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:58:48 PM | BRENT | UP | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:58:32 PM | PALLADIUM | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:58:32 PM | SILVER | DOWN | 88 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:58:17 PM | GOLD | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:58:17 PM | HYPE | UP | 1.7 min | -0.222% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:58:17 PM | WTI | UP | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:57:58 PM | BTC | UP | 2.0 min | -0.099% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:57:58 PM | NEAR | UP | 2.0 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
