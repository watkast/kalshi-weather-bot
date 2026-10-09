# 15-Minute 1¢ Study

*Updated Fri Oct 9, 3:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 891 finished bets | 1% | $28.95 | +30% | +3.25¢ | -$19.25 / $48.20 |

*Expect about **77 buys a day** (~$11.50/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 867 | $18.70 | +20% |
| 5+ min left, hold to the close | 383 | -$0.55 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 891 | -$8.30 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 13257 | 13250 | 52 (0%) | 1.07% | -$880.75 (-55%) | Hold to the close: -$880.75 (-55%) |

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
| Volatility model | 8423 | 4.0% | 0.4% (35) | -580% | ❌ Worse |
| Momentum model | 8423 | 4.1% | 0.4% (35) | -614% | ❌ Worse |
| Mean-reversion model | 8423 | 6.7% | 0.4% (35) | -680% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 8423 | 35 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 1627 | 13 | -8% | -75% | -75% | -72% |
| Volatility model ≥ 5% | 891 | 9 | +30% | -68% | -66% | -63% |
| Volatility model ≥ 10% | 545 | 7 | +88% | -52% | -52% | -48% |
| Momentum model ≥ 2% | 1438 | 11 | -8% | -77% | -78% | -75% |
| Momentum model ≥ 5% | 867 | 8 | +20% | -71% | -72% | -69% |
| Momentum model ≥ 10% | 594 | 6 | +44% | -62% | -63% | -59% |
| Mean-reversion model ≥ 2% | 2941 | 20 | -26% | -85% | -85% | -81% |
| Mean-reversion model ≥ 5% | 1985 | 16 | -11% | -82% | -82% | -77% |
| Mean-reversion model ≥ 10% | 1302 | 12 | +6% | -81% | -81% | -76% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 8620 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 3427 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1203 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 13250 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 52 | 0% | -$880.75 | -55% | — |
| Sell at 2¢ | 443 | 3% | -$1,451.57 | -90% | 33 sec |
| Sell at 3¢ | 295 | 2% | -$1,451.70 | -90% | 47 sec |
| Sell at 5¢ | 216 | 2% | -$1,426.35 | -89% | 56 sec |
| Sell at 10¢ | 142 | 1% | -$1,352.73 | -84% | 64 sec |
| Sell at 25¢ | 81 | 1% | -$1,242.64 | -77% | 81 sec |
| Sell at 50¢ | 53 | 0% | -$1,111.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 379 | 4 | 10% | 3% | +0% | -82% | -86% |
| 2–5 min | 4286 | 26 | 6% | 3% | -41% | -89% | -89% |
| 1–2 min | 3459 | 13 | 3% | 2% | -59% | -94% | -94% |
| Under 1 min | 5122 | 9 | 1% | 0% | -74% | -90% | -90% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 964 | 6 | 4% | 3% | -25% | -90% | -90% |
| HYPE | 964 | 3 | 5% | 2% | -61% | -89% | -88% |
| DOGE | 962 | 2 | 3% | 1% | -74% | -92% | -92% |
| BNB | 961 | 4 | 4% | 2% | -50% | -91% | -92% |
| ETH | 957 | 7 | 5% | 2% | -10% | -89% | -89% |
| NEAR | 954 | 5 | 6% | 3% | -31% | -73% | -74% |
| BTC | 954 | 4 | 5% | 2% | -45% | -88% | -90% |
| SOL | 953 | 0 | 3% | 1% | -100% | -94% | -93% |
| XRP | 951 | 6 | 2% | 1% | -21% | -82% | -82% |
| GOLD | 568 | 0 | 4% | 1% | -100% | -92% | -94% |
| SILVER | 555 | 1 | 3% | 1% | -79% | -94% | -94% |
| WTI | 523 | 3 | 3% | 1% | -35% | -94% | -96% |
| COPPER | 490 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 451 | 0 | 0% | 0% | -100% | -100% | -99% |
| NATGAS | 420 | 3 | 3% | 2% | -33% | -95% | -93% |
| PALLADIUM | 420 | 1 | 1% | 0% | -78% | -98% | -99% |
| EURUSD | 412 | 3 | 3% | 2% | -32% | -72% | -71% |
| GBPUSD | 389 | 1 | 3% | 2% | -76% | -96% | -95% |
| USDJPY | 353 | 3 | 1% | 1% | -21% | -98% | -97% |
| AUDUSD | 25 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 24 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 6676 | 27 | 3% | 2% | -53% | -89% | -89% |
| DOWN (bought NO) | 6574 | 25 | 3% | 1% | -56% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 1389 | 8 | 2% | 1% | -0% | -69% | -69% |
| 0.05–0.1% | 1459 | 4 | 3% | 1% | -60% | -92% | -92% |
| 0.1–0.2% | 2203 | 7 | 4% | 2% | -60% | -92% | -92% |
| 0.2–0.5% | 2521 | 13 | 5% | 3% | -43% | -89% | -88% |
| Over 0.5% | 1046 | 5 | 6% | 2% | -51% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 3343 | 18 | 4% | 2% | -38% | -85% | -85% |
| Morning (6am–12pm) | 3238 | 17 | 4% | 2% | -40% | -91% | -91% |
| Afternoon (12–6pm) | 3048 | 8 | 3% | 1% | -69% | -90% | -90% |
| Evening (6pm–12am) | 3621 | 9 | 3% | 1% | -72% | -95% | -95% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,040 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/9 3:29:50 PM | BTC | DOWN | 10 sec | +0.010% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:29:34 PM | XRP | DOWN | 26 sec | +0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:29:18 PM | NATGAS | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:28:31 PM | HYPE | DOWN | 88 sec | +0.128% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:28:31 PM | SOL | DOWN | 88 sec | +0.076% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:43 PM | BNB | DOWN | 2.3 min | +0.047% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:27 PM | ZEC | DOWN | 2.5 min | +0.408% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:27 PM | DOGE | DOWN | 2.5 min | +0.158% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:27:11 PM | NEAR | DOWN | 2.8 min | +0.492% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:54 PM | ZEC | DOWN | 6 sec | +0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:14:38 PM | WTI | UP | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:38 PM | NATGAS | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:14:22 PM | ETH | DOWN | 38 sec | +0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:14:06 PM | SOL | DOWN | 54 sec | +0.029% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:13:35 PM | HYPE | DOWN | 84 sec | +0.200% | 0¢ | ❌ Lost | $0.00 |
| 10/9 3:12:41 PM | BTC | DOWN | 2.3 min | +0.093% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:12:41 PM | NEAR | DOWN | 2.3 min | +0.478% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 3:11:54 PM | XRP | DOWN | 3.1 min | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:10:50 PM | BNB | DOWN | 4.2 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 3:10:50 PM | DOGE | DOWN | 4.2 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:50 PM | PLATINUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:18 PM | NATGAS | DOWN | 42 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:18 PM | GBPUSD | UP | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:18 PM | USDJPY | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:59:03 PM | GOLD | UP | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:57:59 PM | SOL | DOWN | 2.0 min | +0.236% | 0¢ | ❌ Lost | $0.00 |
| 10/9 2:57:59 PM | XRP | DOWN | 2.0 min | +0.115% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:57:09 PM | DOGE | DOWN | 2.9 min | +0.189% | 1¢ | ❌ Lost | -$0.15 |
| 10/9 2:56:54 PM | ZEC | DOWN | 3.1 min | +0.415% | 0¢ | ❌ Lost | -$0.15 |
| 10/9 2:56:06 PM | BTC | DOWN | 3.9 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
