# 15-Minute 1¢ Study

*Updated Mon Oct 19, 4:17 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2052 finished bets | 1% | $91.90 | +40% | +4.48¢ | $27.95 / $63.95 |

*Expect about **95 buys a day** (~$14.22/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1890 | $72.40 | +35% |
| Momentum model ≥ 2%, hold to the close | 3151 | -$5.00 | -1% |
| Volatility model ≥ 5%, sell at 50¢ | 2052 | -$25.10 | -11% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 24184 | 24177 | 90 (0%) | 1.07% | -$1,674.60 (-57%) | Hold to the close: -$1,674.60 (-57%) |

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
| Volatility model | 15907 | 4.6% | 0.4% (64) | -671% | ❌ Worse |
| Momentum model | 15907 | 4.6% | 0.4% (64) | -695% | ❌ Worse |
| Mean-reversion model | 15907 | 7.7% | 0.4% (64) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15907 | 64 | -50% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3703 | 30 | -7% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2052 | 23 | +40% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1201 | 15 | +75% | -59% | -58% | -55% |
| Momentum model ≥ 2% | 3151 | 26 | -1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1890 | 20 | +35% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1256 | 13 | +42% | -66% | -65% | -60% |
| Mean-reversion model ≥ 2% | 6189 | 41 | -28% | -83% | -83% | -79% |
| Mean-reversion model ≥ 5% | 4301 | 33 | -15% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2846 | 22 | -12% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 16105 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5645 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2427 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 24177 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,674.60 | -57% | — |
| Sell at 2¢ | 870 | 4% | -$2,596.40 | -88% | 46 sec |
| Sell at 3¢ | 590 | 2% | -$2,592.50 | -88% | 47 sec |
| Sell at 5¢ | 424 | 2% | -$2,547.00 | -87% | 50 sec |
| Sell at 10¢ | 257 | 1% | -$2,457.93 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,271.89 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$2,040.85 | -70% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 912 | 5 | 10% | 3% | -48% | -82% | -85% |
| 2–5 min | 7866 | 40 | 7% | 3% | -50% | -88% | -87% |
| 1–2 min | 6182 | 24 | 3% | 2% | -58% | -92% | -92% |
| Under 1 min | 9213 | 21 | 1% | 0% | -67% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1810 | 11 | 4% | 2% | -24% | -90% | -90% |
| HYPE | 1800 | 6 | 5% | 2% | -59% | -89% | -88% |
| BNB | 1798 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1790 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1789 | 9 | 6% | 3% | -40% | -87% | -87% |
| SOL | 1785 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1781 | 7 | 3% | 1% | -52% | -87% | -87% |
| NEAR | 1777 | 9 | 6% | 3% | -35% | -79% | -79% |
| BTC | 1775 | 10 | 5% | 2% | -24% | -88% | -90% |
| GOLD | 924 | 1 | 3% | 1% | -87% | -93% | -94% |
| SILVER | 896 | 4 | 3% | 1% | -48% | -81% | -81% |
| WTI | 869 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 780 | 2 | 2% | 1% | -76% | -85% | -85% |
| PLATINUM | 768 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 710 | 5 | 2% | 2% | -34% | -83% | -82% |
| EURUSD | 710 | 3 | 2% | 1% | -61% | -83% | -82% |
| PALLADIUM | 698 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 663 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 615 | 3 | 1% | 1% | -54% | -99% | -98% |
| AUDUSD | 243 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 196 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 12173 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 12004 | 47 | 3% | 1% | -55% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2742 | 15 | 2% | 1% | -9% | -76% | -76% |
| 0.05–0.1% | 2797 | 10 | 3% | 2% | -48% | -91% | -91% |
| 0.1–0.2% | 4050 | 13 | 5% | 2% | -60% | -89% | -89% |
| 0.2–0.5% | 4686 | 22 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1827 | 6 | 6% | 3% | -66% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5814 | 29 | 4% | 2% | -43% | -87% | -86% |
| Afternoon (12–6pm) | 5706 | 19 | 3% | 1% | -60% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,815 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 4:14:54 PM | EURUSD | UP | 6 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:07 PM | NATGAS | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:07 PM | USDJPY | DOWN | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:14:07 PM | GBPUSD | UP | 52 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 4:13:35 PM | BTC | DOWN | 84 sec | +0.094% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:09:02 PM | XRP | DOWN | 6.0 min | +0.407% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:08:45 PM | HYPE | DOWN | 6.2 min | +0.448% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:08:27 PM | SOL | DOWN | 6.5 min | +0.648% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:08:27 PM | DOGE | DOWN | 6.5 min | +0.481% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:08:27 PM | ETH | DOWN | 6.5 min | +0.432% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:08:11 PM | BNB | DOWN | 6.8 min | +0.296% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:07:21 PM | ZEC | DOWN | 7.6 min | +1.015% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 4:06:49 PM | NEAR | DOWN | 8.2 min | +1.337% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:52 PM | EURUSD | DOWN | 7 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:36 PM | HYPE | UP | 23 sec | -0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:36 PM | BNB | DOWN | 23 sec | -0.019% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:59:20 PM | DOGE | UP | 39 sec | -0.025% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:20 PM | GBPUSD | DOWN | 39 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:59:04 PM | ZEC | UP | 56 sec | -0.171% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:57:59 PM | BTC | UP | 2.0 min | -0.055% | 14¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:43 PM | SOL | UP | 2.3 min | -0.140% | 5¢ | ❌ Lost | -$0.15 |
| 10/19 3:57:43 PM | XRP | UP | 2.3 min | -0.123% | 8¢ | ❌ Lost | -$0.15 |
| 10/19 3:55:34 PM | NEAR | UP | 4.4 min | -0.630% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:55:34 PM | ETH | UP | 4.4 min | -0.166% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:55 PM | DOGE | DOWN | 5 sec | -0.001% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:55 PM | GBPUSD | DOWN | 5 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:39 PM | BTC | UP | 21 sec | -0.005% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:23 PM | SOL | UP | 37 sec | -0.062% | 0¢ | ❌ Lost | $0.00 |
| 10/19 3:44:07 PM | BNB | DOWN | 53 sec | +0.022% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 3:44:07 PM | HYPE | DOWN | 53 sec | +0.134% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
