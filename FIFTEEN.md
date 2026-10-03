# 15-Minute 1¢ Study

*Updated Fri Oct 2, 7:56 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **34 buys a day** (~$5.16/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 389 | $0.90 | +2% |
| Momentum model ≥ 5%, sell at 50¢ | 389 | -$6.35 | -15% |
| Volatility model ≥ 5%, sell at 25¢ | 388 | -$10.70 | -26% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6134 | 6127 | 23 (0%) | 1.07% | -$419.45 (-57%) | Hold to the close: -$419.45 (-57%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3596 | 3.8% | 0.3% (11) | -675% | ❌ Worse |
| Momentum model | 3596 | 4.0% | 0.3% (11) | -717% | ❌ Worse |
| Mean-reversion model | 3596 | 6.9% | 0.3% (11) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3596 | 11 | -61% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 765 | 5 | -24% | -65% | -65% | -60% |
| Volatility model ≥ 5% | 388 | 2 | -32% | -44% | -44% | -39% |
| Volatility model ≥ 10% | 227 | 2 | +35% | -10% | -12% | -4% |
| Momentum model ≥ 2% | 671 | 4 | -28% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 389 | 3 | +2% | -49% | -53% | -47% |
| Momentum model ≥ 10% | 262 | 2 | +12% | -31% | -32% | -26% |
| Mean-reversion model ≥ 2% | 1366 | 7 | -44% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 913 | 6 | -28% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 591 | 4 | -22% | -77% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3793 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1779 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6127 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$419.45 | -57% | — |
| Sell at 2¢ | 243 | 4% | -$664.27 | -90% | 43 sec |
| Sell at 3¢ | 152 | 2% | -$668.17 | -90% | 48 sec |
| Sell at 5¢ | 113 | 2% | -$654.00 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$616.51 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$570.36 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$515.70 | -70% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1997 | 12 | 8% | 4% | -41% | -86% | -87% |
| 1–2 min | 1595 | 6 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 2364 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 428 | 2 | 4% | 1% | -37% | -90% | -90% |
| ZEC | 425 | 2 | 5% | 3% | -44% | -88% | -90% |
| ETH | 423 | 2 | 6% | 3% | -41% | -86% | -85% |
| HYPE | 423 | 2 | 5% | 4% | -42% | -88% | -85% |
| BNB | 422 | 0 | 4% | 1% | -100% | -91% | -93% |
| BTC | 421 | 1 | 7% | 3% | -69% | -84% | -88% |
| XRP | 419 | 3 | 2% | 1% | -6% | -65% | -65% |
| SOL | 417 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 415 | 1 | 6% | 2% | -67% | -85% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 271 | 2 | 3% | 1% | -23% | -94% | -96% |
| COPPER | 254 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 226 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 223 | 2 | 4% | 2% | -16% | -94% | -92% |
| PALLADIUM | 216 | 1 | 2% | 1% | -57% | -96% | -98% |
| GBPUSD | 195 | 1 | 4% | 2% | -52% | -93% | -93% |
| EURUSD | 195 | 1 | 5% | 3% | -52% | -91% | -89% |
| USDJPY | 165 | 3 | 2% | 2% | +70% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 3115 | 14 | 4% | 2% | -48% | -91% | -91% |
| DOWN (bought NO) | 3012 | 9 | 4% | 2% | -66% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 473 | 2 | 1% | 1% | -20% | -56% | -55% |
| 0.05–0.1% | 539 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 926 | 2 | 4% | 2% | -71% | -90% | -91% |
| 0.2–0.5% | 1267 | 5 | 6% | 3% | -56% | -87% | -87% |
| Over 0.5% | 586 | 4 | 7% | 3% | -29% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1708 | 6 | 3% | 2% | -59% | -93% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,151 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 7:56:04 PM | BNB | UP | 3.9 min | -0.143% | — | In play | — |
| 10/2 7:44:47 PM | BTC | DOWN | 13 sec | +0.016% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:44:47 PM | DOGE | UP | 13 sec | -0.034% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:44:47 PM | NEAR | DOWN | 13 sec | +0.009% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:44:31 PM | XRP | DOWN | 29 sec | +0.034% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:44:31 PM | ZEC | DOWN | 29 sec | +0.092% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:44:15 PM | HYPE | UP | 45 sec | -0.143% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:44:15 PM | SOL | DOWN | 45 sec | +0.092% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:43:11 PM | ETH | DOWN | 1.8 min | +0.074% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:40:16 PM | BNB | DOWN | 4.7 min | +0.130% | 1¢ | ❌ Lost | $0.00 |
| 10/2 7:29:18 PM | ETH | UP | 41 sec | -0.044% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:29:18 PM | ZEC | UP | 41 sec | -0.135% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:04 PM | BTC | UP | 56 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:29:04 PM | BNB | UP | 56 sec | -0.082% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:29:04 PM | NEAR | UP | 56 sec | -0.331% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:28:30 PM | XRP | DOWN | 1.5 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:27:43 PM | HYPE | DOWN | 2.3 min | +0.376% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:55 PM | BTC | UP | 4 sec | -0.012% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:39 PM | NEAR | DOWN | 20 sec | +0.015% | 0¢ | ❌ Lost | $0.00 |
| 10/2 7:14:39 PM | ZEC | DOWN | 20 sec | +0.100% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:14:07 PM | BNB | UP | 53 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:48 PM | DOGE | DOWN | 71 sec | +0.067% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:13:16 PM | SOL | DOWN | 1.7 min | +0.188% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:46 PM | ETH | DOWN | 2.2 min | +0.089% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:46 PM | HYPE | UP | 2.2 min | -0.365% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 7:12:46 PM | XRP | DOWN | 2.2 min | +0.148% | 2¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:58 PM | HYPE | UP | 1 sec | -0.002% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:59:41 PM | WTI | DOWN | 19 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:59:09 PM | DOGE | UP | 51 sec | -0.074% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:58:54 PM | BTC | DOWN | 66 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
