# 15-Minute 1¢ Study

*Updated Tue Oct 20, 12:40 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2161 finished bets | 1% | $78.10 | +32% | +3.61¢ | $21.80 / $56.30 |

*Expect about **96 buys a day** (~$14.41/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1994 | $59.35 | +27% |
| Momentum model ≥ 2%, hold to the close | 3324 | -$27.50 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2161 | -$38.90 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25467 | 25459 | 92 (0%) | 1.07% | -$1,811.45 (-58%) | Hold to the close: -$1,811.45 (-58%) |

*In play or awaiting result: 7. Commodity markets can take a few hours to settle.*

## Prediction models

*Each model's chance that our side wins, recorded at the moment we bought. Kalshi's price said about 1%. If a model knows better, only buying when it disagrees with the market should improve results.*

- **Volatility model:** random-walk (Black-Scholes) odds from the gap to the target, time left and the last hour's volatility
- **Momentum model:** same, but assumes the last 5 minutes' trend keeps going
- **Mean-reversion model:** same, but assumes the last 5 minutes' trend reverses

*Models cover the crypto markets (live prices from Coinbase). Readings start with the next watch session (about 12:45 AM MT, Sep 28).*

### How accurate is each model?

| Model | Bets scored | Avg chance it gave | Actual win rate | Accuracy vs market | Verdict |
|---|---|---|---|---|---|
| Volatility model | 16598 | 4.6% | 0.4% (65) | -674% | ❌ Worse |
| Momentum model | 16598 | 4.5% | 0.4% (65) | -696% | ❌ Worse |
| Mean-reversion model | 16598 | 7.8% | 0.4% (65) | -815% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16598 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3928 | 31 | -10% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2161 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1242 | 15 | +69% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3324 | 26 | -7% | -79% | -79% | -75% |
| Momentum model ≥ 5% | 1994 | 20 | +27% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1314 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6520 | 42 | -30% | -83% | -82% | -80% |
| Mean-reversion model ≥ 5% | 4535 | 34 | -17% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3002 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16796 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6022 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2641 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25459 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,811.45 | -58% | — |
| Sell at 2¢ | 922 | 4% | -$2,733.73 | -88% | 46 sec |
| Sell at 3¢ | 626 | 2% | -$2,729.31 | -88% | 47 sec |
| Sell at 5¢ | 444 | 2% | -$2,684.85 | -87% | 51 sec |
| Sell at 10¢ | 271 | 1% | -$2,590.44 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,402.88 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,178.20 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1010 | 5 | 11% | 4% | -53% | -81% | -83% |
| 2–5 min | 8241 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6501 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9703 | 22 | 1% | 0% | -67% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1889 | 11 | 4% | 2% | -27% | -90% | -90% |
| HYPE | 1877 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1876 | 9 | 5% | 2% | -41% | -83% | -82% |
| ETH | 1866 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1865 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1864 | 2 | 3% | 2% | -87% | -92% | -92% |
| XRP | 1857 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1852 | 10 | 6% | 3% | -30% | -79% | -79% |
| BTC | 1850 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 987 | 1 | 3% | 1% | -88% | -92% | -95% |
| SILVER | 951 | 4 | 3% | 1% | -51% | -81% | -81% |
| WTI | 928 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 829 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 821 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 757 | 5 | 2% | 1% | -38% | -84% | -83% |
| EURUSD | 756 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 749 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 713 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 664 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 279 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 229 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12818 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12641 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2816 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2911 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4248 | 13 | 5% | 2% | -62% | -89% | -89% |
| 0.2–0.5% | 4912 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1906 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5834 | 19 | 3% | 1% | -61% | -89% | -89% |
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
| 10/20 12:37:04 PM | NATGAS | DOWN | 7.9 min | — | — | In play | — |
| 10/20 12:29:28 PM | PALLADIUM | UP | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:29:12 PM | DOGE | UP | 48 sec | -0.095% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:29:12 PM | COPPER | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:29:12 PM | NEAR | UP | 48 sec | -0.488% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:28:57 PM | WTI | DOWN | 62 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:27:21 PM | HYPE | UP | 2.6 min | -0.288% | 2¢ | ❌ Lost | -$0.15 |
| 10/20 12:25:58 PM | XRP | UP | 4.0 min | -0.385% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:25:58 PM | BTC | UP | 4.0 min | -0.169% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:25:44 PM | ETH | UP | 4.2 min | -0.280% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:25:28 PM | SOL | UP | 4.5 min | -0.348% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:25:28 PM | BNB | UP | 4.5 min | -0.179% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:25:12 PM | ZEC | UP | 4.8 min | -0.673% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:14:44 PM | BNB | DOWN | 15 sec | -0.009% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:14:28 PM | COPPER | DOWN | 31 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:14:12 PM | WTI | UP | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:14:12 PM | PALLADIUM | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:14:12 PM | SILVER | DOWN | 47 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:13:40 PM | DOGE | UP | 80 sec | -0.177% | 4¢ | ❌ Lost | -$0.15 |
| 10/20 12:13:40 PM | PLATINUM | DOWN | 80 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:13:40 PM | NEAR | UP | 80 sec | -0.417% | 0¢ | ❌ Lost | $0.00 |
| 10/20 12:13:24 PM | XRP | UP | 1.6 min | -0.233% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 12:13:24 PM | GOLD | DOWN | 1.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:13:24 PM | ZEC | UP | 1.6 min | -0.370% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:12:19 PM | ETH | UP | 2.7 min | -0.151% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:12:03 PM | SOL | UP | 2.9 min | -0.300% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:11:47 PM | BTC | UP | 3.2 min | -0.146% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 12:11:15 PM | HYPE | UP | 3.7 min | -0.270% | 0¢ | ❌ Lost | $0.00 |
| 10/20 11:59:47 AM | ETH | DOWN | 13 sec | +0.012% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 11:59:47 AM | XRP | DOWN | 13 sec | +0.023% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
