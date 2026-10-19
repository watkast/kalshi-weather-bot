# 15-Minute 1¢ Study

*Updated Mon Oct 19, 8:46 AM MT. Paper money: every Kalshi 15-minute up/down market (crypto, currencies, commodities). Each time the UP or DOWN side hits 1¢ we buy 14 contracts (14¢ + 1¢ fee) and track that side's price every ~2 seconds until the window closes.*

[← Back to all bots](README.md) · [Sports 1¢ Study](STUDY.md)

## Current strategy

🟢 **Trade.** Profitable in both halves of the data over 100+ bets.

1. **Watch** every 15-minute up/down market (Volatility model ≥ 5%).
2. **Buy** the UP or DOWN side the moment it costs **1¢**: **14 contracts** with a 1¢ limit order (15¢ including the fee). One buy per side per window.
3. **Hold** until the 15 minutes are up. No selling.

| Rule | Based on | Hit rate | P&L (14 per buy) | Return | Avg per bet | Earlier half / later half |
|---|---|---|---|---|---|---|
| Volatility model ≥ 5%, hold to the close | 2008 finished bets | 1% | $97.15 | +43% | +4.84¢ | $30.50 / $66.65 |

*Expect about **94 buys a day** (~$14.12/day at risk); max loss per buy **15¢**.*

<details><summary>Runner-up rules</summary>

| Rule | Bets | P&L | Return |
|---|---|---|---|
| Momentum model ≥ 5%, hold to the close | 1850 | $76.90 | +38% |
| Momentum model ≥ 2%, hold to the close | 3085 | $3.25 | +1% |
| Volatility model ≥ 5%, sell at 50¢ | 2008 | -$19.85 | -9% |

</details>

*Re-picked from the latest data every refresh, using only what's knowable at the moment of buying (market type, time left, price, model readings).*

## Headline

| 1¢ moments caught | Finished | Came back & won | Break-even win rate | Hold-to-close P&L | Best exit so far |
|---|---|---|---|---|---|
| 23815 | 23808 | 90 (0%) | 1.07% | -$1,629.75 (-56%) | Hold to the close: -$1,629.75 (-56%) |

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
| Volatility model | 15686 | 4.6% | 0.4% (64) | -660% | ❌ Worse |
| Momentum model | 15686 | 4.5% | 0.4% (64) | -682% | ❌ Worse |
| Mean-reversion model | 15686 | 7.7% | 0.4% (64) | -793% | ❌ Worse |

*Accuracy vs market compares the model's predictions with Kalshi's 1¢ price (log-loss skill). Positive = the model predicted outcomes better than the market.*

### Would the models have helped?

| Buy only when… | Bets | Won | Hold return | Sell@2¢ | Sell@3¢ | Sell@5¢ |
|---|---|---|---|---|---|---|
| **Any 1¢ (no model)** | 15686 | 64 | -49% | -87% | -87% | -85% |
| Volatility model ≥ 2% | 3632 | 30 | -5% | -77% | -76% | -72% |
| Volatility model ≥ 5% | 2008 | 23 | +43% | -70% | -70% | -66% |
| Volatility model ≥ 10% | 1180 | 15 | +78% | -58% | -57% | -54% |
| Momentum model ≥ 2% | 3085 | 26 | +1% | -78% | -78% | -74% |
| Momentum model ≥ 5% | 1850 | 20 | +38% | -73% | -73% | -68% |
| Momentum model ≥ 10% | 1227 | 13 | +46% | -65% | -64% | -59% |
| Mean-reversion model ≥ 2% | 6087 | 41 | -27% | -83% | -83% | -80% |
| Mean-reversion model ≥ 5% | 4227 | 33 | -14% | -80% | -80% | -77% |
| Mean-reversion model ≥ 10% | 2802 | 22 | -10% | -77% | -77% | -75% |

*Compare each row with the first one: a model helps if its filtered bets earn more.*

![Bounce curve](fifteen/charts/bounce.png)

## How high did the price bounce?

*Share of bets where the bid for our side later reached at least this much before the close.*

