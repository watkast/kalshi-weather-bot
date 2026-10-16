# 15-Minute 1¢ Study

*Updated Thu Oct 15, 11:23 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1581 finished bets | 1% | $76.50 | +44% | +4.84¢ | $26.80 / $49.70 |

*Expect about **88 buys a day** (~$13.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1469 | $51.00 | +32% |
| Momentum model ≥ 2%, hold to the close | 2465 | -$5.45 | -2% |
| Volatility model ≥ 5%, sell at 50¢ | 1581 | -$18.75 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 20260 | 20253 | 78 (0%) | 1.07% | -$1,370.40 (-56%) | Hold to the close: -$1,370.40 (-56%) |

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
| Volatility model | 13004 | 4.4% | 0.4% (53) | -637% | ❌ Worse |
| Momentum model | 13004 | 4.4% | 0.4% (53) | -661% | ❌ Worse |
| Mean-reversion model | 13004 | 7.3% | 0.4% (53) | -762% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13004 | 53 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 2872 | 23 | -7% | -79% | -78% | -74% |
| Volatility model ≥ 5% | 1581 | 18 | +44% | -74% | -72% | -68% |
| Volatility model ≥ 10% | 929 | 11 | +68% | -65% | -64% | -60% |
| Momentum model ≥ 2% | 2465 | 20 | -2% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1469 | 15 | +32% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 983 | 10 | +42% | -71% | -71% | -66% |
| Mean-reversion model ≥ 2% | 4875 | 33 | -26% | -84% | -85% | -81% |
| Mean-reversion model ≥ 5% | 3350 | 26 | -14% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2194 | 15 | -22% | -80% | -81% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13202 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5004 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2047 | 2% | 1% | 1% | 1% | 0% | 0% |
| **All** | 20253 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 78 | 0% | -$1,370.40 | -56% | — |
| Sell at 2¢ | 716 | 4% | -$2,192.24 | -89% | 42 sec |
| Sell at 3¢ | 479 | 2% | -$2,191.59 | -89% | 47 sec |
| Sell at 5¢ | 349 | 2% | -$2,151.55 | -87% | 50 sec |
| Sell at 10¢ | 215 | 1% | -$2,068.75 | -84% | 63 sec |
| Sell at 25¢ | 125 | 1% | -$1,894.65 | -77% | 80 sec |
| Sell at 50¢ | 82 | 0% | -$1,684.90 | -68% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 660 | 5 | 11% | 3% | -28% | -81% | -86% |
| 2–5 min | 6565 | 36 | 7% | 3% | -46% | -88% | -88% |
| 1–2 min | 5271 | 20 | 3% | 2% | -59% | -92% | -92% |
| Under 1 min | 7753 | 17 | 1% | 0% | -68% | -89% | -89% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1482 | 11 | 5% | 3% | -8% | -89% | -89% |
| HYPE | 1477 | 5 | 4% | 2% | -58% | -90% | -89% |
| ETH | 1471 | 8 | 5% | 3% | -34% | -88% | -86% |
| DOGE | 1469 | 2 | 4% | 2% | -83% | -91% | -90% |
| BNB | 1469 | 5 | 4% | 2% | -58% | -90% | -90% |
| SOL | 1464 | 2 | 3% | 2% | -83% | -92% | -92% |
| XRP | 1459 | 7 | 3% | 1% | -41% | -86% | -86% |
| BTC | 1457 | 7 | 5% | 2% | -36% | -88% | -91% |
| NEAR | 1454 | 8 | 5% | 3% | -28% | -78% | -79% |
| GOLD | 816 | 1 | 4% | 1% | -86% | -92% | -94% |
| SILVER | 794 | 4 | 3% | 1% | -42% | -79% | -79% |
| WTI | 766 | 3 | 3% | 1% | -55% | -94% | -96% |
| COPPER | 699 | 2 | 2% | 1% | -73% | -83% | -83% |
| PLATINUM | 676 | 0 | 1% | 0% | -100% | -99% | -98% |
| PALLADIUM | 627 | 2 | 1% | 0% | -70% | -83% | -83% |
| NATGAS | 626 | 4 | 2% | 2% | -40% | -96% | -95% |
| EURUSD | 618 | 3 | 3% | 1% | -55% | -80% | -80% |
| GBPUSD | 579 | 1 | 2% | 1% | -84% | -97% | -96% |
| USDJPY | 542 | 3 | 1% | 1% | -48% | -99% | -98% |
| AUDUSD | 164 | 0 | 1% | 0% | -100% | -99% | -98% |
| USDCAD | 144 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10206 | 39 | 4% | 2% | -56% | -89% | -89% |
| DOWN (bought NO) | 10047 | 39 | 4% | 2% | -55% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2198 | 11 | 2% | 1% | -16% | -79% | -78% |
| 0.05–0.1% | 2287 | 7 | 3% | 1% | -55% | -92% | -92% |
| 0.1–0.2% | 3329 | 10 | 4% | 2% | -63% | -90% | -90% |
| 0.2–0.5% | 3856 | 21 | 6% | 3% | -40% | -88% | -88% |
| Over 0.5% | 1529 | 6 | 6% | 2% | -59% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 4976 | 20 | 4% | 2% | -54% | -87% | -87% |
| Morning (6am–12pm) | 4701 | 26 | 4% | 2% | -36% | -86% | -86% |
| Afternoon (12–6pm) | 4822 | 16 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 5754 | 16 | 3% | 2% | -68% | -94% | -93% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,467 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/15 11:14:24 PM | AUDUSD | UP | 35 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:14:08 PM | GBPUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:36 PM | PLATINUM | UP | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:36 PM | USDJPY | DOWN | 83 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:20 PM | HYPE | DOWN | 1.6 min | +0.157% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:20 PM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:20 PM | EURUSD | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:20 PM | SILVER | UP | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:13:20 PM | USDCAD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:12:46 PM | PALLADIUM | UP | 2.2 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:12:14 PM | BTC | DOWN | 2.8 min | +0.186% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:12:14 PM | NEAR | DOWN | 2.8 min | +0.746% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:12:14 PM | ETH | DOWN | 2.8 min | +0.290% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 11:11:59 PM | DOGE | DOWN | 3.0 min | +0.329% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:11:43 PM | GOLD | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:11:43 PM | COPPER | UP | 3.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:11:27 PM | SOL | DOWN | 3.5 min | +0.485% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:10:38 PM | XRP | DOWN | 4.3 min | +0.322% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:10:22 PM | BNB | DOWN | 4.6 min | +0.178% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 11:09:50 PM | ZEC | DOWN | 5.2 min | +1.483% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:59:40 PM | WTI | UP | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:59:24 PM | HYPE | DOWN | 35 sec | +0.238% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:58:52 PM | XRP | DOWN | 68 sec | +0.090% | 0¢ | ❌ Lost | -$0.15 |
| 10/15 10:58:34 PM | GOLD | UP | 86 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:47 PM | NEAR | DOWN | 2.2 min | +0.265% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:47 PM | ETH | DOWN | 2.2 min | +0.117% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:47 PM | DOGE | DOWN | 2.2 min | +0.234% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:31 PM | ZEC | DOWN | 2.5 min | +0.312% | 1¢ | ❌ Lost | -$0.15 |
| 10/15 10:57:31 PM | BNB | DOWN | 2.5 min | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/15 10:57:31 PM | BTC | DOWN | 2.5 min | +0.128% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
