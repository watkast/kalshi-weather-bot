# 15-Minute 1¢ Study

*Updated Wed Nov 25, 9:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4918 finished bets | 1% | $206.65 | +39% | +4.20¢ | $85.90 / $120.75 |

*Expect about **84 buys a day** (~$12.53/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 4663 | $105.80 | +21% |
| Volatility model ≥ 2%, hold to the close | 9166 | $43.20 | +4% |
| Momentum model ≥ 2%, hold to the close | 7625 | -$38.60 | -4% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 68076 | 68034 | 256 (0%) | 1.07% | -$4,652.05 (-56%) | Hold to the close: -$4,652.05 (-56%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 40277 | 4.5% | 0.4% (165) | -649% | ❌ Worse |
| Momentum model | 40277 | 4.4% | 0.4% (165) | -673% | ❌ Worse |
| Mean-reversion model | 40277 | 7.9% | 0.4% (165) | -789% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 40277 | 165 | -47% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 9166 | 81 | +4% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 4918 | 53 | +39% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 2844 | 32 | +66% | -65% | -63% | -60% |
| Momentum model ≥ 2% | 7625 | 59 | -4% | -79% | -79% | -76% |
| Momentum model ≥ 5% | 4663 | 43 | +21% | -75% | -75% | -71% |
| Momentum model ≥ 10% | 3037 | 28 | +33% | -68% | -68% | -64% |
| Mean-reversion model ≥ 2% | 16403 | 113 | -24% | -82% | -82% | -80% |
| Mean-reversion model ≥ 5% | 11420 | 93 | -9% | -80% | -79% | -77% |
| Mean-reversion model ≥ 10% | 7581 | 66 | -0% | -78% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 40483 | 5% | 3% | 2% | 1% | 1% | 1% |
| Commodities | 16218 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 11333 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 68034 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 256 | 0% | -$4,652.05 | -56% | — |
| Sell at 2¢ | 2786 | 4% | -$7,217.69 | -88% | 47 sec |
| Sell at 3¢ | 1870 | 3% | -$7,212.75 | -88% | 48 sec |
| Sell at 5¢ | 1263 | 2% | -$7,093.10 | -86% | 62 sec |
| Sell at 10¢ | 772 | 1% | -$6,818.73 | -83% | 65 sec |
| Sell at 25¢ | 416 | 1% | -$6,299.09 | -76% | 80 sec |
| Sell at 50¢ | 266 | 0% | -$5,698.55 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 13 | 0 | 31% | 23% | -100% | -47% | -20% |
| 5–10 min | 3516 | 17 | 11% | 4% | -54% | -81% | -83% |
| 2–5 min | 22057 | 116 | 7% | 3% | -48% | -86% | -86% |
| 1–2 min | 16965 | 58 | 3% | 2% | -62% | -92% | -92% |
| Under 1 min | 25483 | 65 | 1% | 0% | -63% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 4528 | 20 | 5% | 2% | -41% | -88% | -87% |
| HYPE | 4521 | 16 | 5% | 2% | -54% | -89% | -88% |
| SOL | 4514 | 20 | 4% | 2% | -42% | -86% | -86% |
| BNB | 4507 | 22 | 5% | 2% | -38% | -86% | -85% |
| DOGE | 4503 | 12 | 4% | 2% | -66% | -89% | -89% |
| ETH | 4498 | 19 | 7% | 3% | -47% | -82% | -82% |
| BTC | 4477 | 24 | 6% | 2% | -26% | -86% | -87% |
| NEAR | 4474 | 18 | 5% | 2% | -47% | -85% | -86% |
| XRP | 4461 | 16 | 4% | 2% | -54% | -89% | -88% |
| GOLD | 2398 | 8 | 5% | 2% | -59% | -83% | -84% |
| WTI | 2382 | 8 | 4% | 2% | -59% | -91% | -92% |
| SILVER | 2341 | 9 | 5% | 2% | -54% | -83% | -84% |
| PLATINUM | 2125 | 5 | 3% | 1% | -78% | -95% | -94% |
| EURUSD | 2077 | 7 | 3% | 1% | -69% | -91% | -90% |
| GBPUSD | 2020 | 8 | 2% | 1% | -63% | -96% | -96% |
| COPPER | 2012 | 6 | 2% | 1% | -72% | -78% | -78% |
| USDJPY | 1973 | 6 | 2% | 1% | -72% | -96% | -96% |
| NATGAS | 1970 | 10 | 2% | 1% | -53% | -77% | -77% |
| PALLADIUM | 1912 | 4 | 1% | 1% | -80% | -93% | -93% |
| AUDUSD | 1542 | 7 | 2% | 1% | -58% | -90% | -90% |
| USDCAD | 1449 | 1 | 3% | 1% | -94% | -95% | -96% |
| BRENT | 1078 | 1 | 2% | 1% | -91% | -96% | -97% |
| 10YRRATE | 557 | 2 | 3% | 1% | -66% | -78% | -76% |
| 30YRRATE | 518 | 0 | 3% | 1% | -100% | -95% | -93% |
| 2YRRATE | 515 | 4 | 4% | 2% | -28% | -57% | -57% |
| 5YRRATE | 506 | 2 | 4% | 2% | -63% | -94% | -95% |
| INX | 139 | 1 | 2% | 1% | -33% | -96% | -96% |
| USDMXN | 37 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 34745 | 132 | 4% | 2% | -56% | -88% | -88% |
| DOWN (bought NO) | 33289 | 124 | 4% | 2% | -57% | -87% | -87% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5875 | 25 | 2% | 1% | -22% | -79% | -78% |
| 0.05–0.1% | 6427 | 26 | 3% | 2% | -35% | -91% | -91% |
| 0.1–0.2% | 10034 | 36 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 12760 | 56 | 7% | 3% | -50% | -86% | -86% |
| Over 0.5% | 5378 | 24 | 7% | 3% | -53% | -86% | -87% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 16330 | 50 | 4% | 2% | -65% | -88% | -88% |
| Morning (6am–12pm) | 16129 | 82 | 4% | 2% | -42% | -86% | -85% |
| Afternoon (12–6pm) | 16751 | 73 | 4% | 2% | -48% | -87% | -87% |
| Evening (6pm–12am) | 18824 | 51 | 4% | 2% | -69% | -89% | -89% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 5,087 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/25 9:29:50 PM | COPPER | DOWN | 10 sec | — | 0¢ | In play | — |
| 11/25 9:29:11 PM | BNB | DOWN | 49 sec | -0.013% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:29:11 PM | DOGE | DOWN | 49 sec | +0.127% | 0¢ | In play | — |
| 11/25 9:29:11 PM | SOL | DOWN | 49 sec | +0.079% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:55 PM | ETH | DOWN | 65 sec | +0.061% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:28:55 PM | HYPE | DOWN | 65 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:28:40 PM | BTC | DOWN | 80 sec | +0.158% | 0¢ | In play | — |
| 11/25 9:28:40 PM | ZEC | DOWN | 80 sec | +0.332% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:28:40 PM | XRP | UP | 80 sec | -0.146% | 0¢ | In play | — |
| 11/25 9:28:21 PM | GOLD | DOWN | 1.6 min | — | 0¢ | In play | — |
| 11/25 9:28:21 PM | AUDUSD | DOWN | 1.6 min | — | 0¢ | In play | — |
| 11/25 9:28:05 PM | PLATINUM | DOWN | 1.9 min | — | 0¢ | In play | — |
| 11/25 9:28:05 PM | SILVER | DOWN | 1.9 min | — | 1¢ | In play | — |
| 11/25 9:25:32 PM | NEAR | DOWN | 4.5 min | +0.683% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:52 PM | USDJPY | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:52 PM | WTI | DOWN | 8 sec | — | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:14:52 PM | GBPUSD | DOWN | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:31 PM | AUDUSD | DOWN | 29 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:14:15 PM | ZEC | DOWN | 45 sec | +0.144% | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:13:59 PM | NEAR | UP | 61 sec | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:13:43 PM | HYPE | DOWN | 77 sec | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:13:20 PM | BRENT | DOWN | 1.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:13:20 PM | XRP | DOWN | 1.7 min | +0.240% | 0¢ | ❌ Lost | $0.00 |
| 11/25 9:13:20 PM | SOL | DOWN | 1.7 min | +0.129% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:12:48 PM | PALLADIUM | DOWN | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:12:48 PM | BNB | DOWN | 2.2 min | +0.041% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:12:33 PM | SILVER | DOWN | 2.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:11:58 PM | ETH | DOWN | 3.0 min | +0.212% | 1¢ | ❌ Lost | -$0.15 |
| 11/25 9:11:42 PM | PLATINUM | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/25 9:11:42 PM | BTC | DOWN | 3.3 min | +0.262% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
