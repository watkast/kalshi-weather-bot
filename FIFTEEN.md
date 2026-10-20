# 15-Minute 1¢ Study

*Updated Tue Oct 20, 1:00 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2161 finished bets | 1% | $78.10 | +32% | +3.61¢ | $21.80 / $56.30 |

*Expect about **96 buys a day** (~$14.40/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1994 | $59.35 | +27% |
| Momentum model ≥ 2%, hold to the close | 3325 | -$27.50 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2161 | -$38.90 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25499 | 25482 | 92 (0%) | 1.07% | -$1,814.60 (-58%) | Hold to the close: -$1,814.60 (-58%) |

*In play or awaiting result: 16. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16610 | 4.6% | 0.4% (65) | -674% | ❌ Worse |
| Momentum model | 16610 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16610 | 7.8% | 0.4% (65) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16610 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3930 | 31 | -10% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2161 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1242 | 15 | +69% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3325 | 26 | -7% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1994 | 20 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1314 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6522 | 42 | -30% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4536 | 34 | -18% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3003 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16808 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6029 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2645 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25482 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,814.60 | -58% | — |
| Sell at 2¢ | 924 | 4% | -$2,736.36 | -88% | 46 sec |
| Sell at 3¢ | 626 | 2% | -$2,732.46 | -88% | 47 sec |
| Sell at 5¢ | 444 | 2% | -$2,688.00 | -87% | 51 sec |
| Sell at 10¢ | 271 | 1% | -$2,593.59 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,406.03 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,181.35 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1011 | 5 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 8248 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6512 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9707 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1890 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1878 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1878 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1867 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1867 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1865 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1858 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1853 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1852 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 988 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 952 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 929 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 830 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 822 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 758 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 757 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 750 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 714 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 664 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 280 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 230 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12833 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12649 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2816 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2913 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4254 | 13 | 5% | 2% | -62% | -89% | -89% |
| 0.2–0.5% | 4915 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1907 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5857 | 19 | 3% | 1% | -61% | -88% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,767 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 12:59:48 PM | PALLADIUM | DOWN | 12 sec | — | 0¢ | In play | — |
| 10/20 12:59:01 PM | GOLD | DOWN | 58 sec | — | 1¢ | In play | — |
| 10/20 12:58:45 PM | HYPE | DOWN | 74 sec | +0.113% | 0¢ | In play | — |
| 10/20 12:58:45 PM | SILVER | DOWN | 74 sec | — | 0¢ | In play | — |
| 10/20 12:58:29 PM | DOGE | DOWN | 1.5 min | +0.127% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:58:29 PM | BTC | DOWN | 1.5 min | +0.080% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:58:29 PM | ETH | DOWN | 1.5 min | +0.088% | 0¢ | In play | — |
| 10/20 12:58:13 PM | ZEC | DOWN | 1.8 min | +0.310% | 0¢ | In play | — |
| 10/20 12:58:13 PM | SOL | DOWN | 1.8 min | +0.158% | 0¢ | In play | — |
| 10/20 12:57:57 PM | USDJPY | DOWN | 2.0 min | — | 0¢ | In play | — |
| 10/20 12:56:20 PM | NEAR | DOWN | 3.6 min | +0.702% | 0¢ | In play | — |
| 10/20 12:56:04 PM | BNB | DOWN | 3.9 min | +0.140% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:55:13 PM | XRP | DOWN | 4.8 min | +0.311% | 1¢ | In play | — |
| 10/20 12:44:19 PM | GBPUSD | DOWN | 40 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:44:19 PM | HYPE | UP | 40 sec | -0.150% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:44:03 PM | USDCAD | UP | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:44:03 PM | AUDUSD | DOWN | 57 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:47 PM | DOGE | UP | 73 sec | -0.136% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:47 PM | ZEC | UP | 73 sec | -0.350% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:31 PM | EURUSD | DOWN | 89 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:31 PM | WTI | DOWN | 89 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:31 PM | BNB | UP | 89 sec | -0.141% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:15 PM | BTC | UP | 1.8 min | -0.098% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:15 PM | COPPER | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:43:15 PM | ETH | UP | 1.8 min | -0.179% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:43:15 PM | NEAR | UP | 1.8 min | -0.626% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:59 PM | XRP | UP | 2.0 min | -0.235% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:59 PM | GOLD | UP | 2.0 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:43 PM | SOL | UP | 2.3 min | -0.247% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:42:43 PM | PALLADIUM | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
