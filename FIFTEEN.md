# 15-Minute 1¢ Study

*Updated Thu Oct 15, 11:54 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1583 finished bets | 1% | $76.20 | +43% | +4.81¢ | $26.65 / $49.55 |

*Expect about **88 buys a day** (~$13.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1469 | $51.00 | +32% |
| Momentum model ≥ 2%, hold to the close | 2469 | -$6.05 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1583 | -$19.05 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20291 | 20284 | 79 (0%) | 1.07% | -$1,360.15 (-55%) | Hold to the close: -$1,360.15 (-55%) |

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
| Volatility model | 13021 | 4.4% | 0.4% (53) | -636% | ❌ Worse |
| Momentum model | 13021 | 4.4% | 0.4% (53) | -660% | ❌ Worse |
| Mean-reversion model | 13021 | 7.3% | 0.4% (53) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13021 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2879 | 23 | -8% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1583 | 18 | +43% | -74% | -73% | -68% |
| Volatility model ≥ 10% | 929 | 11 | +68% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2469 | 20 | -2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1469 | 15 | +32% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 983 | 10 | +42% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4882 | 33 | -26% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3355 | 26 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2198 | 15 | -22% | -80% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13219 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5014 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2051 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20284 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 79 | 0% | -$1,360.15 | -55% | — |
| Sell at 2¢ | 716 | 4% | -$2,181.99 | -88% | 42 sec |
| Sell at 3¢ | 479 | 2% | -$2,181.34 | -88% | 47 sec |
| Sell at 5¢ | 349 | 2% | -$2,141.30 | -87% | 50 sec |
| Sell at 10¢ | 215 | 1% | -$2,058.50 | -83% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,884.40 | -76% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,674.65 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6574 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5277 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7769 | 18 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1484 | 11 | 5% | 3% | -8% | -89% | -89% |
| HYPE | 1479 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1473 | 8 | 5% | 3% | -34% | -88% | -86% |
| BNB | 1471 | 5 | 4% | 2% | -58% | -90% | -90% |
| DOGE | 1470 | 2 | 4% | 2% | -83% | -91% | -90% |
| SOL | 1466 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1461 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1459 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1456 | 8 | 5% | 3% | -28% | -78% | -79% |
| GOLD | 816 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 796 | 4 | 3% | 1% | -42% | -79% | -79% |
| WTI | 768 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 701 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 678 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 628 | 5 | 2% | 2% | -26% | -81% | -80% |
| PALLADIUM | 627 | 2 | 1% | 0% | -70% | -83% | -83% |
| EURUSD | 619 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 579 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 543 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 165 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 145 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10232 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10052 | 40 | 4% | 2% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2199 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2288 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3338 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3860 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1531 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5785 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,464 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 11:44:49 PM | BNB | UP | 10 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:49 PM | PLATINUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:49 PM | COPPER | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:49 PM | NEAR | UP | 10 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:44:33 PM | NATGAS | UP | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:33 PM | SILVER | UP | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:18 PM | XRP | UP | 42 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:44:18 PM | EURUSD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:44:18 PM | ETH | UP | 42 sec | -0.057% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:43:47 PM | WTI | UP | 72 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:43:31 PM | HYPE | UP | 88 sec | -0.195% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:42:27 PM | SOL | UP | 2.5 min | -0.233% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:41:55 PM | ZEC | UP | 3.1 min | -0.522% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 11:41:55 PM | BTC | UP | 3.1 min | -0.171% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:54 PM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:38 PM | NATGAS | DOWN | 21 sec | — | 0¢ | ✅ Won | $13.85 |
| 10/15 11:29:22 PM | WTI | DOWN | 37 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:22 PM | SILVER | UP | 37 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:29:22 PM | USDCAD | DOWN | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:22 PM | AUDUSD | UP | 37 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:29:06 PM | USDJPY | DOWN | 54 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:48 PM | XRP | UP | 72 sec | -0.172% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:48 PM | DOGE | UP | 72 sec | -0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/15 11:28:32 PM | ZEC | UP | 88 sec | -0.366% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:28:16 PM | COPPER | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:45 PM | BNB | UP | 2.2 min | -0.103% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:45 PM | BTC | UP | 2.2 min | -0.107% | 2¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:29 PM | NEAR | UP | 2.5 min | -0.537% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:29 PM | SOL | UP | 2.5 min | -0.246% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:27:13 PM | ETH | UP | 2.8 min | -0.152% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
