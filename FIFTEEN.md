# 15-Minute 1¢ Study

*Updated Thu Oct 15, 4:15 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1547 finished bets | 1% | $80.55 | +47% | +5.21¢ | $28.60 / $51.95 |

*Expect about **88 buys a day** (~$13.15/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1439 | $54.45 | +35% |
| Momentum model ≥ 2%, hold to the close | 2419 | -$0.05 | -0% |
| Volatility model ≥ 5%, sell at 50¢ | 1547 | -$14.70 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 19813 | 19797 | 78 (0%) | 1.07% | -$1,312.35 (-55%) | Hold to the close: -$1,312.35 (-55%) |

*In play or awaiting result: 15. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 12752 | 4.5% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 12752 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 12752 | 7.4% | 0.4% (53) | -761% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 12752 | 53 | -48% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2814 | 23 | -5% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1547 | 18 | +47% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 910 | 11 | +71% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2419 | 20 | -0% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1439 | 15 | +35% | -77% | -76% | -73% |
| Momentum model ≥ 10% | 963 | 10 | +46% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4778 | 33 | -25% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3285 | 26 | -12% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2151 | 15 | -20% | -80% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 12950 | 4% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 4871 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1976 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 19797 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,312.35 | -55% | — |
| Sell at 2¢ | 702 | 4% | -$2,137.83 | -89% | 37 sec |
| Sell at 3¢ | 472 | 2% | -$2,136.27 | -89% | 47 sec |
| Sell at 5¢ | 344 | 2% | -$2,096.75 | -87% | 50 sec |
| Sell at 10¢ | 213 | 1% | -$2,013.32 | -84% | 63 sec |
| Sell at 25¢ | 124 | 1% | -$1,839.91 | -77% | 80 sec |
| Sell at 50¢ | 81 | 0% | -$1,633.60 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 634 | 5 | 11% | 3% | -25% | -81% | -85% |
| 2–5 min | 6418 | 36 | 7% | 3% | -45% | -88% | -88% |
| 1–2 min | 5152 | 20 | 3% | 2% | -58% | -92% | -91% |
| Under 1 min | 7589 | 17 | 1% | 0% | -68% | -89% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1455 | 11 | 5% | 3% | -6% | -89% | -89% |
| HYPE | 1449 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1442 | 8 | 5% | 3% | -33% | -88% | -87% |
| DOGE | 1441 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1440 | 5 | 4% | 2% | -57% | -90% | -90% |
| SOL | 1436 | 2 | 3% | 1% | -83% | -93% | -92% |
| XRP | 1432 | 7 | 3% | 1% | -40% | -86% | -86% |
| BTC | 1429 | 7 | 5% | 2% | -34% | -88% | -91% |
| NEAR | 1426 | 8 | 5% | 3% | -27% | -78% | -78% |
| GOLD | 793 | 1 | 4% | 1% | -85% | -92% | -93% |
| SILVER | 773 | 4 | 3% | 1% | -40% | -79% | -79% |
| WTI | 748 | 3 | 3% | 1% | -53% | -94% | -96% |
| COPPER | 684 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 655 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 610 | 4 | 2% | 2% | -39% | -96% | -94% |
| PALLADIUM | 608 | 2 | 1% | 0% | -69% | -83% | -83% |
| EURUSD | 601 | 3 | 3% | 1% | -53% | -80% | -79% |
| GBPUSD | 565 | 1 | 2% | 1% | -83% | -97% | -96% |
| USDJPY | 525 | 3 | 1% | 1% | -47% | -99% | -98% |
| AUDUSD | 151 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 134 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 9975 | 39 | 3% | 2% | -55% | -89% | -88% |
| DOWN (bought NO) | 9822 | 39 | 4% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2167 | 11 | 2% | 1% | -15% | -79% | -78% |
| 0.05–0.1% | 2233 | 7 | 3% | 1% | -54% | -92% | -92% |
| 0.1–0.2% | 3261 | 10 | 4% | 2% | -62% | -90% | -90% |
| 0.2–0.5% | 3778 | 21 | 6% | 3% | -39% | -88% | -88% |
| Over 0.5% | 1508 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4711 | 16 | 3% | 1% | -60% | -88% | -88% |
| Evening (6pm–12am) | 5409 | 16 | 3% | 2% | -66% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,479 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 4:14:55 PM | WTI | UP | 4 sec | — | 0¢ | In play | — |
| 10/15 4:14:55 PM | NATGAS | UP | 4 sec | — | 0¢ | In play | — |
| 10/15 4:14:55 PM | USDJPY | DOWN | 4 sec | — | 0¢ | In play | — |
| 10/15 4:14:39 PM | EURUSD | UP | 20 sec | — | 0¢ | In play | — |
| 10/15 4:14:23 PM | DOGE | DOWN | 36 sec | +0.041% | 0¢ | In play | — |
| 10/15 4:14:23 PM | NEAR | UP | 36 sec | -0.283% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:14:07 PM | XRP | DOWN | 52 sec | +0.097% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:07 PM | BTC | DOWN | 52 sec | +0.065% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:14:07 PM | SOL | DOWN | 52 sec | +0.062% | 1¢ | In play | — |
| 10/15 4:13:51 PM | HYPE | DOWN | 69 sec | +0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/15 4:13:35 PM | ETH | DOWN | 85 sec | +0.101% | 0¢ | In play | — |
| 10/15 4:12:16 PM | BNB | UP | 2.7 min | -0.133% | 1¢ | In play | — |
| 10/15 4:12:16 PM | ZEC | UP | 2.7 min | -0.371% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 4:12:00 PM | GBPUSD | DOWN | 3.0 min | — | 0¢ | In play | — |
| 10/15 3:59:53 PM | ETH | DOWN | 7 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:59:37 PM | BNB | DOWN | 23 sec | +0.036% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:59:21 PM | XRP | UP | 39 sec | -0.030% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:59:21 PM | DOGE | UP | 39 sec | -0.168% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:58:33 PM | ZEC | UP | 87 sec | -0.178% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:58:33 PM | HYPE | UP | 87 sec | -0.149% | 0¢ | ❌ Lost | $0.00 |
| 10/15 3:57:44 PM | SOL | DOWN | 2.2 min | +0.079% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 3:57:12 PM | BTC | DOWN | 2.8 min | +0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:44:51 PM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:44:35 PM | BTC | UP | 25 sec | -0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/15 3:43:45 PM | NEAR | UP | 75 sec | -0.419% | 0¢ | ❌ Lost | $0.00 |
| 10/15 3:43:45 PM | XRP | UP | 75 sec | -0.119% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:43:45 PM | SOL | UP | 75 sec | -0.118% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 3:43:29 PM | DOGE | UP | 1.5 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:42:58 PM | ETH | DOWN | 2.0 min | +0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 3:42:10 PM | ZEC | UP | 2.8 min | -0.399% | 1¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
