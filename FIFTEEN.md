# 15-Minute 1¢ Study

*Updated Thu Nov 12, 3:27 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4233 finished bets | 1% | $174.35 | +37% | +4.12¢ | $84.25 / $90.10 |

*Expect about **94 buys a day** (~$14.06/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3969 | $102.10 | +24% |
| Volatility model ≥ 2%, hold to the close | 7780 | $44.00 | +5% |
| Momentum model ≥ 2%, hold to the close | 6465 | -$15.10 | -2% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 54465 | 54432 | 209 (0%) | 1.07% | -$3,714.35 (-56%) | Hold to the close: -$3,714.35 (-56%) |

*In play or awaiting result: 21. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 32685 | 4.7% | 0.4% (132) | -669% | ❌ Worse |
| Momentum model | 32685 | 4.6% | 0.4% (132) | -694% | ❌ Worse |
| Mean-reversion model | 32685 | 8.1% | 0.4% (132) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 32685 | 132 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7780 | 70 | +5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 4233 | 46 | +37% | -72% | -70% | -67% |
| Volatility model ≥ 10% | 2447 | 28 | +64% | -62% | -61% | -57% |
| Momentum model ≥ 2% | 6465 | 52 | -2% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 3969 | 38 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2602 | 25 | +35% | -66% | -65% | -61% |
| Mean-reversion model ≥ 2% | 13476 | 92 | -25% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 9419 | 78 | -8% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 6291 | 56 | +1% | -77% | -77% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 32890 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 13066 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 8476 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 54432 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 209 | 0% | -$3,714.35 | -56% | — |
| Sell at 2¢ | 2164 | 4% | -$5,783.71 | -87% | 47 sec |
| Sell at 3¢ | 1472 | 3% | -$5,772.27 | -87% | 48 sec |
| Sell at 5¢ | 1018 | 2% | -$5,656.65 | -85% | 63 sec |
| Sell at 10¢ | 616 | 1% | -$5,427.39 | -82% | 65 sec |
| Sell at 25¢ | 328 | 1% | -$5,036.67 | -76% | 82 sec |
| Sell at 50¢ | 215 | 0% | -$4,559.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2712 | 13 | 11% | 4% | -55% | -81% | -83% |
| 2–5 min | 17596 | 96 | 7% | 3% | -46% | -87% | -87% |
| 1–2 min | 13743 | 45 | 3% | 2% | -64% | -92% | -92% |
| Under 1 min | 20369 | 55 | 1% | 0% | -62% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3681 | 17 | 5% | 2% | -40% | -88% | -88% |
| SOL | 3678 | 16 | 4% | 2% | -45% | -87% | -87% |
| HYPE | 3670 | 11 | 5% | 2% | -62% | -89% | -88% |
| BNB | 3662 | 19 | 5% | 2% | -35% | -86% | -85% |
| DOGE | 3658 | 8 | 4% | 2% | -72% | -90% | -90% |
| ETH | 3653 | 16 | 7% | 3% | -46% | -82% | -81% |
| NEAR | 3634 | 17 | 5% | 2% | -39% | -85% | -85% |
| BTC | 3633 | 17 | 5% | 2% | -36% | -87% | -88% |
| XRP | 3621 | 13 | 3% | 1% | -55% | -89% | -89% |
| GOLD | 1962 | 5 | 5% | 2% | -69% | -82% | -84% |
| WTI | 1953 | 6 | 4% | 2% | -63% | -91% | -92% |
| SILVER | 1913 | 9 | 5% | 2% | -44% | -83% | -82% |
| PLATINUM | 1742 | 4 | 3% | 1% | -79% | -96% | -95% |
| EURUSD | 1680 | 6 | 2% | 1% | -67% | -90% | -89% |
| COPPER | 1628 | 6 | 2% | 1% | -66% | -74% | -74% |
| GBPUSD | 1609 | 6 | 2% | 1% | -65% | -96% | -96% |
| NATGAS | 1601 | 9 | 2% | 1% | -48% | -73% | -73% |
| USDJPY | 1584 | 6 | 2% | 1% | -65% | -96% | -96% |
| PALLADIUM | 1565 | 4 | 1% | 1% | -76% | -92% | -92% |
| AUDUSD | 1138 | 6 | 2% | 1% | -51% | -88% | -88% |
| USDCAD | 1099 | 0 | 2% | 1% | -100% | -96% | -96% |
| BRENT | 702 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 353 | 2 | 4% | 2% | -47% | -66% | -64% |
| 2YRRATE | 338 | 4 | 4% | 2% | +10% | -38% | -36% |
| 30YRRATE | 332 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 311 | 2 | 4% | 2% | -40% | -93% | -95% |
| INX | 32 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 27646 | 109 | 4% | 2% | -55% | -88% | -88% |
| DOWN (bought NO) | 26786 | 100 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5205 | 25 | 2% | 1% | -15% | -77% | -77% |
| 0.05–0.1% | 5593 | 20 | 3% | 2% | -45% | -91% | -91% |
| 0.1–0.2% | 8438 | 31 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9900 | 41 | 6% | 3% | -54% | -87% | -87% |
| Over 0.5% | 3746 | 17 | 7% | 3% | -53% | -87% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 13256 | 44 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 13083 | 60 | 4% | 2% | -48% | -85% | -84% |
| Afternoon (12–6pm) | 13132 | 58 | 4% | 2% | -48% | -86% | -86% |
| Evening (6pm–12am) | 14961 | 47 | 4% | 2% | -64% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,868 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/12 3:27:20 AM | PALLADIUM | UP | 2.6 min | — | — | In play | — |
| 11/12 3:27:20 AM | EURUSD | DOWN | 2.6 min | — | — | In play | — |
| 11/12 3:26:33 AM | XRP | DOWN | 3.5 min | +0.276% | — | In play | — |
| 11/12 3:24:58 AM | DOGE | DOWN | 5.0 min | +0.255% | — | In play | — |
| 11/12 3:24:58 AM | NEAR | DOWN | 5.0 min | +0.455% | — | In play | — |
| 11/12 3:24:58 AM | BTC | DOWN | 5.0 min | +0.181% | — | In play | — |
| 11/12 3:24:42 AM | HYPE | DOWN | 5.3 min | +0.539% | — | In play | — |
| 11/12 3:24:27 AM | AUDUSD | DOWN | 5.5 min | — | — | In play | — |
| 11/12 3:24:27 AM | SOL | DOWN | 5.5 min | +0.329% | — | In play | — |
| 11/12 3:24:27 AM | ZEC | DOWN | 5.5 min | +0.984% | — | In play | — |
| 11/12 3:24:11 AM | BNB | DOWN | 5.8 min | +0.143% | — | In play | — |
| 11/12 3:23:55 AM | ETH | DOWN | 6.1 min | +0.295% | — | In play | — |
| 11/12 3:14:55 AM | GBPUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:55 AM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:55 AM | DOGE | DOWN | 5 sec | +0.045% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:38 AM | COPPER | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:22 AM | XRP | DOWN | 38 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:22 AM | BNB | DOWN | 38 sec | -0.007% | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:22 AM | PALLADIUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:14:06 AM | EURUSD | UP | 54 sec | — | 67¢ | ✅ Won | $13.85 |
| 11/12 3:13:51 AM | AUDUSD | DOWN | 68 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:13:35 AM | GOLD | DOWN | 85 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/12 3:13:03 AM | NEAR | UP | 1.9 min | -0.463% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:13:03 AM | BTC | UP | 1.9 min | -0.108% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:12:48 AM | SOL | UP | 2.2 min | -0.210% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:12:33 AM | HYPE | UP | 2.4 min | -0.225% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:12:33 AM | USDCAD | UP | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:12:17 AM | BRENT | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/12 3:12:17 AM | ETH | UP | 2.7 min | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 11/12 3:10:42 AM | USDJPY | UP | 4.3 min | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
