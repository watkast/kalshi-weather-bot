# 15-Minute 1¢ Study

*Updated Tue Oct 13, 8:31 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1317 finished bets | 1% | $38.00 | +26% | +2.89¢ | $27.35 / $10.65 |

*Expect about **83 buys a day** (~$12.48/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1250 | $19.75 | +15% |
| 5+ min left, hold to the close | 509 | -$18.85 | -25% |
| Volatility model ≥ 5%, sell at 50¢ | 1317 | -$21.00 | -15% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 17189 | 17182 | 65 (0%) | 1.07% | -$1,167.80 (-56%) | Hold to the close: -$1,167.80 (-56%) |

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
| Volatility model | 11311 | 4.4% | 0.4% (46) | -665% | ❌ Worse |
| Momentum model | 11311 | 4.4% | 0.4% (46) | -693% | ❌ Worse |
| Mean-reversion model | 11311 | 7.2% | 0.4% (46) | -782% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 11311 | 46 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2344 | 18 | -11% | -78% | -77% | -73% |
| Volatility model ≥ 5% | 1317 | 13 | +26% | -72% | -71% | -68% |
| Volatility model ≥ 10% | 808 | 9 | +60% | -63% | -61% | -58% |
| Momentum model ≥ 2% | 2057 | 15 | -11% | -79% | -79% | -77% |
| Momentum model ≥ 5% | 1250 | 11 | +15% | -76% | -76% | -73% |
| Momentum model ≥ 10% | 853 | 8 | +33% | -69% | -69% | -64% |
| Mean-reversion model ≥ 2% | 4070 | 27 | -27% | -85% | -85% | -82% |
| Mean-reversion model ≥ 5% | 2784 | 20 | -20% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 1833 | 14 | -12% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 11509 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 4156 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 1517 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 17182 | 3% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 65 | 0% | -$1,167.80 | -56% | — |
| Sell at 2¢ | 595 | 3% | -$1,881.10 | -91% | 33 sec |
| Sell at 3¢ | 397 | 2% | -$1,880.97 | -91% | 46 sec |
| Sell at 5¢ | 287 | 2% | -$1,849.25 | -89% | 48 sec |
| Sell at 10¢ | 182 | 1% | -$1,769.38 | -85% | 63 sec |
| Sell at 25¢ | 101 | 1% | -$1,645.49 | -79% | 77 sec |
| Sell at 50¢ | 65 | 0% | -$1,471.05 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 505 | 4 | 10% | 3% | -25% | -81% | -87% |
| 2–5 min | 5536 | 32 | 6% | 3% | -43% | -88% | -88% |
| 1–2 min | 4524 | 17 | 3% | 2% | -59% | -94% | -93% |
| Under 1 min | 6613 | 12 | 1% | 0% | -74% | -91% | -91% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1292 | 7 | 4% | 2% | -33% | -90% | -90% |
| HYPE | 1287 | 4 | 4% | 2% | -62% | -90% | -89% |
| ETH | 1282 | 8 | 5% | 3% | -24% | -89% | -88% |
| BNB | 1282 | 5 | 4% | 2% | -52% | -90% | -91% |
| DOGE | 1281 | 2 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1278 | 2 | 3% | 1% | -80% | -93% | -92% |
| BTC | 1271 | 6 | 5% | 2% | -37% | -88% | -91% |
| NEAR | 1268 | 7 | 5% | 2% | -28% | -77% | -78% |
| XRP | 1268 | 7 | 2% | 1% | -32% | -85% | -86% |
| GOLD | 681 | 1 | 4% | 1% | -83% | -92% | -93% |
| SILVER | 667 | 2 | 3% | 1% | -65% | -94% | -93% |
| WTI | 637 | 3 | 3% | 1% | -46% | -94% | -96% |
| COPPER | 586 | 0 | 2% | 1% | -100% | -97% | -96% |
| PLATINUM | 559 | 0 | 1% | 0% | -100% | -99% | -99% |
| PALLADIUM | 516 | 1 | 1% | 0% | -82% | -98% | -98% |
| NATGAS | 510 | 3 | 3% | 2% | -45% | -96% | -94% |
| EURUSD | 496 | 3 | 3% | 2% | -44% | -77% | -76% |
| GBPUSD | 468 | 1 | 2% | 1% | -80% | -96% | -96% |
| USDJPY | 424 | 3 | 1% | 1% | -34% | -98% | -98% |
| AUDUSD | 69 | 0 | 0% | 0% | -100% | -100% | -100% |
| USDCAD | 60 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 8639 | 35 | 3% | 2% | -53% | -90% | -89% |
| DOWN (bought NO) | 8543 | 30 | 3% | 2% | -59% | -91% | -92% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2012 | 10 | 2% | 1% | -17% | -77% | -77% |
| 0.05–0.1% | 2044 | 6 | 3% | 1% | -58% | -92% | -91% |
| 0.1–0.2% | 2942 | 9 | 4% | 2% | -62% | -91% | -91% |
| 0.2–0.5% | 3247 | 18 | 6% | 3% | -39% | -89% | -88% |
| Over 0.5% | 1261 | 5 | 6% | 2% | -59% | -88% | -90% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4344 | 20 | 4% | 2% | -47% | -87% | -87% |
| Morning (6am–12pm) | 3923 | 20 | 4% | 2% | -41% | -91% | -91% |
| Afternoon (12–6pm) | 4113 | 10 | 3% | 1% | -71% | -91% | -91% |
| Evening (6pm–12am) | 4802 | 15 | 3% | 2% | -64% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 25 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,545 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/13 8:29:53 PM | DOGE | DOWN | 6 sec | -0.066% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:29:53 PM | BTC | UP | 6 sec | -0.064% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:29:37 PM | SILVER | DOWN | 22 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 8:29:37 PM | USDCAD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:29:37 PM | SOL | UP | 22 sec | -0.116% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:29:37 PM | HYPE | UP | 22 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 8:29:37 PM | GBPUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:29:21 PM | ETH | UP | 38 sec | -0.051% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 8:29:21 PM | XRP | UP | 38 sec | -0.124% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:29:07 PM | BNB | DOWN | 53 sec | +0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:28:35 PM | PLATINUM | DOWN | 85 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:28:19 PM | NEAR | UP | 1.7 min | -0.233% | 5¢ | ❌ Lost | -$0.15 |
| 10/13 8:28:19 PM | WTI | UP | 1.7 min | — | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:28:02 PM | ZEC | UP | 1.9 min | -0.319% | 11¢ | ❌ Lost | -$0.15 |
| 10/13 8:26:58 PM | COPPER | DOWN | 3.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:14:34 PM | BNB | DOWN | 25 sec | -0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:14:34 PM | DOGE | DOWN | 25 sec | +0.070% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:14:18 PM | ETH | DOWN | 41 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 8:14:18 PM | BTC | DOWN | 41 sec | +0.032% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:14:01 PM | PLATINUM | DOWN | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:14:01 PM | XRP | DOWN | 58 sec | +0.073% | 1¢ | ❌ Lost | -$0.15 |
| 10/13 8:14:01 PM | SOL | DOWN | 58 sec | +0.122% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:14:01 PM | ZEC | DOWN | 58 sec | +0.313% | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:13:13 PM | NEAR | DOWN | 1.8 min | +0.311% | 0¢ | ❌ Lost | $0.00 |
| 10/13 8:12:09 PM | HYPE | DOWN | 2.8 min | +0.199% | 6¢ | ❌ Lost | -$0.15 |
| 10/13 8:11:53 PM | SILVER | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/13 8:11:37 PM | COPPER | DOWN | 3.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/13 8:11:37 PM | GOLD | DOWN | 3.4 min | — | 1¢ | ❌ Lost | $0.00 |
| 10/13 7:59:52 PM | NEAR | DOWN | 8 sec | +0.043% | 0¢ | ❌ Lost | $0.00 |
| 10/13 7:59:52 PM | WTI | UP | 8 sec | — | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
