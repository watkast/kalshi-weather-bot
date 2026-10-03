# 15-Minute 1¢ Study

*Updated Fri Oct 2, 6:30 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟡 **Unproven.** Profitable overall, but not in both the earlier and later halves of the data.

1. **Watch** every 15-minute up/down market (5+ min left).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| 5+ min left, hold to the close | 171 finished bets | 1% | $2.80 | +11% | +1.64¢ | $15.40 / -$12.60 |

*Expect about **35 buys a day** (~$5.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 388 | $1.05 | +3% |
| Momentum model ≥ 5%, sell at 50¢ | 388 | -$6.20 | -15% |
| Volatility model ≥ 5%, sell at 25¢ | 384 | -$10.40 | -25% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 6091 | 6082 | 23 (0%) | 1.07% | -$414.80 (-56%) | Hold to the close: -$414.80 (-56%) |

*In play or awaiting result: 9. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 3552 | 3.9% | 0.3% (11) | -679% | ❌ Worse |
| Momentum model | 3552 | 4.0% | 0.3% (11) | -721% | ❌ Worse |
| Mean-reversion model | 3552 | 6.9% | 0.3% (11) | -830% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 3552 | 11 | -60% | -85% | -86% | -83% |
| Volatility model ≥ 2% | 758 | 5 | -24% | -65% | -65% | -60% |
| Volatility model ≥ 5% | 384 | 2 | -32% | -44% | -44% | -39% |
| Volatility model ≥ 10% | 223 | 2 | +37% | -8% | -10% | -3% |
| Momentum model ≥ 2% | 669 | 4 | -27% | -64% | -67% | -63% |
| Momentum model ≥ 5% | 388 | 3 | +3% | -49% | -52% | -47% |
| Momentum model ≥ 10% | 261 | 2 | +12% | -30% | -31% | -26% |
| Mean-reversion model ≥ 2% | 1356 | 7 | -44% | -84% | -85% | -80% |
| Mean-reversion model ≥ 5% | 907 | 6 | -27% | -80% | -81% | -74% |
| Mean-reversion model ≥ 10% | 585 | 4 | -22% | -77% | -80% | -74% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 3749 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 1778 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 555 | 4% | 3% | 2% | 2% | 1% | 1% |
| **All** | 6082 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 23 | 0% | -$414.80 | -56% | — |
| Sell at 2¢ | 242 | 4% | -$659.88 | -90% | 43 sec |
| Sell at 3¢ | 152 | 2% | -$663.52 | -90% | 48 sec |
| Sell at 5¢ | 113 | 2% | -$649.35 | -88% | 64 sec |
| Sell at 10¢ | 74 | 1% | -$611.86 | -83% | 81 sec |
| Sell at 25¢ | 39 | 1% | -$565.71 | -77% | 1.6 min |
| Sell at 50¢ | 21 | 0% | -$511.05 | -69% | 1.9 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 3 | 0 | 100% | 67% | -100% | +73% | +160% |
| 5–10 min | 168 | 2 | 12% | 3% | +13% | -79% | -89% |
| 2–5 min | 1987 | 12 | 8% | 4% | -41% | -86% | -87% |
| 1–2 min | 1582 | 6 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 2342 | 3 | 1% | 0% | -81% | -92% | -92% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| DOGE | 424 | 2 | 4% | 1% | -37% | -89% | -90% |
| ZEC | 420 | 2 | 5% | 3% | -43% | -88% | -90% |
| HYPE | 418 | 2 | 6% | 4% | -41% | -87% | -84% |
| BNB | 418 | 0 | 4% | 1% | -100% | -91% | -93% |
| ETH | 417 | 2 | 6% | 3% | -40% | -86% | -85% |
| BTC | 416 | 1 | 7% | 3% | -69% | -84% | -88% |
| XRP | 413 | 3 | 1% | 1% | -5% | -65% | -65% |
| SOL | 412 | 0 | 3% | 1% | -100% | -93% | -92% |
| NEAR | 411 | 1 | 6% | 2% | -67% | -85% | -88% |
| GOLD | 304 | 0 | 5% | 1% | -100% | -90% | -92% |
| SILVER | 285 | 0 | 2% | 1% | -100% | -95% | -95% |
| WTI | 270 | 2 | 3% | 1% | -22% | -94% | -96% |
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
| UP (bought YES) | 3097 | 14 | 4% | 2% | -47% | -91% | -91% |
| DOWN (bought NO) | 2985 | 9 | 4% | 2% | -65% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 460 | 2 | 1% | 1% | -18% | -55% | -54% |
| 0.05–0.1% | 527 | 0 | 3% | 1% | -100% | -90% | -93% |
| 0.1–0.2% | 915 | 2 | 4% | 2% | -71% | -90% | -91% |
| 0.2–0.5% | 1261 | 5 | 6% | 3% | -56% | -87% | -87% |
| Over 0.5% | 584 | 4 | 7% | 3% | -29% | -86% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 1474 | 5 | 4% | 1% | -61% | -91% | -94% |
| Morning (6am–12pm) | 1640 | 9 | 5% | 3% | -38% | -90% | -88% |
| Afternoon (12–6pm) | 1305 | 3 | 4% | 1% | -73% | -83% | -85% |
| Evening (6pm–12am) | 1663 | 6 | 3% | 2% | -58% | -93% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 3,130 |
| Time from buy to best bounce (bounced bets) | 49 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/2 6:29:35 PM | BNB | UP | 24 sec | -0.053% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:29:09 PM | BTC | DOWN | 50 sec | +0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:28:41 PM | NEAR | DOWN | 79 sec | +0.284% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:30 PM | HYPE | DOWN | 2.5 min | +0.562% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:28 PM | ETH | DOWN | 2.5 min | +0.100% | 1¢ | In play | — |
| 10/2 6:27:18 PM | DOGE | DOWN | 2.7 min | +0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 6:27:16 PM | XRP | DOWN | 2.7 min | +0.222% | 1¢ | In play | — |
| 10/2 6:27:16 PM | SOL | DOWN | 2.7 min | +0.189% | 0¢ | In play | — |
| 10/2 6:25:19 PM | ZEC | DOWN | 4.7 min | +1.235% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:14:54 PM | BTC | UP | 6 sec | -0.001% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:14:52 PM | DOGE | DOWN | 8 sec | +0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:14:12 PM | BNB | DOWN | 48 sec | +0.040% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:13:57 PM | SOL | DOWN | 63 sec | +0.081% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 6:13:35 PM | HYPE | DOWN | 85 sec | +0.196% | 6¢ | ❌ Lost | -$0.15 |
| 10/2 6:13:00 PM | NEAR | DOWN | 2.0 min | +0.526% | 0¢ | ❌ Lost | $0.00 |
| 10/2 6:10:43 PM | ZEC | DOWN | 4.3 min | +0.543% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:59:52 PM | NEAR | DOWN | 7 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:59:52 PM | DOGE | UP | 7 sec | -0.030% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:59:52 PM | BNB | DOWN | 7 sec | -0.056% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:59:52 PM | ZEC | UP | 7 sec | +0.017% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:59:07 PM | XRP | UP | 52 sec | -0.108% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:58:54 PM | BTC | UP | 66 sec | -0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:58:52 PM | SOL | UP | 68 sec | -0.113% | 1¢ | ❌ Lost | -$0.15 |
| 10/2 5:58:36 PM | ETH | UP | 84 sec | -0.048% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:56:31 PM | HYPE | DOWN | 3.5 min | +0.519% | 5¢ | ❌ Lost | -$0.15 |
| 10/2 5:44:27 PM | NEAR | DOWN | 32 sec | +0.081% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:44:27 PM | BNB | DOWN | 32 sec | -0.026% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:44:19 PM | ETH | DOWN | 40 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/2 5:43:30 PM | ZEC | DOWN | 89 sec | +0.450% | 0¢ | ❌ Lost | -$0.15 |
| 10/2 5:43:12 PM | XRP | DOWN | 1.8 min | +0.121% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
