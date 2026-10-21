# 15-Minute 1¢ Study

*Updated Tue Oct 20, 6:12 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2174 finished bets | 1% | $76.30 | +31% | +3.51¢ | $21.35 / $54.95 |

*Expect about **96 buys a day** (~$14.35/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2011 | $57.10 | +26% |
| Momentum model ≥ 2%, hold to the close | 3359 | -$31.85 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2174 | -$40.70 | -17% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25792 | 25782 | 92 (0%) | 1.07% | -$1,853.15 (-59%) | Hold to the close: -$1,853.15 (-59%) |

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
| Volatility model | 16791 | 4.6% | 0.4% (65) | -674% | ❌ Worse |
| Momentum model | 16791 | 4.5% | 0.4% (65) | -697% | ❌ Worse |
| Mean-reversion model | 16791 | 7.8% | 0.4% (65) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16791 | 65 | -52% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3980 | 31 | -11% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2174 | 23 | +31% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1248 | 15 | +68% | -60% | -59% | -56% |
| Momentum model ≥ 2% | 3359 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2011 | 20 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1324 | 13 | +34% | -67% | -67% | -62% |
| Mean-reversion model ≥ 2% | 6601 | 42 | -31% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4596 | 34 | -19% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3043 | 22 | -18% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16989 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6104 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2689 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25782 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,853.15 | -59% | — |
| Sell at 2¢ | 941 | 4% | -$2,770.49 | -88% | 46 sec |
| Sell at 3¢ | 641 | 2% | -$2,765.16 | -88% | 48 sec |
| Sell at 5¢ | 453 | 2% | -$2,720.70 | -87% | 51 sec |
| Sell at 10¢ | 275 | 1% | -$2,626.90 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,444.58 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,219.90 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1038 | 5 | 11% | 4% | -54% | -81% | -84% |
| 2–5 min | 8339 | 41 | 7% | 3% | -52% | -88% | -87% |
| 1–2 min | 6569 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9832 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1909 | 11 | 5% | 2% | -28% | -90% | -90% |
| HYPE | 1899 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1898 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1887 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1887 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1885 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1878 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1874 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1872 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 1003 | 1 | 3% | 1% | -88% | -92% | -94% |
| SILVER | 962 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 940 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 836 | 3 | 2% | 1% | -67% | -75% | -75% |
| PLATINUM | 833 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 771 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 766 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 759 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 724 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 674 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 287 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 238 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12971 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12811 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2846 | 15 | 2% | 1% | -12% | -77% | -76% |
| 0.05–0.1% | 2942 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4303 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4970 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1925 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6157 | 19 | 3% | 1% | -64% | -88% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,782 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 6:12:18 PM | BNB | DOWN | 2.7 min | +0.042% | — | In play | — |
| 10/20 6:12:18 PM | SILVER | DOWN | 2.7 min | — | — | In play | — |
| 10/20 6:10:42 PM | HYPE | DOWN | 4.3 min | +0.381% | — | In play | — |
| 10/20 5:59:54 PM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:59:37 PM | SOL | DOWN | 23 sec | +0.004% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:59:21 PM | BNB | DOWN | 39 sec | +0.018% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:59:21 PM | DOGE | DOWN | 39 sec | +0.040% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:59:21 PM | USDCAD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:59:21 PM | XRP | DOWN | 39 sec | +0.045% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:59:05 PM | PLATINUM | DOWN | 55 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:59:05 PM | NATGAS | UP | 55 sec | — | 3¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:50 PM | HYPE | UP | 69 sec | -0.124% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:58:19 PM | ETH | DOWN | 1.7 min | +0.068% | 5¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:47 PM | ZEC | UP | 2.2 min | -0.248% | 3¢ | ❌ Lost | -$0.15 |
| 10/20 5:57:47 PM | BTC | DOWN | 2.2 min | +0.071% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:53:33 PM | NEAR | DOWN | 6.5 min | +0.383% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:52 PM | COPPER | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:52 PM | HYPE | UP | 8 sec | -0.047% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:44:52 PM | NATGAS | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:52 PM | GOLD | UP | 8 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:36 PM | ZEC | DOWN | 24 sec | +0.014% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:36 PM | BNB | DOWN | 24 sec | +0.000% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:36 PM | DOGE | UP | 24 sec | -0.027% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:20 PM | BTC | DOWN | 40 sec | +0.068% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:44:20 PM | ETH | DOWN | 40 sec | +0.020% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:44:03 PM | WTI | DOWN | 56 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:43:48 PM | SOL | DOWN | 71 sec | +0.063% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:43:16 PM | NEAR | DOWN | 1.7 min | +0.155% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:45 PM | USDCAD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
