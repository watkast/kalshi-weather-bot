# 15-Minute 1¢ Study

*Updated Tue Oct 20, 8:04 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2182 finished bets | 1% | $75.40 | +31% | +3.46¢ | $21.20 / $54.20 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2017 | $56.35 | +25% |
| Momentum model ≥ 2%, hold to the close | 3371 | -$33.35 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2182 | -$41.60 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25924 | 25917 | 95 (0%) | 1.07% | -$1,828.40 (-58%) | Hold to the close: -$1,828.40 (-58%) |

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
| Volatility model | 16862 | 4.6% | 0.4% (67) | -665% | ❌ Worse |
| Momentum model | 16862 | 4.5% | 0.4% (67) | -687% | ❌ Worse |
| Mean-reversion model | 16862 | 7.8% | 0.4% (67) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16862 | 67 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 4001 | 32 | -9% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2182 | 23 | +31% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1252 | 15 | +67% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3371 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2017 | 20 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1328 | 13 | +33% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6639 | 43 | -30% | -82% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4624 | 35 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3062 | 23 | -15% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17060 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6145 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2712 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25917 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 95 | 0% | -$1,828.40 | -58% | — |
| Sell at 2¢ | 947 | 4% | -$2,772.18 | -88% | 46 sec |
| Sell at 3¢ | 646 | 2% | -$2,766.46 | -88% | 48 sec |
| Sell at 5¢ | 457 | 2% | -$2,721.35 | -86% | 55 sec |
| Sell at 10¢ | 278 | 1% | -$2,626.22 | -83% | 64 sec |
| Sell at 25¢ | 150 | 1% | -$2,437.90 | -77% | 80 sec |
| Sell at 50¢ | 97 | 0% | -$2,209.65 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1045 | 5 | 11% | 4% | -54% | -81% | -84% |
| 2–5 min | 8376 | 42 | 7% | 3% | -51% | -87% | -87% |
| 1–2 min | 6607 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9885 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1917 | 11 | 5% | 2% | -29% | -90% | -90% |
| HYPE | 1907 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1906 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1895 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1894 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1893 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1886 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1882 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1880 | 11 | 5% | 2% | -22% | -88% | -90% |
| GOLD | 1010 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 969 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 946 | 3 | 3% | 1% | -63% | -94% | -95% |
| COPPER | 841 | 3 | 2% | 1% | -67% | -75% | -75% |
| PLATINUM | 840 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 775 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 770 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 764 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 727 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 681 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 292 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 242 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13029 | 48 | 4% | 2% | -58% | -87% | -86% |
| DOWN (bought NO) | 12888 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2855 | 15 | 2% | 1% | -12% | -77% | -77% |
| 0.05–0.1% | 2954 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4324 | 14 | 5% | 2% | -60% | -89% | -89% |
| 0.2–0.5% | 4989 | 24 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 1935 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7097 | 21 | 3% | 2% | -66% | -90% | -90% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,787 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 7:59:52 PM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:52 PM | PLATINUM | UP | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:52 PM | GBPUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:37 PM | PALLADIUM | UP | 23 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:05 PM | WTI | DOWN | 55 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:59:05 PM | BTC | DOWN | 55 sec | +0.060% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:05 PM | AUDUSD | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:05 PM | USDCAD | UP | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:59:05 PM | GOLD | DOWN | 55 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:58:33 PM | BNB | DOWN | 86 sec | +0.035% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:58:17 PM | SOL | DOWN | 1.7 min | +0.155% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:58:17 PM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:58:01 PM | NEAR | UP | 2.0 min | -0.612% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:58:01 PM | COPPER | DOWN | 2.0 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:58:01 PM | ZEC | UP | 2.0 min | -0.417% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:57:30 PM | DOGE | DOWN | 2.5 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:57:30 PM | XRP | DOWN | 2.5 min | +0.209% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:57:14 PM | ETH | DOWN | 2.8 min | +0.187% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:53:16 PM | HYPE | DOWN | 6.7 min | +0.613% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:54 PM | PLATINUM | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:54 PM | COPPER | UP | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:54 PM | BNB | DOWN | 5 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:38 PM | ETH | DOWN | 21 sec | +0.040% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:38 PM | NEAR | DOWN | 21 sec | +0.204% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:44:38 PM | USDCAD | DOWN | 21 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:00 PM | SILVER | UP | 59 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:44:00 PM | EURUSD | UP | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:43:45 PM | HYPE | DOWN | 74 sec | +0.175% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:42 PM | XRP | UP | 2.3 min | -0.150% | 3¢ | ❌ Lost | -$0.15 |
| 10/20 7:42:10 PM | SOL | UP | 2.8 min | -0.236% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
