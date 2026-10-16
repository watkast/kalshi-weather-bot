# 15-Minute 1¢ Study

*Updated Fri Oct 16, 7:59 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1619 finished bets | 1% | $72.45 | +40% | +4.47¢ | $38.55 / $33.90 |

*Expect about **89 buys a day** (~$13.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1504 | $47.25 | +29% |
| Momentum model ≥ 2%, hold to the close | 2536 | -$13.85 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1619 | -$22.80 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20819 | 20799 | 79 (0%) | 1.07% | -$1,426.45 (-56%) | Hold to the close: -$1,426.45 (-56%) |

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
| Volatility model | 13298 | 4.4% | 0.4% (53) | -646% | ❌ Worse |
| Momentum model | 13298 | 4.4% | 0.4% (53) | -669% | ❌ Worse |
| Mean-reversion model | 13298 | 7.4% | 0.4% (53) | -774% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13298 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2954 | 23 | -10% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1619 | 18 | +40% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 949 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2536 | 20 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1504 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1003 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4997 | 33 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3437 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2257 | 15 | -24% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13496 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5167 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2136 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20799 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,426.45 | -56% | — |
| Sell at 2¢ | 738 | 4% | -$2,242.57 | -89% | 42 sec |
| Sell at 3¢ | 495 | 2% | -$2,241.40 | -89% | 47 sec |
| Sell at 5¢ | 358 | 2% | -$2,201.75 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,120.87 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,950.70 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,740.95 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 683 | 5 | 10% | 3% | -30% | -82% | -86% |
| 2–5 min | 6747 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5414 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7951 | 18 | 1% | 0% | -68% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1515 | 11 | 5% | 3% | -10% | -89% | -89% |
| HYPE | 1511 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1505 | 8 | 5% | 3% | -36% | -88% | -87% |
| DOGE | 1501 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1501 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1498 | 2 | 3% | 2% | -84% | -92% | -91% |
| XRP | 1492 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1488 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1485 | 8 | 6% | 3% | -30% | -78% | -78% |
| GOLD | 844 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 820 | 4 | 3% | 1% | -44% | -79% | -79% |
| WTI | 787 | 3 | 3% | 1% | -56% | -94% | -95% |
| COPPER | 719 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 703 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 648 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 646 | 5 | 2% | 2% | -28% | -82% | -80% |
| EURUSD | 639 | 3 | 3% | 1% | -56% | -81% | -81% |
| GBPUSD | 599 | 1 | 2% | 1% | -84% | -97% | -97% |
| USDJPY | 559 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 182 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 157 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10486 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10313 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2234 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2332 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3420 | 10 | 4% | 2% | -64% | -90% | -90% |
| 0.2–0.5% | 3957 | 21 | 6% | 3% | -42% | -88% | -88% |
| Over 0.5% | 1550 | 6 | 6% | 3% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4816 | 26 | 4% | 2% | -38% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,423 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 7:59:38 AM | AUDUSD | DOWN | 22 sec | — | — | In play | — |
| 10/16 7:59:38 AM | DOGE | DOWN | 22 sec | +0.047% | — | In play | — |
| 10/16 7:59:38 AM | BNB | DOWN | 22 sec | -0.004% | — | In play | — |
| 10/16 7:58:47 AM | BTC | DOWN | 73 sec | +0.100% | — | In play | — |
| 10/16 7:58:47 AM | ZEC | UP | 73 sec | -0.305% | — | In play | — |
| 10/16 7:58:31 AM | SOL | DOWN | 89 sec | +0.225% | — | In play | — |
| 10/16 7:58:15 AM | WTI | UP | 1.8 min | — | — | In play | — |
| 10/16 7:58:00 AM | NEAR | UP | 2.0 min | -0.637% | — | In play | — |
| 10/16 7:57:44 AM | GOLD | DOWN | 2.2 min | — | — | In play | — |
| 10/16 7:57:28 AM | USDCAD | UP | 2.5 min | — | — | In play | — |
| 10/16 7:57:28 AM | USDJPY | UP | 2.5 min | — | — | In play | — |
| 10/16 7:57:12 AM | EURUSD | DOWN | 2.8 min | — | — | In play | — |
| 10/16 7:57:12 AM | GBPUSD | DOWN | 2.8 min | — | — | In play | — |
| 10/16 7:44:58 AM | PALLADIUM | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:58 AM | BNB | UP | 2 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:58 AM | XRP | DOWN | 2 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:42 AM | HYPE | DOWN | 18 sec | +0.109% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:42 AM | AUDUSD | UP | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:42 AM | PLATINUM | DOWN | 18 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:26 AM | BTC | UP | 34 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:11 AM | ETH | UP | 48 sec | -0.158% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:11 AM | SOL | UP | 48 sec | -0.209% | 0¢ | ❌ Lost | $0.00 |
| 10/16 7:44:11 AM | NEAR | DOWN | 48 sec | +0.282% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:44:11 AM | DOGE | UP | 48 sec | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:43:37 AM | COPPER | UP | 83 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:42:50 AM | EURUSD | DOWN | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:42:50 AM | ZEC | DOWN | 2.1 min | +0.514% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:42:18 AM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 7:41:13 AM | WTI | DOWN | 3.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 7:40:39 AM | SILVER | DOWN | 4.3 min | — | 4¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
