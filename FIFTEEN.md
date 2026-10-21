# 15-Minute 1¢ Study

*Updated Tue Oct 20, 6:32 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2177 finished bets | 1% | $76.00 | +31% | +3.49¢ | $21.20 / $54.80 |

*Expect about **96 buys a day** (~$14.36/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2014 | $56.80 | +25% |
| Momentum model ≥ 2%, hold to the close | 3362 | -$32.15 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2177 | -$41.00 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25820 | 25813 | 93 (0%) | 1.07% | -$1,842.90 (-59%) | Hold to the close: -$1,842.90 (-59%) |

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
| Volatility model | 16810 | 4.6% | 0.4% (66) | -671% | ❌ Worse |
| Momentum model | 16810 | 4.5% | 0.4% (66) | -693% | ❌ Worse |
| Mean-reversion model | 16810 | 7.8% | 0.4% (66) | -812% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16810 | 66 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3984 | 31 | -11% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2177 | 23 | +31% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1250 | 15 | +68% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3362 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2014 | 20 | +25% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1326 | 13 | +34% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6608 | 42 | -31% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4602 | 34 | -19% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3046 | 22 | -18% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 17008 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6112 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2693 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25813 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 93 | 0% | -$1,842.90 | -59% | — |
| Sell at 2¢ | 942 | 4% | -$2,773.98 | -88% | 46 sec |
| Sell at 3¢ | 642 | 2% | -$2,768.52 | -88% | 48 sec |
| Sell at 5¢ | 454 | 2% | -$2,723.80 | -87% | 51 sec |
| Sell at 10¢ | 276 | 1% | -$2,629.34 | -84% | 64 sec |
| Sell at 25¢ | 148 | 1% | -$2,445.02 | -78% | 80 sec |
| Sell at 50¢ | 96 | 0% | -$2,216.90 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1041 | 5 | 10% | 4% | -54% | -81% | -84% |
| 2–5 min | 8346 | 41 | 7% | 3% | -52% | -88% | -87% |
| 1–2 min | 6576 | 25 | 3% | 2% | -59% | -93% | -92% |
| Under 1 min | 9846 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1911 | 11 | 5% | 2% | -28% | -90% | -90% |
| HYPE | 1901 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1900 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1889 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1889 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1887 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1880 | 7 | 3% | 1% | -55% | -87% | -88% |
| NEAR | 1877 | 11 | 6% | 3% | -25% | -79% | -79% |
| BTC | 1874 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 1005 | 1 | 3% | 1% | -88% | -92% | -94% |
| SILVER | 964 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 941 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 837 | 3 | 2% | 1% | -67% | -75% | -75% |
| PLATINUM | 834 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 772 | 5 | 2% | 1% | -40% | -84% | -83% |
| EURUSD | 766 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 759 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 724 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 676 | 3 | 1% | 1% | -59% | -99% | -98% |
| AUDUSD | 288 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 239 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12974 | 46 | 4% | 2% | -59% | -88% | -87% |
| DOWN (bought NO) | 12839 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2849 | 15 | 2% | 1% | -12% | -77% | -77% |
| 0.05–0.1% | 2948 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4307 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4974 | 24 | 6% | 3% | -47% | -88% | -87% |
| Over 0.5% | 1927 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 6993 | 19 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,785 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:29:49 PM | BNB | DOWN | 10 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:29:49 PM | USDCAD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:33 PM | GOLD | DOWN | 26 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:29:01 PM | SILVER | DOWN | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:46 PM | USDJPY | DOWN | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:30 PM | PLATINUM | DOWN | 1.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:30 PM | HYPE | DOWN | 1.5 min | +0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:30 PM | SOL | DOWN | 1.5 min | +0.152% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:28:14 PM | DOGE | DOWN | 1.8 min | +0.075% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:27:58 PM | XRP | DOWN | 2.0 min | +0.165% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:27:27 PM | NATGAS | UP | 2.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:27:11 PM | WTI | DOWN | 2.8 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/20 6:25:20 PM | BTC | DOWN | 4.7 min | +0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:24:16 PM | ETH | DOWN | 5.7 min | +0.243% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:23:29 PM | NEAR | DOWN | 6.5 min | +0.908% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:23:13 PM | ZEC | DOWN | 6.8 min | +0.944% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:51 PM | NEAR | DOWN | 9 sec | +0.095% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:35 PM | COPPER | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:35 PM | AUDUSD | DOWN | 25 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:35 PM | DOGE | UP | 25 sec | -0.020% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:35 PM | BTC | DOWN | 25 sec | +0.058% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:35 PM | SOL | DOWN | 25 sec | +0.069% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:35 PM | ETH | DOWN | 25 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/20 6:14:19 PM | XRP | DOWN | 41 sec | +0.052% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:03 PM | ZEC | DOWN | 57 sec | +0.229% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:14:03 PM | GOLD | DOWN | 57 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:13:48 PM | NEAR | UP | 72 sec | -0.371% | 100¢ | ✅ Won | $13.85 |
| 10/20 6:13:48 PM | USDJPY | DOWN | 72 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 6:12:18 PM | BNB | DOWN | 2.7 min | +0.042% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 6:12:18 PM | SILVER | DOWN | 2.7 min | — | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
