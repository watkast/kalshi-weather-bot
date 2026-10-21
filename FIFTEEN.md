# 15-Minute 1¢ Study

*Updated Tue Oct 20, 7:44 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2179 finished bets | 1% | $75.85 | +31% | +3.48¢ | $21.20 / $54.65 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2015 | $56.65 | +25% |
| Momentum model ≥ 2%, hold to the close | 3365 | -$32.45 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2179 | -$41.15 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25899 | 25884 | 94 (0%) | 1.07% | -$1,837.75 (-58%) | Hold to the close: -$1,837.75 (-58%) |

*In play or awaiting result: 14. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16844 | 4.6% | 0.4% (66) | -670% | ❌ Worse |
| Momentum model | 16844 | 4.5% | 0.4% (66) | -692% | ❌ Worse |
| Mean-reversion model | 16844 | 7.8% | 0.4% (66) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16844 | 66 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3992 | 31 | -11% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2179 | 23 | +31% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1250 | 15 | +68% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3365 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2015 | 20 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1326 | 13 | +34% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6626 | 42 | -31% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4613 | 34 | -19% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3053 | 22 | -18% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17042 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6137 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2705 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25884 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 94 | 0% | -$1,837.75 | -58% | — |
| Sell at 2¢ | 945 | 4% | -$2,768.05 | -88% | 46 sec |
| Sell at 3¢ | 644 | 2% | -$2,762.59 | -88% | 48 sec |
| Sell at 5¢ | 456 | 2% | -$2,717.35 | -86% | 53 sec |
| Sell at 10¢ | 277 | 1% | -$2,622.88 | -83% | 64 sec |
| Sell at 25¢ | 149 | 1% | -$2,436.56 | -77% | 80 sec |
| Sell at 50¢ | 96 | 0% | -$2,211.75 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1044 | 5 | 11% | 4% | -54% | -81% | -84% |
| 2–5 min | 8368 | 41 | 7% | 3% | -52% | -88% | -87% |
| 1–2 min | 6600 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9868 | 23 | 1% | 0% | -67% | -85% | -85% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1915 | 11 | 5% | 2% | -29% | -89% | -90% |
| HYPE | 1905 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1904 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1893 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1892 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1891 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1884 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1880 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1878 | 10 | 5% | 2% | -29% | -88% | -90% |
| GOLD | 1009 | 2 | 4% | 1% | -77% | -81% | -83% |
| SILVER | 968 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 945 | 3 | 3% | 1% | -63% | -94% | -95% |
| COPPER | 839 | 3 | 2% | 1% | -67% | -75% | -75% |
| PLATINUM | 838 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 775 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 768 | 3 | 2% | 1% | -64% | -84% | -84% |
| PALLADIUM | 763 | 2 | 1% | 0% | -76% | -86% | -86% |
| GBPUSD | 726 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 680 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 291 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 240 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 13014 | 47 | 4% | 2% | -59% | -87% | -86% |
| DOWN (bought NO) | 12870 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2852 | 15 | 2% | 1% | -12% | -77% | -77% |
| 0.05–0.1% | 2953 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4318 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4984 | 24 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 1932 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 7064 | 20 | 3% | 2% | -68% | -90% | -90% |

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
| 10/20 7:44:00 PM | SILVER | UP | 59 sec | — | — | In play | — |
| 10/20 7:44:00 PM | EURUSD | UP | 59 sec | — | — | In play | — |
| 10/20 7:43:45 PM | HYPE | DOWN | 74 sec | +0.175% | — | In play | — |
| 10/20 7:42:42 PM | XRP | UP | 2.3 min | -0.150% | — | In play | — |
| 10/20 7:42:10 PM | SOL | UP | 2.8 min | -0.236% | — | In play | — |
| 10/20 7:42:10 PM | BTC | UP | 2.8 min | -0.119% | — | In play | — |
| 10/20 7:40:50 PM | DOGE | UP | 4.2 min | -0.260% | — | In play | — |
| 10/20 7:40:50 PM | ZEC | UP | 4.2 min | -0.541% | — | In play | — |
| 10/20 7:29:13 PM | WTI | DOWN | 46 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:59 PM | ZEC | DOWN | 60 sec | +0.305% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:59 PM | PALLADIUM | DOWN | 60 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:12 PM | DOGE | DOWN | 1.8 min | +0.136% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:12 PM | SOL | DOWN | 1.8 min | +0.177% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:12 PM | AUDUSD | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:12 PM | USDJPY | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:28:12 PM | COPPER | DOWN | 1.8 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:27:41 PM | NEAR | DOWN | 2.3 min | +0.502% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:27:41 PM | BNB | DOWN | 2.3 min | +0.103% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:27:41 PM | HYPE | DOWN | 2.3 min | +0.250% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:27:25 PM | BTC | DOWN | 2.6 min | +0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:27:09 PM | ETH | DOWN | 2.9 min | +0.201% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:27:09 PM | SILVER | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:26:53 PM | XRP | DOWN | 3.1 min | +0.210% | 0¢ | ❌ Lost | $0.00 |
| 10/20 7:26:53 PM | GOLD | DOWN | 3.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:26:53 PM | PLATINUM | DOWN | 3.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:54 PM | PLATINUM | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:54 PM | GBPUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:21 PM | NATGAS | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 7:14:21 PM | PALLADIUM | UP | 39 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 7:13:18 PM | USDJPY | UP | 1.7 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
