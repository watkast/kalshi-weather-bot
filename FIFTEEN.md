# 15-Minute 1¢ Study

*Updated Fri Oct 2, 9:19 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Momentum model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 350 finished bets | 1% | $4.50 | +12% | +1.29¢ | -$5.65 / $10.15 |

*Expect about **80 buys a day** (~$12.04/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 171 | $2.80 | +11% |
| Momentum model ≥ 5%, sell at 50¢ | 350 | -$2.75 | -7% |
| Volatility model ≥ 5%, sell at 25¢ | 345 | -$6.95 | -19% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 5712 | 5706 | 21 (0%) | 1.07% | -$400.80 (-58%) | Hold to the close: -$400.80 (-58%) |

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
| Volatility model | 3290 | 3.6% | 0.3% (9) | -623% | ❌ Worse |
| Momentum model | 3290 | 3.7% | 0.3% (9) | -670% | ❌ Worse |
| Mean-reversion model | 3290 | 6.8% | 0.3% (9) | -796% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3290 | 9 | -65% | -86% | -87% | -84% |
| Volatility model ≥ 2% | 694 | 4 | -34% | -66% | -67% | -64% |
| Volatility model ≥ 5% | 345 | 2 | -25% | -40% | -41% | -37% |
| Volatility model ≥ 10% | 194 | 2 | +54% | +1% | -1% | +6% |
| Momentum model ≥ 2% | 611 | 3 | -41% | -63% | -67% | -64% |
| Momentum model ≥ 5% | 350 | 3 | +12% | -46% | -50% | -45% |
| Momentum model ≥ 10% | 232 | 2 | +25% | -23% | -25% | -20% |
| Mean-reversion model ≥ 2% | 1265 | 6 | -49% | -85% | -87% | -83% |
| Mean-reversion model ≥ 5% | 837 | 6 | -22% | -80% | -83% | -77% |
| Mean-reversion model ≥ 10% | 536 | 4 | -16% | -76% | -81% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3486 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1691 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 529 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 5706 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 21 | 0% | -$400.80 | -58% | — |
| Sell at 2¢ | 216 | 4% | -$624.64 | -90% | 43 sec |
| Sell at 3¢ | 130 | 2% | -$630.10 | -91% | 48 sec |
| Sell at 5¢ | 96 | 2% | -$618.40 | -89% | 66 sec |
| Sell at 10¢ | 67 | 1% | -$579.03 | -83% | 81 sec |
| Sell at 25¢ | 35 | 1% | -$536.95 | -77% | 1.6 min |
| Sell at 50¢ | 19 | 0% | -$482.55 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1879 | 10 | 7% | 3% | -48% | -87% | -89% |
| 1–2 min | 1483 | 6 | 3% | 2% | -56% | -94% | -93% |
| Under 1 min | 2173 | 3 | 1% | 0% | -80% | -91% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 395 | 2 | 4% | 1% | -35% | -90% | -92% |
| ETH | 389 | 2 | 5% | 3% | -36% | -88% | -87% |
| ZEC | 389 | 1 | 5% | 3% | -69% | -88% | -91% |
| BNB | 389 | 0 | 4% | 1% | -100% | -92% | -95% |
| BTC | 388 | 0 | 6% | 2% | -100% | -85% | -90% |
| HYPE | 386 | 2 | 5% | 3% | -36% | -89% | -87% |
| XRP | 385 | 3 | 1% | 1% | +1% | -63% | -62% |
| NEAR | 383 | 1 | 6% | 2% | -65% | -85% | -88% |
| SOL | 382 | 0 | 3% | 1% | -100% | -93% | -92% |
| GOLD | 292 | 0 | 5% | 1% | -100% | -89% | -92% |
| SILVER | 272 | 0 | 1% | 1% | -100% | -97% | -96% |
| WTI | 255 | 2 | 3% | 1% | -17% | -94% | -95% |
| COPPER | 244 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 213 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 211 | 2 | 4% | 2% | -12% | -93% | -91% |
| PALLADIUM | 204 | 1 | 2% | 1% | -54% | -96% | -97% |
| GBPUSD | 186 | 1 | 4% | 2% | -50% | -93% | -93% |
| EURUSD | 185 | 1 | 4% | 3% | -50% | -93% | -92% |
| USDJPY | 158 | 3 | 3% | 2% | +77% | -96% | -93% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 2913 | 13 | 4% | 2% | -48% | -92% | -92% |
| DOWN (bought NO) | 2793 | 8 | 4% | 1% | -67% | -88% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 414 | 2 | 1% | 1% | -9% | -50% | -49% |
| 0.05–0.1% | 479 | 0 | 3% | 0% | -100% | -92% | -95% |
| 0.1–0.2% | 847 | 1 | 3% | 1% | -84% | -92% | -93% |
| 0.2–0.5% | 1190 | 4 | 6% | 3% | -63% | -88% | -89% |
| Over 0.5% | 555 | 4 | 7% | 3% | -26% | -86% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1485 | 8 | 5% | 3% | -39% | -90% | -89% |
| Afternoon (12–6pm) | 1097 | 2 | 3% | 1% | -79% | -83% | -86% |
| Evening (6pm–12am) | 1650 | 6 | 3% | 2% | -58% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,106 |
| Time from buy to best bounce (bounced bets) | 50 sec |
| Price snapshots per bet | 43 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 9:14:51 AM | XRP | UP | 9 sec | -0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:14:35 AM | ZEC | DOWN | 25 sec | +0.066% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:13:45 AM | USDJPY | DOWN | 75 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:13:29 AM | DOGE | UP | 1.5 min | -0.382% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:13:13 AM | ETH | UP | 1.8 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:12:58 AM | PALLADIUM | UP | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:12:58 AM | BTC | UP | 2.0 min | -0.227% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:12:26 AM | COPPER | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:12:10 AM | SOL | UP | 2.8 min | -0.399% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:11:54 AM | HYPE | UP | 3.1 min | -0.446% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:11:54 AM | GOLD | UP | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:11:36 AM | EURUSD | UP | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:11:36 AM | WTI | DOWN | 3.4 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/2 9:11:20 AM | SILVER | UP | 3.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 9:11:20 AM | PLATINUM | UP | 3.7 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:10:17 AM | NEAR | UP | 4.7 min | -1.404% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 9:09:11 AM | GBPUSD | UP | 5.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:59:54 AM | GBPUSD | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:59:22 AM | NATGAS | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 AM | NEAR | UP | 1.8 min | -0.693% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 AM | WTI | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:58:15 AM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | PALLADIUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | BTC | UP | 2.5 min | -0.287% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | PLATINUM | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:28 AM | DOGE | UP | 2.5 min | -0.659% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 8:57:12 AM | EURUSD | UP | 2.8 min | — | 5¢ | ❌ Lost | -$0.15 |
| 10/2 8:56:08 AM | XRP | UP | 3.9 min | -1.035% | 0¢ | ❌ Lost | $0.00 |
| 10/2 8:55:36 AM | HYPE | UP | 4.4 min | -0.640% | 22¢ | ❌ Lost | -$0.15 |
| 10/2 8:55:36 AM | BNB | UP | 4.4 min | -0.470% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
