# 15-Minute 1¢ Study

*Updated Fri Oct 16, 3:29 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1604 finished bets | 1% | $73.95 | +42% | +4.61¢ | $39.30 / $34.65 |

*Expect about **89 buys a day** (~$13.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1490 | $48.60 | +30% |
| Momentum model ≥ 2%, hold to the close | 2504 | -$10.25 | -4% |
| Volatility model ≥ 5%, sell at 50¢ | 1604 | -$21.30 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20530 | 20513 | 79 (0%) | 1.07% | -$1,389.40 (-56%) | Hold to the close: -$1,389.40 (-56%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 13142 | 4.4% | 0.4% (53) | -645% | ❌ Worse |
| Momentum model | 13142 | 4.4% | 0.4% (53) | -668% | ❌ Worse |
| Mean-reversion model | 13142 | 7.4% | 0.4% (53) | -771% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13142 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2918 | 23 | -9% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1604 | 18 | +42% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 939 | 11 | +67% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2504 | 20 | -4% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1490 | 15 | +30% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 995 | 10 | +41% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4930 | 33 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3388 | 26 | -15% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2219 | 15 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13340 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5078 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2095 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20513 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,389.40 | -56% | — |
| Sell at 2¢ | 723 | 4% | -$2,209.42 | -89% | 42 sec |
| Sell at 3¢ | 484 | 2% | -$2,208.64 | -89% | 47 sec |
| Sell at 5¢ | 353 | 2% | -$2,167.95 | -87% | 50 sec |
| Sell at 10¢ | 217 | 1% | -$2,085.13 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,913.65 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,703.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6647 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5343 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7859 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1497 | 11 | 5% | 3% | -9% | -89% | -90% |
| HYPE | 1493 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1487 | 8 | 5% | 3% | -35% | -88% | -87% |
| BNB | 1485 | 5 | 4% | 2% | -59% | -90% | -90% |
| DOGE | 1483 | 2 | 4% | 2% | -83% | -90% | -89% |
| SOL | 1480 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1475 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1471 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1469 | 8 | 5% | 3% | -29% | -78% | -79% |
| GOLD | 829 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 806 | 4 | 3% | 1% | -43% | -79% | -80% |
| WTI | 773 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 709 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 689 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 638 | 2 | 1% | 0% | -71% | -83% | -84% |
| NATGAS | 634 | 5 | 2% | 2% | -26% | -81% | -80% |
| EURUSD | 629 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 590 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 554 | 3 | 1% | 1% | -49% | -99% | -98% |
| AUDUSD | 172 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 150 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10325 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10188 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2220 | 11 | 2% | 1% | -17% | -79% | -78% |
| 0.05–0.1% | 2311 | 7 | 3% | 1% | -56% | -92% | -92% |
| 0.1–0.2% | 3380 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3892 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1534 | 6 | 6% | 2% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5188 | 20 | 4% | 2% | -56% | -87% | -88% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,439 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 3:29:01 AM | ZEC | UP | 58 sec | -0.170% | — | In play | — |
| 10/16 3:29:01 AM | ETH | UP | 58 sec | -0.055% | — | In play | — |
| 10/16 3:28:45 AM | SOL | UP | 74 sec | -0.103% | — | In play | — |
| 10/16 3:28:45 AM | XRP | UP | 74 sec | -0.127% | — | In play | — |
| 10/16 3:28:29 AM | AUDUSD | UP | 1.5 min | — | — | In play | — |
| 10/16 3:27:57 AM | BTC | UP | 2.0 min | -0.083% | — | In play | — |
| 10/16 3:27:24 AM | PLATINUM | UP | 2.6 min | — | — | In play | — |
| 10/16 3:27:08 AM | SILVER | UP | 2.9 min | — | — | In play | — |
| 10/16 3:26:52 AM | PALLADIUM | UP | 3.1 min | — | — | In play | — |
| 10/16 3:25:15 AM | GOLD | UP | 4.8 min | — | — | In play | — |
| 10/16 3:14:47 AM | USDJPY | UP | 12 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:14:47 AM | SOL | DOWN | 12 sec | +0.028% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:14:47 AM | XRP | UP | 12 sec | -0.022% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:14:31 AM | HYPE | UP | 28 sec | -0.068% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:14:31 AM | GOLD | DOWN | 28 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:14:15 AM | PLATINUM | DOWN | 44 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:13:59 AM | ZEC | DOWN | 61 sec | +0.158% | 0¢ | ❌ Lost | $0.00 |
| 10/16 3:13:27 AM | USDCAD | UP | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:13:11 AM | GBPUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:13:11 AM | EURUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:12:39 AM | NEAR | UP | 2.4 min | -0.539% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 3:12:23 AM | DOGE | UP | 2.6 min | -0.125% | 10¢ | ❌ Lost | -$0.15 |
| 10/16 3:12:23 AM | ETH | UP | 2.6 min | -0.183% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 3:12:23 AM | BNB | UP | 2.6 min | -0.149% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:59:46 AM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:59:30 AM | AUDUSD | DOWN | 30 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 2:59:30 AM | BNB | DOWN | 30 sec | -0.029% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:59:15 AM | NEAR | DOWN | 44 sec | +0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/16 2:59:15 AM | BTC | UP | 44 sec | -0.044% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 2:58:58 AM | HYPE | DOWN | 62 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