| Market type | Bets | ≥2¢ | ≥3¢ | ≥5¢ | ≥10¢ | ≥25¢ | ≥50¢ |
|---|---|---|---|---|---|---|---|
| Crypto | 15884 | 4% | 3% | 2% | 1% | 1% | 0% |
| Commodities | 5550 | 2% | 1% | 1% | 1% | 0% | 0% |
| Financials | 2374 | 1% | 1% | 1% | 1% | 0% | 0% |
| **All** | 23808 | 4% | 2% | 2% | 1% | 1% | 0% |

## Exit strategies

*Sell the first time our side's bid reaches the target (after Kalshi's selling fee); otherwise hold to the close. Uses our 2-second snapshots, assuming a 14-contract sale fills.*

| Strategy | Hits | Hit rate | P&L | Return | Typical wait |
|---|---|---|---|---|---|
| Hold to the close | 90 | 0% | -$1,629.75 | -56% | — |
| Sell at 2¢ | 853 | 4% | -$2,555.97 | -88% | 45 sec |
| Sell at 3¢ | 580 | 2% | -$2,551.55 | -88% | 47 sec |
| Sell at 5¢ | 416 | 2% | -$2,507.35 | -87% | 50 sec |
| Sell at 10¢ | 252 | 1% | -$2,419.63 | -84% | 63 sec |
| Sell at 25¢ | 141 | 1% | -$2,227.04 | -77% | 79 sec |
| Sell at 50¢ | 93 | 0% | -$1,996.00 | -69% | 1.6 min |

![Exit strategies](fifteen/charts/exits.png)

## By time left when it hit 1¢

| Time left in window | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Over 10 min | 4 | 0 | 75% | 50% | -100% | +30% | +95% |
| 5–10 min | 877 | 5 | 10% | 3% | -46% | -82% | -85% |
| 2–5 min | 7761 | 40 | 7% | 3% | -49% | -88% | -88% |
| 1–2 min | 6100 | 24 | 3% | 2% | -57% | -92% | -92% |
| Under 1 min | 9066 | 21 | 1% | 0% | -66% | -87% | -87% |

## By market

| Market | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| ZEC | 1785 | 11 | 4% | 2% | -23% | -90% | -90% |
| HYPE | 1775 | 6 | 5% | 2% | -58% | -90% | -88% |
| BNB | 1773 | 9 | 5% | 2% | -38% | -82% | -81% |
| DOGE | 1766 | 3 | 4% | 2% | -79% | -91% | -90% |
| ETH | 1765 | 9 | 6% | 3% | -39% | -87% | -87% |
| SOL | 1760 | 2 | 3% | 2% | -86% | -92% | -92% |
| XRP | 1756 | 7 | 3% | 1% | -51% | -87% | -88% |
| NEAR | 1752 | 9 | 6% | 3% | -34% | -79% | -79% |
| BTC | 1752 | 10 | 5% | 2% | -23% | -88% | -90% |
| GOLD | 908 | 1 | 3% | 1% | -87% | -92% | -94% |
| SILVER | 880 | 4 | 3% | 1% | -47% | -80% | -80% |
| WTI | 853 | 3 | 3% | 1% | -59% | -94% | -95% |
| COPPER | 767 | 2 | 2% | 1% | -76% | -85% | -84% |
| PLATINUM | 754 | 0 | 1% | 0% | -100% | -99% | -99% |
| NATGAS | 698 | 5 | 2% | 2% | -33% | -83% | -82% |
| EURUSD | 697 | 3 | 2% | 1% | -60% | -82% | -82% |
| PALLADIUM | 690 | 2 | 1% | 0% | -73% | -85% | -85% |
| GBPUSD | 649 | 1 | 2% | 1% | -86% | -97% | -97% |
| USDJPY | 606 | 3 | 1% | 0% | -54% | -99% | -98% |
| AUDUSD | 233 | 0 | 0% | 0% | -100% | -99% | -99% |
| USDCAD | 189 | 0 | 1% | 0% | -100% | -99% | -99% |

## UP vs DOWN

| Side | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| UP (bought YES) | 11988 | 43 | 4% | 2% | -59% | -89% | -88% |
| DOWN (bought NO) | 11820 | 47 | 3% | 1% | -54% | -88% | -88% |

## By how far price had to move (crypto)

*Distance between the coin's live price (Coinbase) and the window's target price when we bought.*

