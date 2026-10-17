# 15-Minute 1¢ Study

*Updated Fri Oct 16, 6:48 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1679 finished bets | 1% | $79.70 | +43% | +4.75¢ | $34.80 / $44.90 |

*Expect about **90 buys a day** (~$13.43/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1546 | $42.75 | +26% |
| Momentum model ≥ 2%, hold to the close | 2618 | -$9.15 | -3% |
| Volatility model ≥ 5%, sell at 50¢ | 1679 | -$22.80 | -12% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 21406 | 21399 | 80 (0%) | 1.07% | -$1,484.45 (-57%) | Hold to the close: -$1,484.45 (-57%) |

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
| Volatility model | 13683 | 4.4% | 0.4% (54) | -650% | ❌ Worse |
| Momentum model | 13683 | 4.4% | 0.4% (54) | -673% | ❌ Worse |
| Mean-reversion model | 13683 | 7.4% | 0.4% (54) | -784% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 13683 | 54 | -51% | -88% | -88% | -85% |
| Volatility model ≥ 2% | 3071 | 24 | -10% | -78% | -78% | -74% |
| Volatility model ≥ 5% | 1679 | 19 | +43% | -73% | -72% | -68% |
| Volatility model ≥ 10% | 973 | 11 | +62% | -65% | -64% | -61% |
| Momentum model ≥ 2% | 2618 | 21 | -3% | -80% | -80% | -77% |
| Momentum model ≥ 5% | 1546 | 15 | +26% | -77% | -77% | -73% |
| Momentum model ≥ 10% | 1029 | 10 | +37% | -72% | -72% | -67% |
| Mean-reversion model ≥ 2% | 5188 | 34 | -28% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 3587 | 27 | -17% | -82% | -82% | -78% |
| Mean-reversion model ≥ 10% | 2354 | 16 | -22% | -80% | -80% | -77% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 13881 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5301 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2217 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 21399 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 80 | 0% | -$1,484.45 | -57% | — |
| Sell at 2¢ | 765 | 4% | -$2,307.55 | -89% | 41 sec |
| Sell at 3¢ | 515 | 2% | -$2,305.60 | -89% | 47 sec |
| Sell at 5¢ | 371 | 2% | -$2,265.30 | -87% | 50 sec |
| Sell at 10¢ | 223 | 1% | -$2,186.32 | -84% | 63 sec |
| Sell at 25¢ | 126 | 1% | -$2,019.39 | -78% | 80 sec |
| Sell at 50¢ | 83 | 0% | -$1,806.20 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 730 | 5 | 10% | 3% | -35% | -82% | -85% |
| 2–5 min | 6921 | 37 | 7% | 3% | -47% | -88% | -87% |
| 1–2 min | 5569 | 20 | 3% | 2% | -61% | -92% | -92% |
| Under 1 min | 8175 | 18 | 1% | 0% | -68% | -88% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1559 | 11 | 5% | 3% | -12% | -89% | -90% |
| HYPE | 1554 | 5 | 4% | 2% | -60% | -90% | -89% |
| ETH | 1547 | 8 | 6% | 3% | -37% | -87% | -86% |
| BNB | 1545 | 6 | 5% | 2% | -52% | -89% | -89% |
| DOGE | 1544 | 2 | 4% | 2% | -84% | -91% | -90% |
| SOL | 1541 | 2 | 3% | 2% | -84% | -92% | -92% |
| XRP | 1533 | 7 | 3% | 1% | -43% | -86% | -87% |
| NEAR | 1529 | 8 | 6% | 3% | -31% | -77% | -78% |
| BTC | 1529 | 7 | 5% | 2% | -39% | -88% | -91% |
| GOLD | 864 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 841 | 4 | 3% | 1% | -45% | -80% | -80% |
| WTI | 815 | 3 | 3% | 1% | -57% | -94% | -95% |
| COPPER | 735 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 722 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 665 | 5 | 2% | 2% | -30% | -82% | -81% |
| PALLADIUM | 659 | 2 | 1% | 0% | -72% | -84% | -84% |
| EURUSD | 659 | 3 | 3% | 1% | -58% | -81% | -81% |
| GBPUSD | 615 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 574 | 3 | 1% | 1% | -51% | -99% | -98% |
| AUDUSD | 200 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 169 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 10801 | 40 | 4% | 2% | -58% | -89% | -89% |
| DOWN (bought NO) | 10598 | 40 | 4% | 2% | -56% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2292 | 11 | 2% | 1% | -19% | -79% | -79% |
| 0.05–0.1% | 2377 | 7 | 3% | 1% | -57% | -92% | -91% |
| 0.1–0.2% | 3501 | 11 | 4% | 2% | -61% | -90% | -90% |
| 0.2–0.5% | 4088 | 21 | 6% | 3% | -43% | -88% | -88% |
| Over 0.5% | 1620 | 6 | 7% | 3% | -62% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5359 | 20 | 4% | 2% | -58% | -87% | -88% |
| Morning (6am–12pm) | 5104 | 27 | 4% | 2% | -39% | -87% | -86% |
| Afternoon (12–6pm) | 5104 | 16 | 3% | 1% | -63% | -88% | -89% |
| Evening (6pm–12am) | 5832 | 17 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,446 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/16 6:44:52 PM | DOGE | UP | 8 sec | -0.027% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:52 PM | HYPE | UP | 8 sec | -0.079% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:36 PM | BTC | UP | 24 sec | -0.010% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:44:20 PM | SOL | UP | 40 sec | -0.088% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:44:03 PM | XRP | UP | 56 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:43:47 PM | NEAR | UP | 72 sec | -0.654% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:43:31 PM | ZEC | UP | 88 sec | -0.285% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:42:59 PM | BNB | DOWN | 2.0 min | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:41:22 PM | ETH | DOWN | 3.6 min | +0.130% | 10¢ | ❌ Lost | -$0.15 |
| 10/16 6:29:44 PM | WTI | UP | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:29:44 PM | ZEC | UP | 15 sec | -0.118% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:29:28 PM | NEAR | UP | 31 sec | -0.101% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:56 PM | NATGAS | UP | 64 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:56 PM | HYPE | UP | 64 sec | -0.023% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:28:40 PM | BTC | UP | 80 sec | -0.074% | 1¢ | ❌ Lost | $0.00 |
| 10/16 6:27:53 PM | SOL | UP | 2.1 min | -0.127% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:27:15 PM | BNB | UP | 2.7 min | -0.110% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:26:59 PM | ETH | UP | 3.0 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:25:54 PM | XRP | UP | 4.1 min | -0.214% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:25:06 PM | DOGE | UP | 4.9 min | -0.218% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:14:58 PM | BTC | DOWN | 2 sec | +0.021% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:14:42 PM | SOL | DOWN | 18 sec | +0.013% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:14:26 PM | WTI | DOWN | 34 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:14:26 PM | ETH | UP | 34 sec | -0.016% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:13:37 PM | NEAR | UP | 82 sec | -0.354% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:13:37 PM | HYPE | UP | 82 sec | -0.152% | 0¢ | ❌ Lost | $0.00 |
| 10/16 6:13:21 PM | ZEC | DOWN | 1.6 min | +0.302% | 0¢ | ❌ Lost | -$0.15 |
| 10/16 6:12:00 PM | XRP | UP | 3.0 min | -0.160% | 3¢ | ❌ Lost | -$0.15 |
| 10/16 6:10:56 PM | DOGE | UP | 4.1 min | -0.160% | 1¢ | ❌ Lost | -$0.15 |
| 10/16 6:10:21 PM | BNB | UP | 4.6 min | -0.164% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
