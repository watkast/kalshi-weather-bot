# 15-Minute 1¢ Study

*Updated Sun Oct 18, 11:55 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1985 finished bets | 1% | $86.30 | +39% | +4.35¢ | $31.85 / $54.45 |

*Expect about **95 buys a day** (~$14.20/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1831 | $65.15 | +32% |
| Momentum model ≥ 2%, hold to the close | 3047 | -$6.10 | -2% |
| Volatility model ≥ 2%, hold to the close | 3591 | -$30.65 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23389 | 23382 | 88 (0%) | 1.07% | -$1,603.30 (-57%) | Hold to the close: -$1,603.30 (-57%) |

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
| Volatility model | 15460 | 4.6% | 0.4% (62) | -673% | ❌ Worse |
| Momentum model | 15460 | 4.6% | 0.4% (62) | -696% | ❌ Worse |
| Mean-reversion model | 15460 | 7.7% | 0.4% (62) | -806% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15460 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3591 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1985 | 22 | +39% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1167 | 14 | +69% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 3047 | 25 | -2% | -82% | -82% | -78% |
| Momentum model ≥ 5% | 1831 | 19 | +32% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1217 | 12 | +36% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5999 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4170 | 32 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2759 | 21 | -13% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15658 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5433 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2291 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23382 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,603.30 | -57% | — |
| Sell at 2¢ | 842 | 4% | -$2,518.38 | -89% | 44 sec |
| Sell at 3¢ | 571 | 2% | -$2,514.61 | -89% | 47 sec |
| Sell at 5¢ | 410 | 2% | -$2,470.80 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,385.73 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,199.83 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,969.05 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 861 | 5 | 10% | 3% | -45% | -82% | -84% |
| 2–5 min | 7623 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 5992 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8902 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1759 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1749 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1748 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1744 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1739 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1736 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1731 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1727 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1725 | 9 | 5% | 2% | -30% | -88% | -90% |
| GOLD | 887 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 862 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 837 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 750 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 737 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 685 | 5 | 2% | 2% | -32% | -83% | -81% |
| EURUSD | 680 | 3 | 2% | 1% | -59% | -82% | -82% |
| PALLADIUM | 675 | 2 | 1% | 0% | -72% | -84% | -85% |
| GBPUSD | 631 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 589 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 218 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 173 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11750 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11632 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2677 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2727 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3922 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4556 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1773 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6577 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,856 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 11:44:56 PM | NEAR | UP | 3 sec | -0.067% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:44:56 PM | EURUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:44:56 PM | AUDUSD | DOWN | 3 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:44:25 PM | HYPE | UP | 34 sec | -0.099% | 0¢ | ❌ Lost | $0.00 |
| 10/18 11:44:09 PM | NATGAS | DOWN | 50 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:44:09 PM | WTI | UP | 50 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 11:44:09 PM | SOL | UP | 50 sec | -0.107% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:43:22 PM | XRP | DOWN | 1.6 min | +0.076% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:43:22 PM | GBPUSD | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:43:22 PM | COPPER | DOWN | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:43:06 PM | USDJPY | UP | 1.9 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:43:06 PM | DOGE | DOWN | 1.9 min | +0.139% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:42:35 PM | BTC | DOWN | 2.4 min | +0.083% | 5¢ | ❌ Lost | -$0.15 |
| 10/18 11:42:35 PM | PALLADIUM | DOWN | 2.4 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:42:19 PM | ETH | DOWN | 2.7 min | +0.111% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:40:27 PM | PLATINUM | DOWN | 4.5 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:40:11 PM | ZEC | DOWN | 4.8 min | +0.500% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:39:55 PM | GOLD | DOWN | 5.1 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:39:55 PM | SILVER | DOWN | 5.1 min | — | 2¢ | ❌ Lost | -$0.15 |
| 10/18 11:29:58 PM | NATGAS | DOWN | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:29:58 PM | GBPUSD | UP | 2 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:29:58 PM | DOGE | UP | 2 sec | -0.013% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:29:41 PM | USDJPY | DOWN | 19 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:29:41 PM | WTI | DOWN | 19 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 11:29:25 PM | XRP | UP | 35 sec | -0.076% | 0¢ | ❌ Lost | $0.00 |
| 10/18 11:29:25 PM | NEAR | DOWN | 35 sec | +0.091% | 0¢ | ❌ Lost | $0.00 |
| 10/18 11:29:25 PM | BTC | DOWN | 35 sec | +0.033% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:29:25 PM | ETH | DOWN | 35 sec | +0.037% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:28:54 PM | HYPE | DOWN | 65 sec | +0.088% | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:28:54 PM | PLATINUM | UP | 65 sec | — | 0¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
