# 15-Minute 1¢ Study

*Updated Mon Sep 28, 1:39 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Mean-reversion model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Mean-reversion model ≥ 5%, hold to the close | 111 finished bets | 3% | $27.75 | +195% | +25.00¢ | $6.95 / $20.80 |

*Expect **112 buys in the first 13 hours** — daily pace shows after 24 hours; max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 37 | $22.45 | +405% |
| 2–5 min left, hold to the close | 347 | $20.50 | +41% |
| Mean-reversion model ≥ 2%, hold to the close | 174 | $19.80 | +89% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 1016 | 1005 | 7 (1%) | 1.07% | -$22.60 (-19%) | Hold to the close: -$22.60 (-19%) |

*In play or awaiting result: 11. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 445 | 3.2% | 0.9% (4) | -284% | ❌ Worse |
| Momentum model | 445 | 3.3% | 0.9% (4) | -365% | ❌ Worse |
| Mean-reversion model | 445 | 6.0% | 0.9% (4) | -291% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 445 | 4 | +17% | -90% | -91% | -88% |
| Volatility model ≥ 2% | 83 | 1 | +44% | -87% | -84% | -80% |
| Volatility model ≥ 5% | 41 | 0 | -100% | -78% | -75% | -72% |
| Volatility model ≥ 10% | 21 | 0 | -100% | -88% | -81% | -69% |
| Momentum model ≥ 2% | 74 | 0 | -100% | -88% | -91% | -92% |
| Momentum model ≥ 5% | 42 | 0 | -100% | -83% | -91% | -86% |
| Momentum model ≥ 10% | 29 | 0 | -100% | -91% | -86% | -77% |
| Mean-reversion model ≥ 2% | 174 | 3 | +89% | -85% | -86% | -82% |
| Mean-reversion model ≥ 5% | 111 | 3 | +195% | -82% | -81% | -73% |
| Mean-reversion model ≥ 10% | 70 | 2 | +222% | -79% | -78% | -70% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 640 | 4% | 3% | 2% | 2% | 1% | 1% |
| Commodities | 317 | 1% | 1% | 0% | 0% | 0% | 0% |
| Financials | 48 | 2% | 2% | 2% | 2% | 2% | 2% |
| **All** | 1005 | 3% | 2% | 1% | 1% | 1% | 1% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 7 | 1% | -$22.60 | -19% | — |
| Sell at 2¢ | 32 | 3% | -$112.28 | -93% | 62 sec |
| Sell at 3¢ | 20 | 2% | -$112.80 | -94% | 72 sec |
| Sell at 5¢ | 13 | 1% | -$112.15 | -93% | 1.6 min |
| Sell at 10¢ | 12 | 1% | -$104.88 | -87% | 2.0 min |
| Sell at 25¢ | 9 | 1% | -$90.81 | -75% | 2.1 min |
| Sell at 50¢ | 7 | 1% | -$73.35 | -61% | 2.4 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| 5–10 min | 37 | 2 | 8% | 5% | +405% | -86% | -79% |
| 2–5 min | 347 | 5 | 7% | 3% | +41% | -88% | -90% |
| 1–2 min | 310 | 0 | 2% | 0% | -100% | -97% | -97% |
| Under 1 min | 311 | 0 | 0% | 0% | -100% | -99% | -99% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ETH | 73 | 2 | 4% | 3% | +252% | -90% | -85% |
| DOGE | 73 | 1 | 5% | 3% | +56% | -88% | -83% |
| ZEC | 73 | 1 | 5% | 1% | +73% | -87% | -95% |
| XRP | 72 | 2 | 4% | 3% | +239% | -91% | -91% |
| NEAR | 71 | 0 | 1% | 0% | -100% | -96% | -100% |
| BTC | 71 | 0 | 10% | 3% | -100% | -74% | -83% |
| SOL | 71 | 0 | 3% | 1% | -100% | -92% | -89% |
| BNB | 70 | 0 | 1% | 0% | -100% | -97% | -95% |
| HYPE | 66 | 0 | 3% | 2% | -100% | -93% | -95% |
| GOLD | 57 | 0 | 2% | 0% | -100% | -96% | -100% |
| WTI | 53 | 0 | 2% | 0% | -100% | -96% | -100% |
| SILVER | 50 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 44 | 0 | 5% | 2% | -100% | -92% | -88% |
| COPPER | 40 | 0 | 0% | 0% | -100% | -100% | -100% |
| PLATINUM | 39 | 0 | 0% | 0% | -100% | -100% | -100% |
| PALLADIUM | 34 | 0 | 0% | 0% | -100% | -100% | -100% |
| GBPUSD | 20 | 0 | 0% | 0% | -100% | -100% | -100% |
| EURUSD | 16 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDJPY | 12 | 1 | 8% | 8% | +678% | -86% | -78% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 534 | 5 | 3% | 1% | +12% | -93% | -92% |
| DOWN (bought NO) | 471 | 2 | 3% | 1% | -52% | -93% | -95% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 50 | 0 | 2% | 2% | -100% | -91% | -87% |
| 0.05–0.1% | 62 | 0 | 2% | 0% | -100% | -95% | -100% |
| 0.1–0.2% | 143 | 0 | 3% | 0% | -100% | -90% | -91% |
| 0.2–0.5% | 265 | 2 | 4% | 2% | -18% | -92% | -93% |
| Over 0.5% | 120 | 4 | 8% | 4% | +273% | -84% | -82% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 308 | 1 | 4% | 2% | -62% | -91% | -93% |
| Morning (6am–12pm) | 338 | 4 | 3% | 1% | +36% | -94% | -94% |
| Afternoon (12–6pm) | 83 | 0 | 1% | 0% | -100% | -97% | -100% |
| Evening (6pm–12am) | 276 | 2 | 3% | 1% | -16% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 23 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,832 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 48 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 9/28 1:39:46 PM | DOGE | UP | 5.2 min | -0.790% | — | In play | — |
| 9/28 1:39:46 PM | BTC | UP | 5.2 min | -0.537% | — | In play | — |
| 9/28 1:39:30 PM | ETH | UP | 5.5 min | -0.508% | — | In play | — |
| 9/28 1:38:59 PM | NEAR | UP | 6.0 min | -2.564% | — | In play | — |
| 9/28 1:38:59 PM | BNB | UP | 6.0 min | -0.487% | — | In play | — |
| 9/28 1:29:49 PM | NEAR | DOWN | 10 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:29:34 PM | USDJPY | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:29:18 PM | XRP | UP | 41 sec | -0.287% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:29:02 PM | HYPE | UP | 57 sec | -0.197% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:29:02 PM | BTC | UP | 57 sec | -0.077% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:46 PM | SILVER | DOWN | 73 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:31 PM | WTI | DOWN | 88 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | NATGAS | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | DOGE | UP | 1.7 min | -0.244% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | ETH | UP | 1.7 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:28:15 PM | SOL | UP | 1.7 min | -0.203% | 0¢ | ❌ Lost | $0.00 |
| 9/28 1:27:59 PM | BNB | UP | 2.0 min | -0.122% | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:28 PM | ZEC | UP | 2.5 min | -0.815% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:12 PM | GBPUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:27:12 PM | EURUSD | DOWN | 2.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:14:06 PM | PALLADIUM | UP | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:50 PM | NATGAS | DOWN | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:50 PM | COPPER | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:13:19 PM | WTI | DOWN | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:12:32 PM | GOLD | UP | 2.5 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:12:16 PM | PLATINUM | UP | 2.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 9/28 1:10:08 PM | NEAR | UP | 4.9 min | -2.297% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:10:08 PM | SILVER | UP | 4.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:10:08 PM | XRP | UP | 4.9 min | -1.131% | 1¢ | ❌ Lost | -$0.15 |
| 9/28 1:09:37 PM | HYPE | UP | 5.4 min | -0.681% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
