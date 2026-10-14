# 15-Minute 1¢ Study

*Updated Wed Oct 14, 2:49 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1419 finished bets | 1% | $81.55 | +52% | +5.75¢ | $35.95 / $45.60 |

*Expect about **86 buys a day** (~$12.83/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1334 | $52.30 | +36% |
| Momentum model ≥ 2%, hold to the close | 2205 | $11.15 | +4% |
| Volatility model ≥ 2%, hold to the close | 2541 | $1.40 | +0% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 18351 | 18344 | 70 (0%) | 1.07% | -$1,242.55 (-56%) | Hold to the close: -$1,242.55 (-56%) |

*In play or awaiting result: 6. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 11945 | 4.5% | 0.4% (50) | -649% | ❌ Worse |
| Momentum model | 11945 | 4.4% | 0.4% (50) | -674% | ❌ Worse |
| Mean-reversion model | 11945 | 7.3% | 0.4% (50) | -770% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11945 | 50 | -47% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2541 | 22 | +0% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1419 | 17 | +52% | -73% | -71% | -66% |
| Volatility model ≥ 10% | 855 | 10 | +67% | -64% | -62% | -58% |
| Momentum model ≥ 2% | 2205 | 19 | +4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1334 | 14 | +36% | -77% | -76% | -74% |
| Momentum model ≥ 10% | 900 | 9 | +41% | -71% | -70% | -65% |
| Mean-reversion model ≥ 2% | 4383 | 30 | -25% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3001 | 23 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1978 | 14 | -19% | -80% | -80% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12143 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4493 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1708 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 18344 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 70 | 0% | -$1,242.55 | -56% | — |
| Sell at 2¢ | 639 | 3% | -$2,014.41 | -91% | 34 sec |
| Sell at 3¢ | 431 | 2% | -$2,012.46 | -91% | 46 sec |
| Sell at 5¢ | 315 | 2% | -$1,975.80 | -89% | 49 sec |
| Sell at 10¢ | 199 | 1% | -$1,891.86 | -85% | 63 sec |
| Sell at 25¢ | 115 | 1% | -$1,743.90 | -78% | 79 sec |
| Sell at 50¢ | 76 | 0% | -$1,541.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 576 | 4 | 10% | 2% | -34% | -82% | -88% |
| 2–5 min | 5915 | 35 | 7% | 3% | -42% | -88% | -88% |
| 1–2 min | 4791 | 18 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 7058 | 13 | 1% | 0% | -73% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1361 | 10 | 5% | 3% | -8% | -89% | -90% |
| HYPE | 1357 | 4 | 4% | 2% | -64% | -90% | -89% |
| ETH | 1354 | 8 | 5% | 3% | -28% | -88% | -87% |
| DOGE | 1353 | 2 | 4% | 2% | -81% | -91% | -90% |
| BNB | 1352 | 5 | 5% | 2% | -55% | -90% | -89% |
| SOL | 1349 | 2 | 3% | 1% | -82% | -93% | -92% |
| BTC | 1340 | 6 | 5% | 2% | -40% | -88% | -91% |
| XRP | 1339 | 7 | 2% | 1% | -35% | -86% | -86% |
| NEAR | 1338 | 8 | 5% | 3% | -22% | -77% | -78% |
| GOLD | 729 | 1 | 4% | 1% | -84% | -91% | -93% |
| SILVER | 716 | 2 | 3% | 1% | -67% | -94% | -94% |
| WTI | 684 | 3 | 3% | 1% | -49% | -94% | -96% |
| COPPER | 635 | 1 | 2% | 2% | -85% | -97% | -96% |
| PLATINUM | 608 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 564 | 1 | 1% | 0% | -83% | -98% | -98% |
| NATGAS | 557 | 3 | 2% | 2% | -50% | -96% | -95% |
| EURUSD | 540 | 3 | 3% | 1% | -48% | -78% | -77% |
| GBPUSD | 508 | 1 | 2% | 1% | -82% | -97% | -96% |
| USDJPY | 463 | 3 | 1% | 1% | -40% | -99% | -98% |
| AUDUSD | 104 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 93 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9266 | 35 | 3% | 2% | -56% | -90% | -89% |
| DOWN (bought NO) | 9078 | 35 | 4% | 2% | -55% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2093 | 10 | 2% | 1% | -20% | -78% | -78% |
| 0.05–0.1% | 2139 | 7 | 3% | 1% | -53% | -92% | -91% |
| 0.1–0.2% | 3084 | 10 | 4% | 2% | -60% | -91% | -90% |
| 0.2–0.5% | 3473 | 20 | 6% | 3% | -37% | -88% | -88% |
| Over 0.5% | 1351 | 5 | 6% | 2% | -62% | -89% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4717 | 20 | 4% | 2% | -52% | -87% | -88% |
| Morning (6am–12pm) | 4329 | 23 | 4% | 2% | -38% | -91% | -91% |
| Afternoon (12–6pm) | 4294 | 12 | 3% | 1% | -67% | -90% | -91% |
| Evening (6pm–12am) | 5004 | 15 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,493 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/14 2:44:45 PM | WTI | DOWN | 14 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:44:29 PM | PLATINUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:29 PM | USDCAD | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:29 PM | PALLADIUM | UP | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:44:13 PM | SILVER | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:43:56 PM | GOLD | UP | 64 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:42:49 PM | BTC | UP | 2.2 min | -0.161% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:42:49 PM | XRP | UP | 2.2 min | -0.257% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:42:02 PM | HYPE | UP | 3.0 min | -0.378% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:42:02 PM | NEAR | UP | 3.0 min | -0.688% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:41:27 PM | DOGE | UP | 3.5 min | -0.451% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:41:11 PM | BNB | UP | 3.8 min | -0.204% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:40:40 PM | SOL | UP | 4.3 min | -0.366% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:40:40 PM | ETH | UP | 4.3 min | -0.318% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:40:24 PM | ZEC | UP | 4.6 min | -0.973% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:44 PM | NEAR | UP | 15 sec | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:44 PM | BTC | UP | 15 sec | -0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:29:44 PM | SOL | DOWN | 15 sec | +0.002% | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:44 PM | GOLD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:44 PM | BNB | DOWN | 15 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:29:28 PM | DOGE | UP | 31 sec | -0.073% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:29:12 PM | USDCAD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:12 PM | WTI | UP | 48 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/14 2:29:12 PM | USDJPY | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:28:37 PM | NATGAS | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:28:21 PM | ZEC | UP | 1.6 min | -0.376% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:28:06 PM | ETH | UP | 1.9 min | -0.156% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:28:06 PM | XRP | UP | 1.9 min | -0.234% | 0¢ | ❌ Lost | $0.00 |
| 10/14 2:28:06 PM | COPPER | DOWN | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/14 2:27:49 PM | HYPE | UP | 2.2 min | -0.263% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
