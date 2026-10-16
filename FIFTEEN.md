# 15-Minute 1¢ Study

*Updated Fri Oct 16, 6:38 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1616 finished bets | 1% | $72.60 | +40% | +4.49¢ | $38.55 / $34.05 |

*Expect about **89 buys a day** (~$13.28/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1501 | $47.40 | +29% |
| Momentum model ≥ 2%, hold to the close | 2530 | -$13.25 | -5% |
| Volatility model ≥ 5%, sell at 50¢ | 1616 | -$22.65 | -13% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20725 | 20718 | 79 (0%) | 1.07% | -$1,416.85 (-56%) | Hold to the close: -$1,416.85 (-56%) |

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
| Volatility model | 13253 | 4.4% | 0.4% (53) | -644% | ❌ Worse |
| Momentum model | 13253 | 4.4% | 0.4% (53) | -667% | ❌ Worse |
| Mean-reversion model | 13253 | 7.4% | 0.4% (53) | -772% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13253 | 53 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2949 | 23 | -10% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1616 | 18 | +40% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 947 | 11 | +65% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2530 | 20 | -5% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1501 | 15 | +29% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1001 | 10 | +40% | -72% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4982 | 33 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3427 | 26 | -16% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2249 | 15 | -24% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13451 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5143 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2124 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20718 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,416.85 | -56% | — |
| Sell at 2¢ | 734 | 4% | -$2,234.01 | -89% | 42 sec |
| Sell at 3¢ | 492 | 2% | -$2,232.97 | -89% | 47 sec |
| Sell at 5¢ | 357 | 2% | -$2,192.80 | -87% | 50 sec |
| Sell at 10¢ | 218 | 1% | -$2,111.27 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,941.10 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,731.35 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 675 | 5 | 10% | 3% | -30% | -82% | -86% |
| 2–5 min | 6724 | 36 | 7% | 3% | -47% | -88% | -88% |
| 1–2 min | 5402 | 20 | 3% | 2% | -60% | -92% | -92% |
| Under 1 min | 7913 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1510 | 11 | 5% | 3% | -9% | -89% | -89% |
| HYPE | 1506 | 5 | 4% | 2% | -59% | -90% | -89% |
| ETH | 1500 | 8 | 5% | 3% | -35% | -88% | -87% |
| DOGE | 1496 | 2 | 4% | 2% | -83% | -90% | -89% |
| BNB | 1496 | 5 | 4% | 2% | -59% | -90% | -90% |
| SOL | 1493 | 2 | 3% | 2% | -83% | -92% | -91% |
| XRP | 1487 | 7 | 2% | 1% | -42% | -86% | -87% |
| BTC | 1483 | 7 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1480 | 8 | 5% | 3% | -29% | -78% | -78% |
| GOLD | 841 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 816 | 4 | 3% | 1% | -44% | -79% | -80% |
| WTI | 782 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 716 | 2 | 2% | 1% | -74% | -84% | -83% |
| PLATINUM | 699 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 646 | 2 | 1% | 0% | -71% | -84% | -84% |
| NATGAS | 643 | 5 | 2% | 2% | -27% | -81% | -80% |
| EURUSD | 636 | 3 | 3% | 1% | -56% | -81% | -80% |
| GBPUSD | 596 | 1 | 2% | 1% | -84% | -97% | -97% |
| USDJPY | 558 | 3 | 1% | 1% | -50% | -99% | -98% |
| AUDUSD | 179 | 0 | 1% | 0% | -100% | -99% | -99% |
| USDCAD | 155 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10433 | 39 | 4% | 2% | -57% | -89% | -89% |
| DOWN (bought NO) | 10285 | 40 | 4% | 2% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2227 | 11 | 2% | 1% | -17% | -79% | -79% |
| 0.05–0.1% | 2326 | 7 | 3% | 1% | -56% | -92% | -91% |
| 0.1–0.2% | 3406 | 10 | 4% | 2% | -64% | -90% | -90% |
| 0.2–0.5% | 3945 | 21 | 6% | 3% | -41% | -88% | -88% |
| Over 0.5% | 1544 | 6 | 6% | 3% | -60% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 4735 | 26 | 4% | 2% | -37% | -87% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5802 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,430 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 6:29:44 AM | AUDUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:29:11 AM | GBPUSD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:55 AM | BTC | DOWN | 65 sec | +0.084% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:39 AM | XRP | DOWN | 81 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:23 AM | PLATINUM | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:23 AM | BNB | DOWN | 1.6 min | +0.049% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:23 AM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:27:17 AM | NATGAS | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:27:17 AM | WTI | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:27:01 AM | SILVER | DOWN | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:27:01 AM | ZEC | DOWN | 3.0 min | +0.400% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:26:29 AM | NEAR | DOWN | 3.5 min | +0.572% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:25:24 AM | SOL | DOWN | 4.6 min | +0.323% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:25:24 AM | DOGE | DOWN | 4.6 min | +0.255% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:25:24 AM | ETH | DOWN | 4.6 min | +0.302% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:25:08 AM | HYPE | DOWN | 4.8 min | +0.398% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:14:55 AM | WTI | UP | 4 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:14:55 AM | SILVER | DOWN | 4 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:14:07 AM | COPPER | UP | 53 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:13:33 AM | GOLD | DOWN | 87 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:13:17 AM | NATGAS | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:13:17 AM | EURUSD | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:13:02 AM | PALLADIUM | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:12:14 AM | HYPE | UP | 2.8 min | -0.287% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:12:14 AM | ZEC | UP | 2.8 min | -0.527% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:11:41 AM | SOL | UP | 3.3 min | -0.340% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:11:41 AM | NEAR | UP | 3.3 min | -0.828% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:11:25 AM | USDCAD | DOWN | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:11:09 AM | PLATINUM | DOWN | 3.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:11:09 AM | ETH | UP | 3.8 min | -0.320% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
