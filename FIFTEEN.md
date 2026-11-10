# 15-Minute 1¢ Study

*Updated Tue Nov 10, 12:43 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4147 finished bets | 1% | $183.20 | +40% | +4.42¢ | $89.50 / $93.70 |

*Expect about **96 buys a day** (~$14.46/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3853 | $101.15 | +24% |
| Volatility model ≥ 2%, hold to the close | 7581 | $67.70 | +7% |
| Momentum model ≥ 2%, hold to the close | 6273 | -$6.15 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 51809 | 51782 | 199 (0%) | 1.07% | -$3,521.50 (-56%) | Hold to the close: -$3,521.50 (-56%) |

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
| Volatility model | 31447 | 4.8% | 0.4% (128) | -678% | ❌ Worse |
| Momentum model | 31447 | 4.6% | 0.4% (128) | -703% | ❌ Worse |
| Mean-reversion model | 31447 | 8.2% | 0.4% (128) | -820% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31447 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7581 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4147 | 46 | +40% | -71% | -70% | -66% |
| Volatility model ≥ 10% | 2390 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6273 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3853 | 37 | +24% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 2529 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13020 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9132 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6104 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31652 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12277 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7853 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 51782 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,521.50 | -56% | — |
| Sell at 2¢ | 2066 | 4% | -$5,490.34 | -87% | 47 sec |
| Sell at 3¢ | 1407 | 3% | -$5,478.77 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,361.20 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,136.05 | -81% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,764.16 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,321.75 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2574 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16736 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13086 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19374 | 50 | 1% | 0% | -63% | -84% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3545 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3540 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3532 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3525 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3521 | 8 | 4% | 2% | -71% | -90% | -89% |
| ETH | 3516 | 15 | 7% | 3% | -47% | -81% | -81% |
| NEAR | 3495 | 16 | 5% | 2% | -41% | -85% | -85% |
| BTC | 3495 | 17 | 5% | 2% | -33% | -87% | -88% |
| XRP | 3483 | 13 | 3% | 1% | -53% | -89% | -88% |
| GOLD | 1861 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1835 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1813 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1643 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1578 | 5 | 2% | 1% | -70% | -90% | -89% |
| COPPER | 1540 | 6 | 2% | 1% | -64% | -73% | -72% |
| NATGAS | 1503 | 8 | 2% | 1% | -50% | -78% | -77% |
| GBPUSD | 1498 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1480 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1476 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1038 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 1007 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 602 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 331 | 2 | 5% | 2% | -44% | -64% | -62% |
| 2YRRATE | 314 | 4 | 4% | 2% | +19% | -33% | -31% |
| 30YRRATE | 309 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 291 | 2 | 4% | 2% | -36% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26242 | 104 | 4% | 2% | -54% | -88% | -87% |
| DOWN (bought NO) | 25540 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5096 | 25 | 2% | 1% | -13% | -77% | -76% |
| 0.05–0.1% | 5410 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8138 | 30 | 5% | 2% | -53% | -89% | -89% |
| 0.2–0.5% | 9459 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3541 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12705 | 43 | 4% | 2% | -61% | -87% | -88% |
| Morning (6am–12pm) | 12425 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,908 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 12:43:40 AM | BTC | DOWN | 80 sec | +0.103% | — | In play | — |
| 11/10 12:43:40 AM | ZEC | DOWN | 80 sec | +0.512% | — | In play | — |
| 11/10 12:43:24 AM | HYPE | DOWN | 1.6 min | +0.171% | — | In play | — |
| 11/10 12:43:24 AM | PLATINUM | UP | 1.6 min | — | — | In play | — |
| 11/10 12:43:24 AM | BNB | DOWN | 1.6 min | +0.059% | — | In play | — |
| 11/10 12:42:20 AM | USDJPY | UP | 2.6 min | — | — | In play | — |
| 11/10 12:42:20 AM | EURUSD | DOWN | 2.6 min | — | — | In play | — |
| 11/10 12:40:30 AM | WTI | UP | 4.5 min | — | — | In play | — |
| 11/10 12:40:14 AM | BRENT | UP | 4.8 min | — | — | In play | — |
| 11/10 12:40:14 AM | SILVER | UP | 4.8 min | — | — | In play | — |
| 11/10 12:29:54 AM | PALLADIUM | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:29:54 AM | BRENT | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:29:38 AM | PLATINUM | UP | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:27:31 AM | ZEC | DOWN | 2.5 min | +0.317% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:27:15 AM | DOGE | DOWN | 2.8 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:27:15 AM | AUDUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:59 AM | USDCAD | UP | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:59 AM | GBPUSD | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:43 AM | HYPE | DOWN | 3.3 min | +0.276% | 2¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:43 AM | NEAR | DOWN | 3.3 min | +0.386% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:43 AM | EURUSD | DOWN | 3.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:43 AM | BTC | DOWN | 3.3 min | +0.152% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:26:43 AM | SOL | DOWN | 3.3 min | +0.193% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:25:07 AM | ETH | DOWN | 4.9 min | +0.264% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:25:07 AM | BNB | DOWN | 4.9 min | +0.174% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 12:14:46 AM | HYPE | UP | 13 sec | -0.084% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:14:46 AM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:14:46 AM | EURUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 12:14:46 AM | ETH | UP | 13 sec | -0.023% | 0¢ | ❌ Lost | $0.00 |
| 11/10 12:14:30 AM | DOGE | DOWN | 29 sec | -0.031% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
