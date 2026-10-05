# 15-Minute 1¢ Study

*Updated Mon Oct 5, 12:03 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 573 finished bets | 1% | $22.20 | +36% | +3.87¢ | -$17.50 / $39.70 |

*Expect about **82 buys a day** (~$12.33/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| 5+ min left, hold to the close | 195 | $13.20 | +46% |
| Volatility model ≥ 2%, hold to the close | 1055 | $12.80 | +10% |
| Momentum model ≥ 5%, hold to the close | 578 | $8.35 | +14% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 8091 | 8085 | 36 (0%) | 1.07% | -$465.75 (-48%) | Hold to the close: -$465.75 (-48%) |

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
| Volatility model | 5369 | 4.2% | 0.4% (24) | -611% | ❌ Worse |
| Momentum model | 5369 | 4.3% | 0.4% (24) | -641% | ❌ Worse |
| Mean-reversion model | 5369 | 6.9% | 0.4% (24) | -709% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 5369 | 24 | -43% | -84% | -85% | -82% |
| Volatility model ≥ 2% | 1055 | 10 | +10% | -69% | -69% | -64% |
| Volatility model ≥ 5% | 573 | 6 | +36% | -55% | -55% | -50% |
| Volatility model ≥ 10% | 357 | 4 | +64% | -37% | -38% | -32% |
| Momentum model ≥ 2% | 931 | 7 | -9% | -69% | -72% | -69% |
| Momentum model ≥ 5% | 578 | 5 | +14% | -61% | -64% | -60% |
| Momentum model ≥ 10% | 401 | 4 | +42% | -48% | -49% | -46% |
| Mean-reversion model ≥ 2% | 1866 | 13 | -24% | -82% | -84% | -79% |
| Mean-reversion model ≥ 5% | 1250 | 11 | -2% | -79% | -79% | -72% |
| Mean-reversion model ≥ 10% | 827 | 8 | +12% | -77% | -78% | -71% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 5566 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1910 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 609 | 4% | 3% | 2% | 2% | 1% | 0% |
| **All** | 8085 | 4% | 3% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 36 | 0% | -$465.75 | -48% | — |
| Sell at 2¢ | 321 | 4% | -$858.29 | -89% | 33 sec |
| Sell at 3¢ | 207 | 3% | -$861.02 | -89% | 47 sec |
| Sell at 5¢ | 153 | 2% | -$842.30 | -87% | 61 sec |
| Sell at 10¢ | 104 | 1% | -$791.51 | -82% | 72 sec |
| Sell at 25¢ | 57 | 1% | -$711.08 | -73% | 1.6 min |
| Sell at 50¢ | 35 | 0% | -$621.50 | -64% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 192 | 3 | 12% | 3% | +48% | -79% | -88% |
| 2–5 min | 2600 | 19 | 8% | 4% | -29% | -86% | -86% |
| 1–2 min | 2142 | 9 | 3% | 2% | -54% | -93% | -93% |
| Under 1 min | 3148 | 5 | 1% | 0% | -76% | -88% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 629 | 5 | 5% | 3% | -6% | -89% | -89% |
| ETH | 622 | 5 | 6% | 3% | +2% | -86% | -86% |
| DOGE | 622 | 2 | 4% | 1% | -58% | -91% | -91% |
| HYPE | 619 | 3 | 5% | 3% | -41% | -88% | -86% |
| BNB | 618 | 2 | 4% | 2% | -61% | -90% | -92% |
| SOL | 617 | 0 | 3% | 1% | -100% | -92% | -91% |
| XRP | 615 | 4 | 2% | 1% | -17% | -75% | -76% |
| BTC | 614 | 3 | 6% | 2% | -36% | -86% | -89% |
| NEAR | 610 | 2 | 6% | 3% | -57% | -63% | -64% |
| GOLD | 325 | 0 | 4% | 1% | -100% | -90% | -93% |
| SILVER | 310 | 0 | 2% | 1% | -100% | -96% | -96% |
| WTI | 296 | 2 | 3% | 1% | -28% | -95% | -96% |
| COPPER | 272 | 0 | 1% | 0% | -100% | -99% | -99% |
| PLATINUM | 239 | 0 | 0% | 0% | -100% | -100% | -100% |
| NATGAS | 238 | 2 | 3% | 2% | -22% | -94% | -92% |
| PALLADIUM | 230 | 1 | 2% | 1% | -59% | -96% | -98% |
| EURUSD | 220 | 1 | 5% | 3% | -58% | -92% | -91% |
| GBPUSD | 207 | 1 | 4% | 2% | -55% | -93% | -94% |
| USDJPY | 182 | 3 | 2% | 2% | +54% | -96% | -94% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 4085 | 20 | 4% | 2% | -42% | -88% | -88% |
| DOWN (bought NO) | 4000 | 16 | 4% | 2% | -54% | -89% | -90% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 938 | 7 | 2% | 1% | +26% | -58% | -57% |
| 0.05–0.1% | 941 | 2 | 4% | 1% | -69% | -90% | -92% |
| 0.1–0.2% | 1378 | 5 | 4% | 2% | -54% | -90% | -91% |
| 0.2–0.5% | 1631 | 8 | 6% | 3% | -46% | -87% | -87% |
| Over 0.5% | 676 | 4 | 7% | 3% | -39% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1882 | 8 | 5% | 2% | -50% | -84% | -86% |
| Morning (6am–12pm) | 2058 | 17 | 5% | 3% | -5% | -89% | -87% |
| Afternoon (12–6pm) | 1751 | 4 | 3% | 1% | -73% | -86% | -87% |
| Evening (6pm–12am) | 2394 | 7 | 3% | 2% | -66% | -94% | -94% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,194 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 41 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/4 11:59:54 PM | NEAR | DOWN | 6 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:59:54 PM | XRP | DOWN | 6 sec | +0.027% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:59:38 PM | ETH | DOWN | 22 sec | +0.031% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:59:38 PM | EURUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:59:22 PM | SOL | UP | 38 sec | -0.053% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:49 PM | PLATINUM | UP | 70 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:33 PM | BNB | DOWN | 86 sec | +0.006% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:58:33 PM | WTI | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:57:43 PM | HYPE | DOWN | 2.3 min | +0.260% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:57:11 PM | ZEC | UP | 2.8 min | -0.339% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:57:11 PM | USDJPY | UP | 2.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:56:56 PM | SILVER | UP | 3.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:56:08 PM | GOLD | UP | 3.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:49 PM | GOLD | DOWN | 11 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:33 PM | ZEC | DOWN | 27 sec | +0.080% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:44:17 PM | EURUSD | DOWN | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:44:02 PM | DOGE | DOWN | 57 sec | +0.122% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:40 PM | SOL | DOWN | 2.3 min | +0.176% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:08 PM | HYPE | DOWN | 2.9 min | +0.205% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:08 PM | ETH | DOWN | 2.9 min | +0.220% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:08 PM | BTC | DOWN | 2.9 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:42:08 PM | XRP | DOWN | 2.9 min | +0.286% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:41:52 PM | BNB | DOWN | 3.1 min | +0.142% | 1¢ | ❌ Lost | -$0.15 |
| 10/4 11:41:36 PM | NEAR | DOWN | 3.4 min | +1.285% | 7¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:51 PM | GOLD | UP | 9 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:29:51 PM | BTC | DOWN | 9 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/4 11:29:35 PM | USDJPY | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:35 PM | SILVER | UP | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:03 PM | XRP | UP | 57 sec | -0.113% | 0¢ | ❌ Lost | -$0.15 |
| 10/4 11:29:03 PM | BNB | DOWN | 57 sec | +0.025% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
