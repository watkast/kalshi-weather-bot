# 15-Minute 1¢ Study

*Updated Wed Nov 11, 7:21 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4223 finished bets | 1% | $175.10 | +37% | +4.15¢ | $85.00 / $90.10 |

*Expect about **94 buys a day** (~$14.13/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3953 | $103.90 | +24% |
| Volatility model ≥ 2%, hold to the close | 7760 | $46.10 | +5% |
| Momentum model ≥ 2%, hold to the close | 6444 | -$12.70 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54156 | 54135 | 206 (0%) | 1.07% | -$3,719.15 (-56%) | Hold to the close: -$3,719.15 (-56%) |

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
| Volatility model | 32544 | 4.7% | 0.4% (132) | -668% | ❌ Worse |
| Momentum model | 32544 | 4.6% | 0.4% (132) | -693% | ❌ Worse |
| Mean-reversion model | 32544 | 8.1% | 0.4% (132) | -810% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32544 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7760 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4223 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2440 | 28 | +65% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6444 | 52 | -2% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3953 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2591 | 25 | +36% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13443 | 92 | -25% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9397 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6274 | 56 | +2% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32749 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12976 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8410 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54135 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 206 | 0% | -$3,719.15 | -56% | — |
| Sell at 2¢ | 2153 | 4% | -$5,763.37 | -87% | 47 sec |
| Sell at 3¢ | 1466 | 3% | -$5,751.41 | -87% | 48 sec |
| Sell at 5¢ | 1015 | 2% | -$5,635.40 | -85% | 63 sec |
| Sell at 10¢ | 613 | 1% | -$5,408.12 | -82% | 65 sec |
| Sell at 25¢ | 326 | 1% | -$5,020.09 | -76% | 82 sec |
| Sell at 50¢ | 213 | 0% | -$4,549.40 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2700 | 13 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 17531 | 95 | 7% | 3% | -47% | -87% | -87% |
| 1–2 min | 13666 | 45 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 20226 | 53 | 1% | 0% | -63% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3665 | 17 | 5% | 2% | -40% | -88% | -87% |
| SOL | 3662 | 16 | 4% | 2% | -44% | -87% | -86% |
| HYPE | 3654 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3647 | 19 | 5% | 2% | -34% | -86% | -85% |
| DOGE | 3643 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3637 | 16 | 7% | 3% | -45% | -82% | -81% |
| NEAR | 3618 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3617 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3606 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1951 | 5 | 5% | 2% | -69% | -81% | -83% |
| WTI | 1941 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1903 | 8 | 5% | 2% | -50% | -83% | -83% |
| PLATINUM | 1731 | 4 | 3% | 1% | -78% | -96% | -95% |
| EURUSD | 1667 | 5 | 2% | 1% | -72% | -90% | -90% |
| COPPER | 1616 | 6 | 2% | 1% | -65% | -74% | -74% |
| GBPUSD | 1594 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1591 | 8 | 2% | 1% | -53% | -79% | -78% |
| USDJPY | 1570 | 6 | 2% | 1% | -64% | -97% | -96% |
| PALLADIUM | 1554 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1124 | 6 | 2% | 1% | -50% | -88% | -88% |
| USDCAD | 1089 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 689 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27463 | 108 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26672 | 98 | 4% | 2% | -58% | -86% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5186 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5557 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8400 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9858 | 41 | 6% | 3% | -54% | -87% | -86% |
| Over 0.5% | 3740 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13236 | 43 | 4% | 2% | -63% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14684 | 45 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,871 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/11 7:14:59 PM | PALLADIUM | UP | 1 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:14:11 PM | SILVER | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:55 PM | NATGAS | DOWN | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:23 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:13:07 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:51 PM | GBPUSD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:51 PM | USDJPY | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:51 PM | DOGE | DOWN | 2.1 min | +0.259% | 0¢ | ❌ Lost | $0.00 |
| 11/11 7:12:35 PM | NEAR | DOWN | 2.4 min | +0.464% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:19 PM | BRENT | DOWN | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:03 PM | PLATINUM | DOWN | 2.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 7:12:03 PM | BNB | DOWN | 2.9 min | +0.183% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:22 PM | SOL | DOWN | 3.6 min | +0.456% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:22 PM | ETH | DOWN | 3.6 min | +0.387% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:22 PM | BTC | DOWN | 3.6 min | +0.238% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:22 PM | XRP | DOWN | 3.6 min | +0.363% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:03 PM | HYPE | DOWN | 4.0 min | +0.515% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:11:03 PM | ZEC | DOWN | 4.0 min | +1.170% | 1¢ | ❌ Lost | -$0.15 |
| 11/11 7:10:47 PM | WTI | DOWN | 4.2 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:54 PM | PALLADIUM | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:54 PM | AUDUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:54 PM | NATGAS | DOWN | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:54 PM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:54 PM | BTC | DOWN | 6 sec | +0.037% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:59:38 PM | GBPUSD | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:59:38 PM | ETH | UP | 22 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:59:23 PM | NEAR | DOWN | 37 sec | +0.078% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:59:23 PM | ZEC | DOWN | 37 sec | +0.151% | 0¢ | ❌ Lost | $0.00 |
| 11/11 6:59:04 PM | BRENT | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/11 6:58:48 PM | WTI | DOWN | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
