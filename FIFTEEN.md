# 15-Minute 1¢ Study

*Updated Tue Oct 20, 5:38 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2170 finished bets | 1% | $76.90 | +31% | +3.54¢ | $21.50 / $55.40 |

*Expect about **96 buys a day** (~$14.34/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2005 | $58.00 | +26% |
| Momentum model ≥ 2%, hold to the close | 3352 | -$30.80 | -8% |
| Volatility model ≥ 5%, sell at 50¢ | 2170 | -$40.10 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25764 | 25757 | 92 (0%) | 1.07% | -$1,850.00 (-59%) | Hold to the close: -$1,850.00 (-59%) |

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
| Volatility model | 16774 | 4.6% | 0.4% (65) | -674% | ❌ Worse |
| Momentum model | 16774 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16774 | 7.8% | 0.4% (65) | -817% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16774 | 65 | -52% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3971 | 31 | -11% | -77% | -77% | -73% |
| Volatility model ≥ 5% | 2170 | 23 | +31% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1245 | 15 | +68% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3352 | 26 | -8% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 2005 | 20 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1320 | 13 | +34% | -67% | -66% | -62% |
| Mean-reversion model ≥ 2% | 6595 | 42 | -31% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4591 | 34 | -19% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3039 | 22 | -18% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16972 | 5% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6098 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2687 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25757 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,850.00 | -59% | — |
| Sell at 2¢ | 938 | 4% | -$2,768.12 | -88% | 46 sec |
| Sell at 3¢ | 639 | 2% | -$2,762.79 | -88% | 48 sec |
| Sell at 5¢ | 452 | 2% | -$2,718.20 | -87% | 53 sec |
| Sell at 10¢ | 275 | 1% | -$2,623.75 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,441.43 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,216.75 | -71% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1037 | 5 | 11% | 4% | -54% | -81% | -84% |
| 2–5 min | 8337 | 41 | 7% | 3% | -52% | -88% | -87% |
| 1–2 min | 6565 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9814 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1907 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1897 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1896 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1885 | 9 | 6% | 3% | -43% | -87% | -86% |
| DOGE | 1885 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1883 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1877 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1872 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1870 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 1002 | 1 | 3% | 1% | -88% | -92% | -94% |
| SILVER | 962 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 939 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 835 | 3 | 2% | 1% | -66% | -75% | -75% |
| PLATINUM | 832 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 769 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 765 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 759 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 724 | 1 | 2% | 1% | -87% | -97% | -96% |
| USDJPY | 674 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 287 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 237 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12962 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12795 | 47 | 3% | 1% | -58% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2837 | 15 | 2% | 1% | -12% | -77% | -76% |
| 0.05–0.1% | 2938 | 10 | 3% | 2% | -51% | -92% | -91% |
| 0.1–0.2% | 4301 | 13 | 5% | 2% | -63% | -89% | -89% |
| 0.2–0.5% | 4968 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1925 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 6132 | 19 | 3% | 1% | -63% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,783 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 5:29:45 PM | USDCAD | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:45 PM | USDJPY | DOWN | 15 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:29 PM | NEAR | UP | 31 sec | -0.133% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:29 PM | BNB | UP | 31 sec | -0.024% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:29:29 PM | XRP | UP | 31 sec | -0.090% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:29:12 PM | AUDUSD | UP | 47 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:29:12 PM | GOLD | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:55 PM | BTC | UP | 65 sec | -0.061% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:39 PM | DOGE | UP | 81 sec | -0.126% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:28:08 PM | WTI | DOWN | 1.9 min | — | 3¢ | ❌ Lost | -$0.15 |
| 10/20 5:28:08 PM | SOL | UP | 1.9 min | -0.159% | 0¢ | ❌ Lost | $0.00 |
| 10/20 5:26:56 PM | HYPE | UP | 3.0 min | -0.236% | 4¢ | ❌ Lost | -$0.15 |
| 10/20 5:26:24 PM | ETH | UP | 3.6 min | -0.158% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:25:36 PM | SILVER | UP | 4.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:25:20 PM | ZEC | DOWN | 4.7 min | +0.472% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:50 PM | USDJPY | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:50 PM | PALLADIUM | UP | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:50 PM | GBPUSD | DOWN | 10 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:34 PM | WTI | DOWN | 26 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:18 PM | USDCAD | DOWN | 42 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:02 PM | NATGAS | UP | 58 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:14:02 PM | GOLD | UP | 58 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:13:46 PM | SILVER | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:11:37 PM | PLATINUM | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:11:21 PM | DOGE | UP | 3.6 min | -0.292% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:11:05 PM | BTC | UP | 3.9 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:09:29 PM | ZEC | UP | 5.5 min | -0.967% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:09:13 PM | BNB | UP | 5.8 min | -0.181% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 5:09:13 PM | SOL | UP | 5.8 min | -0.373% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 5:09:13 PM | HYPE | UP | 5.8 min | -0.490% | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
