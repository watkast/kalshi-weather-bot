# 15-Minute 1¢ Study

*Updated Tue Oct 20, 2:33 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2166 finished bets | 1% | $77.50 | +32% | +3.58¢ | $21.65 / $55.85 |

*Expect about **96 buys a day** (~$14.39/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 2001 | $58.60 | +26% |
| Momentum model ≥ 2%, hold to the close | 3338 | -$28.70 | -7% |
| Volatility model ≥ 5%, sell at 50¢ | 2166 | -$39.50 | -16% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 25599 | 25592 | 92 (0%) | 1.07% | -$1,828.10 (-59%) | Hold to the close: -$1,828.10 (-59%) |

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
| Volatility model | 16670 | 4.6% | 0.4% (65) | -676% | ❌ Worse |
| Momentum model | 16670 | 4.5% | 0.4% (65) | -698% | ❌ Worse |
| Mean-reversion model | 16670 | 7.8% | 0.4% (65) | -818% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 16670 | 65 | -51% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3951 | 31 | -10% | -77% | -76% | -73% |
| Volatility model ≥ 5% | 2166 | 23 | +32% | -71% | -70% | -67% |
| Volatility model ≥ 10% | 1244 | 15 | +69% | -60% | -58% | -56% |
| Momentum model ≥ 2% | 3338 | 26 | -7% | -79% | -78% | -75% |
| Momentum model ≥ 5% | 2001 | 20 | +26% | -74% | -74% | -70% |
| Momentum model ≥ 10% | 1317 | 13 | +35% | -67% | -66% | -61% |
| Mean-reversion model ≥ 2% | 6551 | 42 | -30% | -83% | -82% | -79% |
| Mean-reversion model ≥ 5% | 4559 | 34 | -18% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 3020 | 22 | -17% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16868 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 6060 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2664 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 25592 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 92 | 0% | -$1,828.10 | -59% | — |
| Sell at 2¢ | 928 | 4% | -$2,748.82 | -88% | 46 sec |
| Sell at 3¢ | 630 | 2% | -$2,744.40 | -88% | 48 sec |
| Sell at 5¢ | 446 | 2% | -$2,700.20 | -87% | 51 sec |
| Sell at 10¢ | 271 | 1% | -$2,607.09 | -84% | 64 sec |
| Sell at 25¢ | 147 | 1% | -$2,419.53 | -78% | 80 sec |
| Sell at 50¢ | 95 | 0% | -$2,194.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 1023 | 5 | 11% | 4% | -53% | -81% | -84% |
| 2–5 min | 8271 | 41 | 7% | 3% | -51% | -88% | -87% |
| 1–2 min | 6541 | 24 | 3% | 2% | -60% | -93% | -92% |
| Under 1 min | 9753 | 22 | 1% | 0% | -68% | -86% | -86% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1897 | 11 | 4% | 2% | -28% | -90% | -90% |
| HYPE | 1885 | 6 | 5% | 3% | -61% | -89% | -87% |
| BNB | 1884 | 9 | 5% | 2% | -42% | -83% | -82% |
| ETH | 1874 | 9 | 6% | 3% | -42% | -87% | -86% |
| DOGE | 1873 | 3 | 4% | 2% | -80% | -91% | -90% |
| SOL | 1872 | 2 | 3% | 1% | -87% | -92% | -92% |
| XRP | 1865 | 7 | 3% | 1% | -54% | -87% | -88% |
| NEAR | 1860 | 10 | 6% | 3% | -31% | -79% | -79% |
| BTC | 1858 | 10 | 5% | 2% | -28% | -88% | -90% |
| GOLD | 995 | 1 | 4% | 1% | -88% | -92% | -94% |
| SILVER | 956 | 4 | 3% | 1% | -52% | -81% | -81% |
| WTI | 932 | 3 | 3% | 1% | -62% | -94% | -95% |
| COPPER | 832 | 3 | 2% | 1% | -66% | -75% | -74% |
| PLATINUM | 827 | 0 | 1% | 0% | -100% | -99% | -98% |
| NATGAS | 763 | 5 | 2% | 1% | -39% | -84% | -83% |
| EURUSD | 761 | 3 | 2% | 1% | -63% | -84% | -84% |
| PALLADIUM | 755 | 2 | 1% | 0% | -75% | -86% | -86% |
| GBPUSD | 718 | 1 | 2% | 1% | -87% | -97% | -97% |
| USDJPY | 670 | 3 | 1% | 1% | -58% | -99% | -98% |
| AUDUSD | 282 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 233 | 0 | 0% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12882 | 45 | 4% | 2% | -60% | -88% | -87% |
| DOWN (bought NO) | 12710 | 47 | 3% | 1% | -57% | -88% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2824 | 15 | 2% | 1% | -11% | -77% | -76% |
| 0.05–0.1% | 2922 | 10 | 3% | 2% | -50% | -92% | -91% |
| 0.1–0.2% | 4272 | 13 | 5% | 2% | -62% | -89% | -89% |
| 0.2–0.5% | 4933 | 23 | 6% | 3% | -49% | -88% | -87% |
| Over 0.5% | 1914 | 6 | 7% | 3% | -68% | -87% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6450 | 26 | 4% | 2% | -54% | -85% | -85% |
| Morning (6am–12pm) | 6213 | 29 | 4% | 2% | -47% | -88% | -87% |
| Afternoon (12–6pm) | 5967 | 19 | 3% | 1% | -62% | -89% | -89% |
| Evening (6pm–12am) | 6962 | 18 | 3% | 2% | -70% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,760 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/20 2:29:59 PM | DOGE | UP | 0 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:29:59 PM | EURUSD | DOWN | 0 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:43 PM | GBPUSD | DOWN | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:43 PM | USDJPY | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:43 PM | BTC | DOWN | 16 sec | +0.025% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:29:43 PM | PLATINUM | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:43 PM | BNB | UP | 16 sec | -0.005% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:29:27 PM | SOL | DOWN | 32 sec | +0.073% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:27 PM | NEAR | DOWN | 32 sec | +0.241% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:27 PM | ETH | DOWN | 32 sec | +0.046% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:29:11 PM | HYPE | DOWN | 48 sec | +0.114% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:29:11 PM | PALLADIUM | UP | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:29:11 PM | SILVER | UP | 48 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:29:11 PM | USDCAD | DOWN | 48 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:28:55 PM | NATGAS | UP | 65 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:28:55 PM | XRP | UP | 65 sec | -0.083% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:28:55 PM | GOLD | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:27:19 PM | ZEC | DOWN | 2.7 min | +0.512% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:14:20 PM | SOL | DOWN | 39 sec | +0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:14:20 PM | NEAR | DOWN | 39 sec | +0.136% | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:14:03 PM | ZEC | DOWN | 56 sec | +0.265% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:14:03 PM | BTC | DOWN | 56 sec | +0.087% | 0¢ | ❌ Lost | $0.00 |
| 10/20 2:14:03 PM | EURUSD | DOWN | 56 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:13:46 PM | WTI | UP | 74 sec | — | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:13:30 PM | ETH | DOWN | 1.5 min | +0.106% | 1¢ | ❌ Lost | -$0.15 |
| 10/20 2:13:14 PM | USDJPY | UP | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:13:14 PM | COPPER | DOWN | 1.8 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:12:43 PM | NATGAS | UP | 2.3 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/20 2:11:54 PM | DOGE | DOWN | 3.1 min | +0.167% | 3¢ | ❌ Lost | -$0.15 |
| 10/20 2:11:54 PM | BNB | DOWN | 3.1 min | +0.104% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
