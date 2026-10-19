# 15-Minute 1¢ Study

*Updated Sun Oct 18, 7:14 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1969 finished bets | 1% | $87.80 | +40% | +4.46¢ | $32.60 / $55.20 |

*Expect about **95 buys a day** (~$14.23/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1808 | $67.85 | +34% |
| Momentum model ≥ 2%, hold to the close | 3013 | -$2.05 | -1% |
| Volatility model ≥ 2%, hold to the close | 3547 | -$25.10 | -6% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23110 | 23091 | 88 (0%) | 1.07% | -$1,569.10 (-56%) | Hold to the close: -$1,569.10 (-56%) |

*In play or awaiting result: 18. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 15300 | 4.6% | 0.4% (62) | -668% | ❌ Worse |
| Momentum model | 15300 | 4.6% | 0.4% (62) | -690% | ❌ Worse |
| Mean-reversion model | 15300 | 7.7% | 0.4% (62) | -800% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15300 | 62 | -49% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3547 | 29 | -6% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1969 | 22 | +40% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1157 | 14 | +70% | -70% | -68% | -65% |
| Momentum model ≥ 2% | 3013 | 25 | -1% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1808 | 19 | +34% | -79% | -79% | -75% |
| Momentum model ≥ 10% | 1203 | 12 | +38% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5931 | 40 | -26% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4122 | 32 | -14% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2728 | 21 | -12% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15498 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5347 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2246 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23091 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,569.10 | -56% | — |
| Sell at 2¢ | 839 | 4% | -$2,484.96 | -89% | 44 sec |
| Sell at 3¢ | 569 | 2% | -$2,481.19 | -89% | 47 sec |
| Sell at 5¢ | 408 | 2% | -$2,437.90 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,351.53 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,165.63 | -77% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,934.85 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 842 | 5 | 10% | 3% | -44% | -82% | -84% |
| 2–5 min | 7533 | 39 | 7% | 3% | -49% | -88% | -87% |
| 1–2 min | 5929 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8783 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1741 | 11 | 4% | 2% | -21% | -90% | -90% |
| HYPE | 1731 | 6 | 5% | 2% | -57% | -90% | -88% |
| BNB | 1731 | 8 | 5% | 2% | -43% | -89% | -88% |
| DOGE | 1725 | 3 | 4% | 2% | -78% | -90% | -90% |
| ETH | 1722 | 9 | 6% | 3% | -37% | -87% | -87% |
| SOL | 1719 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1713 | 7 | 3% | 1% | -50% | -87% | -87% |
| NEAR | 1709 | 9 | 6% | 3% | -32% | -79% | -79% |
| BTC | 1707 | 9 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 871 | 1 | 3% | 1% | -86% | -92% | -94% |
| SILVER | 847 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 828 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 738 | 2 | 2% | 1% | -75% | -84% | -84% |
| PLATINUM | 727 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 673 | 5 | 2% | 2% | -31% | -82% | -81% |
| EURUSD | 668 | 3 | 3% | 1% | -58% | -82% | -81% |
| PALLADIUM | 663 | 2 | 1% | 0% | -72% | -84% | -84% |
| GBPUSD | 621 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 580 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 207 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 170 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11621 | 42 | 4% | 2% | -58% | -89% | -88% |
| DOWN (bought NO) | 11470 | 46 | 4% | 2% | -54% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2652 | 14 | 2% | 1% | -12% | -82% | -81% |
| 0.05–0.1% | 2694 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3886 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4507 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1756 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6286 | 18 | 3% | 2% | -67% | -92% | -91% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,852 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 7:13:51 PM | COPPER | DOWN | 69 sec | — | — | In play | — |
| 10/18 7:13:13 PM | PALLADIUM | DOWN | 1.8 min | — | — | In play | — |
| 10/18 7:12:51 PM | BNB | DOWN | 2.1 min | +0.087% | — | In play | — |
| 10/18 7:12:31 PM | XRP | DOWN | 2.5 min | +0.322% | — | In play | — |
| 10/18 7:12:21 PM | BTC | DOWN | 2.6 min | +0.208% | — | In play | — |
| 10/18 7:12:19 PM | NEAR | DOWN | 2.7 min | +0.450% | — | In play | — |
| 10/18 7:12:09 PM | ETH | DOWN | 2.9 min | +0.296% | — | In play | — |
| 10/18 7:12:07 PM | DOGE | DOWN | 2.9 min | +0.326% | — | In play | — |
| 10/18 7:11:57 PM | WTI | DOWN | 3.0 min | — | — | In play | — |
| 10/18 7:11:53 PM | SOL | DOWN | 3.1 min | +0.332% | — | In play | — |
| 10/18 7:11:13 PM | NATGAS | DOWN | 3.8 min | — | — | In play | — |
| 10/18 7:10:11 PM | ZEC | DOWN | 4.8 min | +0.801% | — | In play | — |
| 10/18 6:59:51 PM | SILVER | DOWN | 8 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:59:35 PM | USDJPY | DOWN | 24 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:59:29 PM | BNB | UP | 30 sec | -0.098% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:59:19 PM | NEAR | UP | 40 sec | -0.325% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:59:19 PM | ZEC | UP | 40 sec | -0.218% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:59:01 PM | XRP | UP | 58 sec | -0.115% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:58:39 PM | DOGE | UP | 80 sec | -0.194% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:58:39 PM | ETH | UP | 80 sec | -0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:58:07 PM | BTC | UP | 1.9 min | -0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:57:47 PM | SOL | UP | 2.2 min | -0.244% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:56:23 PM | AUDUSD | UP | 3.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:44:45 PM | NATGAS | DOWN | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 6:44:36 PM | GOLD | UP | 24 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:44:02 PM | XRP | DOWN | 57 sec | +0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:43:36 PM | DOGE | DOWN | 83 sec | +0.173% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:43:15 PM | NEAR | DOWN | 1.7 min | +0.537% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 6:42:56 PM | ZEC | DOWN | 2.1 min | +0.581% | 0¢ | ❌ Lost | $0.00 |
| 10/18 6:42:53 PM | BNB | DOWN | 2.1 min | +0.209% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
