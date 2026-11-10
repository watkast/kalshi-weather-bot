# 15-Minute 1¢ Study

*Updated Tue Nov 10, 6:28 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 4157 finished bets | 1% | $182.30 | +39% | +4.39¢ | $89.05 / $93.25 |

*Expect about **96 buys a day** (~$14.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 3871 | $99.35 | +24% |
| Volatility model ≥ 2%, hold to the close | 7602 | $65.45 | +7% |
| Momentum model ≥ 2%, hold to the close | 6295 | -$8.55 | -1% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 52033 | 52006 | 199 (0%) | 1.07% | -$3,549.55 (-56%) | Hold to the close: -$3,549.55 (-56%) |

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
| Volatility model | 31542 | 4.8% | 0.4% (128) | -679% | ❌ Worse |
| Momentum model | 31542 | 4.6% | 0.4% (128) | -704% | ❌ Worse |
| Mean-reversion model | 31542 | 8.1% | 0.4% (128) | -821% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 31542 | 128 | -48% | -87% | -87% | -84% |
| Volatility model ≥ 2% | 7602 | 70 | +7% | -77% | -76% | -71% |
| Volatility model ≥ 5% | 4157 | 46 | +39% | -72% | -70% | -66% |
| Volatility model ≥ 10% | 2396 | 28 | +68% | -62% | -60% | -56% |
| Momentum model ≥ 2% | 6295 | 51 | -1% | -78% | -77% | -74% |
| Momentum model ≥ 5% | 3871 | 37 | +24% | -74% | -73% | -69% |
| Momentum model ≥ 10% | 2538 | 25 | +39% | -65% | -64% | -60% |
| Mean-reversion model ≥ 2% | 13060 | 91 | -23% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 9155 | 78 | -5% | -79% | -79% | -76% |
| Mean-reversion model ≥ 10% | 6123 | 56 | +4% | -77% | -76% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 31747 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 12343 | 3% | 2% | 1% | 1% | 0% | 0% |
| Financials | 7916 | 2% | 2% | 1% | 1% | 0% | 0% |
| **All** | 52006 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 199 | 0% | -$3,549.55 | -56% | — |
| Sell at 2¢ | 2070 | 4% | -$5,517.35 | -87% | 47 sec |
| Sell at 3¢ | 1408 | 3% | -$5,506.43 | -87% | 48 sec |
| Sell at 5¢ | 982 | 2% | -$5,389.25 | -85% | 63 sec |
| Sell at 10¢ | 595 | 1% | -$5,164.10 | -82% | 65 sec |
| Sell at 25¢ | 314 | 1% | -$4,792.21 | -76% | 83 sec |
| Sell at 50¢ | 205 | 0% | -$4,349.80 | -69% | 1.7 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 12 | 0 | 25% | 17% | -100% | -57% | -35% |
| 5–10 min | 2594 | 12 | 11% | 4% | -56% | -81% | -82% |
| 2–5 min | 16797 | 93 | 7% | 3% | -45% | -87% | -86% |
| 1–2 min | 13136 | 44 | 3% | 2% | -63% | -92% | -92% |
| Under 1 min | 19467 | 50 | 1% | 0% | -63% | -85% | -84% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 3555 | 15 | 5% | 2% | -45% | -88% | -88% |
| SOL | 3551 | 16 | 4% | 2% | -42% | -87% | -87% |
| HYPE | 3543 | 11 | 5% | 2% | -61% | -89% | -88% |
| BNB | 3536 | 19 | 5% | 2% | -32% | -86% | -85% |
| DOGE | 3531 | 8 | 4% | 2% | -72% | -90% | -89% |
| ETH | 3526 | 15 | 7% | 3% | -47% | -81% | -81% |
| BTC | 3506 | 17 | 5% | 2% | -34% | -87% | -88% |
| NEAR | 3505 | 16 | 5% | 2% | -41% | -85% | -85% |
| XRP | 3494 | 13 | 3% | 1% | -54% | -89% | -88% |
| GOLD | 1870 | 5 | 6% | 2% | -67% | -81% | -83% |
| WTI | 1844 | 6 | 4% | 2% | -61% | -91% | -92% |
| SILVER | 1822 | 8 | 5% | 2% | -48% | -83% | -82% |
| PLATINUM | 1653 | 4 | 2% | 1% | -77% | -96% | -95% |
| EURUSD | 1586 | 5 | 2% | 1% | -71% | -90% | -89% |
| COPPER | 1549 | 6 | 2% | 1% | -64% | -73% | -73% |
| NATGAS | 1509 | 8 | 2% | 1% | -51% | -78% | -77% |
| GBPUSD | 1505 | 5 | 2% | 1% | -69% | -96% | -96% |
| PALLADIUM | 1487 | 3 | 1% | 0% | -81% | -92% | -92% |
| USDJPY | 1484 | 6 | 2% | 1% | -62% | -96% | -96% |
| AUDUSD | 1047 | 5 | 2% | 1% | -55% | -87% | -88% |
| USDCAD | 1015 | 0 | 2% | 1% | -100% | -96% | -97% |
| BRENT | 609 | 0 | 2% | 1% | -100% | -97% | -97% |
| 10YRRATE | 338 | 2 | 4% | 2% | -45% | -65% | -62% |
| 2YRRATE | 320 | 4 | 4% | 2% | +17% | -34% | -33% |
| 30YRRATE | 313 | 0 | 2% | 1% | -100% | -96% | -94% |
| 5YRRATE | 297 | 2 | 4% | 2% | -37% | -92% | -95% |
| INX | 11 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 26360 | 104 | 4% | 2% | -55% | -88% | -87% |
| DOWN (bought NO) | 25646 | 95 | 4% | 2% | -57% | -86% | -86% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 5106 | 25 | 2% | 1% | -14% | -77% | -76% |
| 0.05–0.1% | 5426 | 20 | 3% | 2% | -44% | -91% | -91% |
| 0.1–0.2% | 8168 | 30 | 5% | 2% | -54% | -89% | -89% |
| 0.2–0.5% | 9485 | 40 | 6% | 3% | -53% | -87% | -86% |
| Over 0.5% | 3554 | 15 | 7% | 3% | -56% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 12908 | 43 | 4% | 2% | -62% | -88% | -88% |
| Morning (6am–12pm) | 12446 | 56 | 4% | 2% | -49% | -84% | -84% |
| Afternoon (12–6pm) | 12535 | 57 | 4% | 2% | -47% | -86% | -86% |
| Evening (6pm–12am) | 14117 | 43 | 4% | 2% | -65% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,896 |
| Time from buy to best bounce (bounced bets) | 51 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 11/10 6:27:49 AM | WTI | DOWN | 2.2 min | — | — | In play | — |
| 11/10 6:27:49 AM | ETH | UP | 2.2 min | -0.295% | — | In play | — |
| 11/10 6:27:33 AM | HYPE | UP | 2.5 min | -0.236% | — | In play | — |
| 11/10 6:27:18 AM | 30YRRATE | DOWN | 2.7 min | — | — | In play | — |
| 11/10 6:27:18 AM | BTC | UP | 2.7 min | -0.194% | — | In play | — |
| 11/10 6:27:18 AM | ZEC | UP | 2.7 min | -0.552% | — | In play | — |
| 11/10 6:26:58 AM | NEAR | UP | 3.0 min | -0.578% | — | In play | — |
| 11/10 6:26:11 AM | DOGE | UP | 3.8 min | -0.358% | — | In play | — |
| 11/10 6:25:35 AM | SOL | UP | 4.4 min | -0.451% | — | In play | — |
| 11/10 6:25:35 AM | XRP | UP | 4.4 min | -0.454% | — | In play | — |
| 11/10 6:14:49 AM | SOL | UP | 10 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 11/10 6:14:49 AM | 30YRRATE | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:49 AM | WTI | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:49 AM | EURUSD | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:32 AM | 2YRRATE | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:32 AM | 5YRRATE | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:32 AM | 10YRRATE | DOWN | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:12 AM | GOLD | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:12 AM | USDJPY | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:14:12 AM | BTC | DOWN | 48 sec | +0.061% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:56 AM | GBPUSD | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:40 AM | BNB | DOWN | 80 sec | +0.063% | 0¢ | ❌ Lost | $0.00 |
| 11/10 6:13:40 AM | NEAR | DOWN | 80 sec | +0.237% | 3¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:40 AM | COPPER | UP | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:40 AM | DOGE | DOWN | 80 sec | +0.104% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:25 AM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:25 AM | AUDUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:13:25 AM | HYPE | DOWN | 1.6 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 11/10 6:11:44 AM | XRP | DOWN | 3.2 min | +0.325% | 0¢ | ❌ Lost | -$0.15 |
| 11/10 6:10:05 AM | PALLADIUM | DOWN | 4.9 min | — | 3¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
