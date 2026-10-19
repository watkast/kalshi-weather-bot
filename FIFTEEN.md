# 15-Minute 1¢ Study

*Updated Sun Oct 18, 11:24 PM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 1984 finished bets | 1% | $86.45 | +39% | +4.36¢ | $31.85 / $54.60 |

*Expect about **95 buys a day** (~$14.21/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1827 | $65.75 | +33% |
| Momentum model ≥ 2%, hold to the close | 3042 | -$5.35 | -2% |
| Volatility model ≥ 2%, hold to the close | 3585 | -$29.75 | -7% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23351 | 23344 | 88 (0%) | 1.07% | -$1,598.35 (-56%) | Hold to the close: -$1,598.35 (-56%) |

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
| Volatility model | 15443 | 4.6% | 0.4% (62) | -673% | ❌ Worse |
| Momentum model | 15443 | 4.6% | 0.4% (62) | -696% | ❌ Worse |
| Mean-reversion model | 15443 | 7.7% | 0.4% (62) | -807% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15443 | 62 | -50% | -88% | -88% | -86% |
| Volatility model ≥ 2% | 3585 | 29 | -7% | -80% | -79% | -75% |
| Volatility model ≥ 5% | 1984 | 22 | +39% | -76% | -75% | -72% |
| Volatility model ≥ 10% | 1167 | 14 | +69% | -70% | -68% | -66% |
| Momentum model ≥ 2% | 3042 | 25 | -2% | -82% | -82% | -79% |
| Momentum model ≥ 5% | 1827 | 19 | +33% | -80% | -79% | -75% |
| Momentum model ≥ 10% | 1217 | 12 | +36% | -76% | -75% | -70% |
| Mean-reversion model ≥ 2% | 5995 | 40 | -27% | -84% | -84% | -81% |
| Mean-reversion model ≥ 5% | 4167 | 32 | -15% | -83% | -82% | -79% |
| Mean-reversion model ≥ 10% | 2758 | 21 | -13% | -81% | -81% | -78% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15641 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5421 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2282 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23344 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 88 | 0% | -$1,598.35 | -56% | — |
| Sell at 2¢ | 841 | 4% | -$2,513.69 | -89% | 44 sec |
| Sell at 3¢ | 570 | 2% | -$2,510.05 | -89% | 47 sec |
| Sell at 5¢ | 409 | 2% | -$2,466.50 | -87% | 50 sec |
| Sell at 10¢ | 247 | 1% | -$2,380.78 | -84% | 63 sec |
| Sell at 25¢ | 137 | 1% | -$2,194.88 | -78% | 77 sec |
| Sell at 50¢ | 91 | 0% | -$1,964.10 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 859 | 5 | 10% | 3% | -45% | -82% | -84% |
| 2–5 min | 7615 | 39 | 7% | 3% | -50% | -88% | -88% |
| 1–2 min | 5980 | 24 | 3% | 2% | -56% | -92% | -92% |
| Under 1 min | 8886 | 20 | 1% | 0% | -67% | -88% | -88% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1757 | 11 | 4% | 2% | -22% | -90% | -90% |
| HYPE | 1747 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1747 | 8 | 5% | 2% | -44% | -89% | -88% |
| DOGE | 1742 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1737 | 9 | 6% | 3% | -38% | -87% | -87% |
| SOL | 1734 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1729 | 7 | 3% | 1% | -50% | -87% | -88% |
| NEAR | 1725 | 9 | 6% | 3% | -33% | -79% | -79% |
| BTC | 1723 | 9 | 5% | 2% | -30% | -89% | -90% |
| GOLD | 885 | 1 | 4% | 1% | -87% | -92% | -94% |
| SILVER | 860 | 4 | 3% | 1% | -46% | -80% | -80% |
| WTI | 835 | 3 | 3% | 1% | -58% | -94% | -95% |
| COPPER | 749 | 2 | 2% | 1% | -75% | -85% | -84% |
| PLATINUM | 735 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 683 | 5 | 2% | 2% | -32% | -83% | -81% |
| EURUSD | 678 | 3 | 3% | 1% | -59% | -82% | -82% |
| PALLADIUM | 674 | 2 | 1% | 0% | -72% | -84% | -85% |
| GBPUSD | 629 | 1 | 2% | 1% | -85% | -97% | -97% |
| USDJPY | 587 | 3 | 1% | 1% | -52% | -99% | -98% |
| AUDUSD | 216 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 172 | 0 | 0% | 0% | -100% | -100% | -100% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11735 | 42 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11609 | 46 | 3% | 2% | -54% | -89% | -89% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2674 | 14 | 2% | 1% | -13% | -82% | -81% |
| 0.05–0.1% | 2719 | 10 | 3% | 2% | -46% | -91% | -91% |
| 0.1–0.2% | 3918 | 13 | 4% | 2% | -59% | -90% | -89% |
| 0.2–0.5% | 4555 | 21 | 6% | 3% | -49% | -88% | -88% |
| Over 0.5% | 1772 | 6 | 6% | 3% | -65% | -88% | -89% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 5767 | 23 | 4% | 2% | -55% | -87% | -88% |
| Morning (6am–12pm) | 5489 | 28 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6539 | 18 | 3% | 2% | -68% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,858 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/18 11:14:44 PM | NATGAS | UP | 16 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:14:28 PM | USDJPY | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:14:28 PM | GBPUSD | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:14:12 PM | GOLD | UP | 47 sec | — | 0¢ | ❌ Lost | $0.00 |
| 10/18 11:13:41 PM | PALLADIUM | UP | 79 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:13:09 PM | XRP | UP | 1.9 min | -0.137% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:53 PM | PLATINUM | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:53 PM | USDCAD | UP | 2.1 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:53 PM | ETH | UP | 2.1 min | -0.104% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:53 PM | DOGE | UP | 2.1 min | -0.212% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:38 PM | NEAR | UP | 2.4 min | -0.454% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:22 PM | SILVER | UP | 2.6 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:06 PM | BTC | UP | 2.9 min | -0.156% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:12:06 PM | SOL | UP | 2.9 min | -0.254% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:11:35 PM | COPPER | UP | 3.4 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:11:03 PM | ZEC | UP | 4.0 min | -0.574% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:10:16 PM | HYPE | UP | 4.7 min | -0.321% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 11:05:16 PM | BNB | UP | 9.7 min | -0.292% | 6¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:55 PM | SOL | UP | 4 sec | -0.059% | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:59:45 PM | EURUSD | UP | 14 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:37 PM | AUDUSD | DOWN | 22 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:27 PM | COPPER | DOWN | 32 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:21 PM | PLATINUM | DOWN | 38 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:15 PM | ETH | DOWN | 44 sec | +0.032% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:15 PM | BTC | DOWN | 44 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:59:05 PM | NATGAS | DOWN | 54 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/18 10:59:05 PM | DOGE | UP | 54 sec | -0.154% | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:59:01 PM | NEAR | UP | 58 sec | -0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/18 10:58:49 PM | XRP | UP | 70 sec | -0.107% | 0¢ | ❌ Lost | $0.00 |
| 10/18 10:58:33 PM | ZEC | UP | 86 sec | -0.294% | 0¢ | ❌ Lost | $0.00 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