| Gap to target at buy | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Under 0.05% | 2705 | 15 | 2% | 1% | -8% | -76% | -75% |
| 0.05–0.1% | 2769 | 10 | 3% | 2% | -47% | -91% | -91% |
| 0.1–0.2% | 3993 | 13 | 4% | 2% | -60% | -90% | -90% |
| 0.2–0.5% | 4620 | 22 | 6% | 3% | -48% | -88% | -88% |
| Over 0.5% | 1794 | 6 | 6% | 3% | -66% | -88% | -88% |

## By time of day

| When (MT) | Bets | Won | ≥2¢ | ≥5¢ | Hold return | Sell@2¢ | Sell@3¢ |
|---|---|---|---|---|---|---|---|
| Night (12–6am MT) | 6064 | 24 | 4% | 2% | -55% | -86% | -86% |
| Morning (6am–12pm) | 5602 | 29 | 4% | 2% | -41% | -87% | -86% |
| Afternoon (12–6pm) | 5549 | 19 | 3% | 1% | -59% | -88% | -89% |
| Evening (6pm–12am) | 6593 | 18 | 3% | 2% | -69% | -92% | -92% |

## Speed & liquidity

| Metric | Typical (median) |
|---|---|
| Our buy vs Kalshi's first 1¢ trade | 26 sec |
| Contracts traded at 1¢ after our buy (room to buy more) | 4,806 |
| Time from buy to best bounce (bounced bets) | 48 sec |
| Price snapshots per bet | 42 |

![Price paths](fifteen/charts/paths.png)

## Latest bets

| When (MT) | Market | Side | Time left | Gap | Peak bid | Result | Hold P&L |
|---|---|---|---|---|---|---|---|
| 10/19 8:44:48 AM | NATGAS | DOWN | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:48 AM | ETH | DOWN | 11 sec | +0.067% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:44:48 AM | COPPER | UP | 11 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:32 AM | USDJPY | UP | 27 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:32 AM | DOGE | DOWN | 27 sec | +0.043% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:16 AM | XRP | UP | 43 sec | -0.100% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:16 AM | ZEC | UP | 43 sec | -0.118% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:16 AM | BNB | DOWN | 43 sec | +0.051% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:44:16 AM | USDCAD | UP | 43 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:44:00 AM | PLATINUM | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:43:43 AM | BTC | UP | 76 sec | -0.115% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:43:27 AM | NEAR | UP | 1.5 min | -0.718% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:42:55 AM | HYPE | UP | 2.1 min | -0.245% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:42:07 AM | WTI | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:29:47 AM | NEAR | UP | 13 sec | -0.130% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:29:47 AM | COPPER | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:29:47 AM | AUDUSD | DOWN | 13 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:29:31 AM | XRP | DOWN | 29 sec | +0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:29:15 AM | BTC | UP | 45 sec | -0.105% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:29:15 AM | HYPE | DOWN | 45 sec | +0.168% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:29:15 AM | ZEC | UP | 45 sec | -0.273% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:29:00 AM | PLATINUM | DOWN | 59 sec | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:28:43 AM | BNB | UP | 77 sec | -0.131% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:28:27 AM | NATGAS | UP | 1.6 min | — | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:28:27 AM | ETH | UP | 1.6 min | -0.267% | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:27:40 AM | SILVER | DOWN | 2.3 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:27:08 AM | GOLD | DOWN | 2.9 min | — | 1¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:57 AM | BTC | DOWN | 2 sec | +0.101% | 0¢ | ❌ Lost | $0.00 |
| 10/19 8:14:41 AM | DOGE | UP | 18 sec | -0.125% | 0¢ | ❌ Lost | -$0.15 |
| 10/19 8:14:25 AM | BNB | UP | 34 sec | -0.021% | 1¢ | ❌ Lost | -$0.15 |

## Raw data

- [fifteen/bets.csv](fifteen/bets.csv) — one row per bet with every metric
- `fifteen/snaps/` — our ~2-second bid/ask snapshots for every open bet, one file per day
- `fifteen/ticks/` — every Kalshi trade in each market from 1 min before our buy to the close
- [fifteen/status.json](fifteen/status.json) — bot health
